/**
 * Yarivi — Cloudflare Pages Functions Middleware
 * Intercepta /partials/featured.html e /partials/latest.html e retorna HTML
 * dinâmico (catálogo + KV YARIVI_PUBLISHED). A renderização fica em
 * functions/_lib/home.js, compartilhada com functions/index.js (home).
 *
 * Se o KV não estiver configurado ou houver qualquer erro,
 * serve o arquivo estático original como fallback.
 */
import { featuredHTML, latestHTML, getVisibleArticles } from '../_lib/home.js';

export async function onRequest(context) {
  const { request, env, next } = context;
  const url = new URL(request.url);
  const path = url.pathname;

  if (path !== '/partials/featured.html' && path !== '/partials/latest.html') {
    return next();
  }

  try {
    const visible = await getVisibleArticles(env, url.origin);
    if (!visible) return next(); // KV não configurado → arquivo estático

    const html = path === '/partials/featured.html' ? featuredHTML(visible) : latestHTML(visible);
    return new Response(html, {
      headers: {
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'public, max-age=60',
      },
    });
  } catch (err) {
    console.error('[yarivi/partials-middleware]', err.message);
    return next();
  }
}
