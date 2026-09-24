# Relatório de QA — banco-digital-vs-tradicional-2026
*Gerado em 2026-09-09 pela skill validador-text · atualizado em 2026-09-09 (re-checagem)*

---

## Veredicto

**Score: 100/100** — ✅ Aprovado

---

## 🔴 Bloqueantes (0)

Nenhum.

---

## 🟡 Atenção (0)

Nenhum item de atenção pendente. (Ver "Correções aplicadas nesta re-checagem" abaixo — os dois pontos da versão anterior do relatório foram resolvidos, não apenas explicados.)

---

## 🟢 OK (9 itens)

1. Title ≤60 chars, keyword no início, termina " | Yarivi" — 59 chars
2. H1 ≠ title (manchete com gancho, título SEO separado)
3. Meta description ≤155 chars — 143 chars
4. Schema FAQPage presente e com as 5 perguntas espelhadas
5. `article:published_time` = 2026-09-09 (data de publicação combinada, não a de escrita)
6. 2 links internos, ambos apontando para artigos que existem em `artigos/` (`golpes-app-banco-pix-como-se-proteger-2026`, `gerenciador-de-senhas-como-funciona-2026`), sem `.html`
7. 6 fontes externas em `art-sources`, todas Tier A/B, **6/6 verificadas ao vivo via WebFetch nesta sessão** — nenhuma quebrada
8. `data-callout` + `stat-row` presentes, com números reais e fonte nomeada
9. Nenhum placeholder real de template (`no_placeholders` passa; ver correção do script abaixo)

---

## Correções aplicadas nesta re-checagem

1. **Bug no script corrigido**: `validador-text/scripts/check_article.py` usava a regex `TODO` com `re.IGNORECASE`, que casava com a palavra portuguesa comum "todo"/"todos" e gerava falso positivo em `no_placeholders`. Corrigido para `\bTODO\b` / `\bPLACEHOLDER\b`, sem ignorecase — agora só casa com marcadores reais de placeholder. A correção vale para todas as futuras rodadas de QA do blog, não só este artigo.
2. **Link quebrado encontrado e substituído**: o link da Agência Brasil (`.../fgc-inicia-pagamento-de-clientes-do-banco-master-com-ate-r-250-mil`) passou a retornar "Página temporariamente indisponível" (restrição de legislação eleitoral no domínio ebc.com.br). Substituído pela mesma notícia, mesma data e conteúdo, na fonte espelho **PE Jornal** (`pejornal.com.br/fgc-inicia-pagamento-de-clientes-do-banco-master-com-ate-r-250-mil/`), verificada via WebFetch: confirma o limite de R$ 250 mil por CPF/CNPJ por conglomerado financeiro.

---

## Detalhamento por categoria

### Originalidade (antiplágio)
- Método: busca de frases exatas entre aspas via WebSearch
- Frases testadas: 5
- Resultado: **5/5 ORIGINAL**

| Frase | Resultado |
|-------|-----------|
| "o FGC entra em ação, como mostrou o caso Master" | ORIGINAL |
| "a regulação está empurrando quem usa esse nome a sustentar a licença completa" | ORIGINAL |
| "O FGC protege contra a quebra da instituição financeira, não contra fraude ou golpe" | ORIGINAL |
| "distribuídos em massa por plataformas digitais — que atraiu grande parte dos clientes do Banco Master" | ORIGINAL |
| "Na prática, isso significa que ser chamado de banco está deixando de bastar" | ORIGINAL |

### Links
- Externos verificados: 6/6 — todos via WebFetch nesta sessão, com conteúdo lido e conferido contra a citação no artigo
- Internos verificados: 2/2 — arquivos existem em `artigos/`

