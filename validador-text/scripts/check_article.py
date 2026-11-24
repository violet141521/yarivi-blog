#!/usr/bin/env python3
"""
check_article.py v2 — QA do blog Yarivi (skill validador-text).

Uso:
  python check_article.py <slug>                       # imprime JSON com checagens + nota
  python check_article.py <slug> --manual arq.json     # inclui achados manuais (antiplágio, links via WebFetch, auditoria de dados, ajustes)
  python check_article.py <slug> --write               # também grava rascunhos/qa-<slug>.md e registra a rodada

Nota (0-100), aprovação >= 90 e zero bloqueantes:
  Dados e fontes 25 | Originalidade 15 | SEO técnico 15 | Links 10 | Estilo 20 | Utilidade 15

JSON manual (todos os campos opcionais):
{
  "plagio": [{"frase": "...", "match": null}, {"frase": "...", "match": "https://..."}],
  "links_verificados": {"https://exemplo.com": 200},
  "dados": {"mantidos": ["..."], "removidos": ["..."], "sem_fonte_remanescentes": 0, "citacoes_sem_origem": 0},
  "ajustes": {"estilo": [{"pontos": -2, "motivo": "..."}], "utilidade": [], "dados": []},
  "correcoes_rodada": ["o que foi corrigido antes desta rodada"]
}
"""
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.request

BLOG_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CATALOG_PATH = os.path.join(BLOG_ROOT, "artigos", "_catalog.json")
APPROVAL_SCORE = 90
CAT_MAX = {"dados": 25, "originalidade": 15, "seo": 15, "links": 10, "estilo": 20, "utilidade": 15}
CAT_NAME = {"dados": "Dados e fontes", "originalidade": "Originalidade", "seo": "SEO técnico",
            "links": "Links", "estilo": "Estilo Yarivi", "utilidade": "Utilidade ao leitor"}

MESES = {"janeiro": 1, "fevereiro": 2, "março": 3, "marco": 3, "abril": 4, "maio": 5, "junho": 6, "julho": 7,
         "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12}
STOP = {"de", "do", "da", "dos", "das", "em", "para", "com", "por", "que", "e", "o", "a", "os", "as", "um", "uma",
        "no", "na", "nos", "nas", "se", "ao", "às", "como", "mais", "ou", "mas", "nem", "são", "é", "foi", "será"}
JARGAO = ["npu", "api", "latência", "latencia", "criptografia", "token", "firmware", "kernel", "gpu", "cpu",
          "algoritmo", "machine learning", "llm", "ransomware", "phishing", "vpn", "ssd", "oled", "ips",
          "hertz", "hz", "benchmark", "open source", "código aberto", "backup", "nuvem", "ia generativa",
          "deepfake", "criptográfic", "esim", "5g", "6g", "wi-fi 7", "ghz", "nanômetro", "nm"]
EXPLICA = re.compile(r"\(|—|–|, ou |ou seja|isto é|em outras palavras|chamad[oa]|conhecid[oa]|significa|"
                     r"\bé (um|uma|o|a|quando|como)\b|\bsão (os|as|um|uma)\b|funciona como|como se fosse|"
                     r"serve para|quer dizer|nome (técnico )?d[oae]", re.I)
ATRIBUI = re.compile(r"segundo|de acordo com|conforme|aponta|afirma|informou|divulgou|publicou|relat[oó]rio|"
                     r"levantamento|pesquisa d[aeo]|dados d[aeo]|cálculo (do )?yarivi|conta do yarivi|"
                     r"estimativa|anunciou|disse|diz |declarou|segundo o", re.I)
ACAO = re.compile(r"faça agora|faça|confira|verifique|ative|desative|guarde|compare|baixe|use |usar |"
                  r"antes de comprar|anote|revise|teste|escolha|procure|peça", re.I)


# ---------------------------------------------------------------- utilidades HTML
def find_html(slug):
    for sub in ("rascunhos", "artigos"):
        p = os.path.join(BLOG_ROOT, sub, f"{slug}.html")
        if os.path.exists(p):
            return p, sub
    print(json.dumps({"error": f"Artigo não encontrado em rascunhos/ nem artigos/: {slug}"}))
    sys.exit(1)


def extract_tag(html, tag):
    m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", html, re.I | re.S)
    return m.group(1).strip() if m else ""


def meta(html, name):
    for pat in (rf'<meta[^>]*name=["\']{re.escape(name)}["\'][^>]*content=(["\'])(.*?)\1',
                rf'<meta[^>]*content=(["\'])(.*?)\1[^>]*name=["\']{re.escape(name)}["\']'):
        m = re.search(pat, html, re.I)
        if m:
            return m.group(2).strip()
    return ""


def og(html, prop):
    m = re.search(rf'<meta[^>]*property=["\']{re.escape(prop)}["\'][^>]*content=(["\'])(.*?)\1', html, re.I)
    return m.group(2).strip() if m else ""


def strip_html(h):
    h = re.sub(r"<script[^>]*>.*?</script>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<style[^>]*>.*?</style>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    for a, b in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&#39;", "'")):
        h = h.replace(a, b)
    return re.sub(r"\s+", " ", h).strip()


