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
git add artigos/{SLUG}.html artigos/_catalog.json sitemap.xml rascunhos/fila.json
git commit -m "feat: publica {SLUG}"
git push origin main
```

> `sitemap.xml` deve estar sempre no `git add` — ele é regenerado a cada publicação
> (passo 4.5 da Operação 3) e precisa ir ao ar junto com o artigo.

## Como verificar

Aguardar ~1 min e checar https://yarivi.com ou https://yarivi-blog.pages.dev
O painel de deployments fica em: Cloudflare Dashboard → Workers & Pages → yarivi-blog

## Verificar sitemap após deploy

Abrir https://yarivi.com/sitemap.xml e confirmar que o novo artigo aparece na lista.
O número de entradas `<url>` deve ser `(total de artigos no _catalog.json) + 3`.
