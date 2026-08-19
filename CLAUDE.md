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
- `functions/partials/_middleware.js` — Pages Function que serve featured/latest dinâmico via KV
- `functions/api/publicar.js` — endpoint para publicar artigo de qualquer dispositivo
- `signal-seo-writer/` e `signal-publicador/` — fonte das skills (instaladas no Claude)
- `validador-text/` — skill de QA editorial: antiplágio, links, SEO automático (instalar no Claude)
- `signal-blog-publisher/` — skill antiga (aposentada; referência)
- `pesquisas/` — relatórios de pesquisa salvos

## Fluxo editorial (sempre seguir)

1. **Pauta**: skill `signal-seo-writer` — pesquisa (via skill `pesquisa`, fallback WebSearch), 10 temas, usuária escolhe 5
2. **Produção**: os 5 artigos viram rascunhos em `rascunhos/` com status `aguardando-revisao` na fila — **nunca publicar direto**
2.5. **QA automático** (novo): skill `validador-text` gera `rascunhos/qa-[slug].md` com antiplágio, links quebrados e checklist SEO — rodar antes de apresentar o artigo à usuária para revisão
2.6. **Auditoria de dados** (obrigatório): antes de entregar o rascunho para revisão, verificar **todos** os números, percentuais, datas e estatísticas no texto. Para cada dado:
   - Se tiver fonte verificável (WebSearch confirma): manter e citar a fonte na seção `art-sources`
   - Se não tiver fonte verificável: **remover do texto**, reescrevendo a frase para manter coerência (sem inventar ou aproximar)
   - Reportar à usuária quais dados foram mantidos (com fonte) e quais foram removidos (sem fonte)
   - Atenção especial a: citações diretas atribuídas a organizações, datas de leis/documentos, porcentagens de adoção/uso, contagens (alunos, usuários, mercado)
3. **Revisão**: a usuária lê o artigo + relatório QA e aprova/pede mudanças no chat
4. **Commit** (requer PC): skill `signal-publicador` move artigo para `artigos/`, atualiza `_catalog.json` e `fila.json`. O artigo fica acessível pela URL direta mas **invisível na home**.
5. **Publicar na home** (qualquer dispositivo): a usuária decide quando tornar o artigo visível — via URL do celular ou dashboard Cloudflare (ver seção abaixo).

## Cloudflare KV — controle de visibilidade

A home é servida por uma Pages Function que lê dois arquivos:
- `artigos/_catalog.json` — metadata de todos os artigos (git)
- KV namespace `YARIVI_PUBLISHED` — quais slugs estão visíveis (Cloudflare)

**Para publicar um artigo (tornar visível na home):**

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
- **Regra de dados**: nenhum número, percentual, data ou estatística vai ao ar sem fonte verificada. Se não há fonte, remover e reescrever — nunca manter dado inventado ou aproximado sem aviso
- SEO: `<title>` keyword-first ≤60 chars ≠ H1 (manchete com gancho); FAQ com schema FAQPage; 1-3 links internos
- Checklist completo: `signal-seo-writer/references/seo-checklist.md`
- Antes de publicar, a skill `signal-publicador` atualiza a data do artigo (meta `article:published_time`, JSON-LD `datePublished`/`dateModified` e o byline) para o dia real da publicação — nunca mantém a data de quando foi escrito

## Estado atual (2026-08-01)

- **Rebranding concluído**: Signal. → Yarivi; domínio yarivi.com registrado na Cloudflare
- 5 rascunhos na fila aguardando revisão. 2 aprovados (agente-de-ia, celular-dobravel); 3 pendentes (robô humanoide, PC com IA/NPU, bateria estado sólido)
- Agendamento seg-sex 18:00 criado e ativo (task ID: yarivi-publicador-diario)
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
9. Criar páginas: Sobre nós, Anuncie, Escreva para nós, Contato — e reincluir coluna "Yarivi" no footer com links reais
10. Inserir links de afiliados nos artigos pertinentes — fazer após aprovação do AdSense (mapear quais artigos já publicados têm oportunidade e adicionar antes/durante a revisão dos novos)
11. Reativar newsletter — reinserir `nl-root` em `script.js`, botão no nav, CTA nos artigos e coluna "Yarivi" no footer (`partials/footer.html`)
12. Criar redes sociais do Yarivi (Twitter/X, Instagram, LinkedIn, YouTube) e adicionar coluna "Social" no footer (`partials/footer.html`) com links reais
13. Versão em inglês do blog — artigos menos Brasil-específicos, maior alcance orgânico (decidir estrutura: subdomínio `en.yarivi.com` vs. pasta `/en/`)
14. ~~Validação de plágio dos artigos~~ — skill `validador-text` criada (2026-08-12): antiplágio DIY via WebSearch + link checker + checklist SEO automático. **Pendente: instalar a skill no Claude** (abrir `validador-text/SKILL.md` no Claude → Save skill). Spec em `docs/validador-text-spec.md`.
15. Adicionar 1 imagem por artigo — todos os artigos publicados e futuros devem ter ao menos uma imagem ilustrativa (definir padrão: gerada, stock ou captura; onde inserir no HTML; atributo `alt` descritivo para SEO).
