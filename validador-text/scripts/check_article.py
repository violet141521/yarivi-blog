#!/usr/bin/env python3
"""
check_article.py — Análise técnica de artigo Yarivi para a skill validador-text.
Uso: python check_article.py <slug>
Saída: JSON com resultados de SEO, links, contagem de palavras e frases para antiplágio.
"""

import json
import re
import sys
import os
import urllib.request
import urllib.error
from collections import Counter

BLOG_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CATALOG_PATH = os.path.join(BLOG_ROOT, "artigos", "_catalog.json")

def load_html(slug):
    path = os.path.join(BLOG_ROOT, "rascunhos", f"{slug}.html")
    if not os.path.exists(path):
        print(json.dumps({"error": f"Arquivo não encontrado: {path}"}))
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def extract_tag(html, tag, attr=None, attr_val=None):
    """Extrai primeiro conteúdo de uma tag."""
    if attr and attr_val:
        pattern = rf'<{tag}[^>]*{attr}=["\']?{re.escape(attr_val)}["\']?[^>]*>(.*?)</{tag}>'
    else:
        pattern = rf'<{tag}[^>]*>(.*?)</{tag}>'
    m = re.search(pattern, html, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else ""

def extract_meta(html, name):
    pattern = rf'<meta[^>]*name=["\']?{re.escape(name)}["\']?[^>]*content=["\']([^"\']*)["\']'
    m = re.search(pattern, html, re.IGNORECASE)
    if not m:
        pattern = rf'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']?{re.escape(name)}["\']?'
        m = re.search(pattern, html, re.IGNORECASE)
    return m.group(1).strip() if m else ""

def extract_og(html, prop):
    pattern = rf'<meta[^>]*property=["\']?{re.escape(prop)}["\']?[^>]*content=["\']([^"\']*)["\']'
    m = re.search(pattern, html, re.IGNORECASE)
    return m.group(1).strip() if m else ""

def strip_html(html):
    """Remove todas as tags HTML, retorna texto limpo."""
    text = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', ' ', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&lt;', '<', text)
    text = re.sub(r'&gt;', '>', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_body_text(html):
    """Extrai texto do corpo do artigo, excluindo art-sources e byline."""
    # Remove seções que não fazem parte do corpo editorial
    html = re.sub(r'<div[^>]*class=["\'][^"\']*art-sources[^"\']*["\'].*?</div>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<div[^>]*class=["\'][^"\']*byline[^"\']*["\'].*?</div>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<nav[^>]*>.*?</nav>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<footer[^>]*>.*?</footer>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # Extrai apenas o conteúdo dentro de <article> ou <main> se existir
    art = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
    if art:
        html = art.group(1)
    return strip_html(html)

def extract_links(html):
    """Retorna (externos, internos) como listas de hrefs."""
    hrefs = re.findall(r'<a[^>]*href=["\']([^"\']+)["\']', html, re.IGNORECASE)
    external = [h for h in hrefs if h.startswith("http://") or h.startswith("https://")]
    internal = [h for h in hrefs if h.startswith("/artigos/") or h.startswith("../artigos/")]
    return external, internal

def extract_slug_from_href(href):
    m = re.search(r'artigos/([^./#?]+)(?:\.html)?', href)
    return m.group(1) if m else None

def check_http_status(url, timeout=10):
    """Verifica status HTTP de uma URL. Retorna (status_code, final_url)."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Yarivi-QA-Bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.url
    except urllib.error.HTTPError as e:
        return e.code, url
    except urllib.error.URLError:
        return 0, url  # 0 = timeout/DNS fail
    except Exception:
        return -1, url

def check_faq_schema(html):
    """Verifica presença de FAQPage no JSON-LD."""
    scripts = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
                         html, re.DOTALL | re.IGNORECASE)
    for s in scripts:
        if "FAQPage" in s:
            return True
    return False

def extract_sample_phrases(text, n=5, min_words=15, max_words=25):
    """Extrai n frases do miolo do texto para antiplágio."""
    # Divide em sentenças por pontuação
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Filtra pelo comprimento em palavras
    candidates = []
    for s in sentences:
        words = s.split()
        if min_words <= len(words) <= max_words:
            candidates.append(s.strip())
    # Pega do miolo (evita lead e conclusão)
    if len(candidates) <= n:
        return candidates
    start = len(candidates) // 4
    end = 3 * len(candidates) // 4
    pool = candidates[start:end]
    # Distribui uniformemente
    step = max(1, len(pool) // n)
    return [pool[i * step] for i in range(min(n, len(pool)))]

def word_overlap_similarity(title1, title2):
    """Similaridade por sobreposição de palavras significativas (ignora stopwords)."""
    stopwords = {"de", "do", "da", "dos", "das", "em", "para", "com", "por", "que", "e",
                 "o", "a", "os", "as", "um", "uma", "no", "na", "nos", "nas", "se", "ao",
                 "às", "como", "mais", "ou", "mas", "nem", "são", "é", "foi", "será"}
    def words(t):
        return set(w.lower() for w in re.split(r'\W+', t) if w and w.lower() not in stopwords and len(w) > 2)
    w1, w2 = words(title1), words(title2)
    if not w1 or not w2:
        return 0.0
    return len(w1 & w2) / max(len(w1), len(w2))

def load_catalog():
    if not os.path.exists(CATALOG_PATH):
        return []
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("articles", [])

def check_seo(html, title, h1, meta_desc, body_text, internal_links):
    checks = {}

    # R5.1 title ≤ 60 chars
    checks["title_length"] = {"pass": len(title) <= 60, "value": len(title), "detail": f"{len(title)} chars"}

    # R5.2 title termina com | Yarivi
    checks["title_yarivi"] = {"pass": "yarivi" in title.lower(), "detail": ""}

    # R5.3 h1 != title (ignorando pipes e sufixos)
    title_clean = re.sub(r'\s*\|.*$', '', title).strip().lower()
    checks["h1_ne_title"] = {"pass": h1.lower()[:60] != title_clean[:60], "detail": ""}

    # R5.4 meta description
    checks["meta_desc_present"] = {"pass": bool(meta_desc), "detail": ""}
    checks["meta_desc_length"] = {"pass": len(meta_desc) <= 155, "value": len(meta_desc), "detail": f"{len(meta_desc)} chars"}

    # R5.5 FAQ schema
    checks["faq_schema"] = {"pass": check_faq_schema(html), "detail": ""}

    # R5.6 sem placeholders
    placeholders = re.findall(r'\[\.\.\.\]|TODO|PLACEHOLDER|\[inserir\]', body_text, re.IGNORECASE)
    checks["no_placeholders"] = {"pass": len(placeholders) == 0, "detail": f"Encontrados: {placeholders}" if placeholders else ""}

    # R5.7 ao menos 1 link interno
    checks["internal_link_exists"] = {"pass": len(internal_links) >= 1, "detail": f"{len(internal_links)} encontrado(s)"}

    # R5.8 article:published_time
    pub_time = extract_og(html, "article:published_time")
    checks["published_time"] = {"pass": bool(pub_time), "detail": pub_time or "ausente"}

    return checks

def run(slug):
    html = load_html(slug)
    catalog = load_catalog()
    catalog_slugs = {a["slug"] for a in catalog}
    catalog_titles = [(a["slug"], a.get("manchete", "")) for a in catalog]

    title = strip_html(extract_tag(html, "title"))
    h1 = strip_html(extract_tag(html, "h1"))
    meta_desc = extract_meta(html, "description")
    body_text = extract_body_text(html)
    word_count = len(body_text.split())
    reading_time = max(1, round(word_count / 200))
    external_links, internal_links = extract_links(html)

    # SEO checks
    seo_checks = check_seo(html, title, h1, meta_desc, body_text, internal_links)

    # Link status
    link_status = []
    for url in set(external_links):
        status, final_url = check_http_status(url)
        link_status.append({"url": url, "status": status, "final_url": final_url})

    # Internal link validation
    internal_link_issues = []
    for href in internal_links:
        s = extract_slug_from_href(href)
        if s and s not in catalog_slugs:
            internal_link_issues.append({"href": href, "slug": s})

    # Duplicate title detection
    duplicate_candidates = []
    for cat_slug, cat_title in catalog_titles:
        if cat_slug != slug:
            sim = word_overlap_similarity(title, cat_title)
            if sim > 0.70:
                duplicate_candidates.append({"slug": cat_slug, "title": cat_title, "similarity": round(sim, 2)})

    # Sample phrases for plagiarism check
    sample_phrases = extract_sample_phrases(body_text)

    result = {
        "slug": slug,
        "title": title,
        "title_len": len(title),
        "h1": h1,
        "meta_description": meta_desc,
        "meta_desc_len": len(meta_desc),
        "word_count": word_count,
        "reading_time": reading_time,
        "external_links": external_links,
        "internal_links": internal_links,
        "seo_checks": seo_checks,
        "link_status": link_status,
        "internal_link_issues": internal_link_issues,
        "duplicate_candidates": duplicate_candidates,
        "sample_phrases": sample_phrases,
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Uso: python check_article.py <slug>"}))
        sys.exit(1)
    run(sys.argv[1])
