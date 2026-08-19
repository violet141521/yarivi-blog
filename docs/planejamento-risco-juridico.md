# Planejamento — Análise de Risco Jurídico do Yarivi

Criado em 2026-08-17.
Blog: yarivi.com | Dona: Mi (violet141521@gmail.com)
Status: pendente — executar antes de escalar monetização.

---

## Por que fazer isso agora

O blog já tem 13 artigos no ar, monetização planejada (AdSense + afiliados) e dados de leitores coletados via Cloudflare Analytics. Cada um desses pontos cria exposição jurídica. Identificar os riscos antes de submeter ao AdSense e cadastrar em programas de afiliados evita suspensão de conta, multas LGPD ou ações de marca.

---

## Bloco 1 — Uso de Marcas e Produtos Citados

### O risco
Citar nomes de marcas (Apple, Samsung, NVIDIA, etc.) em artigos pode gerar alegação de uso indevido de marca registrada, especialmente em contexto comparativo ou depreciativo.

### Passos

**1.1 Mapear todos os artigos publicados**
- Abrir `artigos/_catalog.json`
- Listar os 13 artigos publicados
- Para cada artigo, identificar marcas e produtos mencionados no título e no corpo

**1.2 Classificar o tipo de menção**
Para cada marca encontrada, classificar como:
- **Descritiva** (ex: "o iPhone tem câmera X") → baixo risco
- **Comparativa** (ex: "o iPhone é melhor que o Android") → médio risco; verificar se tem base factual
- **Depreciativa** (ex: crítica negativa sem evidência) → alto risco; revisar ou remover

**1.3 Verificar uso de imagens de produto**
- Identificar de onde vêm as imagens usadas nos artigos
- Imagens de sites oficiais das marcas: verificar se a marca autoriza uso editorial
- Imagens próprias ou de banco gratuito (Unsplash, Pexels): OK
- Imagens de outros blogs ou captura de tela sem crédito: risco; substituir ou creditar

**1.4 Adicionar disclaimer padrão de editorial**
- Criar frase padrão para incluir no rodapé de artigos com reviews:
  > "Os nomes de marcas e produtos citados são propriedade de seus respectivos donos. A menção é estritamente editorial, sem vínculo comercial, exceto onde indicado como link de afiliado."
- Inserir via template de artigo no `signal-seo-writer`

---

## Bloco 2 — Reviews de Produtos

### O risco
Reviews podem gerar reclamação da marca citada (difamação comercial) ou de consumidores que compraram baseados na recomendação (responsabilidade por conselho). No Brasil, o CDC pode ser acionado.

### Passos

**2.1 Auditar reviews existentes**
- Identificar quais dos 13 artigos se enquadram como review ou recomendação de compra
- Verificar se cada afirmação técnica tem fonte citada (link para fabricante, benchmark público, notícia)

**2.2 Checklist de segurança para reviews**
Aplicar em cada review existente e em todos os futuros:
- [ ] Afirmações de desempenho têm fonte nomeada (fabricante, benchmark externo)?
- [ ] Opiniões negativas são baseadas em fatos verificáveis (não em preferência pessoal)?
- [ ] O artigo deixa claro que é opinião editorial, não conselho de compra profissional?
- [ ] Há disclaimer: "Este artigo não substitui avaliação técnica especializada"?

**2.3 Criar disclaimer padrão para reviews**
Adicionar bloco padronizado no início ou fim de artigos de review:
> "Este artigo é de natureza informativa e editorial. As opiniões são da autora com base em informações públicas disponíveis na data de publicação. Não constitui aconselhamento profissional de compra."

**2.4 Processo para reviews futuros**
- Toda afirmação de especificação técnica deve ter link de fonte (fabricante ou benchmark)
- Reviews negativos passam por revisão adicional antes da publicação
- Incluir data de publicação visível (já feito via `signal-publicador`)

---

## Bloco 3 — Links de Afiliado

### O risco
No Brasil, o CDC (Art. 36) e as diretrizes do Conar exigem transparência em publicidade. Não declarar que um link é de afiliado pode ser caracterizado como publicidade encoberta. O Google AdSense também exige disclosure explícito de afiliados.

### Passos

**3.1 Mapear links de afiliado existentes**
- Verificar se algum dos 13 artigos já contém links com parâmetros de afiliado (ex: `?tag=`, `?ref=`, `amzn.to`)
- Se sim: adicionar disclosure imediatamente

**3.2 Criar disclosure padrão de afiliados**
Texto a incluir no início de qualquer artigo com link de afiliado:
> "⚠️ Aviso: Este artigo contém links de afiliado. Se você comprar pelo link, o Yarivi pode receber uma comissão sem custo adicional para você."

**3.3 Atualizar a página de Política de Privacidade**
Incluir seção "Links de Afiliado" explicando:
- O que é um link de afiliado
- Quais programas o Yarivi participa (Amazon Associates, etc.)
- Que a recomendação editorial não é condicionada à comissão

**3.4 Criar política interna de afiliados**
Regra para o fluxo editorial (adicionar ao `CLAUDE.md`):
- Nenhum link de afiliado entra em artigo sem disclosure no topo
- Links de afiliado não substituem a melhor recomendação para o leitor
- Após cadastro em programas: criar lista de produtos por artigo elegível

**3.5 Checklist pré-publicação de artigo com afiliado**
- [ ] Disclosure visível no início do artigo?
- [ ] Link com parâmetro de rastreamento correto?
- [ ] Produto recomendado de fato relevante para o tema do artigo?
- [ ] Preço/disponibilidade verificados na data de publicação?