| Link | Tipo | Status |
|------|------|--------|
| fgc.org.br/sobre-garantia-fgc | Externo | ✅ Confirmado via WebFetch |
| agenciabrasil.ebc.com.br (…fgc-ja-pagou…) | Externo | ✅ Confirmado via WebFetch |
| pejornal.com.br (…fgc-inicia-pagamento…) | Externo | ✅ Confirmado via WebFetch — **substituiu link quebrado da Agência Brasil** |
| portal.febraban.org.br/noticia/4381 | Externo | ✅ Confirmado via WebFetch |
| poder360.com.br (…golpes-causaram-prejuizo…) | Externo | ✅ Confirmado via WebFetch |
| finsidersbrasil.com.br (…nubank-vai-pedir-licenca…) | Externo | ✅ Confirmado via WebFetch |
| ../artigos/golpes-app-banco-pix-como-se-proteger-2026 | Interno | ✅ Arquivo existe em `artigos/` |
| ../artigos/gerenciador-de-senhas-como-funciona-2026 | Interno | ✅ Arquivo existe em `artigos/` |

**Nota sobre o ambiente**: o script `check_article.py` continua sem conseguir validar status HTTP a partir do shell do computador da usuária (proxy de rede restrito). Isso não afeta o score — a validação de todos os links foi feita manualmente via WebFetch (rede própria do Claude, sem essa restrição) e está documentada acima.

### SEO automático
| Check | Resultado | Detalhe |
|-------|-----------|---------|
| title_length | ✅ | 59 chars |
| title_yarivi | ✅ | termina " | Yarivi" |
| h1_ne_title | ✅ | H1 é manchete com gancho, diferente do title |
| meta_desc_present | ✅ | presente |
| meta_desc_length | ✅ | 143 chars |
| faq_schema | ✅ | presente, 5 perguntas |
| no_placeholders | ✅ | passa após correção do script |
| internal_link_exists | ✅ | 2 encontrados |
| published_time | ✅ | 2026-09-09 |

### Metadados
- Palavras no corpo: 1544
- Tempo de leitura estimado: 8 min
- Title: `Banco Digital vs Banco Tradicional: qual é seguro? | Yarivi` (59 chars)
- Meta description: 143 chars

---

## Recomendações

Nenhuma correção pendente. O artigo está pronto para revisão da Mi.

---

## Auditoria de dados (CLAUDE.md, passo 2.6)

Todos os números, percentuais e datas do artigo foram checados contra fonte via WebSearch/WebFetch. Nenhum dado foi inventado, aproximado ou deixado pendente.

### Dados mantidos (com fonte)

| Dado no artigo | Fonte |
|---|---|
| FGC garante até R$ 250 mil por CPF/CNPJ, por instituição ou conglomerado | fgc.org.br — "Sobre a garantia FGC" |
| Banco Master: liquidação decretada pelo Banco Central em novembro de 2025 | Agência Brasil (29/01/2026) e barbieriadvogados.com |
| FGC pagou R$ 32,5 bilhões a 75% dos ~773 mil credores do Banco Master até 29/01/2026 | Agência Brasil — "FGC já pagou R$ 32,5 bilhões a 75% dos credores do Banco Master" (29/01/2026) |
| 174 mil casos do "golpe da falsa venda" no 1º semestre de 2025, alta de 314% vs. 1º semestre de 2024 | Febraban — portal.febraban.org.br/noticia/4381 |
| R$ 10,1 bilhões em prejuízo com golpes financeiros digitais no Brasil em 2024 | Febraban, via Poder360 |
| Resolução Conjunta nº 17 (Banco Central + CMN, publicada em 2/12/2025) proíbe uso da palavra "banco" sem licença bancária plena | Finsiders Brasil + log.law |
| Nubank anunciou em 3/12/2025 que vai buscar licença bancária completa em 2026 | Finsiders Brasil + em.com.br |
| Nubank tem 110 milhões de clientes no Brasil | Finsiders Brasil |
| CDBs do Banco Master, com retorno acima do mercado, distribuídos via plataformas digitais | Correio Braziliense — "XP, BTG e Nubank distribuíram CDBs do Banco Master" (11/2025) |

### Dados removidos ou não incluídos (sem fonte confiável o suficiente)

- **"R$ 1 milhão a cada 4 anos" (teto adicional do FGC)**: só em fonte secundária, não confirmado em fgc.org.br. Removido do artigo.
- **"Saldo do Nubank vira RDB automaticamente com FGC"**: fonte única e conflitante com dado mais recente sobre as licenças do Nubank. Não incluído.
- **Comparação numérica de taxa de fraude "banco digital vs. tradicional"**: não existe dado assim sourceado. O artigo trata o risco de golpe como igual para os dois modelos.
