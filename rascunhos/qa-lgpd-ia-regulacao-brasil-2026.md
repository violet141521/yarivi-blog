# Relatório de QA — lgpd-ia-regulacao-brasil-2026
*Gerado em 2026-09-09 pela skill validador-text · atualizado em 2026-09-09 (re-checagem)*

---

## Veredicto

**Score: 100/100** — ✅ Aprovado

---

## 🔴 Bloqueantes (0)

*(nenhum)*

---

## 🟡 Atenção (0)

O ponto de atenção da versão anterior foi resolvido, não apenas explicado — ver "Correções aplicadas" abaixo.

---

## 🟢 OK (10 itens)

- Title ≤ 60 chars, termina " | Yarivi", keyword no início
- H1 ≠ title, com gancho de curiosidade e número verificável
- Meta description 142 chars, com keyword e promessa clara
- Slug contém keyword principal
- Schema `NewsArticle` completo
- Schema `FAQPage` presente e coerente com as 4 perguntas do corpo
- 2 links internos válidos (`reconhecimento-facial-brasil-2026`, `plano-brasileiro-inteligencia-artificial-pbia-2026`)
- `article:published_time` = 2026-09-09
- Nenhum placeholder real de template (`no_placeholders` passa após correção do script)
- 10 fontes externas em `art-sources` (9 originais + 1 adicionada nesta re-checagem), **10/10 verificadas**, nenhuma quebrada

---

## Correções aplicadas nesta re-checagem

1. **Bug no script corrigido**: `TODO` com `re.IGNORECASE` casava com "todos"/"todo sistema" (português). Corrigido para `\bTODO\b` sem ignorecase — vale para toda a fila, não só este artigo.
2. **Link quebrado encontrado e substituído**: `gov.br/anpd/.../sancoes-administrativas-o-que-muda-apos-1o-de-agosto-de-2021` retornava erro 401. Substituído pela fonte espelho **LGPD Brasil** (`lgpdbrasil.com.br/sancoes-administrativas-o-que-muda-apos-1o-de-agosto-de-2021/`), verificada via WebFetch: confirma a mesma data (1º/08/2021) de entrada em vigor das sanções administrativas.
3. **Fonte adicional para o nome da empresa multada**: o artigo cita "Telekall Infoservice" como a microempresa multada pela ANPD em julho/2023, mas a fonte original (Turivius) não nomeia a empresa explicitamente — só o setor (telemarketing) e o valor. Adicionada uma segunda fonte, **Tecnoblog** (`tecnoblog.net/noticias/anpd-estreia-multa-por-violacao-da-lgpd-e-pune-empresa-de-telemarketing/`), que nomeia "Telekall Infoservice" e confirma o valor de R$ 14,4 mil — agora o dado específico do nome da empresa tem fonte direta, não só inferência.

---

## Detalhamento por categoria

### Originalidade (antiplágio)
- Método: 5 frases de 15-25 palavras retiradas do corpo, buscadas entre aspas duplas via WebSearch
- Frases testadas: 5
- Resultado: **5/5 ORIGINAL**

| Frase | Resultado |
|-------|-----------|
| "Ao mesmo tempo, a ANPD vem publicando notas técnicas, abrindo consultas públicas e sinalizando fiscalização mais ativa sobre IA." | ✅ ORIGINAL |
| "A Câmara criou uma Comissão Especial em 20 de maio de 2025, sob relatoria do deputado Aguinaldo Ribeiro." | ✅ ORIGINAL |
| "Não há levantamento mais recente e igualmente verificável disponível, mas o cenário de baixa adequação é coerente com o número de multas até hoje." | ✅ ORIGINAL |
| "Liste cada ferramenta de IA usada na empresa e o que ela processa: nome, e-mail, comportamento de compra, currículo, imagem." | ✅ ORIGINAL |
| "Se um sistema aprova, nega ou classifica alguém automaticamente, tenha um processo simples de contestação com revisão humana." | ✅ ORIGINAL |

### Links
- Externos no artigo: 10 (9 originais + 1 adicionada nesta re-checagem)
- Verificação manual (WebFetch nesta sessão): **10/10 abriram com conteúdo válido**, nenhuma quebrada

