/**
 * Yarivi — /sitemap.xml dinâmico
 * Lista só os artigos que já estão no ar (data_pub <= hoje em São Paulo, ou
 * liberados antes da hora no KV). Assim os artigos com data futura, que sobem
 * no push semanal, só entram no sitemap no dia deles — sem novo deploy.
 * Em caso de erro, serve o sitemap.xml estático do repositório.
 */
import { getVisibleArticles } from './_lib/home.js';
import { sitemapXML } from './_lib/sitemap.js';
import { hojeBR } from './_lib/datas.js';

export async function onRequestGet(context) {
  const { request, env, next } = context;
  try {
    const artigos = await getVisibleArticles(env, new URL(request.url).origin);
    return new Response(sitemapXML(artigos, hojeBR()), {
      headers: {
        'Content-Type': 'application/xml; charset=utf-8',
        'Cache-Control': 'public, max-age=3600',
      },
    });
  } catch (err) {
    console.error('[yarivi/sitemap]', err.message);
    return next();
  }
}
