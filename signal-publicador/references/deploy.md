# Deploy — Cloudflare Pages

STATUS: CONFIGURADO — deploy automático via git push para o branch main.

## Como funciona

- **Projeto Cloudflare Pages:** yarivi-blog
- **Domínios:** yarivi.com, www.yarivi.com, yarivi-blog.pages.dev
- **Método:** integração Git — qualquer push para `main` dispara deploy automático
- **Sem token necessário:** o deploy acontece via GitHub; basta `git push origin main`

## Comando de deploy (executar após subir o lote da semana)

```bash
cd C:\Repositorio\ClaudeProject\Aula1\BlogTI
node scripts/gerar-sitemap.mjs
node scripts/gerar-home-estatica.mjs
git add artigos/{SLUG1}.html artigos/{SLUG2}.html ... artigos/_catalog.json sitemap.xml index.html rascunhos/fila.json img/{SLUG}.webp ...
git add -u rascunhos/   # registra a saída dos rascunhos movidos
git commit -m "feat: lote semanal — N artigos (DD/MM a DD/MM)"
git push origin main
```

> Um push por lote. Cada artigo aparece sozinho na home e no `/sitemap.xml` à meia-noite
> (São Paulo) da sua `data_pub` — `functions/_lib/datas.js`. Não precisa de deploy diário.

## Como verificar

Aguardar ~1 min e checar https://yarivi.com ou https://yarivi-blog.pages.dev
O painel de deployments fica em: Cloudflare Dashboard → Workers & Pages → yarivi-blog

## Verificar sitemap após deploy

Abrir https://yarivi.com/sitemap.xml: devem aparecer só os artigos com data até hoje.
O número de entradas `<url>` deve ser `(artigos com data_pub <= hoje) + 5`. Os agendados
entram sozinhos no dia deles.
