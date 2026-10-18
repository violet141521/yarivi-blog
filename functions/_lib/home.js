/**
 * Yarivi — renderização das manchetes da home (compartilhado)
 * Usado por:
 *   - functions/index.js                 → injeta o card do hero e as manchetes direto no HTML da home ("/")
 *   - functions/partials/_middleware.js  → serve /partials/featured.html e /partials/latest.html
 *
 * Fonte dos dados:
 *   - artigos/_catalog.json  → metadata de todos os artigos
 *   - data_pub de cada artigo → aparece sozinho quando a data chega (fuso São Paulo)
 *   - KV YARIVI_PUBLISHED    → libera um slug antes da data (/api/publicar)
 */
import { hojeBR, estaNoAr } from './datas.js';

export const CAT = {
  ai:  { label: 'IA & ML',   cls: 'tag-ai'  },
  hw:  { label: 'Hardware',  cls: 'tag-hw'  },
  mob: { label: 'Mobile',    cls: 'tag-mob' },
  sw:  { label: 'Software',  cls: 'tag-sw'  },
  sec: { label: 'Segurança', cls: 'tag-sec' },
  fut: { label: 'Futuro',    cls: 'tag-fut' },
};

const esc = s => String(s ?? '')
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

export function fmtDate(iso) {
  const [y, m, d] = iso.split('-').map(Number);
  const meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'];
  return `${d} ${meses[m - 1]} ${y}`;
}

// Capa do artigo (campos img/thumb do catálogo); sem imagem, mostra o emoji
function cover(src, emoji, lazy = true) {
  if (!src) return emoji;
  return `<img src="${esc(src)}" alt="" width="1536" height="1024" decoding="async"${lazy ? ' loading="lazy"' : ''}>`;
}

// Card ao lado do título (hero): o último artigo publicado
export function heroHTML(arts) {
  const a = arts[0];
  if (!a) return '';
  const c = CAT[a.categoria] || { label: a.categoria, cls: '' };
  const img = a.img
    ? `<div class="hcard-img has-img" aria-hidden="true"><img src="${esc(a.img)}" alt="" width="1536" height="1024" decoding="async" fetchpriority="high"></div>`
    : `<div class="hcard-img ${a.grad}" aria-hidden="true"><span class="hcard-emoji">${a.emoji}</span></div>`;
  return `
                    <a href="/artigos/${a.slug}" class="hero-card" aria-label="Ler: ${esc(a.manchete)}">
                        ${img}
                        <div class="hcard-body">
                            <div class="tags">
                                <span class="tag ${c.cls}">${c.label}</span>
                                <span class="tag tag-dest">Mais recente</span>
                            </div>
                            <h2 class="art-title hcard-title">${esc(a.manchete)}</h2>
                            <p class="art-excerpt">${esc(a.excerpt)}</p>
                            <div class="art-meta">
                                <span>${fmtDate(a.data_pub)}</span>
                                <span class="sep">${a.read_time} de leitura</span>
                            </div>
                            <span class="read-link" aria-hidden="true">Ler artigo →</span>
                        </div>
                    </a>`;
}

// "Em destaque" começa no 2º artigo — o mais recente já está no card do hero
export function featuredHTML(arts) {
  arts = arts.slice(1);
  if (!arts.length) return '';
  const [main, ...sides] = arts.slice(0, 5);
  const mc = CAT[main.categoria] || { label: main.categoria, cls: '' };

  const mainCard = `
        <a href="/artigos/${main.slug}" class="feat-main fu" aria-label="Ler: ${esc(main.manchete)}">
            <div class="feat-img${main.img ? ' has-img' : ''}" aria-hidden="true">${cover(main.img, main.emoji, false)}</div>
            <div class="feat-body">
                <div class="tags">
                    <span class="tag ${mc.cls}">${mc.label}</span>
                    <span class="tag tag-dest">Análise</span>
                </div>
                <h2 class="art-title feat-title">${esc(main.manchete)}</h2>
                <p class="feat-excerpt">${esc(main.excerpt)}</p>
                <div class="art-meta">
                    <span>${fmtDate(main.data_pub)}</span>
                    <span class="sep">${main.read_time} de leitura</span>
                    <span class="sep">Novo</span>
                </div>
                <span class="read-link" aria-hidden="true">Ler análise completa →</span>
            </div>
        </a>`;

  const sideCards = sides.map(a => {
    const sc = CAT[a.categoria] || { label: a.categoria, cls: '' };
    return `
            <a href="/artigos/${a.slug}" class="side-card fu">
                <div class="side-icon${a.thumb ? ' has-img' : ''}" aria-hidden="true">${cover(a.thumb, a.emoji)}</div>
                <div>
                    <div class="tags">
                        <span class="tag ${sc.cls}">${sc.label}</span>
                    </div>
                    <div class="side-title">${esc(a.manchete)}</div>
                    <div class="side-meta">${fmtDate(a.data_pub)} · ${a.read_time}</div>
                </div>
            </a>`;
  }).join('');

  return `<div class="wrap section" id="em-destaque">
    <div class="sec-head fu">
        <h2 class="sec-title"><span class="sec-bar" aria-hidden="true"></span>Em destaque</h2>
        <a href="#ultimas" class="sec-link">Ver todos →</a>
    </div>

    <div class="featured-grid">
        ${mainCard}

        <div class="feat-sidebar">
            ${sideCards}
        </div>
    </div>
</div>`;
}

