---
name: signal-seo-writer
description: >
  Pipeline SEO-first para pesquisar, escrever e publicar artigos otimizados para o Google
  no blog Yarivi (C:\Repositorio\ClaudeProject\Aula1\BlogTI). Use esta skill sempre que o
  usuário quiser: artigo otimizado para SEO, ranquear no Google, tráfego orgânico, artigo
  com palavra-chave, post para monetização/AdSense, "escreve pra ranquear", ou publicação
  no Signal com foco em busca. Diferente do fluxo editorial comum, aqui a palavra-chave e a
  intenção de busca vêm ANTES do texto. Fluxo: pauta de 10 temas → usuário escolhe 5 →
  keyword research → artigos salvos como RASCUNHOS em rascunhos/fila.json para revisão —
  a publicação em si é da skill signal-publicador, após aprovação. Acione também quando o
  usuário pedir: "monta uma pauta", "sugere temas", "escreve os artigos da semana".
---

# Yarivi SEO Writer

Pipeline: **Pauta (10 temas) → Escolha de 5 → Keyword research → Estrutura SEO → Pesquisa de conteúdo → Artigos → RASCUNHOS na fila de publicação**.

Esta skill NÃO publica no blog. Ela produz rascunhos em `rascunhos/` e os registra em
`rascunhos/fila.json` com status `aguardando-revisao`. Quem publica é a skill
`signal-publicador`, depois que o usuário aprovar — isso garante que nada vai ao ar sem
revisão humana.

## PASSO 0 — Pauta: 10 temas para o usuário escolher 5

Quando o usuário pedir uma pauta (ou não tiver tema definido), a pesquisa de temas usa a
**skill `pesquisa`** (funil de pesquisa do usuário): invoque-a com o objetivo "mapear os
temas de tecnologia mais quentes dos últimos 30 dias (Brasil e mundo) para pauta de blog"
e use o **Nível 1 (varredura em ângulos paralelos)** — um ângulo por categoria do blog
(IA, Segurança, Hardware, Software, Mobile, Futuro). Não é preciso avançar aos Níveis 2/3:
a varredura basta para uma pauta.

Fallback: se as ferramentas do Perplexity que a skill `pesquisa` usa estiverem
indisponíveis (retornos vazios/erro de autenticação), faça a varredura com os mesmos
ângulos via WebSearch — o formato do funil se mantém, muda só a ferramenta.

Com a varredura em mãos, monte **10 propostas de tema** variando as categorias.

Para cada proposta, uma linha:
`N. [emoji] Tema — por que agora (1 frase) — keyword provável`

Evite temas já cobertos pelos artigos existentes em `artigos/` (leia os títulos antes).
**Pause e aguarde o usuário escolher 5.** Só então rode o pipeline abaixo para cada
tema escolhido (Passos 1-4 por artigo; pode processar em sequência ou informar progresso).

A diferença central em relação a um fluxo editorial: aqui o artigo nasce de uma **demanda de
busca real**. Primeiro descobrimos o que as pessoas digitam no Google sobre o tema e por quê
(intenção); só então escrevemos — para ser a melhor resposta àquela busca. Isso importa porque
o objetivo do blog é tráfego orgânico e monetização: um texto excelente que ninguém busca não
gera visitas.

> Antes de começar, leia `references/article-template.html` e `references/blog-structure.md`
> (o template e os componentes visuais do Signal) e `references/seo-checklist.md`
> (o checklist que o artigo precisa passar antes de publicar).

## Entradas necessárias

- **Tema** — pode ser vago; a keyword research vai afunilar
- Se o usuário não informou o tema, pergunte antes de começar

---

## PASSO 1 — Keyword research (WebSearch paralelo)

Execute no mesmo turno 4 buscas para mapear a demanda:

1. `[tema] como funciona` — capta intenção informacional básica
2. `[tema] vale a pena / melhor / vs` — capta intenção comparativa/comercial
3. `[tema] 2026 Brasil` — capta o recorte local e recente
4. `[tema] dúvidas perguntas frequentes` — capta long-tails e a seção FAQ

Do resultado, extraia:
- **Keyword principal**: o termo mais buscado que o artigo pode responder por inteiro
  (específico o bastante para um blog novo competir — "computação quântica riscos senha"
  rankeia; "computação quântica" não)
- **3-5 keywords secundárias / long-tails**: variações e perguntas relacionadas
- **Intenção dominante**: informacional ("o que é"), comercial ("qual o melhor") ou
  transacional ("como contratar") — o formato do artigo segue a intenção

## PASSO 2 — Estrutura SEO (antes de escrever qualquer parágrafo)

Defina e apresente ao usuário em um bloco curto:

```
🔑 Keyword principal: [termo]
🎯 Intenção: [informacional/comercial] — formato: [guia/comparativo/lista/FAQ]
📄 Título SEO / <title> (≤60 chars): [keyword no início, claro e direto]
🗞️ Manchete H1 (pode ser diferente!): [gancho emocional de curiosidade — ver regra no Passo 4]
📝 Meta description (≤155 chars): [promessa clara + keyword]
🔗 Slug: [keyword-principal-ano]
🏗️ Esqueleto H2/H3: [4-6 H2, cada um respondendo uma busca real; keywords secundárias
   distribuídas nos H2 — nunca forçadas]
```

