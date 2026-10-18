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
- `artigos/` — artigos publicados + `_catalog.json` (metadata de todos os artigos)
- `rascunhos/` — artigos aguardando revisão + `fila.json` (fila de publicação com status)
- `partials/featured.html` e `partials/latest.html` — fallback estático (não editar mais)
- `index.html` traz nav, hero, manchetes, categorias e rodapé **direto no HTML** (wrappers com `data-static`; o `script.js` não busca de novo). O card ao lado do título (`#hero-card-root`) mostra sempre o último artigo publicado, e "Em destaque" começa no 2º. Em produção, `functions/index.js` troca o card do hero e as manchetes pela lista atual (artigos com data_pub até hoje + liberados no KV) a cada visita (cache 60s). Renderização compartilhada em `functions/_lib/home.js`. Após subir o lote, rodar `python scripts/gerar-thumbs.py`, `node scripts/gerar-home-estatica.mjs` e `node scripts/gerar-sitemap.mjs` (fallbacks estáticos; ambos já ignoram artigos com data futura). Os cards da home mostram a capa de cada artigo (campos `img`/`thumb` no catálogo, preenchidos automaticamente por `gerar-home-estatica.mjs`; miniaturas 640px em `img/thumb/`); sem imagem, mostram o emoji
- `sobre.html` (quem faz, política editorial `#politica-editorial`, correções `#correcoes`, FAQ com schema FAQPage) e `404.html` (servido pelo Pages com status 404; lista de recentes é estática)
- `functions/partials/_middleware.js` — Pages Function que serve featured/latest dinâmico via KV
- `functions/api/publicar.js` — endpoint para liberar um artigo antes da data dele (de qualquer dispositivo)
- `functions/sitemap.xml.js` — sitemap dinâmico (só artigos com data até hoje)
- `signal-seo-writer/` e `signal-publicador/` — fonte das skills (instaladas no Claude)
- `validador-text/` — skill de QA editorial: antiplágio, links, SEO automático (instalar no Claude)
- `signal-blog-publisher/` — skill antiga (aposentada; referência)
- `pesquisas/` — relatórios de pesquisa salvos

## Fluxo editorial (sempre seguir)

1. **Pauta**: skill `signal-seo-writer` — pesquisa (via skill `pesquisa`, fallback WebSearch), 10 temas, usuária escolhe 5
2. **Produção**: os 5 artigos viram rascunhos em `rascunhos/` com status `aguardando-revisao` na fila — **nunca publicar direto**
2.5. **QA automático** (executar imediatamente após escrever cada artigo): skill `validador-text` gera `rascunhos/qa-[slug].md` com antiplágio, links quebrados e checklist SEO
2.6. **Auditoria de dados + correção automática** (executar imediatamente após o QA, antes de apresentar à usuária — obrigatório): verificar **todos** os números, percentuais, datas e estatísticas no texto. Para cada dado:
   - Se tiver fonte verificável (WebSearch confirma): manter e citar a fonte na seção `art-sources`
   - Se não tiver fonte verificável: **remover do texto imediatamente e reescrever a frase** para manter coerência — nunca inventar, aproximar ou deixar o dado pendente para a usuária decidir
   - **As correções são aplicadas no próprio arquivo do rascunho** — a Mi recebe sempre a versão já corrigida, nunca o rascunho bruto
   - Ao apresentar o rascunho, incluir um resumo compacto: dados mantidos (fonte citada) e dados removidos (como a frase foi reescrita)
   - Atenção especial a: citações diretas atribuídas a organizações, datas de leis/documentos, porcentagens de adoção/uso, contagens (alunos, usuários, mercado)
2.7. **Prompt de imagem** (executar logo após escrever cada artigo, junto com QA/auditoria):
   skill `signal-seo-writer` gera `rascunhos/img-[slug].md` com metáfora central, prompt de
   geração (inglês) e alt-text (português), seguindo o padrão visual em
   `signal-seo-writer/references/imagem-prompt.md` (render cinematográfico escuro, teal neon
   `#34D399` como cor primária, uma metáfora literal central por imagem, sem texto/logos/rostos)
