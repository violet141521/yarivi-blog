# Relatório 2 — Proteção de direitos autorais e da marca "Signal."

**Data**: 2026-07-18
**Escopo**: imagens usadas no site, registro da marca "Signal" no INPI, termos de reuso do conteúdo próprio
**Aviso**: organiza fatos, custos e passos; a decisão de registro de marca se beneficia de conferência por advogado(a) ou agente da propriedade industrial, principalmente na busca de anterioridade.

---

## 1. Licença das imagens usadas

**Resultado da auditoria: o site não usa nenhuma imagem.** Zero tags `<img>`, zero `<svg>`, zero background-image com arquivo externo nos 12 artigos, index e partials. O visual é 100% tipografia, emoji e CSS. As fontes (Fraunces, Manrope) são do Google Fonts, ambas sob licença **SIL Open Font License** — uso comercial e self-host permitidos.

**Situação atual: risco zero de violação de direito autoral de imagem.** Isso é raro e vale proteger com uma política antes que a primeira imagem entre.

### Política de imagens para o futuro (adotar antes da 1ª imagem)

1. Fontes aceitas: Unsplash, Pexels, Pixabay (licenças próprias que permitem uso comercial sem atribuição) e Wikimedia Commons (verificar licença item a item — CC BY exige crédito).
2. **Nunca** usar: imagem de busca do Google, print de site/produto sem checagem, imagem de agência (Getty/Shutterstock) sem compra, foto de pessoa identificável sem cautela (direito de imagem, art. 20 do Código Civil).
3. Imagens geradas por IA: permitidas, mas checar os termos da ferramenta quanto a uso comercial; não gerar imagens imitando estilo de artista vivo nem com marcas/personagens de terceiros.
4. Fotos de produto (quando houver review): preferir foto oficial de press kit do fabricante (uso editorial aceito) ou foto própria.
5. **Registro de licença**: criar `imagens/licencas.md` e anotar, para cada imagem: arquivo, origem (URL), autor, licença, data de download. É a prova em caso de questionamento — serviços de "copyright trolling" (PicRights, Copytrack) atuam no Brasil e cobram retroativamente.

## 2. Registro da marca "Signal" no INPI

### O problema específico do nome

"Signal" é palavra comum em tecnologia e tem colisão notória: o mensageiro **Signal** (Signal Foundation) atua exatamente no universo tech — e o blog é de tecnologia. Além disso, marca nominativa fraca/evocativa em inglês tende a ter várias anterioridades no INPI em classes próximas. Consequências práticas:

- O registro **nominativo** puro de "Signal" tem chance relevante de indeferimento ou oposição na(s) classe(s) de interesse.
- Caminhos que aumentam muito a chance: registrar a **marca mista** (logotipo "Signal." com o ponto e a identidade visual) e/ou nome composto ("Signal Tec", "Blog Signal") — a distintividade vem do conjunto.
- Convivência é possível quando não há confusão entre segmentos (princípio da especialidade), mas blog de tecnologia × app de tecnologia é próximo o bastante para merecer busca cuidadosa.

### Classes de Nice relevantes

| Classe | Cobre | Prioridade |
|--------|-------|-----------|
| **41** | Publicação online de conteúdo editorial, educação, entretenimento | Essencial |
| **35** | Publicidade, marketing de afiliados, espaço publicitário no site | Recomendada quando monetizar |
| 38 | Telecomunicações (é a classe típica do mensageiro Signal) | Não registrar — é onde mora o conflito |

### Custos (tabela 2026, por classe)

- GRU 389 (especificação pré-aprovada): **R$ 440 com desconto de 50%** para pessoa física, MEI, ME e EPP (sem desconto: R$ 880).
- GRU 394 (especificação livre): mais cara (~R$ 1.720 sem desconto).
- Certificado do primeiro decênio: gratuito desde a mudança recente de taxas.
- Estimativa realista para 1 classe com desconto: **~R$ 440-500**. Duas classes: ~R$ 880-1.000.
- Prazo médio até a concessão: **12 a 24 meses** (a proteção retroage ao depósito).
- Requisito: pessoa física pode registrar se exercer atividade compatível; como o plano do blog envolve MEI (ver pesquisa `pesquisa-mei-adsense-afiliados-2026-04-28.md`), o CNAE do MEI deve ser compatível com a classe pedida.

### Passo a passo do registro

