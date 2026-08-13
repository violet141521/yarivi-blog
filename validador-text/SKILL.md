---
name: validador-text
description: >
  Valida a qualidade de um artigo do blog Yarivi antes da revisão humana.
  Roda antiplágio DIY (WebSearch), verifica links quebrados, confere checklist SEO
  e gera um relatório em rascunhos/qa-[slug].md.
  Use SEMPRE que: um rascunho acabou de ser escrito, a usuária pedir "valida o artigo [slug]",
  "roda o QA", "verifica os links", "checa plágio", antes de aprovar qualquer rascunho.
  Também pode ser chamada automaticamente pela skill signal-seo-writer ao finalizar um artigo.
---

# validador-text

Gera um relatório de qualidade para artigos do Yarivi **antes** da aprovação humana.
Spec completa: `docs/validador-text-spec.md`

Blog: `C:\Repositorio\ClaudeProject\Aula1\BlogTI`
Artigo: `rascunhos/{slug}.html`
Relatório: `rascunhos/qa-{slug}.md`
Template: `validador-text/references/qa-template.md`
Script de análise: `validador-text/scripts/check_article.py`

---

## Passo 1 — Identificar o slug

Se o usuário não informou o slug:
1. Ler `rascunhos/fila.json`
2. Listar artigos com `status: "aguardando-revisao"` e perguntar qual validar
3. Se só houver um, perguntar confirmação e prosseguir

---

## Passo 2 — Análise técnica (via script Python)

Rodar via Bash (instalar dependências se necessário):

```bash
cd /caminho/para/BlogTI
pip install beautifulsoup4 requests --break-system-packages --quiet 2>/dev/null
python validador-text/scripts/check_article.py {slug}
```

O script retorna um JSON com:
- `title`, `h1`, `meta_description`, `word_count`, `internal_links`, `external_links`
- `seo_checks`: resultado de cada item R5.x (pass/fail + detalhe)
- `link_status`: status HTTP de cada link externo
- `internal_link_issues`: slugs internos não encontrados no catalog
- `duplicate_title`: slugs com título similar (se houver)
- `sample_phrases`: 5 frases extraídas para antiplágio (15-25 palavras cada)
- `reading_time`: tempo calculado

**Se o script falhar** (Python não disponível, etc.): executar as verificações manualmente
lendo o arquivo HTML com a ferramenta Read e verificando cada item da spec.

---

## Passo 3 — Antiplágio DIY

Para cada uma das 5 `sample_phrases` retornadas pelo script:

1. Buscar a frase **entre aspas duplas** via WebSearch:
   - Query: `"[frase exata]"`
2. Verificar se algum resultado contém a frase exata no snippet
3. Anotar: `ORIGINAL` (sem correspondência) ou `⚠️ MATCH: [URL]`

**Critério de resultado:**
- 0/5 com match → Originalidade: Alta ✅
- 1-2/5 com match → Originalidade: Média 🟡
- 3+/5 com match → Originalidade: Baixa 🔴 (bloquear aprovação)

**Importante:** correspondência parcial (palavras comuns, frases genéricas) não conta — só correspondência de frase completa e específica.

---

## Passo 4 — Calcular score e gerar relatório

Score base: 100
- Cada 🔴 Bloqueante: -15 pontos
- Cada 🟡 Atenção: -5 pontos

Preencher o template em `validador-text/references/qa-template.md` com os resultados e salvar em `rascunhos/qa-{slug}.md`.

Veredicto final:
- Score ≥ 70 e zero 🔴: "✅ APROVADO para revisão humana"
- Score < 70 ou ≥ 1 🔴: "🔴 REPROVADO — corrigir antes de aprovar"

---

## Passo 5 — Apresentar resultado no chat

Exibir resumo conciso:
```
📋 QA — [manchete do artigo]
Score: XX/100 | Veredicto: ✅/🔴

🔴 Bloqueantes (N):
  • [item] — [detalhe]

🟡 Atenção (N):
  • [item] — [detalhe]

🟢 OK (N itens)

Relatório completo: rascunhos/qa-{slug}.md
```

Se houver 🔴 bloqueantes: "Recomendo corrigir antes de aprovar. Quer que eu corrija algum item?"
Se aprovado: "Artigo pronto para revisão. Use a skill signal-publicador quando quiser publicar."
