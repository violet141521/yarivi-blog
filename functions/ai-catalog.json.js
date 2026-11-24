/**
 * Yarivi — /ai-catalog.json dinâmico
 * Catálogo estruturado dos artigos que já estão no ar (mesma regra do sitemap
 * e da home). Em caso de erro, serve o ai-catalog.json estático do repositório.
 */
import { getVisibleArticles } from './_lib/home.js';
import { aiCatalogJSON } from './_lib/llms.js';

export async function onRequestGet(context) {
  const { request, env, next } = context;
  try {
    const artigos = await getVisibleArticles(env, new URL(request.url).origin);
    return new Response(aiCatalogJSON(artigos), {
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        'Cache-Control': 'public, max-age=3600',
      },
    });
  } catch (err) {
    console.error('[yarivi/ai-catalog]', err.message);
    return next();
  }
}
