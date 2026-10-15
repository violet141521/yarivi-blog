// Regenera as manchetes escritas direto no index.html (#featured-root e #latest-root)
// a partir de artigos/_catalog.json, usando o mesmo HTML da Function da home.
// Considera publicado todo artigo do catálogo com arquivo em artigos/.
// Uso: node scripts/gerar-home-estatica.mjs   (rodar após cada publicação)
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { featuredHTML, latestHTML } from '../functions/_lib/home.js';

const root = new URL('..', import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const { articles } = JSON.parse(readFileSync(root + 'artigos/_catalog.json', 'utf8'));
const visible = articles
  .filter(a => existsSync(`${root}artigos/${a.slug}.html`))
  .sort((a, b) => new Date(b.data_pub) - new Date(a.data_pub));

function replaceInner(html, id, inner) {
  const open = html.indexOf(`<div id="${id}"`);
  if (open < 0) throw new Error(`#${id} não encontrado`);
  const start = html.indexOf('>', open) + 1;
  const re = /<div\b|<\/div>/g; re.lastIndex = start;
  let depth = 1, m;
  while ((m = re.exec(html))) { depth += m[0] === '</div>' ? -1 : 1; if (!depth) break; }
  if (depth) throw new Error(`#${id} sem fechamento`);
  return html.slice(0, start) + inner + '\n        ' + html.slice(m.index);
}

let html = readFileSync(root + 'index.html', 'utf8');
html = replaceInner(html, 'featured-root', featuredHTML(visible));
html = replaceInner(html, 'latest-root', latestHTML(visible));
writeFileSync(root + 'index.html', html);
console.log(`index.html: ${visible.length} artigos (mais recente: ${visible[0].slug})`);
