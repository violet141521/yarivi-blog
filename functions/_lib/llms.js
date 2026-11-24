/**
 * Yarivi — llms.txt e ai-catalog.json (compartilhado)
 * Usado por functions/llms.txt.js e functions/ai-catalog.json.js (dinâmicos,
 * filtram por data a cada dia) e por scripts/gerar-llms.mjs (cópias estáticas
 * de fallback no repositório). Recebe só os artigos que já estão no ar.
 * Mesmo padrão do sitemap (functions/_lib/sitemap.js).
 */
const SITE = 'https://yarivi.com';

// Ordem das seções no llms.txt e rótulos por extenso
export const CATEGORIAS = [
  ['ai', 'Inteligência Artificial'],
  ['sec', 'Segurança digital'],
  ['mob', 'Celulares e mobile'],
  ['fut', 'Futuro e tendências'],
  ['sw', 'Software'],
  ['hw', 'Hardware'],
];
const LABEL = Object.fromEntries(CATEGORIAS);

const RESUMO = 'As principais notícias de IA, hardware, cibersegurança, software e mobile ' +
  'explicadas em português brasileiro — sem jargão, sem clickbait. Novo artigo todo dia útil.';
const DESCRICAO = 'Yarivi é um veículo de jornalismo tecnológico em PT-BR, lançado em agosto ' +
  'de 2026 e com foco no público brasileiro. Cobre inteligência artificial, celulares, ' +
  'segurança digital, hardware, software e tendências de tecnologia, sempre com linguagem acessível.';

const umaLinha = s => String(s ?? '').replace(/\s+/g, ' ').trim();
const textoLink = s => umaLinha(s).replace(/([\[\]])/g, '\\$1');

// Mais recente primeiro; mesma data mantém a ordem recebida (sort estável)
const recentes = artigos => [...artigos].sort((a, b) =>
  a.data_pub < b.data_pub ? 1 : a.data_pub > b.data_pub ? -1 : 0);

export function llmsTXT(artigos) {
  const linhas = ['# Yarivi', '', `> ${RESUMO}`, '', DESCRICAO, ''];
  const ordenados = recentes(artigos);
  const conhecidas = new Set(CATEGORIAS.map(([c]) => c));
  const secoes = [...CATEGORIAS];
  for (const a of ordenados) {
    if (!conhecidas.has(a.categoria)) { conhecidas.add(a.categoria); secoes.push([a.categoria, a.categoria]); }
  }
  for (const [cod, rotulo] of secoes) {
    const itens = ordenados.filter(a => a.categoria === cod);
    if (!itens.length) continue;
    linhas.push(`## ${rotulo}`, '');
    for (const a of itens) {
      linhas.push(`- [${textoLink(a.manchete)}](${SITE}/artigos/${a.slug}): ${umaLinha(a.excerpt)}`);
    }
    linhas.push('');
  }
  linhas.push(
    '## Páginas', '',
    `- [Início](${SITE}/): página inicial, com os artigos mais recentes e em destaque`,
    `- [Sobre e política editorial](${SITE}/sobre): quem faz o Yarivi, como os artigos são apurados e como pedir correções`,
    `- [Contato](${SITE}/contato): como falar com a redação do Yarivi`,
    `- [Política de Privacidade](${SITE}/privacidade)`,
    `- [Termos de Uso](${SITE}/termos)`,
    '',
    '## Optional', '',
    `- [Sitemap](${SITE}/sitemap.xml): lista completa de URLs do site`,
    `- [Catálogo estruturado](${SITE}/ai-catalog.json): catálogo dos artigos em JSON, para agentes e ferramentas de IA`,
    '',
  );
  return linhas.join('\n');
}

export function aiCatalog(artigos) {
  const ordenados = recentes(artigos);
  const items = ordenados.map(a => {
    const item = {
      title: umaLinha(a.manchete),
      url: `${SITE}/artigos/${a.slug}`,
      description: umaLinha(a.excerpt),
      category: LABEL[a.categoria] || a.categoria,
      categoryCode: a.categoria,
      datePublished: a.data_pub,
      readingTime: a.read_time,
      language: 'pt-BR',
    };
    if (a.img) item.image = SITE + a.img;
    return item;
  });
  return {
    name: 'Yarivi',
    url: SITE,
    description: 'Veículo de jornalismo tecnológico em português brasileiro — IA, celulares, ' +
      'segurança digital, hardware, software e tendências de tecnologia.',
    language: 'pt-BR',
    lastUpdated: ordenados[0]?.data_pub ?? null,
    itemCount: items.length,
    categories: CATEGORIAS.map(([code, label]) => ({ code, label })),
    items,
  };
}

export function aiCatalogJSON(artigos) {
  return JSON.stringify(aiCatalog(artigos), null, 2) + '\n';
}
