/**
 * Yarivi — renderização das manchetes da home (compartilhado)
 * Usado por:
 *   - functions/index.js                 → injeta as manchetes direto no HTML da home ("/")
 *   - functions/partials/_middleware.js  → serve /partials/featured.html e /partials/latest.html
 *
 * Fonte dos dados:
 *   - artigos/_catalog.json  → metadata de todos os artigos
 *   - KV YARIVI_PUBLISHED    → quais slugs estão visíveis na home
 */

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

export function featuredHTML(arts) {
  if (!arts.length) return '';
  const [main, ...sides] = arts.slice(0, 5);
  const mc = CAT[main.categoria] || { label: main.categoria, cls: '' };

  const mainCard = `
        <a href="/artigos/${main.slug}" class="feat-main fu" aria-label="Ler: ${esc(main.manchete)}">
            <div class="feat-img" aria-hidden="true">${main.emoji}</div>
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
                <div class="side-icon">${a.emoji}</div>
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
            <div class="card-thumb ${a.grad}">${a.emoji}</div>
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
 * Lista de artigos visíveis na home (catálogo ∩ KV), mais recente primeiro.
 * Guarda o resultado no cache da borda por 60s para não gastar uma operação
 * "list" do KV a cada visita (o plano grátis do KV tem 1.000 lists/dia).
 * Retorna null se o KV não estiver configurado.
 */
export async function getVisibleArticles(env, origin) {
  if (!env.YARIVI_PUBLISHED) return null;

  const cache = typeof caches !== 'undefined' ? caches.default : null;
  const cacheKey = new Request(`${origin}/__yarivi-cache/home-visible-v1`);
  if (cache) {
    const hit = await cache.match(cacheKey);
    if (hit) return hit.json();
  }

  const catalogRes = await env.ASSETS.fetch(new Request(`${origin}/artigos/_catalog.json`));
  if (!catalogRes.ok) throw new Error(`Catálogo HTTP ${catalogRes.status}`);
  const { articles } = await catalogRes.json();

  const kvList = await env.YARIVI_PUBLISHED.list();
  const published = new Set(kvList.keys.map(k => k.name));

  // Artigos com mesma data mantêm a ordem do catálogo (sort estável)
  const visible = articles
    .filter(a => published.has(a.slug))
    .sort((a, b) => new Date(b.data_pub) - new Date(a.data_pub));

  if (cache) {
    await cache.put(cacheKey, new Response(JSON.stringify(visible), {
      headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=60' },
    }));
  }
  return visible;
}
