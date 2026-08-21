# Pendências — Blog Yarivi

Atualizado em 2026-08-17. Ordem = prioridade (dependências primeiro).

## Crítico (bloqueia o resto)

- [x] **Domínio do blog** — yarivi.com registrado na Cloudflare (2026-08-01)
- [x] **Configurar Cloudflare** — Pages + DNS + SSL configurados (2026-08-01)
- [ ] **Abrir empresa (MEI ou CNPJ)** — necessário para afiliados e para AdSense/Mediavine como pessoa jurídica; após abrir, atualizar `contato.html`, `privacidade.html` e `termos.html` com razão social e CNPJ

## Alto

- [ ] **Análise de risco jurídico** — exposição em conteúdo (marcas/produtos citados, reviews, links de afiliado, dados de acesso)
- [ ] **Proteção de direitos autorais** — licença das imagens usadas, registro de marca do nome "Yarivi", termos sobre reuso do conteúdo
- [ ] **Páginas legais (LGPD)** — privacidade, termos e contato já existem; atualizar com CNPJ após abrir MEI; disclosure de links afiliados a incluir
- [ ] **AdSense** — pré-requisitos já cumpridos (13 artigos publicados + páginas legais no ar); submeter em google.com/adsense

## Médio

- [ ] **Analisar concorrentes** — benchmarking de blogs de tech BR (estrutura, monetização, SEO)
- [x] **Agendar publicação via Claude** — task `yarivi-publicador-diario` ativa seg–sex 18:00 (2026-08-07)
- [ ] **Google Search Console + Analytics** — indexação e métricas (pré-requisito comum do AdSense)
- [x] **Sitemap.xml / robots.txt** — gerados e no ar (2026-08-01)
- [ ] **Cadastro em programas de afiliados** (Amazon Associates etc.) — depende do CNPJ
- [ ] **Backup / versionamento do site** — segurança básica antes de escalar o volume de artigos
- [ ] **Instalar skill validador-text** — skill criada em 2026-08-12 (antiplágio + link checker + checklist SEO); abrir `validador-text/SKILL.md` no Claude → Save skill

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

## Concluídos recentemente

- [x] **Cloudflare Cache Rules** — `yarivi-cache-artigos` e `yarivi-bypass-api` criadas (2026-08-10)
- [x] **Corrigir redirects 301/308** — links internos com `.html` corrigidos em partials, middleware e artigos (2026-08-08)
- [x] **Skill validador-text criada** — antiplágio DIY + link checker + checklist SEO (2026-08-12); pendente apenas a instalação

## Em andamento

- [ ] 5 rascunhos aguardando revisão (agente-de-ia, robô humanoide, RTX Spark, dobráveis, bateria sólida)
- [ ] **Seção "Leia também"** — adicionar bloco com links para artigos relacionados do Yarivi ao final de cada artigo (melhora retenção e reduz bounce rate)
