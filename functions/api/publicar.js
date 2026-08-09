/**
 * Yarivi — Endpoint de publicação via URL
 * GET /api/publicar?slug=[slug]&key=[PUBLISH_KEY]
 *
 * Adiciona o slug ao KV YARIVI_PUBLISHED → artigo aparece na home imediatamente.
 * Funciona em qualquer navegador (celular, tablet, PC) sem precisar do Claude.
 *
 * Variáveis de ambiente necessárias (configurar no Cloudflare Pages):
 *   PUBLISH_KEY       → senha secreta (Environment variable)
 *   YARIVI_PUBLISHED  → KV namespace binding
 */

function page(title, icon, msg, detail = '') {
  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>${title} — Yarivi</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:system-ui,-apple-system,sans-serif;background:#0f1117;color:#e2e8f0;
      display:flex;align-items:center;justify-content:center;min-height:100vh;padding:1.25rem}
    .card{background:#1a1f2e;border:1px solid #2d3748;border-radius:16px;
      padding:2rem 1.75rem;max-width:460px;width:100%;text-align:center}
    .icon{font-size:2.75rem;margin-bottom:1rem}
    h1{font-size:1.35rem;font-weight:700;margin-bottom:.625rem}
    p{color:#94a3b8;line-height:1.6;font-size:.95rem}
    .detail{font-size:.85rem;background:#0f1117;border:1px solid #2d3748;
      border-radius:8px;padding:.5rem .75rem;color:#34d399;margin-top:.75rem;
      word-break:break-word;line-height:1.5}
    .home{color:#34d399;text-decoration:none;display:inline-block;
      margin-top:1.5rem;font-size:.9rem;border:1px solid #2d3748;
      border-radius:8px;padding:.5rem 1rem}
    .home:hover{background:#2d3748}
  </style>
</head>
<body>
  <div class="card">
    <div class="icon">${icon}</div>
    <h1>${title}</h1>
    <p>${msg}</p>
    ${detail ? `<p class="detail">${detail}</p>` : ''}
    <a class="home" href="https://yarivi.com">← Ir para o blog</a>
  </div>
</body>
</html>`;
}

function resp(html, status = 200) {
  return new Response(html, {
    status,
    headers: { 'Content-Type': 'text/html; charset=utf-8' },
  });
}

export async function onRequestGet(context) {
  const { request, env } = context;
  const url   = new URL(request.url);
  const slug  = url.searchParams.get('slug')?.trim();
  const key   = url.searchParams.get('key');

  // — Validar chave —
  if (!env.PUBLISH_KEY || !key || key !== env.PUBLISH_KEY) {
    return resp(page('Acesso negado', '🔒',
      'Chave de publicação inválida ou ausente.'), 401);
  }

  // — Validar slug —
  if (!slug) {
    return resp(page('Parâmetro ausente', '⚠️',
      'Adicione <code>?slug=nome-do-artigo</code> na URL e tente novamente.'), 400);
  }

  // — Verificar se o slug existe no catálogo —
  let article;
  try {
    const catalogRes = await env.ASSETS.fetch(
      new Request(`${url.origin}/artigos/_catalog.json`)
    );
    if (!catalogRes.ok) throw new Error(`HTTP ${catalogRes.status}`);
    const { articles } = await catalogRes.json();
    article = articles.find(a => a.slug === slug);
  } catch (err) {
    return resp(page('Erro ao ler catálogo', '❌',
      'Não foi possível acessar o catálogo de artigos. Tente novamente em instantes.',
      err.message), 500);
  }

  if (!article) {
    return resp(page('Artigo não encontrado', '🔍',
      'Esse slug não existe no catálogo. Verifique se o artigo foi committado e o <code>_catalog.json</code> atualizado.',
      slug), 404);
  }

  // — Verificar se já foi publicado —
  const existing = await env.YARIVI_PUBLISHED.get(slug);
  if (existing) {
    return resp(page('Já publicado', 'ℹ️',
      'Este artigo já está visível na home do Yarivi.',
      article.manchete));
  }

  // — Publicar! —
  await env.YARIVI_PUBLISHED.put(slug, 'true');

  return resp(page('Publicado! 🎉', '✅',
    'O artigo agora está visível na home do Yarivi. A home atualiza em até 1 minuto (cache).',
    article.manchete));
}
