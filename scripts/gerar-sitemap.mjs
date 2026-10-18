// Regenera o sitemap.xml estático (fallback) a partir de artigos/_catalog.json,
// com os artigos já no ar hoje (data_pub <= hoje em São Paulo), na ordem do
// catálogo. Em produção /sitemap.xml é servido por functions/sitemap.xml.js,
// que aplica o mesmo filtro todo dia — este arquivo só vale se a Function falhar.
// Uso: node scripts/gerar-sitemap.mjs   (rodar no push semanal)
import { readFileSync, writeFileSync } from 'node:fs';
import { sitemapXML } from '../functions/_lib/sitemap.js';
import { hojeBR, estaNoAr } from '../functions/_lib/datas.js';

const root = new URL('..', import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const { articles } = JSON.parse(readFileSync(root + 'artigos/_catalog.json', 'utf8'));
const hoje = hojeBR();
const noAr = articles.filter(a => estaNoAr(a, hoje));
writeFileSync(root + 'sitemap.xml', sitemapXML(noAr, hoje));
console.log(`sitemap.xml: ${noAr.length} artigos + 5 páginas = ${noAr.length + 5} URLs` +
  (articles.length > noAr.length ? ` (${articles.length - noAr.length} agendados ficaram de fora até a data)` : ''));