def body_html(html):
    m = re.search(r'<article[^>]*class=["\'][^"\']*art-body[^"\']*["\'][^>]*>(.*?)</article>', html, re.S | re.I)
    if not m:
        m = re.search(r"<article[^>]*>(.*?)</article>", html, re.S | re.I)
    b = m.group(1) if m else html
    for cls in ("art-sources", "art-related"):
        b = re.sub(rf'<div[^>]*class=["\'][^"\']*{cls}[^"\']*["\'].*?</div>', "", b, flags=re.S | re.I)
    return b


def jsonld_blocks(html):
    out = []
    for s in re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.S | re.I):
        try:
            out.append(json.loads(s))
        except Exception:
            out.append({"_raw": s})
    return out


def flatten_ld(blocks):
    items = []
    for b in blocks:
        if isinstance(b, list):
            items += b
        elif isinstance(b, dict) and "@graph" in b:
            items += b["@graph"]
        else:
            items.append(b)
    return [i for i in items if isinstance(i, dict)]


def faq_questions(html):
    n = 0
    for it in flatten_ld(jsonld_blocks(html)):
        if "FAQPage" in json.dumps(it.get("@type", "")) or "_raw" in it and "FAQPage" in it["_raw"]:
            n = max(n, len(it.get("mainEntity", [])) if "mainEntity" in it else it.get("_raw", "").count('"Question"'))
    return n


def keywords_of(html):
    for it in flatten_ld(jsonld_blocks(html)):
        k = it.get("keywords")
        if isinstance(k, list) and k:
            return [str(x).lower() for x in k]
        if isinstance(k, str) and k:
            return [x.strip().lower() for x in k.split(",")]
    k = meta(html, "keywords")
    return [x.strip().lower() for x in k.split(",") if x.strip()]


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def words_of(t):
    return set(w.lower() for w in re.split(r"\W+", t) if w and w.lower() not in STOP and len(w) > 2)


def toks(t):
    return set(w.lower() for w in re.split(r"\W+", t) if len(w) >= 2 and w.lower() not in STOP)


def kw_in(kw, t):
    if not kw:
        return False
    return kw in t.lower() or toks(kw) <= toks(t)


def similarity(a, b):
    wa, wb = words_of(a), words_of(b)
    return len(wa & wb) / max(len(wa), len(wb)) if wa and wb else 0.0


