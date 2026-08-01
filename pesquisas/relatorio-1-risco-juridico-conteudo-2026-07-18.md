# Relatório 1 — Análise de risco jurídico: exposição em conteúdo

**Data**: 2026-07-18
**Escopo**: 12 artigos do Blog Signal. (7 publicados + 5 rascunhos), `script.js`, partials e fila de publicação
**Framework**: matriz severidade (1-5) × probabilidade (1-5) — skill `legal:legal-risk-assessment`
**Aviso**: este relatório organiza riscos e prioridades; não substitui parecer de advogado(a).

---

## 1. O que foi auditado (fatos levantados no código)

- **Marcas citadas com frequência**: iPhone/Apple (52×), Samsung/Galaxy (72×), Google (33×), Intel (32×), Windows (24×), Gartner (24×), WhatsApp (17×), Toyota (15×), Nvidia (21×), Microsoft (13×), IDC (16×), Motorola (5×), BYD (8×), Itaú (4×), Banco do Brasil, Claro, Deloitte, Goldman Sachs.
- **Tom de review/opinião**: 4 artigos "vale a pena" (dobrável, PC com NPU, bateria, robô humanoide) com juízo de valor e recomendação de compra/espera.
- **Preços citados**: R$ 12.999 a R$ 15.999 (dobráveis), US$ 2.899-20.000 (robôs) etc.
- **Afirmações factuais negativas sobre empresas nomeadas**: ex. rascunho `agente-de-ia-o-que-e-2026.html` — "agente de codificação da Amazon deletou o ambiente de produção... 13 horas fora do ar" e caso "PocketOS".
- **Links de afiliado**: **nenhum ainda** (monetização planejada, não implementada).
- **Dados de acesso**: sem analytics, sem AdSense, sem cookies próprios. Únicos pontos: (a) `localStorage` com preferência de tema (`signal-theme`) — não é dado pessoal; (b) **Google Fonts carregado do CDN do Google** (`fonts.googleapis.com`) — envia o IP do visitante ao Google sem consentimento.
- **Mitigante já presente**: todo dado tem fonte nomeada com link (padrão editorial Signal) — 60+ links externos para Gartner, IDC, Exame, Tecnoblog, CNN etc.

---

## 2. Registro de riscos (matriz)

| ID | Risco | Sev. | Prob. | Score | Nível |
|----|-------|------|-------|-------|-------|
| R1 | Citação nominativa de marcas em conteúdo informativo | 2 | 1 | 2 | 🟢 Baixo |
| R2 | Afirmação factual negativa sobre empresa nomeada estar imprecisa (Amazon, PocketOS) → notificação extrajudicial / dano à imagem | 3 | 2 | 6 | 🟡 Médio |
| R3 | Review "vale a pena" virar publicidade comparativa depreciativa **quando houver afiliados** (favorece marca que comissiona) | 3 | 3 | 9 | 🟡 Médio |
| R4 | Link de afiliado sem identificação de publicidade (CDC art. 36 + Guia CONAR 2026, que passou a incluir afiliados expressamente) | 3 | 4 | 12 | 🟠 Alto* |
| R5 | Coleta de IP via Google Fonts remoto sem base legal/consentimento (LGPD) | 2 | 3 | 6 | 🟡 Médio |
| R6 | Preços e datas desatualizados induzirem leitor a erro (CDC — informação enganosa por desatualização) | 2 | 3 | 6 | 🟡 Médio |
| R7 | Analytics/AdSense futuros sem consentimento e sem política de privacidade | 4 | 4 | 16 | 🔴 Crítico* |

\* R4 e R7 são riscos **condicionais**: só se materializam se afiliados/anúncios entrarem no ar sem as mitigações. Hoje o score efetivo é baixo; o valor mostrado é o cenário "ativar monetização sem preparar nada". A mitigação transforma ambos em 🟢.

### Análise resumida por risco

**R1 — Citar marcas (🟢 aceitar e documentar).** A Lei 9.279/96 (art. 132, IV) permite citar marca alheia em publicação sem conotação comercial e sem depreciar seu caráter distintivo. Blogs comparativos para orientar o consumidor são exemplo clássico de uso permitido. O padrão atual do Signal (informativo, com fontes) está dentro do seguro.

**R2 — Fatos negativos sobre empresas (🟡 mitigar).** Afirmações do tipo "a IA da Amazon derrubou produção por 13h" são o ponto mais sensível do conteúdo atual: se a informação estiver errada ou sem fonte verificável, há risco de notificação/remoção e, em tese, responsabilização civil. Mitigação: (a) sempre atribuir — "segundo [veículo]" com link para fonte primária; (b) preferir fatos amplamente reportados; (c) manter tom factual, sem adjetivação ("desastre", "vergonha").

