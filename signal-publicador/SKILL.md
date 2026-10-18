---
name: signal-publicador
description: >
  Publica no blog Yarivi (C:\Repositorio\ClaudeProject\Aula1\BlogTI) os artigos aprovados
  na fila de rascunhos, em lote semanal com 1 data por dia útil. Use sempre que o usuário
  disser "sobe os aprovados", "publica o lote", "publica o próximo", "publica o artigo X",
  "aprova o artigo Y" (marcar aprovação na fila), ou qualquer pedido de gerenciar a fila de
  publicação do Yarivi (ver status, reordenar, descartar, mudar datas).
---

# Yarivi Publicador

Gerencia a fila `rascunhos/fila.json` e sobe os artigos aprovados **em lote**: um único
commit/push por semana, com cada artigo datado para um dia útil diferente. A regra de ouro:
**só publica o que tem `status: "aprovado"`**. Rascunho em `aguardando-revisao` nunca vai
ao ar — a aprovação humana é o que separa rascunho de publicação.

**Como o artigo aparece no site (desde 2026-10-17):** a home (`functions/index.js`) e o
`/sitemap.xml` (`functions/sitemap.xml.js`) mostram cada artigo sozinhos quando a `data_pub`
dele chega (meia-noite, fuso America/Sao_Paulo — regra em `functions/_lib/datas.js`). Não é
preciso rodar git nem abrir link no dia. O link `https://yarivi.com/api/publicar?slug=...&key=...`
continua existindo só para **liberar um artigo antes da data**. Antes da data o artigo já
abre pela URL direta, mas não aparece na home, no sitemap nem no `index.html` estático.

Blog: `C:\Repositorio\ClaudeProject\Aula1\BlogTI`
Fila: `rascunhos/fila.json` | Rascunhos: `rascunhos/*.html`
Deploy: `signal-publicador/references/deploy.md` no repositório do blog.

## Operação 1 — Marcar aprovação (quando o usuário aprova artigos)

1. Ler `rascunhos/fila.json` (os itens ficam em `fila` e em `novos_rascunhos`)
2. Para cada artigo aprovado pelo usuário: `status` → `"aprovado"`, adicionar `"aprovado_em"` (ISO).
   **Regra: quem foi aprovado primeiro é publicado primeiro.** Ao aprovar, reatribuir `ordem` do
   artigo para `max(ordem de todos os itens da fila e de novos_rascunhos) + 1`, de modo que a
   ordem numérica reflita a ordem de aprovação. Vários aprovados de uma vez: seguir a ordem em
   que o usuário os citou. Nunca reordenar os já aprovados, a menos que o usuário peça.
3. Se o usuário descartar algum: `status` → `"descartado"` (manter o arquivo em rascunhos/)
4. Se o usuário pedir mudanças no texto: editar o HTML do rascunho, manter `aguardando-revisao` até novo OK
5. Mostrar o estado da fila ao final (ordem, slug, status)

## Operação 2 — Agendamento

Não existe mais tarefa agendada diária (a `yarivi-publicador-diario` foi desligada em
2026-10-17). Não criar tarefa agendada de publicação: o lote é subido quando a usuária pede,
e a liberação diária é automática pela data. Se a usuária pedir uma tarefa, sugerir no máximo
uma semanal que **só avisa** quantos aprovados há (nunca sobe sem o OK dela — ver Operação 3, passo 2).

## Operação 3 — Subir o lote da semana ("sobe os aprovados", "publica o lote")

1. **Montar o calendário.** Ler `rascunhos/fila.json` e listar os itens `status: "aprovado"`
   por menor `ordem`. Sobe **só o que tiver**, no máximo 5 (uma semana); se houver mais de 5,
   os excedentes ficam para o próximo lote.
   - Se não houver aprovados: informar "fila vazia — nada a subir" e encerrar sem tocar em nada.
   - Datas: 1 artigo por dia útil (segunda a sexta), em ordem. O primeiro dia é o **próximo
     dia útil depois de hoje** e nunca o mesmo dia nem anterior à maior `data_pub` que já
     está no `_catalog.json` (sem dois artigos no mesmo dia). Ex.: lote subido no sábado
     17/10 com 3 aprovados → seg 19/10, ter 20/10, qua 21/10.
