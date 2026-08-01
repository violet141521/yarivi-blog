---
name: signal-publicador
description: >
  Publica no blog Signal (C:\Repositorio\ClaudeProject\Aula1\BlogTI) os artigos aprovados
  na fila de rascunhos, um por vez. Use sempre que: uma tarefa agendada pedir para publicar
  o próximo artigo da fila, o usuário disser "publica o próximo", "publica o artigo X",
  "aprova o artigo Y" (marcar aprovação na fila), "agenda a publicação dos aprovados", ou
  qualquer pedido de gerenciar a fila de publicação do Signal (ver status, reordenar,
  descartar). Também cuida de criar a tarefa agendada de seg-sex no horário definido.
---

# Yarivi Publicador

Gerencia a fila `rascunhos/fila.json` e publica artigos aprovados — 1 por execução.
A regra de ouro: **só publica o que tem `status: "aprovado"`**. Rascunho em
`aguardando-revisao` nunca vai ao ar, mesmo que seja o único da fila — a aprovação
humana é o que separa rascunho de publicação.

Blog: `C:\Repositorio\ClaudeProject\Aula1\BlogTI`
Fila: `rascunhos/fila.json` | Rascunhos: `rascunhos/*.html`

## Operação 1 — Marcar aprovação (quando o usuário aprova artigos)

1. Ler `rascunhos/fila.json`
2. Para cada artigo aprovado pelo usuário: `status` → `"aprovado"`, adicionar `"aprovado_em"` (ISO)
3. Se o usuário descartar algum: `status` → `"descartado"` (manter o arquivo em rascunhos/)
4. Se o usuário pedir mudanças no texto: editar o HTML do rascunho, manter `aguardando-revisao` até novo OK
5. Mostrar o estado da fila ao final (ordem, slug, status)

## Operação 2 — Agendar publicação (após haver aprovados)

Quando o usuário pedir para agendar:
1. Confirmar o horário (padrão em `fila.json` → `horario_publicacao`, hoje 08:00; se o
   usuário indicar outro, atualizar o campo)
2. Criar UMA tarefa agendada recorrente (ferramenta de scheduled tasks do Cowork) com
   cron de segunda a sexta no horário definido — ex. para 08:00: `0 8 * * 1-5` — e prompt:
   "Use a skill signal-publicador para publicar o próximo artigo aprovado da fila do blog Yarivi"
3. Uma única tarefa recorrente basta: cada execução publica 1 artigo (o próximo aprovado)
   e, quando a fila esvazia, a execução não faz nada e reporta fila vazia.

## Operação 3 — Publicar o próximo (execução agendada ou "publica o próximo")

1. Ler `rascunhos/fila.json`. Selecionar o artigo com `status: "aprovado"` de menor `ordem`.
   - Se não houver aprovados: informar "fila vazia — nada publicado" e encerrar sem tocar em nada.
2. Mover `rascunhos/{slug}.html` → `artigos/{slug}.html` (o caminho `../style.css` já
   funciona, mesma profundidade).
3. **Atualizar a data do artigo para o dia real da publicação** (nunca manter a data de
   quando foi escrito). Editar no HTML movido:
   - `<meta property="article:published_time" content="AAAA-MM-DD">` → data de hoje
   - no JSON-LD `NewsArticle`: `"datePublished"` e `"dateModified"` → data de hoje (ISO)
   - o `<span class="sep">` do byline (ex. `16 jul 2026`) → data de hoje por extenso, no
     mesmo formato (dia, mês abreviado em minúsculas, ano)
4. Atualizar `partials/featured.html` e `partials/latest.html` seguindo exatamente os
   padrões de `references/blog-structure.md` (novo artigo vira destaque; destaque anterior
   vai ao 1º side-card, máximo 4; novo card no topo do latest). Use os metadados do
   próprio item da fila (titulo, manchete, emoji, categoria, excerpt, read_time) — a
   manchete H1 (`manchete_h1`) é o texto do título nos cards, não o `titulo_seo`.
5. Atualizar a fila: `status` → `"publicado"`, adicionar `"publicado_em"` (ISO).
6. **Deploy (quando o blog estiver no Cloudflare Pages):** rodar o deploy conforme
   `references/deploy.md`. Enquanto o arquivo indicar "DEPLOY AINDA NÃO CONFIGURADO",
   pule esta etapa sem erro.
7. Reportar: artigo publicado (slug + manchete), quantos aprovados restam na fila e a
   data prevista do próximo (próximo dia útil).

## Operação 4 — Status da fila

Se o usuário perguntar "como está a fila": tabela com ordem, manchete, status e datas.
