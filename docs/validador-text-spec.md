# Spec — skill `validador-text`
*Gerada pela skill /planejar em 2026-08-12*

## Problema

O fluxo editorial do Yarivi não tem etapa automatizada de controle de qualidade antes da aprovação humana. Artigos com links quebrados, partes plagiadas ou falhas básicas de SEO podem passar despercebidos e chegar à publicação.

## Fora de escopo (MVP)
- Detecção de conteúdo gerado por AI
- Verificação gramatical / estilo via LLM
- Análise de densidade de keyword
- APIs pagas de antiplágio (Copyscape, Copyleaks)
- Interface visual / dashboard

---

## Requisitos (notação EARS)

### R1 — Relatório de QA
QUANDO a skill `validador-text` é invocada com um slug, o sistema DEVE gerar o arquivo `rascunhos/qa-[slug].md` contendo:
- Score geral 0–100 (ponderado: cada 🔴 = -15pts, cada 🟡 = -5pts, base 100)
- Lista de problemas agrupados por categoria com severidade
- Recomendações acionáveis para cada problema

R1.1 QUANDO todos os checks passam, o sistema DEVE exibir "✅ APROVADO para revisão humana".
R1.2 QUANDO há pelo menos um 🔴 Bloqueante, o sistema DEVE exibir "🔴 REPROVADO — corrigir antes de aprovar".

---

### R2 — Verificação de originalidade (antiplágio DIY)
QUANDO o artigo é processado:

R2.1 O sistema DEVE extrair 5 frases do corpo do texto (ignorar `<h1-h6>`, `art-sources`, byline) com comprimento entre 15 e 25 palavras, preferencialmente do miolo do artigo (não lead nem conclusão).

R2.2 Para cada frase extraída, o sistema DEVE buscar a frase exata (entre aspas duplas) via WebSearch.

R2.3 QUANDO um resultado de busca contém a frase exata no snippet ou título, o sistema DEVE marcar a frase como 🔴 **Potencial cópia** e listar a URL da fonte.

R2.4 QUANDO nenhuma das 5 frases tem correspondência exata, o sistema DEVE reportar "Originalidade: alta (5/5 frases únicas)".

R2.5 QUANDO 1–2 frases têm correspondência, o sistema DEVE reportar 🟡 e indicar as frases problemáticas.

R2.6 QUANDO 3 ou mais frases têm correspondência, o sistema DEVE reportar 🔴 e bloquear a aprovação.

---

### R3 — Verificação de links externos
QUANDO o artigo é processado:

R3.1 O sistema DEVE parsear todos os elementos `<a href="...">` do HTML cujo href começa com `http://` ou `https://`.

R3.2 Para cada URL externa, o sistema DEVE realizar um HTTP GET e verificar o status code (timeout: 10s).

R3.3 QUANDO o status é 4xx ou 5xx, o sistema DEVE marcar como 🔴 **Link quebrado** com a URL e o status.

R3.4 QUANDO o status é 3xx, o sistema DEVE marcar como 🟡 **Redirecionamento** com a URL original e a de destino (se disponível).

R3.5 QUANDO o fetch falha por timeout ou DNS, o sistema DEVE marcar como 🟡 **Link inacessível** e sugerir verificação manual.

---

### R4 — Links internos válidos
R4.1 QUANDO um href começa com `/artigos/` ou é um caminho relativo `../artigos/`, o sistema DEVE extrair o slug do path.

R4.2 QUANDO o slug não existe como entrada em `artigos/_catalog.json`, o sistema DEVE marcar como 🔴 **Link interno inválido — slug não publicado**.

---

### R5 — Checklist SEO automático
QUANDO o artigo é processado, verificar cada item:

| ID | Verificação | Falha → severidade |
|----|------------|-------------------|
| R5.1 | `<title>` ≤ 60 caracteres | 🔴 |
| R5.2 | `<title>` termina com " \| Yarivi" | 🟡 |
| R5.3 | H1 visível ≠ conteúdo do `<title>` | 🟡 |
| R5.4 | `<meta name="description">` presente e ≤ 155 chars | 🔴 se ausente · 🟡 se longo |
| R5.5 | Schema `FAQPage` presente no `<script type="application/ld+json">` | 🟡 |
| R5.6 | Placeholder `[...]` ou `TODO` no corpo do texto | 🔴 |
| R5.7 | Pelo menos 1 link interno (`/artigos/`) | 🟡 |
| R5.8 | `<meta property="article:published_time">` presente | 🟡 |

---

### R6 — Deduplicação de título
R6.1 QUANDO o artigo é processado, o sistema DEVE comparar o conteúdo de `<title>` contra todos os títulos em `artigos/_catalog.json`.

R6.2 QUANDO a sobreposição de palavras significativas (ignorando stopwords comuns) entre o novo título e qualquer título existente supera 70%, o sistema DEVE marcar como 🟡 **Título similar** e listar o artigo conflitante (slug + título).

---

### R7 — Contagem de palavras e tempo de leitura
R7.1 QUANDO o artigo é processado, o sistema DEVE contar as palavras do corpo (strip de HTML, excluindo `art-sources`).

R7.2 QUANDO o total de palavras < 600, o sistema DEVE marcar como 🟡 **Artigo curto** (risco para SEO — artigos informativos idealmente têm 800+ palavras).

R7.3 O sistema DEVE calcular o tempo de leitura estimado (`ceil(palavras / 200)` minutos) e exibi-lo no relatório.

---

## Premissas e gatilhos de replanejamento

| Premissa | Gatilho de revisão |
|----------|--------------------|
| WebSearch cobre frases plagiadas da maioria das fontes web abertas | Se mais de 20% dos artigos aprovados tiverem plágio descoberto após publicação → avaliar Copyscape API |
| Links são verificáveis pelo ambiente de execução da skill | Se firewall/proxy bloquear curl → configurar User-Agent ou usar WebFetch como fallback |
| `_catalog.json` é a fonte de verdade para slugs publicados | Se estrutura do catalog mudar → atualizar R4 |

---

## Integração no fluxo editorial

**Posição:** entre Passo 2 (rascunho pronto) e Passo 3 (revisão humana).

Fluxo atualizado:
```
1. Pauta (signal-seo-writer)
2. Produção → rascunho em rascunhos/
2.5. 🆕 Validação → validador-text → rascunhos/qa-[slug].md
3. Revisão humana (lê artigo + relatório de QA)
4. Aprovação
5. Publicação (signal-publicador)
```

A skill `signal-publicador` pode futuramente checar se `rascunhos/qa-[slug].md` existe antes de publicar (guarda-costas extra — opcional).
