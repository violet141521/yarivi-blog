# Yarivi — Resumo do Processo Editorial

## O que é o Yarivi
Blog de tecnologia em português (BR) para leitores curiosos, não especialistas.
**Meta**: 1.000 sessões/mês → monetização (afiliados → AdSense → Mediavine).
**Domínio**: yarivi.com (Cloudflare Pages)

---

## Fluxo editorial em 4 passos

### 1. Pauta
- Skill: `signal-seo-writer`
- Gera 10 sugestões de temas com base em pesquisa de palavras-chave
- Mi escolhe 5

### 2. Produção (rascunhos)
- Os 5 artigos são escritos e salvos em `rascunhos/`
- Status inicial: `aguardando-revisao` no arquivo `rascunhos/fila.json`
- **Nunca publicar direto — sempre passar pela revisão**

### 3. Revisão
- Mi lê cada rascunho e aprova ou pede ajustes no chat
- Após aprovação, status vira `aprovado` na fila

### 4. Publicação
- Skill: `signal-publicador`
- 1 artigo por dia útil (seg–sex), às 08:00, via tarefa agendada
- A skill atualiza a data do artigo para o dia real de publicação
- Atualiza `partials/featured.html` e `partials/latest.html` na home
- Status vira `publicado` na fila

---

## Regras importantes

- **Aprovação humana obrigatória** — nada vai ao ar sem status `aprovado`
- **Estilo Yarivi**: frases curtas, analogia antes de jargão, dados com fonte, ação concreta no final
- **SEO**: título keyword-first ≤60 chars, H1 diferente do title (gancho), FAQ com schema, 1–3 links internos

---

## Estrutura de pastas

```
BlogTI/
├── index.html / style.css / script.js   ← base do site (não editar sem pedido)
├── artigos/                              ← artigos publicados
├── rascunhos/
│   └── fila.json                         ← controle de status
├── partials/
│   ├── featured.html                     ← destaque da home
│   └── latest.html                       ← últimas publicações
└── pesquisas/                            ← relatórios salvos
```

---

## Estado atual (2026-08-01)

| Item | Status |
|---|---|
| Rebranding Signal → Yarivi | ✅ Concluído |
| Domínio yarivi.com | ✅ Registrado |
| Cloudflare Pages (deploy) | ✅ Configurado |
| Sitemap + robots.txt | ✅ Gerados |
| Google Search Console | ⏳ Pendente |
| Rascunhos aprovados | 2 de 5 (agente-de-ia, celular-dobravel) |
| Rascunhos pendentes | 3 (robô humanoide, PC com IA/NPU, bateria estado sólido) |
| Tarefa agendada de publicação | ⏳ Criar após aprovar todos os rascunhos |
| AdSense | ⏳ Após 12+ artigos publicados |
| Newsletter | ⏳ Desativada temporariamente |
| Redes sociais do Yarivi | ⏳ A criar |
| Páginas legais (privacidade, contato, sobre) | ⏳ A criar |