# ---------------------------------------------------------------- datas e fontes
def parse_date_text(s):
    """Retorna (date, precisao) ou (None, None). precisao: 'dia' | 'mes' | 'ano'."""
    m = re.search(r"(\d{1,2})/(\d{1,2})/(20\d{2})", s)
    if m:
        try:
            return datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1))), "dia"
        except ValueError:
            pass
    m = re.search(r"(\d{1,2}) de ([a-zçã]+)(?: de)? (20\d{2})", s, re.I)
    if m and m.group(2).lower() in MESES:
        try:
            return datetime.date(int(m.group(3)), MESES[m.group(2).lower()], int(m.group(1))), "dia"
        except ValueError:
            pass
    m = re.search(r"([a-zçã]+) de (20\d{2})", s, re.I)
    if m and m.group(1).lower() in MESES:
        return datetime.date(int(m.group(2)), MESES[m.group(1).lower()], 28), "mes"
    m = re.search(r"\b(0?[1-9]|1[0-2])/(20\d{2})\b", s)
    if m:
        return datetime.date(int(m.group(2)), int(m.group(1)), 28), "mes"
    m = re.search(r"/(20\d{2})/(0?[1-9]|1[0-2])/", s)
    if m:
        return datetime.date(int(m.group(1)), int(m.group(2)), 28), "mes"
    m = re.search(r"\b(20[12]\d)\b", s)
    if m:
        return datetime.date(int(m.group(1)), 12, 31), "ano"
    return None, None


def extract_sources(html):
    m = re.search(r'<div[^>]*class=["\'][^"\']*art-sources[^"\']*["\'][^>]*>(.*?)</div>', html, re.S | re.I)
    if not m:
        return []
    out = []
    for li in re.findall(r"<li[^>]*>(.*?)</li>", m.group(1), re.S | re.I):
        h = re.search(r'href=["\']([^"\']+)["\']', li)
        label = strip_html(li)
        url = h.group(1) if h else ""
        d, prec = parse_date_text(label)
        if d is None:
            d, prec = parse_date_text(url)
        out.append({"url": url, "label": label, "data": d.isoformat() if d else None, "precisao": prec})
    return out


# ---------------------------------------------------------------- links
def http_status(url, timeout=10):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 Yarivi-QA/2.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.url
    except urllib.error.HTTPError as e:
        return e.code, url
    except urllib.error.URLError:
        return 0, url
    except Exception:
        return -1, url


def slug_of(href):
    m = re.search(r"artigos/([^./#?]+)", href)
    return m.group(1) if m else None


def load_catalog():
    if not os.path.exists(CATALOG_PATH):
        return []
    with open(CATALOG_PATH, encoding="utf-8") as f:
        return json.load(f).get("articles", [])


def other_articles_meta(slug):
    """slug -> (título, keyword principal) de artigos e rascunhos (menos o próprio)."""
    res = {}
    for sub in ("artigos", "rascunhos"):
        d = os.path.join(BLOG_ROOT, sub)
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            if fn.endswith(".html") and fn[:-5] != slug and fn[:-5] not in res:
                try:
                    h = open(os.path.join(d, fn), encoding="utf-8").read()
                except Exception:
                    continue
                kws = keywords_of(h)
                res[fn[:-5]] = (strip_html(extract_tag(h, "title")), kws[0] if kws else "")
    return res


