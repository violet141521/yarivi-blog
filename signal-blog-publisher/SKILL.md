---
name: signal-blog-publisher
description: >
  Pipeline completo para pesquisar, escrever e publicar artigos no blog Signal.
  (C:\Repositorio\ClaudeProject\Aula1\BlogTI). Use esta skill SEMPRE que o usuário
  mencionar: publicar artigo no blog, escrever post para o Signal, criar conteúdo
  de tecnologia para o blog, adicionar artigo, pesquisar e publicar, "coloca no blog",
  "publica no Signal", ou qualquer pedido que combine pesquisa de tema tech + publicação
  no blog. O pipeline executa automaticamente: pesquisa em 4 ângulos com WebSearch →
  rascunho do artigo em HTML no estilo Signal. → publicação atualizando featured.html
  e latest.html. Não precisa de nenhuma configuração extra — só o tema do artigo.
---

# Signal. Blog Publisher

Pipeline completo: **Pesquisa → Artigo → Publicação** no blog Signal. (BlogTI).

> Antes de começar, leia `references/article-template.html` para ter o template HTML
> pronto em contexto e `references/blog-structure.md` para o guia de componentes e categorias.

---

## Entradas necessárias

- **Tema do artigo** — pode ser vago ("quero escrever sobre privacidade") ou específico
- **Categoria** (opcional) — se não informada, inferir da pesquisa

Se o usuário não informou o tema, pergunte antes de começar.

---

## PASSO 1 — Pesquisa em 4 ângulos (WebSearch paralelo)

Decomponha o tema em 4 ângulos complementares e execute as buscas **no mesmo turno**
(em paralelo). Ângulos sugeridos para tech:

1. **Tendências BR** — o que blogs e portais brasileiros estão cobrindo sobre o tema
2. **Explicação acessível** — como o tema é explicado para leigos, analogias usadas
3. **Dados e novidades 2026** — números concretos, lançamentos, marcos recentes
4. **Impacto no cotidiano** — o que muda na vida real das pessoas

Adapte os ângulos ao tema. Para segurança, inclua ângulo de ameaças práticas.
Para hardware, inclua reviews e comparativos. Para IA, inclua impacto no trabalho.

### Síntese da pesquisa

Depois das buscas, identifique:
- **3-5 fatos concretos** com números (percentuais, valores, datas)
- **1 conceito central** que vai ser o "hook" emocional do artigo
- **A solução ou saída** — todo bom artigo tech termina com "mas há uma resposta"
- **Fontes Tier A/B** para citar (institutos, empresas conhecidas, portais especializados)

---

## PASSO 2 — Escrever o artigo HTML

Use o template em `references/article-template.html` e substitua todos os placeholders
`{{PLACEHOLDER}}`. Guie-se pelo `references/blog-structure.md` para escolher os
componentes certos (data-callout, stat-row, paradox-box, etc.).

### Checklist do artigo

- [ ] Título com gancho emocional (não técnico — "o que isso muda pra você")
- [ ] Lead de 2-3 linhas que resume o porquê de ler
- [ ] Ao menos 1 **data-callout** com dado concreto e surpreendente
- [ ] Ao menos 1 **stat-row** com 3-4 números de impacto (se o tema tiver dados)
- [ ] **summary-box** ao final com "Resumo em N pontos"
- [ ] **art-sources** com fontes reais da pesquisa (Tier A/B em destaque)
- [ ] Tempo de leitura estimado (palavras ÷ 200 = minutos, arredondar)
- [ ] Slug limpo: `tema-principal-ano` (ex: `perigo-quantico-criptografia-2026`)

### Tom e estilo Signal.

O blog fala com leitores curiosos, não com especialistas. Regras de ouro:
- Explique cada conceito técnico com uma analogia do dia a dia antes de nomeá-lo
- Frases curtas. Parágrafos de 2-4 linhas.
- Não use jargão sem explicar: "RSA (o cadeado matemático que protege seus dados)"
- Ganchos emocionais primeiro, explicação técnica depois
- Termine com ação concreta que o leitor pode tomar

---

## PASSO 3 — Publicar no blog

O blog fica em: `C:\Repositorio\ClaudeProject\Aula1\BlogTI`

