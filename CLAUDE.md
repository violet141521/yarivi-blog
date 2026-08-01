# Yarivi — Contexto do projeto

Blog de tecnologia em português (BR) para leitores curiosos, não especialistas.
Objetivo: tráfego orgânico e monetização (afiliados → AdSense → Journey by Mediavine a 1.000 sessões/mês).
Dona: Mi (violet141521@gmail.com).

## Nome e domínio

- **Nome do blog**: Yarivi (antes: Signal.)
- **Domínio**: yarivi.com (registrado na Cloudflare em 2026-08-01)
- Raiz Tupi: "yara" = senhora das águas

## Estrutura

- `index.html`, `style.css`, `script.js` — base do site (não editar sem pedido explícito)
- `artigos/` — artigos publicados (7 no ar)
- `rascunhos/` — artigos aguardando revisão + `fila.json` (fila de publicação com status)
- `partials/featured.html` e `partials/latest.html` — home (só a signal-publicador atualiza)
- `signal-seo-writer/` e `signal-publicador/` — fonte das skills (instaladas no Claude)
- `signal-blog-publisher/` — skill antiga (aposentada; referência)
- `pesquisas/` — relatórios de pesquisa salvos

## Fluxo editorial (sempre seguir)

1. **Pauta**: skill `signal-seo-writer` — pesquisa (via skill `pesquisa`, fallback WebSearch), 10 temas, usuária escolhe 5
2. **Produção**: os 5 artigos viram rascunhos em `rascunhos/` com status `aguardando-revisao` na fila — **nunca publicar direto**
3. **Revisão**: a usuária lê e aprova/pede mudanças no chat
4. **Publicação**: skill `signal-publicador` — 1 artigo aprovado por dia útil (seg-sex) às 08:00 via tarefa agendada; atualiza partials e marca `publicado`

## Regras

- Nada vai ao ar sem aprovação humana (status `aprovado` na fila)
- Estilo Yarivi: frases curtas, analogia antes de jargão, dados com fonte nomeada, ação concreta no final
- SEO: `<title>` keyword-first ≤60 chars ≠ H1 (manchete com gancho); FAQ com schema FAQPage; 1-3 links internos
- Checklist completo: `signal-seo-writer/references/seo-checklist.md`
- Antes de publicar, a skill `signal-publicador` atualiza a data do artigo (meta `article:published_time`, JSON-LD `datePublished`/`dateModified` e o byline) para o dia real da publicação — nunca mantém a data de quando foi escrito

## Estado atual (2026-08-01)

- **Rebranding concluído**: Signal. → Yarivi; domínio yarivi.com registrado na Cloudflare
- 5 rascunhos na fila aguardando revisão. 2 aprovados (agente-de-ia, celular-dobravel); 3 pendentes (robô humanoide, PC com IA/NPU, bateria estado sólido)
- Agendamento seg-sex 08:00 ainda NÃO criado — criar quando a usuária aprovar todos os rascunhos
- Hospedagem decidida: Cloudflare Pages (deploy AINDA NÃO configurado — ver `signal-publicador/references/deploy.md`; pendente: configurar Pages no painel Cloudflare)
- Perplexity MCP com tokens expirados (skill `pesquisa` usa fallback WebSearch)
- Cor de destaque secundária: `--teal: #34D399` no tema escuro, `#059669` no tema claro (`style.css`)
- Seção de assinatura por e-mail (newsletter) removida temporariamente: botão "Assinar grátis" do nav, seção da home (`partials/newsletter.html` desativada em `script.js`) e o bloco de CTA no rodapé de todos os artigos publicados e rascunhos

## Pendências

1. Configurar Cloudflare Pages (conectar repositório + DNS yarivi.com → Pages)
2. Gerar sitemap.xml e robots.txt após deploy
3. Submeter ao Google Search Console
4. Aprovar 3 rascunhos restantes → criar tarefa agendada de publicação seg-sex 08:00
5. Pós-deploy: páginas legais (privacidade/contato) e aplicar ao AdSense com 12+ artigos
6. Reativar a assinatura por e-mail (newsletter) mais para frente — reinserir `nl-root` em `script.js`, o botão do nav e o CTA nos artigos quando a usuária decidir retomar