| Link | Status |
|------|--------|
| senado.leg.br (PL 2338/2023) | ✅ Confirmado |
| lgpdbrasil.com.br (sanções 1º/08/2021) | ✅ Confirmado — **substituiu link 401 do gov.br/anpd** |
| lefosse.com (Nota Técnica 12/2025) | ✅ Confirmado |
| pessoaepessoa.com.br (zero multas 2024) | ✅ Confirmado |
| turivius.com (multas LGPD) | ✅ Confirmado |
| tecnoblog.net (Telekall Infoservice) | ✅ Confirmado — **adicionada para nomear a empresa multada** |
| diap.org.br (Comissão Especial/Aguinaldo Ribeiro) | ✅ Confirmado |
| desinformante.com.br (votação adiada p/ 2026) | ✅ Confirmado |
| confidata.com.br (agenda regulatória 2026-2027) | ✅ Confirmado |
| la.logicalis.com (36% aderência LGPD) | ✅ Confirmado |

- Internos verificados: 2/2 — arquivos existem em `artigos/`

### SEO automático
| Check | Resultado | Detalhe |
|-------|-----------|---------|
| title_length | ✅ pass | 46 chars |
| title_yarivi | ✅ pass | termina " \| Yarivi" |
| h1_ne_title | ✅ pass | H1 diferente do title |
| meta_desc_present | ✅ pass | — |
| meta_desc_length | ✅ pass | 142 chars |
| faq_schema | ✅ pass | — |
| no_placeholders | ✅ pass | — |
| internal_link_exists | ✅ pass | 2 encontrados |
| published_time | ✅ pass | 2026-09-09 |

### Metadados
- Palavras no corpo: 1397
- Tempo de leitura estimado: 7 min
- Title: `LGPD e IA: o que muda pro seu negócio | Yarivi` (46 chars)
- Meta description: 142 chars

---

## Auditoria de dados (obrigatória — CLAUDE.md 2.6)

Todos os números, datas e percentuais do artigo foram verificados via WebSearch/WebFetch. Nenhum dado foi inventado, aproximado ou deixado pendente.

### ✅ Dados mantidos (com fonte verificada)

| Dado | Fonte |
|---|---|
| Sanções administrativas da LGPD (arts. 52-54) em vigor desde 1º/08/2021 | LGPD Brasil (fonte espelho, link oficial estava fora do ar) |
| Única multa em dinheiro da ANPD a empresa privada: R$ 14.400 (2× R$ 7.200), Telekall Infoservice, julho/2023 | Pessoa e Pessoa Advogados + **Tecnoblog** (nomeia a empresa) + Turivius |
| Zero multas em dinheiro contra empresa privada em 2024 | Pessoa e Pessoa Advogados |
| PL 2338/2023 aprovado pelo Senado em 10/12/2024, remetido à Câmara em 17/03/2025 | Senado Federal — tramitação oficial |
| Comissão Especial da Câmara instalada em 20/05/2025, relator dep. Aguinaldo Ribeiro | DIAP |
| Votação adiada de 2025 para 2026 por impasses políticos | Desinformante (19/12/2025), Confidata (18/04/2026) |
| Nota Técnica nº 12/2025/CON1/CGN/ANPD, publicada em 15/05/2025 | Lefosse Advogados |
| Artigo 20 da LGPD — direito de revisão de decisão automatizada | Texto da LGPD, citado via Lefosse |
| 36% das empresas brasileiras diziam-se totalmente aderentes à LGPD (pesquisa Logicalis, 2023) | Logicalis — dado explicitamente datado de 2023 no texto |

### ❌ Dados removidos ou reescritos por falta de fonte verificável

| Dado/afirmação original | O que foi feito |
|---|---|
| Manchete sugerida no brief: "Empresas estão deixando Brasil por causa de regulação de IA" | Removida — sem sustentação em nenhuma busca. H1 reescrito para "Desde 2021, a LGPD só multou uma empresa — isso está prestes a mudar" |
| Estatística genérica "80%"/"16%" de conformidade | Não incluída — números conflitantes entre fontes sem metodologia comparável |
| Comparação internacional "US$ 1,7 bi em multas" | Não incluída — só em fonte secundária, sem link ao relatório primário |

---

## Recomendações

1. Nenhuma correção pendente.
2. Se a publicação ocorrer numa data diferente de 2026-09-09, lembrar a skill `signal-publicador` de atualizar `article:published_time`, `datePublished`/`dateModified` e o byline.
3. Se, entre a pesquisa e a publicação, o PL 2338 for votado na Câmara, revisar o parágrafo sobre o status atual do Marco Legal da IA antes de publicar.
