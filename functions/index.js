/**
 * Yarivi — Home ("/") com as manchetes direto no HTML
 *
 * O index.html já sai do repositório com as manchetes escritas no HTML
 * (para o Google e leitores sem JavaScript). Esta Function troca o conteúdo
 * de #hero-card-root, #featured-root e #latest-root pela lista atual (catálogo + KV), para a
 * home refletir na hora o que foi publicado via /api/publicar.
 *
 * Sem KV ou com erro → serve o index.html estático como está.
 *
 * Atenção: o _headers do Pages não é aplicado a respostas de Functions.
 * Por isso os cabeçalhos de segurança abaixo espelham o bloco "/*" do
 * _headers — ao mudar o CSP lá (ex.: AdSense), mude aqui também.
 */
import { heroHTML, featuredHTML, latestHTML, getVisibleArticles } from './_lib/home.js';

const SECURITY_HEADERS = {
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'DENY',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=(), accelerometer=(), gyroscope=(), magnetometer=()',
  'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self'; frame-src 'none'; frame-ancestors 'none'; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests",
};

function withSecurity(res) {
  const out = new Response(res.body, res);
  for (const [k, v] of Object.entries(SECURITY_HEADERS)) {
    if (!out.headers.has(k)) out.headers.set(k, v);
  }
  return out;
}

export async function onRequestGet(context) {
  const { request, env, next } = context;
  const asset = await next();

  const type = asset.headers.get('Content-Type') || '';
  if (!asset.ok || !type.includes('text/html')) return withSecurity(asset);

  let visible;
  try {
    visible = await getVisibleArticles(env, new URL(request.url).origin);
  } catch (err) {
    console.error('[yarivi/home]', err.message);
    return withSecurity(asset);
  }
  if (!visible || !visible.length) return withSecurity(asset);

  const hero = heroHTML(visible);
  const feat = featuredHTML(visible);
  const latest = latestHTML(visible);

  const rewritten = new HTMLRewriter()
    .on('#hero-card-root',     { element(el) { el.setInnerContent(hero, { html: true }); } })
    .on('#featured-root', { element(el) { el.setInnerContent(feat, { html: true }); } })
    .on('#latest-root',   { element(el) { el.setInnerContent(latest, { html: true }); } })
    .transform(asset);

  const res = withSecurity(rewritten);
  res.headers.set('Cache-Control', 'public, max-age=60');
  return res;
}
