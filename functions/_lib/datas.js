/**
 * Yarivi — regra de visibilidade por data (compartilhado)
 *
 * Os artigos sobem em lote (1 push por semana), cada um com a sua própria
 * data_pub (1 por dia útil). Um artigo aparece na home e no sitemap quando:
 *   - a data_pub dele já chegou (data_pub <= hoje, fuso America/Sao_Paulo), ou
 *   - o slug foi liberado antes da hora no KV YARIVI_PUBLISHED (/api/publicar).
 */
export const FUSO = 'America/Sao_Paulo';

/** Data de hoje em São Paulo, formato AAAA-MM-DD. */
export function hojeBR(agora = new Date()) {
  return new Intl.DateTimeFormat('en-CA', {
    timeZone: FUSO, year: 'numeric', month: '2-digit', day: '2-digit',
  }).format(agora);
}

/** true se o artigo já pode aparecer (data chegou ou liberado no KV). */
export function estaNoAr(artigo, hoje = hojeBR(), liberados = new Set()) {
  return String(artigo.data_pub) <= hoje || liberados.has(artigo.slug);
}
