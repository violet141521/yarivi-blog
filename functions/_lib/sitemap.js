/**
 * Yarivi — geração do sitemap.xml (compartilhado)
 * Usado por functions/sitemap.xml.js (dinâmico, filtra por data a cada dia)
 * e por scripts/gerar-sitemap.mjs (cópia estática de fallback no repositório).
 * Recebe só os artigos que já estão no ar, na ordem em que devem aparecer.
 */
const SITE = 'https://yarivi.com';

function url(loc, lastmod, changefreq, priority) {
  return `  <url>
    <loc>${SITE}${loc}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>${changefreq}</changefreq>
    <priority>${priority}</priority>
  </url>`;
}

export function sitemapXML(artigos, hoje) {
  const linhas = [
    url('/', hoje, 'daily', '1.0'),
    url('/sobre', hoje, 'monthly', '0.6'),
    ...artigos.map(a => url(`/artigos/${a.slug}`, a.data_pub, 'monthly', '0.8')),
    url('/contato', hoje, 'yearly', '0.5'),
    url('/privacidade', hoje, 'yearly', '0.5'),
    url('/termos', hoje, 'yearly', '0.3'),
  ];
  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${linhas.join('\n')}
</urlset>
`;
}
