# Deploy — Cloudflare Pages

STATUS: CONFIGURADO — deploy automático via git push para o branch main.

## Como funciona

- **Projeto Cloudflare Pages:** yarivi-blog
- **Domínios:** yarivi.com, www.yarivi.com, yarivi-blog.pages.dev
- **Método:** integração Git — qualquer push para `main` dispara deploy automático
- **Sem token necessário:** o deploy acontece via GitHub; basta `git push origin main`

## Comando de deploy (executar após publicar artigo)

```bash
cd C:\Repositorio\ClaudeProject\Aula1\BlogTI
git add artigos/{SLUG}.html partials/featured.html partials/latest.html rascunhos/fila.json
git commit -m "feat: publica {SLUG}"
git push origin main
```

## Como verificar

Aguardar ~1 min e checar https://yarivi.com ou https://yarivi-blog.pages.dev
O painel de deployments fica em: Cloudflare Dashboard → Workers & Pages → yarivi-blog
