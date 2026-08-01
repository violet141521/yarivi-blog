# Relatório 3 — Páginas legais e LGPD

**Data**: 2026-07-18
**Escopo**: política de privacidade, termos de uso, aviso de cookies, disclosure de afiliados — pendência nº 3 do blog (pós-deploy, pré-AdSense)
**Framework**: formato de compliance-check da skill `legal:compliance-check`
**Aviso**: modelos e roteiro para implementação; revisão por advogado(a) é recomendada antes de escalar a monetização.

---

## Resumo

**Prosseguir com condições.** O blog hoje quase não trata dados pessoais (sem analytics, sem cookies próprios, newsletter desativada) — o momento é ideal para nascer conforme. As páginas legais são pré-requisito prático para o AdSense (o Google exige política de privacidade com conteúdo específico) e para a Journey/Mediavine. A implementação é 100% executável internamente, em 4 fases atreladas ao roadmap já existente do blog.

## Regulamentos aplicáveis

| Norma | Como se aplica ao Signal | Exigência-chave |
|-------|--------------------------|-----------------|
| **LGPD** (Lei 13.709/2018) | IP, cookies e e-mail (futura newsletter) são dados pessoais | Base legal por tratamento; direitos do titular respondidos em **15 dias**; canal do encarregado |
| **Guia de Cookies da ANPD** | Banner e política de cookies quando houver cookies não essenciais | Consentimento livre, informado, inequívoco e **granular**; proibição de dark patterns; registro do consentimento |
| **Res. CD/ANPD nº 2/2022** (pequeno porte) | Blog individual/MEI = agente de pequeno porte | **Dispensa a nomeação de encarregado (DPO)**, mas exige manter canal de contato para titulares |
| **Marco Civil da Internet** (Lei 12.965/2014) | Guarda de registros e transparência | Informar coleta em termos claros |
| **CDC art. 36** + **Guia CONAR 2026** | Links de afiliado = publicidade | Identificação ostensiva; o link por si só **não basta** como aviso |
| **Política do Google AdSense** | Pré-requisito da monetização | Política de privacidade declarando cookies de terceiros (Google) para anúncios + CMP certificada para tráfego europeu (recomendada também para Brasil) |

## Requisitos (estado atual)

| # | Requisito | Status | Ação |
|---|-----------|--------|------|
| 1 | Política de privacidade | ❌ Não existe | Fase 1 |
| 2 | Termos de uso (com seção de reuso de conteúdo — Relatório 2) | ❌ Não existe | Fase 1 |
| 3 | Política/aviso de cookies | ❌ Não existe | Fase 1 (página) + Fase 3 (banner) |
| 4 | Disclosure de afiliados | ❌ Não existe | Fase 1 (página) + aviso por artigo quando ativar |
| 5 | Canal de contato do titular | ⚠️ E-mail existe, não publicado | Fase 1 (constar nas páginas) |
| 6 | Eliminar vazamento de IP (Google Fonts remoto) | ❌ Fonts via CDN Google | Fase 1 (self-host — ver Relatório 1) |
| 7 | Banner de consentimento/CMP | ➖ Ainda não necessário (sem cookies não essenciais) | Fase 3, antes de analytics/AdSense |
| 8 | Consentimento da newsletter | ➖ Newsletter desativada | Fase 4, ao reativar |

## Plano passo a passo

### Fase 1 — Criar as 4 páginas (agora; pré-deploy) · R$ 0 · ~1 sessão de trabalho

**Passo 1. Criar `legal/` no site com 4 páginas HTML** (mesmo layout dos artigos, sem index na busca interna, com `<meta name="robots" content="noindex">` opcional — manter indexável é aceitável e o AdSense verifica a existência):

- `legal/privacidade.html` — conteúdo mínimo:
  1. Quem é a controladora (Mi / futuramente MEI, e-mail violet141521@gmail.com);
  2. O que é coletado hoje: nenhum dado pessoal pelo site em si; preferência de tema salva localmente no navegador (localStorage, não sai do aparelho);
  3. O que passará a ser coletado quando ativado: estatísticas de audiência e cookies de publicidade de terceiros (Google AdSense) — com a frase exigida pelo Google de que "terceiros, incluindo o Google, usam cookies para veicular anúncios com base em visitas anteriores" + link para as configurações de anúncios do Google e para aboutads.info;
  4. Bases legais por finalidade (consentimento para cookies de anúncio; legítimo interesse para métricas essenciais — documentar o teste de legítimo interesse quando ativar);
  5. Direitos do titular (acesso, correção, eliminação, revogação do consentimento, informação sobre compartilhamento) e prazo de resposta de 15 dias;
  6. Canal do encarregado: o e-mail do blog (Res. ANPD nº 2/2022 dispensa DPO para pequeno porte, mas o canal é obrigatório);
  7. Data de vigência e histórico de versões.