# ---------------------------------------------------------------- análise
def analyze(slug, manual):
    path, sub = find_html(slug)
    html = open(path, encoding="utf-8").read()
    catalog = load_catalog()
    cat_by_slug = {a["slug"]: a for a in catalog}

    title = strip_html(extract_tag(html, "title"))
    h1 = strip_html(extract_tag(html, "h1"))
    desc = meta(html, "description")
    kws = keywords_of(html)
    kw = kws[0] if kws else ""
    body = body_html(html)
    paragraphs = [strip_html(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", body, re.S | re.I)]
    paragraphs = [p for p in paragraphs if p]
    text = strip_html(body)
    lead_m = re.search(r'<p[^>]*class=["\'][^"\']*art-lead[^"\']*["\'][^>]*>(.*?)</p>', html, re.S | re.I)
    lead = strip_html(lead_m.group(1)) if lead_m else (paragraphs[0] if paragraphs else "")
    wc = len(text.split())
    h2s = [strip_html(x) for x in re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.S | re.I)]

    pub = og(html, "article:published_time")
    ref_date = None
    if slug in cat_by_slug and cat_by_slug[slug].get("data_pub"):
        ref_date = datetime.date.fromisoformat(cat_by_slug[slug]["data_pub"])
    elif pub:
        try:
            ref_date = datetime.date.fromisoformat(pub[:10])
        except ValueError:
            pass
    today = datetime.date.today()
    write_date = today  # recência é medida contra a data em que o artigo é escrito/revisado
    items = {k: [] for k in CAT_MAX}   # categoria -> lista de dicts {nivel, texto, pontos}
    points = dict(CAT_MAX)

    def pen(cat, pts, nivel, texto):
        points[cat] -= pts
        items[cat].append({"nivel": nivel, "texto": texto, "pontos": -pts})

    def ok(cat, texto):
        items[cat].append({"nivel": "ok", "texto": texto, "pontos": 0})

    blockers = []

    def block(cat, pts, texto):
        pen(cat, pts, "bloqueante", texto)
        blockers.append(texto)

    # ---------- DADOS E FONTES (25)
    sources = extract_sources(html)
    if len(sources) < 3:
        pen("dados", 3, "atencao", f"Só {len(sources)} fonte(s) listada(s); o padrão Yarivi é ter 3 ou mais")
    else:
        ok("dados", f"{len(sources)} fontes listadas")
    old, undated = [], []
    for s in sources:
        if not s["data"]:
            undated.append(s)
            continue
        age = (write_date - datetime.date.fromisoformat(s["data"])).days
        s["idade_dias"] = age
        if age > 365:
            old.append(s)
    for s in old[:2]:
        pen("dados", 8, "atencao", f"Fonte com mais de 1 ano ({s['data'][:10]}): {s['label'][:80]} — só vale para fato histórico fixo")
    if len(old) > 2:
        pen("dados", 0, "atencao", f"+{len(old) - 2} fonte(s) antigas além das 2 já descontadas")
    for s in undated[:3]:
        pen("dados", 2, "atencao", f"Fonte sem data identificável: {s['label'][:80]} — acrescente a data no rótulo")
    if not old and not undated and sources:
        ok("dados", "Todas as fontes têm data e estão dentro de 1 ano")
    unattributed = []
    src_names = [x["label"].split(" — ")[0].strip().lower() for x in sources if x["label"]]
    src_names = [n for n in src_names if len(n) >= 3]
    for p in paragraphs:
        if p == lead:
            continue
        nums = re.findall(r"(?:R\$\s?[\d.,]+|\d+[.,]?\d*\s?%|\b\d{2,}[.,]?\d*\s?(?:milh|bilh|mil\b|mi\b|bi\b|mm\b|nm\b|km|hz|ghz|gb|tb|mah|anos|dias|meses|pessoas|usuários|brasileiros)\w*)", p, re.I)
        if nums and not ATRIBUI.search(p) and not any(n in p.lower() for n in src_names):
            unattributed.append(p[:90])
    for p in unattributed[:4]:
        pen("dados", 2, "atencao", f"Parágrafo com número sem atribuição à fonte: «{p}…»")
    if not unattributed:
        ok("dados", "Parágrafos com números citam a fonte no próprio texto")
    d = manual.get("dados", {})
    for _ in range(int(d.get("sem_fonte_remanescentes", 0))):
        pen("dados", 5, "atencao", "Dado sem fonte verificável remanescente (auditoria 2.6)")
    for _ in range(int(d.get("citacoes_sem_origem", 0))):
        pen("dados", 5, "atencao", "Citação direta sem origem verificada (auditoria 2.6)")
    for a in manual.get("ajustes", {}).get("dados", []):
        pen("dados", -int(a["pontos"]) if a["pontos"] < 0 else 0, "atencao", f"Ajuste manual: {a['motivo']}")

    # ---------- ORIGINALIDADE (15)
    cands = [s for s in sentences(text) if 15 <= len(s.split()) <= 25]
    if len(cands) < 5:
        cands = [s for s in sentences(text) if 10 <= len(s.split()) <= 35]
    mid = cands[len(cands) // 6: 5 * len(cands) // 6] or cands
    with_nums = [s for s in mid if re.search(r"\d", s)]
    without = [s for s in mid if not re.search(r"\d", s)]
    picked = with_nums[:2]
    step = max(1, len(without) // 3)
    picked += without[::step][: 5 - len(picked)]
    for s in mid:
        if len(picked) >= 5:
            break
        if s not in picked:
            picked.append(s)
    sample_phrases = picked[:5]
    pl = manual.get("plagio")
    if pl is None:
        pen("originalidade", 15, "atencao", "Antiplágio não executado (pendente: 5 frases via WebSearch)")
    else:
        matches = [x for x in pl if x.get("match")]
        tested = len(pl)
        if tested < 5:
            pen("originalidade", min(9, 3 * (5 - tested)), "atencao", f"Só {tested} de 5 frases testadas")
        if len(matches) >= 3:
            block("originalidade", 15, f"Potencial cópia: {len(matches)} frases com correspondência exata")
        elif matches:
            pen("originalidade", 6 * len(matches), "atencao",
                f"{len(matches)} frase(s) com correspondência: " + "; ".join(m["match"] for m in matches))
        else:
            ok("originalidade", f"{tested} de {tested} frases testadas sem correspondência")

    # ---------- SEO (15)
    def chk(cat, cond, pts, good, bad, nivel="atencao"):
        (ok(cat, good) if cond else pen(cat, pts, nivel, bad))

    chk("seo", len(title) <= 60, 2, f"<title> com {len(title)} caracteres", f"<title> com {len(title)} caracteres (máx. 60)")
    chk("seo", "yarivi" in title.lower(), 1, "<title> termina com Yarivi", "<title> sem a marca Yarivi")
    tclean = re.sub(r"\s*\|.*$", "", title).strip().lower()
    chk("seo", h1.lower()[:60] != tclean[:60], 2, "H1 diferente do <title>", "H1 igual ao <title>")
    chk("seo", bool(desc), 1, "Meta description presente", "Meta description ausente")
    chk("seo", 110 <= len(desc) <= 155, 1, f"Meta description com {len(desc)} caracteres", f"Meta description com {len(desc)} caracteres (ideal 110–155)")
    fq = faq_questions(html)
    chk("seo", fq > 0, 2, "Schema FAQPage presente", "Schema FAQPage ausente")
    ph = re.findall(r"\[\.\.\.\]|\bTODO\b|\bPLACEHOLDER\b|\[inserir\]|\{\{[^}]+\}\}", text + html[:0])
    if ph:
        block("seo", 1, f"Placeholder no texto: {ph[:3]}")
    else:
        ok("seo", "Sem placeholders")
    chk("seo", bool(pub), 1, "article:published_time presente", "article:published_time ausente")
    if kw:
        chk("seo", kw_in(kw, title), 1, f"Palavra-chave «{kw}» no <title>", f"Palavra-chave «{kw}» ausente do <title>")
        chk("seo", kw_in(kw, desc), 1, "Palavra-chave na meta description", "Palavra-chave ausente da meta description")
        first100 = " ".join(text.split()[:100])
        chk("seo", kw_in(kw, first100) or kw_in(kw, lead), 1, "Palavra-chave nas primeiras 100 palavras", "Palavra-chave fora das primeiras 100 palavras")
        chk("seo", any(kw_in(kw, h) or len(toks(kw) & toks(h)) >= max(1, len(toks(kw)) - 1) for h in h2s),
            1, "Palavra-chave (ou quase toda) em algum H2", "Nenhum H2 contém a palavra-chave")
    else:
        pen("seo", 4, "atencao", "Sem palavras-chave no JSON-LD/meta keywords para conferir")

    # ---------- LINKS (10)
    hrefs = re.findall(r'<a[^>]*href=["\']([^"\']+)["\']', html, re.I)
    ext = sorted({h for h in hrefs if h.startswith("http")})
    internal = [h for h in hrefs if "artigos/" in h and not h.startswith("http")]
    verified = dict(manual.get("links_verificados", {}))
    link_status, pending = [], []
    offline_probe = http_status(ext[0], 6)[0] if ext else 200
    offline = offline_probe in (0, -1)
    for u in ext:
        if u in verified:
            link_status.append({"url": u, "status": verified[u], "via": "manual"})
            continue
        st, fin = (offline_probe, u) if (offline or u == ext[0]) else http_status(u)
        if st in (0, -1):
            pending.append(u)
        else:
            link_status.append({"url": u, "status": st, "via": "script", "final_url": fin})
    for l in link_status:
        st = l["status"]
        if st >= 400:
            block("links", 4, f"Link quebrado ({st}): {l['url']}")
        elif 300 <= st < 400:
            pen("links", 1, "atencao", f"Redirecionamento ({st}): {l['url']}")
    if pending:
        pen("links", min(3, 1 + len(pending) // 3), "atencao",
            f"{len(pending)} link(s) sem verificação HTTP (PC sem rede). Verificar via WebFetch e passar em links_verificados")
    elif ext and not any(i["nivel"] != "ok" for i in items["links"]):
        ok("links", f"{len(ext)} link(s) externos verificados (status 2xx)")
    if not internal:
        pen("links", 3, "atencao", "Nenhum link interno")
    else:
        ok("links", f"{len(internal)} link(s) interno(s)")
    base_date = ref_date or today
    for h in internal:
        s = slug_of(h)
        if not s:
            continue
        if s not in cat_by_slug and not os.path.exists(os.path.join(BLOG_ROOT, "rascunhos", s + ".html")):
            pen("links", 3, "atencao", f"Link interno para artigo inexistente: {s}")
        elif s in cat_by_slug and cat_by_slug[s].get("data_pub"):
            if datetime.date.fromisoformat(cat_by_slug[s]["data_pub"]) > base_date:
                block("links", 5, f"Link interno para artigo com data posterior ({cat_by_slug[s]['data_pub']}): {s}")
    if "art-related" not in html:
        pen("links", 2, "atencao", "Seção «Leia também» ausente")

    # ---------- ESTILO (20)
    sl = [s for s in sentences(text)]
    lens = [len(s.split()) for s in sl] or [0]
    avg = sum(lens) / len(lens)
    long_ratio = sum(1 for n in lens if n > 30) / len(lens)
    if avg <= 20:
        ok("estilo", f"Frases curtas (média {avg:.1f} palavras)")
    elif avg <= 25:
        pen("estilo", 2, "atencao", f"Frases um pouco longas (média {avg:.1f} palavras; ideal ≤20)")
    elif avg <= 30:
        pen("estilo", 4, "atencao", f"Frases longas (média {avg:.1f} palavras)")
    else:
        pen("estilo", 6, "atencao", f"Frases muito longas (média {avg:.1f} palavras)")
    if long_ratio < 0.10:
        ok("estilo", f"Poucas frases acima de 30 palavras ({long_ratio:.0%})")
    elif long_ratio < 0.20:
        pen("estilo", 2, "atencao", f"{long_ratio:.0%} das frases passam de 30 palavras")
    else:
        pen("estilo", 4, "atencao", f"{long_ratio:.0%} das frases passam de 30 palavras")
    unexplained = []
    low = text.lower()
    for j in JARGAO:
        i = low.find(j)
        if i == -1 or not re.search(rf"(?<!\w){re.escape(j)}(?!\w)", low):
            continue
        i = re.search(rf"(?<!\w){re.escape(j)}(?!\w)", low).start()
        ctx = text[max(0, i - 90): i + len(j) + 130]
        if not EXPLICA.search(ctx):
            unexplained.append(j)
    for j in unexplained[:4]:
        pen("estilo", 1, "atencao", f"Termo técnico sem explicação perto da 1ª ocorrência: «{j}»")
    if not unexplained:
        ok("estilo", "Termos técnicos vêm acompanhados de explicação")
    tail = " ".join(paragraphs[-4:])
    chk("estilo", bool(ACAO.search(tail)), 3, "Fecha com ação concreta", "Sem ação concreta no final (padrão Yarivi: «Faça agora…»)")
    lw = len(lead.split())
    chk("estilo", 0 < lw <= 60, 3, f"Lead enxuto ({lw} palavras)", f"Lead com {lw} palavras (ideal até 60)")
    for a in manual.get("ajustes", {}).get("estilo", []):
        pen("estilo", abs(int(a["pontos"])), "atencao", f"Ajuste manual: {a['motivo']}")

    # ---------- UTILIDADE (15)
    lead_hit = bool(re.search(r"\d", lead)) or (kw and len(toks(kw) & toks(lead)) >= max(1, len(toks(kw)) - 1))
    chk("utilidade", bool(lead_hit) and lw > 0, 4, "Lead responde ao tema (dado ou palavra-chave logo no início)",
        "Lead não entrega a resposta/dado principal logo de cara")
    if len(h2s) >= 4:
        ok("utilidade", f"{len(h2s)} seções H2")
    elif len(h2s) == 3:
        pen("utilidade", 1, "atencao", "Só 3 seções H2 (ideal 4 ou mais)")
    else:
        pen("utilidade", 3, "atencao", f"Só {len(h2s)} seções H2")
    if fq >= 3:
        ok("utilidade", f"FAQ com {fq} perguntas")
    elif fq == 2:
        pen("utilidade", 1, "atencao", "FAQ com só 2 perguntas")
    else:
        pen("utilidade", 3, "atencao", f"FAQ com {fq} pergunta(s)")
    imgs = re.findall(r"<img\b[^>]*>", html, re.I)
    body_imgs = [i for i in imgs if "art-header" not in i]
    has_alt = any(re.search(r'alt=["\'][^"\']{15,}', i) for i in body_imgs)
    has_prompt = os.path.exists(os.path.join(BLOG_ROOT, "rascunhos", f"img-{slug}.md")) or sub == "artigos"
    if body_imgs and has_alt:
        ok("utilidade", "Imagem com alt-text descritivo")
    elif has_prompt:
        ok("utilidade", "Prompt de imagem (img-*.md) criado; <img> entra quando o .webp existir")
    else:
        pen("utilidade", 2, "atencao", "Sem imagem nem prompt de imagem (img-{slug}.md)")
    if 900 <= wc <= 2200:
        ok("utilidade", f"{wc} palavras")
    elif 700 <= wc < 900 or 2200 < wc <= 2800:
        pen("utilidade", 1, "atencao", f"{wc} palavras (faixa ideal 900–2.200)")
    else:
        pen("utilidade", 3, "atencao", f"{wc} palavras (fora da faixa 700–2.800)")
    others = other_articles_meta(slug)
    cannibal = []
    for s, (t, k) in others.items():
        if (kw and k and kw == k) or similarity(title, t) > 0.6:
            cannibal.append({"slug": s, "titulo": t, "keyword": k})
    if cannibal:
        pen("utilidade", 5, "atencao", "Possível canibalização: " + ", ".join(c["slug"] for c in cannibal[:3]))
    else:
        ok("utilidade", "Sem artigo com a mesma palavra-chave ou título parecido")
    for a in manual.get("ajustes", {}).get("utilidade", []):
        pen("utilidade", abs(int(a["pontos"])), "atencao", f"Ajuste manual: {a['motivo']}")

    cats = {k: {"nome": CAT_NAME[k], "max": CAT_MAX[k], "pontos": max(0, points[k]), "itens": items[k]} for k in CAT_MAX}
    score = sum(c["pontos"] for c in cats.values())
    aprovado = score >= APPROVAL_SCORE and not blockers
    return {
        "slug": slug, "origem": sub, "title": title, "h1": h1, "keyword": kw,
        "meta_description_len": len(desc), "word_count": wc, "reading_time": max(1, round(wc / 200)),
        "frases_antiplagio": sample_phrases, "links_externos": ext, "links_pendentes": pending,
        "fontes": sources, "canibalizacao": cannibal,
        "categorias": cats, "score": score, "bloqueantes": blockers,
        "aprovado": aprovado,
        "veredicto": "✅ APROVADO (nota ≥ 90, sem bloqueantes)" if aprovado else
                     "🔴 REPROVADO — corrigir e refazer o QA (exige nota ≥ 90 e zero bloqueantes)",
    }


# ---------------------------------------------------------------- relatório
OUT_DIR = os.path.join(BLOG_ROOT, "rascunhos")


def history_path(slug):
    return os.path.join(OUT_DIR, f"qa-{slug}.rodadas.json")


def write_report(res, manual):
    slug = res["slug"]
    hp = history_path(slug)
    hist = json.load(open(hp, encoding="utf-8")) if os.path.exists(hp) else []
    hist.append({"rodada": len(hist) + 1, "data": datetime.date.today().isoformat(), "score": res["score"],
                 "aprovado": res["aprovado"], "correcoes": manual.get("correcoes_rodada", [])})
    json.dump(hist, open(hp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    L = [f"# Relatório de QA — {slug}",
         f"*Gerado em {datetime.date.today().isoformat()} pela skill validador-text v2 (rodada {len(hist)})*", "",
         "## Veredicto", "", f"**Score: {res['score']}/100** — {res['veredicto']}", "",
         "| Categoria | Pontos |", "|---|---|"]
    for c in res["categorias"].values():
        L.append(f"| {c['nome']} | {c['pontos']}/{c['max']} |")
    L += ["", f"## 🔴 Bloqueantes ({len(res['bloqueantes'])})", ""]
    L += [f"- {b}" for b in res["bloqueantes"]] or ["*(nenhum)*"]
    atencao = [(c["nome"], i) for c in res["categorias"].values() for i in c["itens"] if i["nivel"] == "atencao"]
    L += ["", f"## 🟡 Atenção ({len(atencao)})", ""]
    L += [f"- **{n}** ({i['pontos']} pts): {i['texto']}" for n, i in atencao] or ["*(nenhum)*"]
    oks = [(c["nome"], i) for c in res["categorias"].values() for i in c["itens"] if i["nivel"] == "ok"]
    L += ["", f"## 🟢 OK ({len(oks)} itens)", ""] + [f"- {i['texto']}" for _, i in oks]
    d = manual.get("dados", {})
    L += ["", "## Auditoria de dados (passo 2.6)", "", "**Mantidos (com fonte):**"]
    L += [f"- {x}" for x in d.get("mantidos", [])] or ["- *(não informado)*"]
    L += ["", "**Removidos ou reescritos:**"] + ([f"- {x}" for x in d.get("removidos", [])] or ["- nenhum"])
    L += ["", "## Originalidade (antiplágio)", ""]
    if manual.get("plagio"):
        L += ["| Frase | Resultado |", "|---|---|"]
        L += [f"| {p['frase'][:110]} | {'⚠️ ' + p['match'] if p.get('match') else 'ORIGINAL'} |" for p in manual["plagio"]]
    else:
        L += ["Frases sugeridas para teste (WebSearch, entre aspas):"] + [f"- {s}" for s in res["frases_antiplagio"]]
    L += ["", "## Fontes", ""]
    for s in res["fontes"]:
        L.append(f"- {s['data'] or 'sem data'} ({s['precisao'] or '-'}) — {s['label'][:100]}")
    L += ["", "## Metadados", "", f"- Palavras: {res['word_count']} | Leitura: {res['reading_time']} min",
          f"- Title: `{res['title']}` ({len(res['title'])} chars) | Meta description: {res['meta_description_len']} chars",
          f"- Palavra-chave principal: {res['keyword'] or '—'}", "", "## Histórico de rodadas", "",
          "| Rodada | Data | Nota | Resultado | Correções aplicadas antes |", "|---|---|---|---|---|"]
    for h in hist:
        L.append(f"| {h['rodada']} | {h['data']} | {h['score']} | {'✅' if h['aprovado'] else '🔴'} | {'; '.join(h['correcoes']) or '—'} |")
    out = os.path.join(OUT_DIR, f"qa-{slug}.md")
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "Uso: python check_article.py <slug> [--manual arq.json] [--write]"}))
        sys.exit(1)
    slug = args[0]
    if "--out-dir" in args:
        OUT_DIR = args[args.index("--out-dir") + 1]
        os.makedirs(OUT_DIR, exist_ok=True)
    manual = {}
    if "--manual" in args:
        manual = json.load(open(args[args.index("--manual") + 1], encoding="utf-8"))
    res = analyze(slug, manual)
    if "--write" in args:
        res["relatorio"] = write_report(res, manual)
    print(json.dumps(res, ensure_ascii=False, indent=2, default=str))