export function latestHTML(arts) {
  if (!arts.length) return '';

  const cards = arts.map(a => {
    const cat = CAT[a.categoria] || { label: a.categoria, cls: '' };
    return `
        <a href="/artigos/${a.slug}" class="art-card fu" data-category="${a.categoria}">
            <div class="card-thumb ${a.grad}${a.thumb ? ' has-img' : ''}" aria-hidden="true">${cover(a.thumb, a.emoji)}</div>
            <div class="card-body">
                <div class="tags">
                    <span class="tag ${cat.cls}">${cat.label}</span>
                    <span class="tag tag-dest" style="margin-left:.25rem;">Análise</span>
                </div>
                <h3 class="art-title card-title">${esc(a.manchete)}</h3>
                <p class="art-excerpt card-excerpt">${esc(a.excerpt)}</p>
                <div class="art-meta" style="margin-top:.625rem;"><span>${fmtDate(a.data_pub)}</span><span class="sep">${a.read_time}</span></div>
            </div>
        </a>`;
  }).join('');

  return `<div class="wrap section" id="ultimas">
    <div class="sec-head fu">
        <h2 class="sec-title"><span class="sec-bar" aria-hidden="true"></span>Últimas notícias</h2>
        <a href="#ultimas" class="sec-link">Ver arquivo →</a>
    </div>

    <div class="latest-grid">
        ${cards}
    </div>
</div>`;
}

/**
 * Lista de artigos visíveis na home, mais recente primeiro: data_pub <= hoje
 * (São Paulo) OU slug liberado no KV. Guarda o resultado no cache da borda por
 * 60s para não gastar uma operação "list" do KV a cada visita (o plano grátis
 * do KV tem 1.000 lists/dia). Sem KV configurado, vale só a regra da data.
 */
export async function getVisibleArticles(env, origin) {
  const hoje = hojeBR();
  const cache = typeof caches !== 'undefined' ? caches.default : null;
  const cacheKey = new Request(`${origin}/__yarivi-cache/home-visible-v2-${hoje}`);
  if (cache) {
    const hit = await cache.match(cacheKey);
    if (hit) return hit.json();
  }

  const catalogRes = await env.ASSETS.fetch(new Request(`${origin}/artigos/_catalog.json`));
  if (!catalogRes.ok) throw new Error(`Catálogo HTTP ${catalogRes.status}`);
  const { articles } = await catalogRes.json();

  let liberados = new Set();
  if (env.YARIVI_PUBLISHED) {
    try {
      const kvList = await env.YARIVI_PUBLISHED.list();
      liberados = new Set(kvList.keys.map(k => k.name));
    } catch (err) {
      console.error('[yarivi/home] KV indisponível, usando só a data:', err.message);
    }
  }

  // Artigos com mesma data mantêm a ordem do catálogo (sort estável)
  const visible = articles
    .filter(a => estaNoAr(a, hoje, liberados))
    .sort((a, b) => new Date(b.data_pub) - new Date(a.data_pub));

  if (cache) {
    await cache.put(cacheKey, new Response(JSON.stringify(visible), {
      headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=60' },
    }));
  }
  return visible;
}
