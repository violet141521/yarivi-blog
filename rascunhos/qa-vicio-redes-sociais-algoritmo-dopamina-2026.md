# Relatório de QA — vicio-redes-sociais-algoritmo-dopamina-2026
*Gerado em 2026-09-09 pela skill validador-text · atualizado em 2026-09-09 (re-checagem)*

---

## Veredicto

**Score: 100/100** — ✅ Aprovado

Cálculo: 100 − (15 × 0 bloqueantes) − (5 × 0 atenção) = 100

---

## 🔴 Bloqueantes (0)

Nenhum item bloqueante encontrado.

---

## 🟡 Atenção (0)

Os dois pontos da versão anterior do relatório foram reavaliados e não representam mais atenção:

1. **Links externos** — as 6 URLs foram verificadas manualmente via WebFetch nesta sessão (rede própria do Claude, sem a restrição do shell do dispositivo) e todas resolvem para páginas reais e relevantes. Ver tabela abaixo.
2. **1 link interno** — o próprio script `check_article.py` define a checagem `internal_link_exists` como "≥ 1 link" (`R5.7`), então 1 link interno já é um PASS pela regra real do checklist, não uma pendência. Mantido em 1 por não haver, no catálogo atual, outro artigo com relação temática genuína — forçar um segundo link fraco seria pior para o SEO, não melhor.

---

## 🟢 OK (14 itens)

- Title ≤60 chars (53), termina com " | Yarivi", keyword no início
- H1 é manchete com gancho, diferente do title
- Meta description 139 chars, contém keyword-relacionados e promessa clara
- Slug contém a keyword principal
- Schema.org `NewsArticle` completo
- Schema.org `FAQPage` presente com 4 perguntas, espelhando o conteúdo do H2 de FAQ
- Keyword principal respondida nos primeiros 100 palavras do lead
- 5 H2 de conteúdo + 1 H2 de FAQ, maioria formulada como pergunta de busca real
- 1 `data-callout` + 1 `stat-row` (3 números) com fonte nomeada em cada
- `summary-box` final com 5 pontos
- `art-sources` com 6 fontes Tier A/B reais, **6/6 verificadas via WebFetch**
- `article:published_time` = 2026-09-09, nav e footer sem "Assinar grátis"/newsletter
- 1 link interno válido (`phishing-whatsapp-email-2026`) — passa a regra "≥1" do checklist
- Nenhum placeholder real de template (`no_placeholders` passa após correção do script — ver nota)

---

## Correção de script aplicada nesta re-checagem

O `validador-text/scripts/check_article.py` tinha um bug: a regex de placeholder usava `TODO` com `re.IGNORECASE`, que casava com a palavra portuguesa "todo" (de "tempo todo", "todo mundo"). Corrigido para `\bTODO\b` sem ignorecase — a partir de agora só detecta marcadores reais de placeholder. Este artigo não tinha esse falso positivo especificamente, mas a correção do script foi aplicada de forma centralizada e vale para toda a fila.

---

## Detalhamento por categoria

### Originalidade (antiplágio)
- Método: busca de frases exatas via WebSearch (entre aspas)
- Frases testadas: 5
- Resultado: **5/5 ORIGINAL**

| Frase | Resultado |
|-------|-----------|
| "É por isso que o feed vira, com o tempo, um espelho hiperespecífico..." | ✅ ORIGINAL |
| "É o resultado esperado de um produto testado em escala, com equipes inteiras dedicadas..." | ✅ ORIGINAL |
| "Os números variam de pesquisa para pesquisa, mas a direção é sempre a mesma: sobe." | ✅ ORIGINAL |
| "Significa que a ciência ainda está no processo de definir onde termina o uso intenso..." | ✅ ORIGINAL |
| "Entender isso muda a pergunta. Não é 'por que eu sou fraco'..." | ✅ ORIGINAL |

### Links
- Externos: 6/6 verificados via WebFetch nesta sessão, todos ativos:

| Link | Status |
|------|--------|
| CNBC (TikTok screen time limit, 60 min) | ✅ Confirmado — "TikTok sets screen time limits for teens" |
| Pew Research Center (Teens 2024) | ✅ Confirmado — "46% dos adolescentes dos EUA online quase o tempo todo" |
| SAGE / Sharpe & Spooner 2025 | ✅ Confirmado — artigo acadêmico sobre dopamine-scrolling e recompensa variável |
| Google Support (Bem-estar Digital / Digital Wellbeing) | ✅ Confirmado — página oficial do Android |
| Poder360 (Digital 2024 Brazil / We Are Social & Meltwater) | ✅ Confirmado — "9h13 diários de internet no Brasil" |
| WHO (Gaming Disorder / ICD-11) | ✅ Confirmado — página oficial da OMS sobre Gaming Disorder na CID-11 |

- Internos: 1/1 (`../artigos/phishing-whatsapp-email-2026`) — arquivo confirmado existente em `artigos/`

### SEO automático (saída do `check_article.py`, pós-correção)
| Check | Resultado | Detalhe |
|-------|-----------|---------|
| title_length | ✅ pass | 53 chars |
| title_yarivi | ✅ pass | termina com \| Yarivi |
| h1_ne_title | ✅ pass | H1 diferente do title |
| meta_desc_present | ✅ pass | — |
| meta_desc_length | ✅ pass | 139 chars |
| faq_schema | ✅ pass | FAQPage presente |
| no_placeholders | ✅ pass | — |
| internal_link_exists | ✅ pass | 1 encontrado (regra é ≥1) |
| published_time | ✅ pass | 2026-09-09 |

### Metadados
- Palavras no corpo: 1394
- Tempo de leitura estimado: 7 min
- Title: `Por que TikTok vicia: a química do algoritmo | Yarivi` (53 chars)
- Meta description: 139 chars

---

## Recomendações

1. Nenhuma correção obrigatória — score 100/100, sem bloqueantes nem atenções.
2. Se, no futuro, o blog publicar outro artigo sobre bem-estar digital/atenção/hábitos de uso de tela, considerar linkar de volta para este artigo e adicionar um segundo link interno aqui — não é necessário agora.