**R3 — Reviews + afiliados (🟡 monitorar, vira regra editorial).** É vedado comparativo que deprecia marca para favorecer outra comercializada por quem publica. Enquanto não há afiliados, a opinião é livre (liberdade editorial). Quando houver, a regra passa a ser: nunca rebaixar o concorrente do produto afiliado; separar visivelmente opinião editorial de link comercial.

**R4 — Disclosure de afiliados (🟠→🟢 com mitigação).** O Guia CONAR de 2026 incluiu afiliados expressamente: remuneração por clique/venda caracteriza publicidade e a simples presença do link **não basta** como identificação. Mitigação obrigatória antes do 1º link: aviso claro no topo do artigo + página de disclosure (ver Relatório 3).

**R5 — Google Fonts (🟡 mitigar barato).** Precedente europeu (multa na Alemanha) considera o envio do IP ao Google sem consentimento uma violação; a lógica se transporta para a LGPD (IP = dado pessoal). Mitigação: **self-host das fontes Fraunces e Manrope** (baixar via google-webfonts-helper, servir do próprio Cloudflare Pages). Elimina o único vazamento de dado atual do site e ainda melhora performance.

**R6 — Desatualização (🟡 processo editorial).** Artigos com preço e "vale a pena" envelhecem rápido. Mitigação: exibir "atualizado em" visível, revisar artigos de preço a cada 90 dias, usar faixas ("a partir de R$ X, em julho/2026").

**R7 — Monetização sem base LGPD (🔴 condicional — bloqueio de gate).** AdSense usa cookies de terceiros para anúncios; o Google exige política de privacidade que declare isso e recomenda/exige CMP (plataforma de consentimento certificada). Ativar sem isso arrisca banimento da conta AdSense (perda da monetização, o pior cenário de negócio do blog) + irregularidade LGPD. Mitigação: gate formal — **nenhum script de analytics/anúncio entra no site antes das páginas legais + banner de consentimento** (plano no Relatório 3).

---

## 3. Plano de ação passo a passo

### Fase A — Agora (antes do deploy) · custo R$ 0
1. **Self-host Google Fonts** — baixar Fraunces + Manrope, colocar em `/fonts/`, trocar os `<link>` por `@font-face` no `style.css`. Aplicar em index, artigos e rascunhos. *(resolve R5)*
2. **Revisão de atribuição nos 12 artigos** — conferir que toda afirmação negativa sobre empresa nomeada tem "segundo [fonte]" + link (foco: `agente-de-ia-o-que-e-2026.html`, casos Amazon e PocketOS; confirmar que "PocketOS" é caso real e não exemplo inventado — se inventado, sinalizar como hipotético ou remover). *(resolve R2)*
3. **Selo "atualizado em"** — garantir que artigos com preço mostrem mês/ano dos valores. *(mitiga R6)*

### Fase B — Antes do 1º link de afiliado
4. **Criar regra editorial fixa** (adicionar ao `seo-checklist.md`): (a) aviso de afiliado no topo de qualquer artigo com link comissionado; (b) proibido depreciar concorrente de produto afiliado; (c) opinião editorial escrita antes de escolher o programa de afiliado. *(resolve R3/R4)*
5. **Publicar página de disclosure** (entregue no Relatório 3).

### Fase C — Antes de analytics/AdSense
6. **Gate LGPD**: páginas legais no ar + banner de consentimento/CMP certificada funcionando **antes** de qualquer tag do Google. *(resolve R7)*

### Rotina contínua
7. Revisar este registro de riscos a cada trimestre ou quando: chegar notificação de terceiro, ativar afiliado novo, ANPD publicar norma sobre cookies/consentimento (tema está na agenda regulatória 2025-2026 da ANPD).

---

## Fontes

- [Migalhas — Os limites à utilização de marcas em peças publicitárias](https://www.migalhas.com.br/depeso/352927/os-limites-a-utilizacao-de-marcas-em-pecas-publicitarias)
- [Legale — Proteção jurídica das marcas: fundamentos e limites](https://legale.com.br/blog/protecao-juridica-das-marcas-fundamentos-criterios-e-limites-no-brasil/)
- [CONAR — Guia de Marketing e Publicidade por Influenciadores Digitais 2026 (PDF)](http://conar.org.br/pdf/260525_GUIA_INFLUENCIADORES_CONAR_v6.pdf)
- [Migalhas — Guia CONAR 2026: o que todo influenciador precisa saber](https://www.migalhas.com.br/depeso/456124/guia-conar-2026-o-que-todo-influenciador-precisa-saber-agora)
- [Shopee — Identificação de conteúdo publicitário: regras do CONAR para afiliados](https://help.shopee.com.br/portal/10/article/196794)
- [The Register — multa GDPR por Google Fonts remoto](https://www.theregister.com/2022/01/31/website_fine_google_fonts_gdpr/)
- [Google AdSense — Conteúdo obrigatório (política de privacidade)](https://support.google.com/adsense/answer/1348695?hl=pt-BR)