2. **Avisar antes e esperar o OK (obrigatório).** Antes de mexer em qualquer arquivo, mostrar
   à usuária: **quantos artigos vão subir** e a tabela dia → manchete → slug (e quantos
   aprovados ficam para o próximo lote, se houver). Só seguir depois que ela confirmar
   (ela pode trocar a ordem ou as datas).
3. Para cada artigo do lote, mover `rascunhos/{slug}.html` → `artigos/{slug}.html` (o caminho
   `../style.css` já funciona, mesma profundidade).
4. **Datar o artigo com o dia agendado dele** (não a data em que foi escrito nem a de hoje).
   Editar no HTML movido:
   - `<meta property="article:published_time" content="AAAA-MM-DD">` → data agendada
   - no JSON-LD `NewsArticle`: `"datePublished"` e `"dateModified"` → data agendada (ISO)
   - o `<span class="sep">` do byline (ex. `16 jul 2026`) → data agendada por extenso, no
     mesmo formato (dia, mês abreviado em minúsculas, ano)
5. **Links internos e "Leia também" sem spoiler.** Em cada artigo do lote, nenhum link pode
   apontar para um artigo com `data_pub` posterior à do próprio artigo (inclusive outros do
   mesmo lote). Se houver, trocar por um artigo já no ar da mesma categoria. O mesmo vale para
   links adicionados em artigos antigos.
6. Atualizar `artigos/_catalog.json`: adicionar cada artigo com os campos slug, manchete
   (= `manchete_h1` da fila), categoria, emoji, grad (mapa: ai→g1, hw→g2, sec→g3, sw→g4,
   mob→g5, fut→g6), excerpt, read_time e `data_pub` = **data agendada**. Manter o array em
   ordem de `data_pub` decrescente (o mais futuro no início). **Não editar `partials/*` nem
   o KV.**
7. Regenerar os arquivos estáticos de fallback (eles já filtram por `data_pub <= hoje`, então
   os agendados ficam de fora até o dia — é o esperado):
   ```
   python scripts/gerar-thumbs.py
   node scripts/gerar-sitemap.mjs
   node scripts/gerar-home-estatica.mjs
   ```
   `gerar-thumbs.py` cria as miniaturas `img/thumb/{slug}.webp` (640px) usadas nos cards da
   home; `gerar-home-estatica.mjs` preenche sozinho os campos `img`/`thumb` de cada artigo no
   `_catalog.json` (capa = primeiro `<img src="../img/...">` do artigo) — não preencher à mão.
   Artigo sem imagem continua com o emoji no card.
   Nunca escrever o `sitemap.xml` à mão. Em produção, `/sitemap.xml` é gerado pela Function
   a cada dia; o arquivo é só o fallback.
8. Atualizar a fila: para cada artigo, `status` → `"publicado"`, `"publicado_em"` = data
   agendada (ISO) e `"subido_em"` = data de hoje (ISO).
9. **Imagens:** para cada slug, se existir `img/{slug}.webp` (ou `.jpg`/`.png`), incluir no
   commit junto com a miniatura `img/thumb/{slug}.webp` — nunca subir sem a imagem quando ela
   estiver disponível.
10. **Deploy:** um único commit/push com o lote inteiro, conforme `references/deploy.md`.
    Se o push falhar por falta de credenciais, reportar que o commit está feito e falta o push.
11. Reportar: tabela dia → manchete → slug, quantos aprovados restam na fila, e lembrar que
    cada artigo aparece sozinho na home à meia-noite do seu dia (link `/api/publicar` só se
    quiser antecipar).

"Publica o artigo X" ou "publica o próximo" fora do lote: mesmos passos para um artigo só,
com a data = próximo dia útil livre (ou hoje, se a usuária pedir que vá ao ar já).

## Operação 4 — Status da fila

Se o usuário perguntar "como está a fila": tabela com ordem, manchete, status e datas.
Para itens `publicado` com `publicado_em` no futuro, mostrar como **agendado (vai ao ar em DD/MM)**.

## Mudar a data de um artigo já subido

Editar as 3 datas no HTML (passo 4), a `data_pub` no `_catalog.json` e `publicado_em` na
fila, rodar os 2 scripts do passo 7 e fazer commit/push.
