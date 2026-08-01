# Relatório de custos detalhado — Blog Signal.

**Data**: 2026-07-18
**Escopo**: todos os custos para tirar o blog do papel com conformidade jurídica completa, consolidando os Relatórios 1-3 (risco em conteúdo, marca/direitos autorais, páginas legais/LGPD) + operação e monetização.
**Moeda**: R$ (valores de 2026; câmbio usado quando o preço é em US$: confirmar na contratação). Valores marcados com ~ são estimativas de mercado, não tabela oficial.

---

## 1. Visão geral — quanto custa cada cenário

| Cenário | Ano 1 | Anos seguintes |
|---------|-------|----------------|
| **A. Mínimo para lançar** (deploy + páginas legais) | **R$ 40** | R$ 40/ano |
| **B. Recomendado** (A + marca depositada em 1 classe) | **R$ 480** | R$ 40/ano |
| **C. Monetização formalizada** (B + MEI a partir da 1ª receita) | **R$ 480 + R$ 86/mês após abrir o MEI** | R$ 40 + ~R$ 1.033/ano de MEI |
| **D. Completo com revisão profissional** (C + advogado nas páginas legais) | **~R$ 980 a R$ 1.980 + MEI** | idem C |

O blog pode ir ao ar 100% conforme com **R$ 40** (domínio). Todo o resto escala com gatilhos: marca quando decidir o nome definitivo, MEI quando a primeira receita chegar, advogado quando a receita justificar.

---

## 2. Custos item a item

### 2.1 Infraestrutura (obrigatório para o deploy)

| Item | Valor | Recorrência | Observação |
|------|-------|-------------|------------|
| Domínio `.com.br` (registro.br) | **R$ 40** | Anual, preço fixo (mesmo valor na renovação) | Registro direto no registro.br; privacidade WHOIS incluída para pessoa física. **Urgente**: os canônicos já apontam para `signal.com.br` — verificar disponibilidade antes do deploy |
| Cloudflare Pages (hospedagem) | **R$ 0** | — | Plano free: sites estáticos ilimitados, SSL, domínio próprio, 500 builds/mês — mais que suficiente |
| Cloudflare Web Analytics (sem cookies) | R$ 0 | — | Alternativa ao GA4 que não exige banner de consentimento |
| Bloqueio de AI crawlers (Cloudflare) | R$ 0 | — | Opção nativa do painel, grátis |
| E-mail profissional `contato@signal.com.br` (opcional) | R$ 0 | — | Cloudflare Email Routing (redireciona para o Gmail atual, grátis) |

**Subtotal infraestrutura: R$ 40/ano.**

### 2.2 Conformidade LGPD e páginas legais (Relatório 3)

| Item | Valor | Recorrência | Quando |
|------|-------|-------------|--------|
| Redação das 4 páginas legais (privacidade, termos, cookies, afiliados) | **R$ 0** (feito internamente, com os roteiros do Relatório 3) | — | Pré-deploy |
| Self-host das fontes (Fraunces/Manrope, licença SIL OFL) | R$ 0 | — | Pré-deploy |
| Banner de consentimento — opção 1: **mensagem de consentimento do próprio Google AdSense** (Consent Mode v2) | **R$ 0** | — | Antes de ativar AdSense — suficiente para começar |
| Banner — opção 2: CMP dedicada, plano gratuito (AdOpt — brasileira, focada em LGPD; ou CookieYes free até 100 páginas) | R$ 0 | — | Alternativa com mais controle; confirmar limite de pageviews do plano free na contratação |
| Banner — opção 3: CMP paga (quando o tráfego estourar o plano free) | ~R$ 55-90/mês (CookieYes a partir de US$ 10/mês; Cookiebot US$ 8-96/mês conforme tráfego) | Mensal | Só com tráfego alto — a essa altura a receita de anúncios cobre |
| Revisão das 4 páginas por advogado(a) (opcional, recomendado) | **~R$ 500-1.500** (serviço avulso; estimativa de mercado — pedir 2-3 orçamentos) | Única | Quando a receita justificar; não é pré-requisito do AdSense |

**Subtotal LGPD: R$ 0 para lançar; R$ 500-1.500 opcional.**

### 2.3 Marca e propriedade intelectual (Relatório 2)

| Item | Valor | Recorrência | Observação |
|------|-------|-------------|------------|
| Busca de anterioridade no INPI | **R$ 0** | — | Fazer antes de tudo — decide se "Signal" é viável ou se vai de marca mista/nome composto |
| Depósito da marca — GRU 389, especificação pré-aprovada, **com 50% de desconto** (pessoa física, MEI, ME, EPP) | **R$ 440/classe** | Única | Classe 41 (publicação online) agora; classe 35 (publicidade) quando monetizar |
| Depósito sem desconto (referência) | R$ 880/classe | Única | Só se registrar por empresa fora do Simples |
| GRU 394 (especificação livre) | até ~R$ 1.720/classe | Única | Evitar — a pré-aprovada cobre blog/publicação |
| Certificado do 1º decênio | **R$ 0** | — | Ficou gratuito na tabela atual do INPI |
| Renovação da marca | Tabela INPI vigente à época | A cada 10 anos | Só em ~2037; valor será o da tabela futura |
| Contingências (responder exigência simples) | R$ 0 | — | Respondível pelo e-Marcas sem custo na maioria dos casos |
| Contingências (oposição de terceiro / recurso) | ~R$ 475+ por GRU específica + eventual honorário | Eventual | Risco real dado o conflito potencial com "Signal" (mensageiro); é aqui que um agente de PI pode entrar |
| Agente de PI / advogado para conduzir o registro (opcional) | ~R$ 700-2.000 de honorários (estimativa de mercado) | Única | Alternativa: fazer sozinha com o passo a passo do Relatório 2 — o processo é online e viável |
| Política de imagens + registro de licenças | R$ 0 | — | Site hoje não usa nenhuma imagem; política preventiva custa só disciplina |

