// Preenche os campos "img" e "thumb" de cada artigo em artigos/_catalog.json,
// usados pelos cards da home (functions/_lib/home.js).
//   img   -> capa original, achada no primeiro <img src="../img/..."> do artigo
//   thumb -> img/thumb/<arquivo> se existir (gerada por scripts/gerar-thumbs.py),
//            senão a própria capa
// Artigo sem imagem fica sem os campos e a home mostra o emoji.
// Chamado automaticamente por gerar-home-estatica.mjs; também roda sozinho.
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

const root = new URL('..', import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1');

export function sincronizarImagens() {
  const path = root + 'artigos/_catalog.json';
  const raw = readFileSync(path, 'utf8');
  const catalog = JSON.parse(raw);
  let comImg = 0;
  for (const a of catalog.articles) {
    delete a.img; delete a.thumb;
    const file = `${root}artigos/${a.slug}.html`;
    if (!existsSync(file)) continue;
    const m = readFileSync(file, 'utf8').match(/<img[^>]+src="\.\.\/img\/([^"\/]+)"/);
    if (!m || !existsSync(`${root}img/${m[1]}`)) continue;
    a.img = `/img/${m[1]}`;
    a.thumb = existsSync(`${root}img/thumb/${m[1]}`) ? `/img/thumb/${m[1]}` : a.img;
    comImg++;
  }
  const out = JSON.stringify(catalog, null, 2);
  if (out !== raw) writeFileSync(path, out);
  console.log(`_catalog.json: ${comImg}/${catalog.articles.length} artigos com imagem de capa`);
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) sincronizarImagens();