3. **Revisão**: a usuária lê o artigo **já auditado e corrigido** + relatório QA e aprova/pede mudanças no chat
4. **Lote semanal** (requer PC, 1 push por semana): a skill `signal-publicador` **avisa antes quantos aprovados vão subir** (máx. 5, só o que tiver) com o calendário, e após o OK move os artigos para `artigos/` com **1 data por dia útil** (seg-sex, a partir do próximo dia útil), atualiza `_catalog.json`, `fila.json`, sitemap e home estática, e faz um único commit/push.
5. **Ir ao ar** (automático): cada artigo aparece sozinho na home e no `/sitemap.xml` à meia-noite (São Paulo) da sua `data_pub` — regra em `functions/_lib/datas.js`. Antes disso só abre pela URL direta. O link `/api/publicar` serve apenas para liberar um artigo **antes** da data.

## Visibilidade na home — data + KV

A home e o `/sitemap.xml` são servidos por Pages Functions que mostram um artigo quando:
- a `data_pub` dele em `artigos/_catalog.json` já chegou (fuso São Paulo) — **regra principal, automática**; ou
- o slug está no KV `YARIVI_PUBLISHED` — para liberar antes da data.

**Para liberar um artigo antes da data dele:**

Opção A — URL simples (funciona no celular):
```
https://yarivi.com/api/publicar?slug=[slug]&key=[PUBLISH_KEY]
```

Opção B — Cloudflare Dashboard:
```
dash.cloudflare.com → Workers & Pages → KV → YARIVI_PUBLISHED
→ Create entry: key = [slug], value = true
```

A home atualiza em até 1 minuto após a publicação (cache de 60s).

**Configuração inicial (feita uma vez):**
1. Workers & Pages → KV → Create namespace `YARIVI_PUBLISHED`
2. Pages → yarivi → Settings → Functions → KV namespace bindings → Add: `YARIVI_PUBLISHED`
3. Pages → yarivi → Settings → Environment variables → Add: `PUBLISH_KEY` (senha forte)
4. Adicionar os 12 slugs existentes no KV (todos com valor `true`):
   - bateria-estado-solido-celular-2026
   - celular-dobravel-vale-a-pena-2026
   - pc-com-ia-npu-vale-a-pena-2026
   - robo-humanoide-2026
   - agente-de-ia-o-que-e-2026
   - como-explicar-ia-para-leigos-2026
   - qualquer-pessoa-pode-criar-um-app-2026
   - celular-obsoleto-ia-npu-2026
   - futuro-profissoes-2026-2030
   - phishing-whatsapp-email-2026
   - perigo-quantico-criptografia-2026
   - ia-generativa-mercado-trabalho-2026
5. `git push` → Pages deploya com as Functions ativas

## Regras

- Nada vai ao ar sem aprovação humana (status `aprovado` na fila)
- Estilo Yarivi: frases curtas, analogia antes de jargão, dados com fonte nomeada, ação concreta no final
- **Regra de dados**: nenhum número, percentual, data ou estatística vai ao ar sem fonte verificada. A auditoria acontece imediatamente após escrever — se não há fonte, o dado é removido e a frase reescrita automaticamente antes de qualquer apresentação à usuária. Nunca manter dado inventado, aproximado ou sem fonte
- SEO: `<title>` keyword-first ≤60 chars ≠ H1 (manchete com gancho); FAQ com schema FAQPage; 1-3 links internos
- Checklist completo: `signal-seo-writer/references/seo-checklist.md`
- Ao subir o lote, a skill `signal-publicador` data cada artigo (meta `article:published_time`, JSON-LD `datePublished`/`dateModified`, byline e `data_pub` no catálogo) com **o dia útil em que ele vai ao ar** — 1 artigo por dia, nunca a data de quando foi escrito
- Links internos e "Leia também" nunca apontam para artigo com data posterior à do próprio artigo

## Estado atual (2026-08-01)

