# Signal. Blog — Guia de Estrutura e Componentes

## Estrutura de arquivos

```
BlogTI/
├── index.html              # Homepage (não editar)
├── style.css               # Estilos globais (não editar)
├── script.js               # Carrega partials (não editar)
├── artigos/                # ← Artigos ficam aqui
│   └── {slug}.html
└── partials/
    ├── featured.html       # ← Atualizar: artigo em destaque
    ├── latest.html         # ← Atualizar: grade de últimas notícias
    ├── nav.html
    ├── hero.html
    ├── categories.html
    ├── newsletter.html
    └── footer.html
```

---

## CSS: Componentes especiais do corpo do artigo

Use dentro de `<article class="art-body">`.

### `data-callout` — Destaque de dado importante
Para números surpreendentes, alertas, contexto que muda a percepção.
```html
<div class="data-callout">
    <p>Texto do dado com <strong>dado em destaque</strong> aqui.</p>
</div>
```

### `stat-row` + `stat-box` — Grid de estatísticas visuais
Para 3-4 números de impacto lado a lado. Use quando tiver dados concretos.
```html
<div class="stat-row">
    <div class="stat-box">
        <div class="stat-num">+53%</div>
        <div class="stat-label">descrição curta do dado</div>
    </div>
</div>
```

### `paradox-box` — Insight central ou twist surpreendente
Para o conceito mais importante do artigo. Fundo roxo/âmbar, destaque visual forte.
```html
<div class="paradox-box">
    <h3>⚠️ Título do insight</h3>
    <p>Explicação do paradoxo ou conceito central.</p>
</div>
```

### `summary-box` — Resumo final em pontos (sempre usar)
```html
<div class="summary-box">
    <h2>Resumo em N pontos</h2>
    <ol>
        <li><strong>Ponto 1</strong> — explicação curta.</li>
    </ol>
</div>
```

### `art-table-wrap` + `art-table` — Tabela de dados
```html
<div class="art-table-wrap">
    <table class="art-table">
        <thead><tr><th>Col 1</th><th>Col 2</th></tr></thead>
        <tbody><tr><td>dado</td><td>dado</td></tr></tbody>
    </table>
</div>
```

### `art-sources` — Seção de fontes (sempre incluir)
```html
<div class="art-sources">
    <h4>Fontes</h4>
    <ul>
        <li>Nome — <em>Título</em>, ano</li>
        <li><a href="URL" target="_blank" rel="noopener">Portal — Título</a></li>
    </ul>
</div>
```

---

## Tags disponíveis

```html
<span class="tag tag-ai">IA & ML</span>
<span class="tag tag-sec">Segurança</span>
<span class="tag tag-hw">Hardware</span>
<span class="tag tag-sw">Software</span>
<span class="tag tag-mob">Mobile</span>
<span class="tag tag-fut">Futuro</span>
<span class="tag tag-dest">Análise</span>
```

---

## Padrão do `<head>` do artigo

- `<title>`: Título + " | Signal."
- `<meta name="description">`: até 160 caracteres
- `<meta property="article:published_time">`: data ISO (YYYY-MM-DD)
- Schema.org `NewsArticle` com: headline, description, datePublished, articleSection, keywords
- `<link rel="stylesheet" href="../style.css">` (caminho relativo — artigos ficam em subpasta)

---

## Como atualizar `featured.html`

```
featured-grid
├── feat-main fu          ← ARTIGO PRINCIPAL (substituir pelo novo)
└── feat-sidebar
    ├── side-card fu      ← Inserir artigo anterior aqui (primeiro)
    ├── side-card fu
    ├── side-card fu
    └── side-card fu      ← Remover este se já tiver 4 (manter máximo 4)
```

## Como atualizar `latest.html`

Inserir novo card **antes** do primeiro `<a class="art-card fu">` existente.
O grid aceita qualquer número de cards.