- `legal/termos.html` — objeto do site (conteúdo informativo, não é consultoria), limitação de responsabilidade (preços e specs mudam; decisões de compra são do leitor), propriedade intelectual + regras de reuso (Relatório 2, opção B), lei e foro brasileiros.
- `legal/cookies.html` — tabela de cookies/armazenamento: hoje só `signal-theme` (localStorage, essencial de preferência, sem consentimento exigido); seções "quando ativarmos estatísticas" e "quando ativarmos anúncios" já redigidas e marcadas como "ainda não ativo" (honestidade > boilerplate).
- `legal/afiliados.html` — declaração de que alguns links poderão gerar comissão sem custo ao leitor, que a opinião editorial não é vendida e que artigos com links comissionados trazem aviso no topo.

**Passo 2. Linkar no rodapé** (`partials/footer.html`): Privacidade · Termos · Cookies · Afiliados · Contato. Única edição em arquivo base — pedir aprovação explícita antes (regra do projeto).

**Passo 3. Self-host das fontes** (detalhado no Relatório 1) — remove o único envio de dado pessoal atual e simplifica a política.

**Passo 4. Redação em estilo Signal**: as páginas legais também devem ser legíveis — frases curtas, sem juridiquês inútil. Transparência é requisito da LGPD (art. 6º, VI).

### Fase 2 — Deploy (Cloudflare Pages)

**Passo 5.** Conferir que Cloudflare Web Analytics, se ativado, está no modo sem cookies (é o padrão — não exige consentimento, só menção na política). Evitar ativar o RUM com cookies.

**Passo 6.** `robots.txt` + bloqueio de AI crawlers (Relatório 2).

### Fase 3 — Antes de Google Analytics / AdSense · custo R$ 0-30/mês

**Passo 7. Instalar CMP** (banner de consentimento). Opções: modo de consentimento do próprio Google com a mensagem GDPR/LGPD do AdSense (grátis) ou CMP certificada (Cookiebot, CookieYes, AdOpt — a AdOpt é brasileira e focada em LGPD, com plano gratuito para sites pequenos). Requisitos do banner segundo o Guia da ANPD: opção real de recusar com o mesmo destaque do aceitar, granularidade por finalidade, sem dark patterns, registro do consentimento, link para a política.

**Passo 8. Só depois do banner ativo**, inserir as tags (Analytics/AdSense) condicionadas ao consentimento (Google Consent Mode v2).

**Passo 9. Atualizar `cookies.html` e `privacidade.html`** tirando o "ainda não ativo" e listando os cookies reais (nome, finalidade, prazo, terceiro).

### Fase 4 — Ao reativar a newsletter

**Passo 10.** Formulário com: finalidade explícita ("enviar a newsletter, nada mais"), checkbox não pré-marcada, double opt-in (confirmação por e-mail), link de descadastro em todo envio, e menção na política (base legal: consentimento). Escolher provedor de e-mail com DPA/adequação LGPD.

### Rotina

**Passo 11.** Revisar as 4 páginas a cada 6 meses ou quando: ativar ferramenta nova que colete dado, ANPD publicar norma de cookies (agenda 2025-2026 em andamento), AdSense mudar requisitos. Manter changelog no fim de cada página.

## Riscos de não fazer

| Risco | Severidade | Quando morde |
|-------|-----------|--------------|
| Reprovação/banimento no AdSense por falta de política de privacidade | Alta (mata a monetização) | Na aplicação, com 12+ artigos |
| Sanção LGPD (advertência → multa) | Média (ANPD prioriza casos maiores, mas advertência é real) | Após analytics/ads sem consentimento |
| Journey/Mediavine exige compliance de consentimento | Alta | Ao atingir 1.000 sessões/mês |
| Perda de confiança do leitor (sem páginas legais o site parece amador) | Média | Sempre |

## Aprovações necessárias

| Quem | O quê |
|------|-------|
| Mi | Aprovar textos das 4 páginas antes de irem ao ar (regra do blog: nada publica sem aprovação) |
| Mi | Autorizar a edição do `partials/footer.html` (arquivo base) |
| Advogado(a) — opcional, recomendado | Revisão única das 4 páginas quando a receita justificar (~R$ 500-1.500 avulso) |

## Fontes

- [ANPD — Guia Orientativo: Cookies e Proteção de Dados Pessoais (PDF oficial)](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf)
- [LegalSuite — Cookies e banners de consentimento: LGPD e ANPD em 2026](https://legalsuite.com.br/blog/digital-cookies-banner-lgpd-2026)
- [GoAdopt — Consentimento AdSense: adequação à LGPD e políticas do Google](https://goadopt.io/blog/consentimento-adsense-guia-lgpd-e-as-politicas-do-google/)
- [Google AdSense — Conteúdo obrigatório](https://support.google.com/adsense/answer/1348695?hl=pt-BR)
- [Google AdSense — Requisitos de qualificação](https://support.google.com/adsense/answer/9724?hl=pt-BR)
- [Google AdSense — Política de consentimento UE / CMP certificada](https://support.google.com/adsense/answer/7670013?hl=pt-BR)
- [CONAR — Guia de Publicidade por Influenciadores 2026 (PDF)](http://conar.org.br/pdf/260525_GUIA_INFLUENCIADORES_CONAR_v6.pdf)