---

## Bloco 4 — Dados de Acesso e LGPD

### O risco
O blog coleta dados de visitantes via Cloudflare Analytics. A LGPD (Lei 13.709/2018) exige base legal para coleta, informação ao titular, política de privacidade acessível e, dependendo do volume, registro das operações.

### Passos

**4.1 Mapear todos os dados coletados**
Levantar cada ferramenta ativa e o que ela coleta:

| Ferramenta | Dado coletado | Base legal |
|---|---|---|
| Cloudflare Analytics | IP anonimizado, páginas visitadas, país | Interesse legítimo (analytics) |
| Cloudflare Bot Fight Mode | IP, fingerprint de bot | Segurança legítima |
| Formulário de contato | Nome + e-mail | Consentimento do usuário |
| AdSense (quando ativo) | Cookies de publicidade | Consentimento explícito |
| Newsletter (quando reativada) | E-mail + data de cadastro | Consentimento explícito |

**4.2 Verificar a Política de Privacidade atual**
- Abrir `privacidade.html`
- Confirmar que cobre todos os itens da tabela acima
- Verificar se menciona: direitos do titular (acesso, correção, exclusão), canal de contato, prazo de retenção

**4.3 Implementar aviso de cookies (se não existir)**
- Verificar se o site tem banner de consentimento de cookies
- Se AdSense for ativado: banner de consentimento é obrigatório (Google exige para usuários na UE e recomenda para BR)
- Opção gratuita: Cookiebot (plano free) ou implementação manual com localStorage

**4.4 Criar processo de resposta a titulares**
Definir o que fazer se um leitor solicitar:
- Acesso aos dados coletados → responder em até 15 dias
- Exclusão dos dados → confirmar exclusão e prazo
- Canal de contato: e-mail listado em `contato.html`
- Documentar o processo em arquivo interno (`docs/lgpd-processo.md`)

**4.5 Verificar conformidade do formulário de contato**
- O formulário em `contato.html` coleta quais dados?
- Há checkbox de consentimento antes do envio?
- Os dados são armazenados? Onde? Por quanto tempo?

---

## Bloco 5 — Proteção do Nome e Marca "Yarivi"

### O risco
O nome "Yarivi" não está registrado. Outra empresa pode registrar antes, criando conflito de domínio ou obrigando a rebranding.

### Passos

**5.1 Pesquisar disponibilidade da marca**
- Acessar o INPI (inpi.gov.br) e buscar "Yarivi" nas classes:
  - Classe 38 (serviços de comunicação / blog)
  - Classe 41 (educação / publicação de conteúdo)
- Verificar se há marcas iguais ou similares registradas

**5.2 Avaliar custo-benefício do registro**
- Registro de marca no INPI: ~R$355–710 por classe (pessoa física)
- Prazo: 12–18 meses para concessão
- Decisão: registrar agora (proteção imediata da data de depósito) ou aguardar MEI?

**5.3 Verificar uso indevido do nome**
- Buscar "Yarivi" no Google, Instagram, X e TikTok
- Se houver perfis com o nome: avaliar se criam confusão com o blog

---

## Bloco 6 — Responsabilidade por Comentários e UGC

### O risco
Se o blog tiver seção de comentários no futuro, comentários de usuários podem gerar responsabilidade por difamação ou desinformação. O Marco Civil da Internet (Lei 12.965/2014) regula isso.

### Passos

**6.1 Verificar se o blog tem comentários ativos**
- O blog atualmente não tem sistema de comentários → risco zero por ora

**6.2 Criar regra para futuro**
- Se implementar comentários: usar sistema com moderação prévia ou moderação por palavra-chave
- Criar "Termos de Uso dos Comentários" antes de ativar
- Definir política de remoção (prazo de resposta a denúncias)

---

## Entregáveis do processo

Ao final da análise, produzir:

1. **Relatório de riscos** — lista priorizada por nível (alto / médio / baixo) com status de cada item
2. **Disclaimers padronizados** — textos prontos para reviews e afiliados (inserir no template do `signal-seo-writer`)
3. **Seção "Links de Afiliado"** — texto para incluir na `privacidade.html`
4. **Processo LGPD** — arquivo `docs/lgpd-processo.md` com fluxo de resposta a titulares
5. **Decisão sobre registro de marca** — sim/não + próximo passo

---

## Ordem de execução recomendada

| Prioridade | Bloco | Motivo |
|---|---|---|
| 1º | Bloco 4 — LGPD | Risco de multa ativa agora (dados já sendo coletados) |
| 2º | Bloco 3 — Afiliados | Pré-requisito do AdSense e dos programas de afiliado |
| 3º | Bloco 2 — Reviews | Necessário antes de escalar volume de artigos |
| 4º | Bloco 1 — Marcas | Importante, mas risco atual é baixo (conteúdo editorial) |
| 5º | Bloco 5 — Marca Yarivi | Urgência cresce com o tráfego |
| 6º | Bloco 6 — UGC | Irrelevante até ativar comentários |

---

## Quem executa

Cada bloco pode ser feito por Mi com apoio do Claude, **exceto**:
- Registro de marca no INPI → requer decisão de Mi + pagamento de taxa
- Consultoria jurídica formal → opcional, mas recomendada antes de escalar para 10k+ sessões/mês

*Este planejamento é orientativo e não substitui assessoria jurídica profissional.*
