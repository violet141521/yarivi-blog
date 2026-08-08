/**
 * Yarivi — Cloudflare Pages Functions Middleware
 * Intercepta /partials/featured.html e /partials/latest.html
 * e retorna HTML dinâmico baseado em:
 *   - artigos/_catalog.json  → metadata de todos os artigos
 *   - KV YARIVI_PUBLISHED    → quais slugs estão visíveis na home
 *
 * Se o KV não estiver configurado ou houver qualquer erro,
 * serve o arquivo estático original como fallback.
 */

const CAT = {
  ai:  { label: 'IA & ML',   cls: 'tag-ai'  },
  hw:  { label: 'Hardware',  cls: 'tag-hw'  },
  mob: { label: 'Mobile',    cls: 'tag-mob' },
  sw:  { label: 'Software',  cls: 'tag-sw'  },
  sec: { label: 'Segurança', cls: 'tag-sec' },
  fut: { label: 'Futuro',    cls: 'tag-fut' },
};

function fmtDate(iso) {
  const [y, m, d] = iso.split('-').map(Number);
  const meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'];
  return `${d} ${meses[m - 1]} ${y}`;
}

function featuredHTML(arts) {
  if (!arts.length) return '';
  const [main, ...sides] = arts.slice(0, 5);
  const mc = CAT[main.categoria] || { label: main.categoria, cls: '' };

  const mainCard = `
        <a href="artigos/${main.slug}" class="feat-main fu" aria-label="Ler: ${main.manchete}">
            <div class="feat-img" aria-hidden="true">${main.emoji}</div>
            <div class="feat-body">
                <div class="tags">
                    <span class="tag ${mc.cls}">${mc.label}</span>
                    <span class="tag tag-dest">Análise</span>
                </div>
                <h2 class="art-title feat-title">${main.manchete}</h2>
                <p class="feat-excerpt">${main.excerpt}</p>
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
            <a href="artigos/${a.slug}" class="side-card fu">
                <div class="side-icon">${a.emoji}</div>
                <div>
                    <div class="tags">
                        <span class="tag ${sc.cls}">${sc.label}</span>
                    </div>
                    <div class="side-title">${a.manchete}</div>
                    <div class="side-meta">${fmtDate(a.data_pub)} · ${a.read_time}</div>
                </div>
            </a>`;
  }).join('');

  return `<div class="wrap section" id="em-destaque">
    <div class="sec-head fu">
        <h2 class="sec-title"><span class="sec-bar" aria-hidden="true"></span>Em destaque</h2>
        <a href="#" class="sec-link">Ver todos →</a>
    </div>

    <div class="featured-grid">
        ${mainCard}

        <div class="feat-sidebar">
            ${sideCards}
        </div>
    </div>
</div>`;
}

function latestHTML(arts) {
  if (!arts.length) return '';

  const cards = arts.map(a => {
    const cat = CAT[a.categoria] || { label: a.categoria, cls: '' };
    return `
        <a href="artigos/${a.slug}" class="art-card fu" data-category="${a.categoria}">
            <div class="card-thumb ${a.grad}">${a.emoji}</div>
            <div class="card-body">
                <div class="tags">
                    <span class="tag ${cat.cls}">${cat.label}</span>
                    <span class="tag tag-dest" style="margin-left:.25rem;">Análise</span>
                </div>
                <h3 class="art-title card-title">${a.manchete}</h3>
                <p class="art-excerpt card-excerpt">${a.excerpt}</p>
                <div class="art-meta" style="margin-top:.625rem;"><span>${fmtDate(a.data_pub)}</span><span class="sep">${a.read_time}</span></div>
            </div>
        </a>`;
  }).join('');

  return `<div class="wrap section" id="ultimas">
    <div class="sec-head fu">
        <h2 class="sec-title"><span class="sec-bar" aria-hidden="true"></span>Últimas notícias</h2>
        <a href="#" class="sec-link">Ver arquivo →</a>
    </div>

    <div class="latest-grid">
        ${cards}
    </div>
</div>`;
}

export async function onRequest(context) {
  const { request, env, next } = context;
  const path = new URL(request.url).pathname;

  // Só intercepta os dois partials dinâmicos; tudo mais passa para os arquivos estáticos
  if (path !== '/partials/featured.html' && path !== '/partials/latest.html') {
    return next();
  }

  // Fallback: KV não configurado ainda → serve arquivo estático (safe during setup)
  if (!env.YARIVI_PUBLISHED) {
    return next();
  }

  try {
    const origin = new URL(request.url).origin;

    // 1. Buscar catálogo (arquivo estático do mesmo Pages deployment)
    const catalogRes = await env.ASSETS.fetch(
      new Request(`${origin}/artigos/_catalog.json`)
    );
    if (!catalogRes.ok) throw new Error(`Catálogo HTTP ${catalogRes.status}`);
    const { articles } = await catalogRes.json();

    // 2. Buscar slugs publicados do KV (list retorna até 1000 keys)
    const kvList = await env.YARIVI_PUBLISHED.list();
    const published = new Set(kvList.keys.map(k => k.name));

    // 3. Filtrar visíveis e ordenar por data decrescente
    //    Artigos com mesma data mantêm a ordem do catálogo (sort estável)
    const visible = articles
      .filter(a => published.has(a.slug))
      .sort((a, b) => new Date(b.data_pub) - new Date(a.data_pub));

    // 4. Gerar HTML no formato exato dos partials estáticos
    const html = path === '/partials/featured.html'
      ? featuredHTML(visible)
      : latestHTML(visible);

    return new Response(html, {
      headers: {
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'public, max-age=60',  // 1 min — home atualiza logo após publicação
      },
    });
  } catch (err) {
    // Qualquer erro → serve arquivo estático como fallback
    console.error('[yarivi/partials-middleware]', err.message);
    return next();
  }
}