Se o usuário estiver presente, aguarde o OK antes de escrever. Se estiver rodando de forma
autônoma (sem interação), prossiga com a melhor estrutura.

## PASSO 3 — Pesquisa de conteúdo (WebSearch paralelo)

Agora sim o conteúdo. 3 buscas no mesmo turno guiadas pelo esqueleto:

1. Dados e números recentes que respondem à keyword principal
2. O que os 3 primeiros resultados do Google já cobrem (para cobrir melhor e achar lacunas)
3. Casos reais / exemplos brasileiros

Extraia 3-5 fatos com números e fontes Tier A/B (institutos, empresas, portais especializados).

## PASSO 4 — Escrever o artigo

Use `references/article-template.html` substituindo os `{{PLACEHOLDERS}}` e os componentes
de `references/blog-structure.md` (data-callout, stat-row, paradox-box, summary-box,
art-sources). O estilo Signal continua valendo: frases curtas, analogias antes de jargão,
parágrafos de 2-4 linhas.

Regras SEO na escrita — cada uma existe por um motivo:

- **Título da aba ≠ manchete da página — use os dois.** O `<title>` (o que o Google
  mostra) fica keyword-first e ≤60 chars. Já o H1 visível no artigo é a manchete: ali
  o gancho emocional manda — curiosidade, número surpreendente, pergunta simples.
  Ex.: `<title>` "Golpe do deepfake de voz: como se proteger | Yarivi" + H1 "Três
  segundos da sua voz bastam para esvaziar uma conta". Perguntas simples no início
  também funcionam muito bem ("Passkey vale a pena?"). Um título sem alma perde o
  clique mesmo ranqueando; um H1 sem keyword não perde nada.
- **Responda a keyword principal nos primeiros 100 palavras.** O Google (e o leitor) decide
  em segundos se a página responde à busca. Gancho emocional + resposta direta no lead.
- **H2 formulados como as perguntas que as pessoas buscam.** H2 = mini-título de busca.
  Ex.: "Computadores quânticos podem quebrar senhas?" em vez de "O panorama atual".
- **Keyword principal**: no título, no primeiro H2, no slug e ~2-4 vezes no corpo, sempre
  natural. Keyword stuffing derruba ranking — se soar repetitivo lendo em voz alta, corte.
- **Seção FAQ ao final** (antes do summary-box): 3-4 perguntas long-tail do Passo 1 com
  respostas de 2-4 linhas. Alvo: featured snippets e "As pessoas também perguntam".
- **1-3 links internos** para outros artigos do blog em `artigos/` quando houver relação
  real de tema (âncora descritiva, não "clique aqui"). Links internos distribuem autoridade
  e mantêm o leitor no site.
- **Schema.org**: além do `NewsArticle` do template, adicione um bloco `FAQPage` com as
  perguntas da seção FAQ.
- **Meta description** definida no Passo 2 vai no `<meta name="description">`.

Depois de escrever, passe o artigo pelo `references/seo-checklist.md` e corrija o que faltar.

## PASSO 5 — Salvar como rascunho na fila (NÃO publicar)

1. Salvar o artigo em `C:\Repositorio\ClaudeProject\Aula1\BlogTI\rascunhos\{{SLUG}}.html`
   (mesma profundidade de `artigos/`, então o `../style.css` do template já funciona)
2. Registrar em `C:\Repositorio\ClaudeProject\Aula1\BlogTI\rascunhos\fila.json` — adicionar
   ao array `fila` (criar o arquivo se não existir):

```json
{
  "slug": "{{SLUG}}",
  "titulo_seo": "{{TITLE_TAG}}",
  "manchete_h1": "{{H1}}",
  "categoria": "{{CATEGORY_KEY}}",
  "emoji": "{{EMOJI}}",
  "excerpt": "{{EXCERPT_CURTO}}",
  "read_time": "{{N}} min",
  "status": "aguardando-revisao",
  "ordem": <próximo número sequencial>,
  "criado_em": "<data ISO>"
}
```

3. NÃO tocar em `artigos/`, `partials/featured.html` nem `partials/latest.html` — isso é
   trabalho da skill `signal-publicador`, após aprovação do usuário.

Ao final de todos os artigos, apresente a lista: slug, título, manchete e keyword de cada
um, e oriente: "Revise os rascunhos (abra os arquivos de `rascunhos/` no navegador). Diga
quais aprova — aí a signal-publicador agenda a publicação."

---

## Referência rápida de categorias

| Categoria   | TAG_CLASS  | CATEGORY_KEY | Emoji |
|-------------|------------|--------------|-------|
| IA & ML     | tag-ai     | ai           | 🤖    |
| Segurança   | tag-sec    | sec          | 🔒    |
| Hardware    | tag-hw     | hw           | 💻    |
| Software    | tag-sw     | sw           | 💾    |
| Mobile      | tag-mob    | mob          | 📱    |
| Futuro      | tag-fut    | fut          | 🔮    |

Gradient classes para card-thumb: `g1` roxo, `g2` âmbar, `g3` teal, `g4` verde, `g5` azul, `g6` índigo.
