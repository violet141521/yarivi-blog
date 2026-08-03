# Pendências — Blog Signal.

Atualizado em 2026-07-17. Ordem = prioridade (dependências primeiro).

## Crítico (bloqueia o resto)

- [ ] **Domínio do blog** — registrar domínio (~R$40/ano)
- [ ] **Configurar Cloudflare** — Pages + DNS + SSL (ver `signal-publicador/references/deploy.md`)
- [ ] **Abrir empresa (MEI ou CNPJ)** — necessário para afiliados e para AdSense/Mediavine como pessoa jurídica

## Alto

- [ ] **Análise de risco jurídico** — exposição em conteúdo (marcas/produtos citados, reviews, links de afiliado, dados de acesso)
- [ ] **Proteção de direitos autorais** — licença das imagens usadas, registro de marca do nome "Signal", termos sobre reuso do conteúdo
- [ ] **Páginas legais (LGPD)** — política de privacidade, termos de uso, aviso de cookies, disclosure de links afiliados
- [ ] **AdSense** — aplicar só após páginas legais prontas e 12+ artigos no ar

## Médio

- [ ] **Analisar concorrentes** — benchmarking de blogs de tech BR (estrutura, monetização, SEO)
- [ ] **Agendar "Programado" e publicar via Claude** — tarefa seg-sex 08:00 (depende do deploy no ar + rascunhos aprovados)
- [ ] **Google Search Console + Analytics** — indexação e métricas (também pré-requisito comum do AdSense)
- [ ] **Sitemap.xml / robots.txt** — SEO técnico, normalmente resolvido no deploy
- [ ] **Cadastro em programas de afiliados** (Amazon Associates etc.) — depende do CNPJ
- [ ] **Backup / versionamento do site** — segurança básica antes de escalar o volume de artigos

## Segurança — Painel Cloudflare (fazer após o deploy)

Configurações no dashboard do Cloudflare que não dependem de arquivos no repositório:

- [ ] **SSL/TLS → Edge Certificates → Always Use HTTPS**: ativar
- [ ] **SSL/TLS → Edge Certificates → HSTS**: ativar com `max-age=31536000; includeSubDomains; preload` (aguardar site estável antes de ativar o preload)
- [ ] **SSL/TLS → Edge Certificates → Minimum TLS Version**: definir como TLS 1.2
- [ ] **SSL/TLS → Edge Certificates → TLS 1.3**: ativar
- [ ] **SSL/TLS → Edge Certificates → Automatic HTTPS Rewrites**: ativar
- [ ] **Security → Bots → Bot Fight Mode**: ativar (plano gratuito)
- [ ] **Scrape Shield → Hotlink Protection**: ativar (impede que outros sites "roubem" as imagens do Yarivi)
- [ ] **Scrape Shield → Email Address Obfuscation**: ativar (se o e-mail aparecer em alguma página pública)

Arquivos já configurados (commit e deploy atualizam automaticamente):
- `_headers` — Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy
- `_redirects` — diretórios internos redirecionam para /index.html
- `robots.txt` — diretórios internos bloqueados para crawlers

## Já em andamento (contexto do projeto)

- [ ] 5 rascunhos aguardando aprovação (agente de IA, robô humanoide, RTX Spark, dobráveis, bateria sólida)
