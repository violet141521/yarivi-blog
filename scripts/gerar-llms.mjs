// Regenera llms.txt e ai-catalog.json estáticos (fallback) a partir de
// artigos/_catalog.json, com os artigos já no ar hoje (data_pub <= hoje em São
// Paulo). Em produção os dois são servidos por functions/llms.txt.js e
// functions/ai-catalog.json.js, que aplicam o mesmo filtro todo dia — estes
// arquivos só valem se a Function falhar.
// Uso: node scripts/gerar-llms.mjs   (rodar no push semanal, junto do sitemap)
import { readFileSync, writeFileSync } from 'node:fs';
import { llmsTXT, aiCatalogJSON } from '../functions/_lib/llms.js';
import { hojeBR, estaNoAr } from '../functions/_lib/datas.js';

const root = new URL('..', import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const { articles } = JSON.parse(readFileSync(root + 'artigos/_catalog.json', 'utf8'));
const hoje = hojeBR();
const noAr = articles.filter(a => estaNoAr(a, hoje));
writeFileSync(root + 'llms.txt', llmsTXT(noAr));
writeFileSync(root + 'ai-catalog.json', aiCatalogJSON(noAr));
console.log(`llms.txt e ai-catalog.json: ${noAr.length} artigos` +
  (articles.length > noAr.length ? ` (${articles.length - noAr.length} agendados ficaram de fora até a data)` : ''));