1. **Busca de anterioridade** (grátis, 1-2h): [busca.inpi.gov.br](https://busca.inpi.gov.br) → pesquisar "signal" nas classes 41, 35 e 38, radical exato e aproximado. Anotar processos vivos, titulares e classes. **Este passo decide a estratégia** — se houver "Signal" vivo na 41, partir direto para marca mista/nome composto.
2. **Decidir a forma da marca**: nominativa ("Signal"), mista (logo "Signal." — recomendada) ou composta. Se mista, finalizar o logo antes (o desenho depositado é o protegido; mudou o logo, muda o registro).
3. **Cadastro no e-INPI** (grátis): criar login gov.br/INPI como pessoa física ou pelo CNPJ do MEI (o que der o desconto e for compatível com a atividade).
4. **Emitir e pagar a GRU 389** (~R$ 440/classe com desconto).
5. **Depósito no e-Marcas**: preencher formulário, classe(s), especificação pré-aprovada, anexar a arte (se mista). Guardar o número do processo.
6. **Acompanhar a RPI** (Revista da Propriedade Industrial, sai toda terça): fase de oposição dura 60 dias após a publicação; responder exigências no prazo (geralmente 60 dias) — perder prazo arquiva o pedido. Dica: ativar o push do INPI ou verificação mensal agendada.
7. **Concessão**: certificado do 1º decênio já incluso. Renovação a cada 10 anos.

### Enquanto o registro não sai

- Registrar o **domínio** imediatamente (registro.br, ~R$ 40/ano): os artigos já usam `signal.com.br` como canônico — **verificar disponibilidade real antes do deploy**; se estiver tomado, decidir o domínio definitivo primeiro e corrigir todos os canônicos/JSON-LD, porque trocar depois custa SEO. Atenção: domínio não é marca (STJ) — ter o domínio não protege o nome, e vice-versa.
- Usar "Signal." consistentemente com a identidade visual (uso contínuo e datado ajuda em eventual disputa).
- Guardar provas de anterioridade de uso: prints datados, Wayback Machine, primeiro deploy.

## 3. Termos de reuso do conteúdo próprio

Hoje o rodapé diz "© 2026 Signal. Todos os direitos reservados." — juridicamente correto (direito autoral existe sem registro, Lei 9.610/98), mas não diz o que terceiros podem fazer, nem protege contra o cenário mais provável: **cópia integral por outros sites e raspagem para treino de IA**.

### Decisão a tomar (recomendação: opção B)

| Opção | O que permite | Efeito |
|-------|---------------|--------|
| A. Todos os direitos reservados (atual) | Nada sem autorização | Máximo controle, zero divulgação espontânea |
| **B. Citação livre com limite + link** | Trechos de até ~2 parágrafos com crédito e link para o artigo | Protege o conteúdo e ainda gera backlinks (bom para SEO) |
| C. Creative Commons BY-NC-ND | Cópia integral não comercial, sem derivadas, com crédito | Divulgação máxima, mas concorrentes de AdSense podem republicar e diluir seu tráfego — não recomendada para um blog que vive de sessão |

### Passo a passo

1. Redigir a seção "Uso do conteúdo" dentro dos Termos de Uso (Relatório 3), com: titularidade (Lei 9.610/98), o que é permitido (citação parcial + crédito + link), o que é proibido (reprodução integral, uso comercial, treino de modelos de IA sem autorização), e canal de contato para licenciamento (violet141521@gmail.com).
2. Atualizar o rodapé: "© 2026 Signal. Todos os direitos reservados. · Termos de uso" (link).
3. No deploy (Cloudflare Pages): ativar o bloqueio de AI crawlers do Cloudflare (painel → configuração de bots, opção nativa e gratuita) + `robots.txt` com bloqueio a `GPTBot`, `CCBot`, `Google-Extended` etc. — sinaliza a proibição, ainda que não a garanta.
4. Rotina trimestral: buscar no Google um trecho literal de 1-2 artigos entre aspas para detectar cópia integral; se achar, pedir remoção (e-mail ao site, depois DMCA/denúncia ao Google se hospedado fora).

## 4. Resumo de custos e prioridades

| Ação | Custo | Quando |
|------|-------|--------|
| Política de imagens + licencas.md | R$ 0 | Antes da 1ª imagem |
| Busca de anterioridade INPI | R$ 0 | Esta semana (decide a estratégia do nome) |
| Domínio (verificar + registrar) | ~R$ 40/ano | **Antes do deploy** (canônicos já apontam para signal.com.br) |
| Depósito da marca (1 classe, mista) | ~R$ 440-500 | Após busca + logo final |
| 2ª classe (35) | +~R$ 440 | Quando ativar afiliados/AdSense |
| Termos de reuso + robots.txt anti-IA | R$ 0 | Junto com as páginas legais (Relatório 3) |

## Fontes

- [RDM Advogados — Registro de marca no INPI: passo a passo e custos 2026](https://rdmadvogados.com.br/blog/registro-de-marca-no-inpi-passo-a-passo-e-quanto-custa-em-2026/)
- [Oficial Marca — Tabela de taxas INPI 2026](https://oficialmarca.com.br/blog/quanto-custa-registrar-marca-2026/)
- [Contabilizei — Quanto custa registrar uma marca (taxas, prazo, INPI)](https://www.contabilizei.com.br/contabilidade-online/quanto-custa-registrar-uma-marca/)
- [INPI — e-Marcas (formulário eletrônico)](https://gru.inpi.gov.br/emarcas/)
- [INPI — Manual de Marcas: disponibilidade do sinal marcário](https://manualdemarcas.inpi.gov.br/projects/manual/wiki/5%C2%B711_An%C3%A1lise_do_requisito_da_disponibilidade_do_sinal_marc%C3%A1rio)
- [STJ — Registro de marca no INPI não garante exclusividade de uso do nome em site](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias-antigas/2016/2016-12-13_08-04_Registro-de-marca-no-INPI-nao-garante-exclusividade-de-uso-do-nome-em-site.aspx)
- [Marcas Já — Nomes semelhantes na hora de registrar](https://marcasja.com.br/blog/como-evitar-problemas-com-nomes-semelhantes-na-hora-de-registrar-uma-marca/)