- **Rebranding concluído**: Signal. → Yarivi; domínio yarivi.com registrado na Cloudflare
- 5 rascunhos na fila aguardando revisão. 2 aprovados (agente-de-ia, celular-dobravel); 3 pendentes (robô humanoide, PC com IA/NPU, bateria estado sólido)
- Agendamento diário desligado em 2026-10-17: publicação agora é lote semanal com datas escalonadas + liberação automática pela data
- Hospedagem decidida: Cloudflare Pages (deploy AINDA NÃO configurado — ver `signal-publicador/references/deploy.md`; pendente: configurar Pages no painel Cloudflare)
- Perplexity MCP com tokens expirados (skill `pesquisa` usa fallback WebSearch)
- Cor de destaque secundária: `--teal: #34D399` no tema escuro, `#059669` no tema claro (`style.css`)
- Seção de assinatura por e-mail (newsletter) removida temporariamente: botão "Assinar grátis" do nav, seção da home (`partials/newsletter.html` desativada em `script.js`) e o bloco de CTA no rodapé de todos os artigos publicados e rascunhos

## Pendências

### ✅ Concluídos
1. ~~Configurar Cloudflare Pages~~ — concluído (2026-08-01)
2. ~~Gerar sitemap.xml e robots.txt~~ — concluído (2026-08-01)
3. ~~Aprovar 3 rascunhos restantes~~ — concluído (2026-08-07); tarefa agendada seg-sex ativa às 18:00 (yarivi-publicador-diario)
4. ~~Cloudflare: investigar origem dos ~274 redirects 301/308 (22% do tráfego)~~ — concluído (2026-08-08): causa era links internos com `.html`; corrigidos em `partials/featured.html`, `partials/latest.html`, `functions/partials/_middleware.js` e artigos com cross-links
5. ~~Cloudflare: criar Cache Rules~~ — concluído (2026-08-10): `yarivi-cache-artigos` (URI Path starts with `/artigos/` and does not contain `.` → Eligible for cache) e `yarivi-bypass-api` (URI Path starts with `/api/` → Bypass cache). Nota: operador `matches regex` requer plano Business; substituído por `starts_with` + `not contains "."`

### 🔜 A fazer (em ordem)
6. Submeter ao Google Search Console
7. Aplicar ao AdSense — pré-requisitos cumpridos: páginas legais criadas + 13 artigos publicados
8. Abrir MEI para formalizar o blog como negócio — após abrir, atualizar `contato.html`, `privacidade.html` e `termos.html`: trocar "Milena" pela razão social e adicionar CNPJ como identificador do controlador de dados (LGPD)
9. ~~Página Sobre~~ — criada (2026-10-05), com coluna "Institucional" no footer. Pendente: Anuncie, Escreva para nós; foto/bio da Mi na Sobre (opcional)
10. Inserir links de afiliados nos artigos pertinentes — fazer após aprovação do AdSense (mapear quais artigos já publicados têm oportunidade e adicionar antes/durante a revisão dos novos)
11. Reativar newsletter **só com serviço de e-mail real** (o formulário antigo simulava inscrição e foi removido em 2026-10-05 de artigos, rascunhos, templates e `partials/newsletter.html`) — reinserir `nl-root` em `script.js`, botão no nav, CTA nos artigos e coluna "Yarivi" no footer (`partials/footer.html`)
12. Criar redes sociais do Yarivi (Twitter/X, Instagram, LinkedIn, YouTube) e adicionar coluna "Social" no footer (`partials/footer.html`) com links reais
13. Versão em inglês do blog — artigos menos Brasil-específicos, maior alcance orgânico (decidir estrutura: subdomínio `en.yarivi.com` vs. pasta `/en/`)
14. ~~Validação de plágio dos artigos~~ — skill `validador-text` criada (2026-08-12): antiplágio DIY via WebSearch + link checker + checklist SEO automático. **Pendente: instalar a skill no Claude** (abrir `validador-text/SKILL.md` no Claude → Save skill). Spec em `docs/validador-text-spec.md`.
15. ~~Definir padrão de imagem por artigo~~ — concluído (2026-09-08): padrão visual e prompt documentados em `signal-seo-writer/references/imagem-prompt.md`; geração automática do prompt incluída no fluxo editorial (passo 2.7). Imagens inseridas em todos os 64 artigos (2026-10-17); miniaturas em `img/thumb/` usadas nos cards da home.