### 3a. Salvar o arquivo do artigo

```
C:\Repositorio\ClaudeProject\Aula1\BlogTI\artigos\{{SLUG}}.html
```

### 3b. Atualizar `partials/featured.html`

O novo artigo vira o **destaque principal**. O artigo que era destaque vai para o
primeiro slot da sidebar. Padrão do bloco principal a substituir:

```html
<article class="feat-main fu">
    <div class="feat-img">{{EMOJI}}</div>
    <div class="feat-body">
        <div class="tags">
            <span class="tag {{TAG_CLASS}}">{{TAG_LABEL}}</span>
            <span class="tag tag-dest">Análise</span>
        </div>
        <h2 class="art-title feat-title">{{TITULO}}</h2>
        <p class="feat-excerpt">{{LEAD_CURTO}}</p>
        <div class="art-meta" style="margin-bottom:.5rem;">
            <span>{{DATA_DISPLAY}}</span>
            <span class="sep">{{READ_TIME}} de leitura</span>
            <span class="sep">Novo</span>
        </div>
        <a href="artigos/{{SLUG}}.html" class="read-link">Ler análise completa →</a>
    </div>
</article>
```

O artigo que sai do destaque principal vira o **primeiro side-card**:

```html
<a href="artigos/{{SLUG_ANTERIOR}}.html" class="side-card fu">
    <div class="side-icon">{{EMOJI_ANTERIOR}}</div>
    <div>
        <div class="tags" style="margin-bottom:.375rem;">
            <span class="tag {{TAG_ANTERIOR}}">{{LABEL_ANTERIOR}}</span>
        </div>
        <div class="side-title">{{TITULO_ANTERIOR}}</div>
        <div class="side-meta">{{DATA_ANTERIOR}} · {{TEMPO_ANTERIOR}}</div>
    </div>
</a>
```

Se o artigo anterior estava em `href="#"` (placeholder), apenas remova-o.

### 3c. Atualizar `partials/latest.html`

Inserir o novo artigo como **primeiro card** na `.latest-grid`, antes de todos os outros:

```html
<a href="artigos/{{SLUG}}.html" class="art-card fu" data-category="{{CATEGORY_KEY}}">
    <div class="card-thumb {{GRADIENT_CLASS}}">{{EMOJI}}</div>
    <div class="card-body">
        <div class="tags">
            <span class="tag {{TAG_CLASS}}">{{TAG_LABEL}}</span>
            <span class="tag tag-dest" style="margin-left:.25rem;">Análise</span>
        </div>
        <h3 class="art-title card-title">{{TITULO_CURTO}}</h3>
        <p class="art-excerpt card-excerpt">{{EXCERPT}}</p>
        <div class="art-meta" style="margin-top:.625rem;">
            <span>{{DATA_DISPLAY}}</span>
            <span class="sep">{{READ_TIME}}</span>
        </div>
    </div>
</a>
```

---

## Referência rápida de categorias

| Categoria   | TAG_CLASS  | CATEGORY_KEY | Emoji sugerido |
|-------------|------------|--------------|----------------|
| IA & ML     | tag-ai     | ai           | 🤖             |
| Segurança   | tag-sec    | sec          | 🔒 ou ⚛️       |
| Hardware    | tag-hw     | hw           | 🔋 ou 💻       |
| Software    | tag-sw     | sw           | 🐧 ou 💾       |
| Mobile      | tag-mob    | mob          | 📱             |
| Futuro      | tag-fut    | fut          | 🛰️ ou 🔮      |

Gradient classes para card-thumb: `g1` (roxo/IA), `g2` (âmbar), `g3` (teal/seg),
`g4` (verde), `g5` (azul), `g6` (índigo). Escolha o que combinar visualmente.

---

## Verificação final

Depois de criar/atualizar todos os arquivos, confirme:

1. ✅ `artigos/{{SLUG}}.html` criado
2. ✅ `partials/featured.html` atualizado (novo artigo como destaque)
3. ✅ `partials/latest.html` atualizado (novo artigo como primeiro card)
4. ✅ Links `href` usando caminho relativo correto (`artigos/...` nos partials, `../style.css` no artigo)

Informe o usuário com um resumo e o link `http://localhost:3000/#` para ver o resultado.
