/**
 * Yarivi — /llms.txt dinâmico
 * Lista só os artigos que já estão no ar (mesma regra do sitemap e da home:
 * data_pub <= hoje em São Paulo, ou liberados antes da hora no KV). Assim os
 * agendados entram no dia deles, sem novo deploy.
 * Em caso de erro, serve o llms.txt estático do repositório.
 */
import { getVisibleArticles } from './_lib/home.js';
import { llmsTXT } from './_lib/llms.js';

export async function onRequestGet(context) {
  const { request, env, next } = context;
  try {
    const artigos = await getVisibleArticles(env, new URL(request.url).origin);
    return new Response(llmsTXT(artigos), {
      headers: {
        'Content-Type': 'text/plain; charset=utf-8',
        'Cache-Control': 'public, max-age=3600',
      },
    });
  } catch (err) {
    console.error('[yarivi/llms]', err.message);
    return next();
  }
}
