# Relatório de QA — ia-open-source-llama-mistral-2026
*Gerado em 2026-09-09 pela skill validador-text · atualizado em 2026-09-09 (re-checagem)*

---

## Veredicto

**Score: 100/100** — ✅ Aprovado

---

## 🔴 Bloqueantes (0)

*(nenhum)*

---

## 🟡 Atenção (0)

O ponto de atenção da versão anterior (falso positivo do script) foi resolvido corrigindo o próprio script — ver abaixo.

---

## 🟢 OK (9 itens)

- Title ≤ 60 chars, keyword no início, termina " | Yarivi" (51 chars)
- H1 (manchete com gancho) ≠ title
- Meta description presente, 145 chars (≤155)
- Slug contém keyword principal (`ia-open-source-llama-mistral-2026`)
- Schema.org `NewsArticle` completo
- Schema.org `FAQPage` presente com as 5 perguntas
- 2 links internos válidos, ambos para artigos existentes
- `article:published_time` presente (2026-09-09)
- 6 fontes externas em `art-sources`, **6/6 verificadas**, nenhuma quebrada

---

## Correção de script aplicada nesta re-checagem

`validador-text/scripts/check_article.py` tinha `TODO` com `re.IGNORECASE`, que casava com "todo"/"Todos" em português (ex.: "Todos sob licença Apache 2.0"). Corrigido para `\bTODO\b` sem ignorecase — agora só detecta marcadores reais de placeholder. Correção aplicada de forma centralizada, vale para toda a fila.

---

## Detalhamento por categoria

### Originalidade (antiplágio)
- Método: busca de frases exatas entre aspas via WebSearch
- Frases testadas: 5
- Resultado: **5/5 ORIGINAL**

| Frase | Resultado |
|-------|-----------|
| "Não existe um número mágico universal, porque depende da versão exata do modelo e de como ele é comprimido para download." | ✅ ORIGINAL |
| "Dica prática: deixe o Gerenciador de Tarefas (Windows) ou o Monitor de Atividade (Mac) aberto enquanto testa o primeiro modelo." | ✅ ORIGINAL |
| "É a única etapa em que você precisa de internet — depois disso, o modelo roda 100% offline, mesmo sem sinal." | ✅ ORIGINAL |
| "Como o modelo roda dentro do seu computador, o que você digita não sai da sua máquina, nem passa por servidor de terceiros." | ✅ ORIGINAL |
| "Numa assinatura como o ChatGPT Plus, a troca de versão do modelo por trás acontece automaticamente — você não escolhe quando nem qual versão usar." | ✅ ORIGINAL |

### Links
- Externos no artigo: 6 — todos verificados manualmente via WebFetch nesta sessão

| Link | Status |
|------|--------|
| ai.meta.com/blog/llama-4-multimodal-intelligence/ | ✅ Confirmado — post oficial Meta, abr. 2025, Scout 109B/Maverick 400B |
| huggingface.co/meta-llama/Llama-3.1-8B-Instruct | ✅ Confirmado — model card oficial |
| mistral.ai/news/mistral-3/ | ✅ Confirmado — anúncio oficial, dez. 2025, Apache 2.0 |
| ollama.com/library/llama3.1 | ✅ Confirmado — 4.9GB de download |
| help.openai.com/.../what-is-chatgpt-plus | ✅ Confirmado — US$20/mês |
| the-decoder.com (Qwen 3.8, Alibaba, Apache 2.0) | ✅ Confirmado |

- Internos: 2/2 verificados como artigos existentes em `artigos/`

### SEO automático
| Check | Resultado | Detalhe |
|-------|-----------|---------|
| title_length | ✅ | 51 chars |
| title_yarivi | ✅ | termina " \| Yarivi" |
| h1_ne_title | ✅ | H1 é manchete com gancho, diferente do title |
| meta_desc_present | ✅ | presente |
| meta_desc_length | ✅ | 145 chars |
| faq_schema | ✅ | FAQPage presente |
| no_placeholders | ✅ | passa após correção do script |
| internal_link_exists | ✅ | 2 encontrados |
| published_time | ✅ | 2026-09-09 |

### Metadados
- Palavras no corpo: 1.646
- Tempo de leitura estimado: 8 min
- Title: `Rodar IA grátis no seu PC: Llama e Mistral | Yarivi` (51 chars)
- Meta description: 145 chars

---

## Recomendações

Nenhuma correção pendente. O artigo está pronto para revisão da Mi.
