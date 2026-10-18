// Regenera as manchetes escritas direto no index.html (#hero-card-root, #featured-root e #latest-root)
// a partir de artigos/_catalog.json, usando o mesmo HTML da Function da home.
// Considera no ar todo artigo do catálogo com arquivo em artigos/ e data_pub <= hoje
// (São Paulo) — os agendados para dias seguintes ficam de fora; a Function da home
// mostra cada um sozinha quando a data chega.
// Antes, sincroniza as capas (campos img/thumb) no catálogo — ver sincronizar-imagens.mjs.
// Uso: node scripts/gerar-home-estatica.mjs   (rodar após cada publicação)
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { heroHTML, featuredHTML, latestHTML } from '../functions/_lib/home.js';
import { hojeBR, estaNoAr } from '../functions/_lib/datas.js';
import { sincronizarImagens } from './sincronizar-imagens.mjs';

sincronizarImagens();

const root = new URL('..', import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const { articles } = JSON.parse(readFileSync(root + 'artigos/_catalog.json', 'utf8'));
const visible = articles
  .filter(a => existsSync(`${root}artigos/${a.slug}.html`) && estaNoAr(a, hojeBR()))
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
html = replaceInner(html, 'hero-card-root', heroHTML(visible));
html = replaceInner(html, 'featured-root', featuredHTML(visible));
html = replaceInner(html, 'latest-root', latestHTML(visible));
writeFileSync(root + 'index.html', html);

// Versão do style.css no link (?v=hash) — o navegador guarda o CSS por 24h (_headers);
// com a versão no link, ele baixa o novo assim que o arquivo muda.
const cssV = createHash('md5').update(readFileSync(root + 'style.css')).digest('hex').slice(0, 8);
for (const f of ['index.html', 'sobre.html', '404.html']) {
  const page = readFileSync(root + f, 'utf8');
  const out = page.replace(/href="\/style\.css(\?v=[^"]*)?"/g, `href="/style.css?v=${cssV}"`);
  if (out !== page) writeFileSync(root + f, out);
}
console.log(`index.html: ${visible.length} artigos (mais recente: ${visible[0].slug})`);