**Subtotal marca: R$ 440 (1 classe, com desconto) — segunda classe +R$ 440 quando monetizar.**

### 2.4 Formalização e monetização

| Item | Valor | Recorrência | Quando |
|------|-------|-------------|--------|
| Abertura do MEI | **R$ 0** | — | Quando a 1ª receita (afiliados/AdSense) se aproximar; formalização pelo gov.br é gratuita — desconfiar de sites que cobram |
| DAS mensal do MEI (prestação de serviços) | **R$ 86,05/mês** (R$ 81,05 INSS + R$ 5,00 ISS) | Mensal | ~R$ 1.033/ano; valor 2026, reajusta com o salário mínimo |
| Conta no Google AdSense | R$ 0 | — | Aplicar com 12+ artigos e páginas legais no ar |
| Programas de afiliados (Amazon, Shopee, Magalu etc.) | R$ 0 | — | Adesão gratuita; custo é só a regra de disclosure (Relatório 1) |
| Journey by Mediavine | R$ 0 (revenue share) | — | A 1.000 sessões/mês; sem mensalidade, ficam com % da receita |
| Provedor de newsletter (quando reativar) | R$ 0 no início | — | Brevo/Mailchimp free tier cobrem os primeiros milhares de contatos; escolher um com DPA/LGPD |

**Subtotal monetização: R$ 0 até a 1ª receita; depois R$ 86,05/mês de MEI.**

---

## 3. Cronograma de desembolso (cenário recomendado B→C)

| Momento | Ação | Desembolso |
|---------|------|-----------|
| **Esta semana** | Verificar + registrar `signal.com.br` | R$ 40 |
| Esta semana | Busca de anterioridade INPI | R$ 0 |
| Pré-deploy | Páginas legais, self-host de fontes, robots.txt | R$ 0 |
| Logo definitivo pronto | Depósito da marca mista, classe 41 (GRU 389 c/ desconto) | R$ 440 |
| 12+ artigos no ar | Aplicar ao AdSense + mensagem de consentimento do Google | R$ 0 |
| 1ª receita chegando | Abrir MEI | R$ 0 (depois R$ 86,05/mês) |
| Receita estabilizada | (Opcional) revisão jurídica das páginas + classe 35 da marca | ~R$ 500-1.500 + R$ 440 |
| **Total ano 1 (sem opcionais)** | | **R$ 480 + MEI proporcional** |

---

## 4. O que NÃO precisa pagar (armadilhas comuns)

- **"Despachantes" de INPI e MEI** que cobram centenas de reais por processos que são online e simples — o depósito de marca e a abertura de MEI são autosserviço.
- **Geradores pagos de política de privacidade** (R$ 30-100/mês) — o roteiro do Relatório 3 cobre o conteúdo; gerador não dá validade jurídica extra.
- **CMP paga desde o dia 1** — a mensagem de consentimento nativa do Google AdSense é gratuita e aceita; CMP paga só quando o tráfego estourar planos free.
- **Registro de direito autoral dos textos** — a proteção da Lei 9.610/98 é automática, sem registro; guardar provas de anterioridade (Wayback, deploy datado) é grátis.
- **Renovar domínio por registradoras intermediárias** (R$ 60-80/ano) — direto no registro.br é R$ 40 fixo.

## 5. Resumo executivo

Custo de conformidade total no ano 1: **R$ 480** (domínio + marca em 1 classe). O maior custo do projeto não é jurídico, é o MEI (~R$ 1.033/ano) — e ele só nasce quando a receita nascer. Os dois únicos desembolsos com prazo de risco são o **domínio** (canônicos já apontam para signal.com.br; se outro registrar, o SEO planejado quebra) e a **busca INPI** (grátis, mas decide se R$ 440 vão para "Signal" ou para um nome/logo ajustado).

## Fontes

- [Registro.br — pagamento de domínio (R$ 40/ano fixo)](https://registro.br/ajuda/pagamento-de-dominio/)
- [Receita Federal / Simples Nacional — atualização de valores MEI 2026](https://www8.receita.fazenda.gov.br/simplesnacional/Noticias/NoticiaCompleta.aspx?id=c3b2044c-ff97-432a-b33c-ecf2a3df6dc3)
- [gov.br Empresas & Negócios — valor das contribuições mensais do MEI](https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/perguntas-frequentes/pagamento-da-contribuicao-mensal-carne-mensal/qual-o-valor-das-contribuicoes)
- [FENACON — contribuição mensal do MEI em 2026 (R$ 81,05 INSS)](https://fenacon.org.br/noticias/contribuicao-mensal-do-mei-sobe-para-r-8105-em-2026/)
- [Oficial Marca — tabela de taxas INPI 2026](https://oficialmarca.com.br/blog/quanto-custa-registrar-marca-2026/)
- [RDM Advogados — registro de marca INPI: custos 2026](https://rdmadvogados.com.br/blog/registro-de-marca-no-inpi-passo-a-passo-e-quanto-custa-em-2026/)
- [CookieYes vs Cookiebot — comparativo de preços de CMP 2026](https://www.enzuzo.com/blog/cookiebot-vs-cookieyes)
- [Cookiebot — pricing](https://www.cookiebot.com/en/pricing/)
- [Google AdSense — requisitos de qualificação (gratuito)](https://support.google.com/adsense/answer/9724?hl=pt-BR)
