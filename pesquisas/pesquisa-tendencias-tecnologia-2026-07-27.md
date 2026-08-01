# Pesquisa: Tendências de Tecnologia 2026
**Data:** 2026-07-27 | **Método:** Pesquisa em Funil v3 | **Motor:** Exa (modo simples) | **Nível:** 3 (Deep Dive completo)

---

## Sumário Executivo

2026 é o ano em que a IA saiu do laboratório e entrou no processo. Não como chatbot, mas como agente que executa tarefas de ponta a ponta — e os resultados são mensuráveis. Dois movimentos são interdependentes e formam o núcleo desta pesquisa:

1. **IA Agente e Multiagente**: empresas brasileiras registram ROI real (Banco do Brasil +30% receita, Magalu R$100M em 8 meses, Azzas 2154 R$1M em 7 semanas). Mas apenas 15% das grandes empresas alcançam ROI positivo — a diferença está em dados estruturados, governança e human-in-the-loop.

2. **Hardware AI-first e Chips**: a corrida pelos ASICs de inferência chegou ao mercado — OpenAI Jalapeño, Etched Sohu, Amazon Trainium3. Nos dispositivos, os NPUs chegaram a 80 TOPS em laptops mas o ecossistema de software não acompanhou: para LLMs locais, a GPU discreta ainda vence. O futuro é híbrido, não substituto.

**Para o Blog Signal:** 4 artigos de alto potencial identificados, com casos brasileiros concretos e dados verificados.

---

## Sub-tópico 1: IA Agente e Multiagente

### O que mudou em 2026

A virada não é de tecnologia — é de arquitetura. Até 2024, a IA conversava. Em 2026, a IA age: acessa sistemas, toma decisões, executa etapas e devolve resultado. Essa transição de "assistente que responde" para "agente que executa" é o que o Rodrigo Bessa, Country Manager da Salesforce Brasil, chamou de "era da IA agêntica" no Agentforce World Tour de maio de 2026.

### Casos brasileiros com dados verificados

**Banco do Brasil — "Resume Aí" + Salesforce Agentforce**
Em menos de 12 meses de implementação: +5 pontos no NPS, +30% de receita, 30-34% de ganho em eficiência operacional. O agente "Resume Aí" reúne, em segundos, informações espalhadas por 900+ sistemas legados — transações, conversas, perfil financeiro, análise de sentimento — e entrega um briefing ao gerente antes do atendimento. De 12 mil funcionários em maio de 2026, o banco vai para 36 mil usuários do sistema até o fim do ano. (Fontes: Época Negócios, jul/2026; TI Inside, mai/2026 — 2 fontes independentes ✓)

**Magalu — "WhatsApp da Lu"**
Lançado em novembro de 2025, o canal gerou mais de R$100 milhões em vendas em 8 meses, alcançou 7,7 milhões de usuários únicos e registrou taxa de conversão 3× maior que os demais canais digitais. NPS de 84,5. Quase 20% de recompra. Ganhou Leão de Bronze em Cannes 2026 na categoria Inovação em Canal de Vendas.

O insight mais relevante: o resultado não vem da IA em si — vem da infraestrutura de dados por trás. A IA personalizou porque tinha décadas de histórico de compras, catálogo estruturado e jornada mapeada. "IA não cria contexto comercial. Ela amplifica o contexto que já existe." (Hub RVOps, jul/2026)

**Azzas 2154 (Animale / Maria Filó / Farm)**
Piloto em 10 lojas do Rio: R$1 milhão extra em 7 semanas, avanço de 5,7% nas vendas vs grupo de controle (teste A/B rigoroso). +8,6% no ticket médio, até 16 pp de conversão. Uma loja reduziu 80% do tempo de elaboração do plano semanal. Resultado: expansão imediata para 320 lojas. (Exame, jun/2026)

**Insider (moda) — "IAra" no WhatsApp**
IA proprietária desenvolvida em novembro de 2025, lançada em dezembro. Entre março e junho de 2026: R$400 mil em vendas, 1.600 pedidos, taxa de conversão de 20%, ROI de 200× sobre o custo da tecnologia. (Exame, jul/2026)

**Mitsui Sumitomo Seguros**
GenAI aplicada ao processo de subscrição (não ao backoffice): +92% no fechamento de novos negócios. A chave foi integrar a IA ao gargalo de receita, não à eficiência operacional. (Peers.com.br, jul/2026)

### A divisão real: quem consegue ROI e quem não consegue

Dados do estudo Peers + TEC Institute + MIT Technology Review Brasil: apenas 15% das grandes empresas alcançam ROI positivo com GenAI. A McKinsey confirma: menos de 10% das organizações escalaram AI Agents em qualquer função individual.

O padrão dos que conseguem: IA integrada ao front office (vendas, precificação, subscrição), não ao backoffice. Os que ficam presos em piloto eterno: tratam IA como ferramenta de eficiência operacional marginal.

### Arquitetura técnica: como funciona na prática

Seis padrões canônicos de orquestração multiagente são usados em produção (fonte: glukhov.org, jul/2026; baseado em NeurIPS 2025 — análise de 1.600+ rastros):

| Padrão | Funcionamento | Custo em tokens | Melhor para |
|--------|--------------|-----------------|-------------|
| Orquestrador-Trabalhador | Hub central delega a workers especializados | 2-3× single-agent | Maioria dos casos |
| Pipeline Sequencial | Cadeia linear, ordem determinística | 2-3× | Processos com etapas fixas |
| Fan-Out / Fan-In | Execução paralela + agregação | 4-6× | Tarefas independentes paralelizáveis |
| Hierárquico | Árvore de delegação (gerente → supervisores → workers) | 3-5× | Problemas grandes demais para um agente |
| Enxame | Coordenação emergente sem hub central | 6-10× | Exploração, pesquisa |
| Malla (Mesh) | Comunicação peer-to-peer direta | 4-8× | Colaboração entre sistemas de equipes diferentes |

A Anthropic usa em produção: lead em Opus (planeja + sintetiza) + subagentes em Sonnet (executam em paralelo). Pesquisa simples: 1 agente, 3-10 tool calls. Pesquisa complexa: 10+ subagentes.

**Custo de multi-agente:** 3-10× mais tokens que single-agent. No sistema de Research do Claude, até 15× mais que um chat. Conclusão: multi-agente só vale quando a tarefa paga essa conta.

### Riscos e o que trava a adoção em escala

Principais pontos de falha em produção (TrueFoundry, abr/2026; X-Apps, mai/2026; SoftDesign, jul/2026):

1. **Gerenciamento de estado**: a maioria dos frameworks trata mal a persistência entre chamadas — o agente "esquece" o que aconteceu antes.
2. **Observabilidade zero**: sem logs de decisão por agente, depuração é adivinhação. Trilha de auditoria não é opcional.
3. **Falsa sensação de autonomia**: o sistema parece autônomo, a supervisão humana relaxa — e quando erra, não há log para entender por quê.
4. **Custo em escala**: um workflow de $0,50 em testes pode chegar a $50.000/mês com 100k execuções.
5. **Contexto insuficiente vs. acesso amplo demais**: cada agente precisa de exatamente o contexto necessário — nem mais (risco de segurança/compliance) nem menos (decisões erradas).

**Human-in-the-Loop não é etapa temporária**: em processos regulados, financeiros ou de alto risco reputacional, a aprovação humana em pontos críticos é arquitetura permanente, não limitação do MVP.

---

## Sub-tópico 2: Hardware AI-first e Chips

### A virada: do "mais FLOPS" para "custo por token"

A métrica que governa o mercado de chips de IA mudou. Não é mais teraflops por segundo — é custo por milhão de tokens de inferência. Inferência (servir respostas a usuários) ultrapassou o treinamento em gasto operacional. A consequência: todo grande player está construindo seu próprio chip de inferência. (Silicon Analysts, jul/2026)

### A corrida dos ASICs de inferência

**OpenAI Jalapeño** (anunciado 24 jun 2026, com Broadcom)
Primeiro chip próprio da OpenAI — desenvolvido do zero em 9 meses (o ciclo de desenvolvimento de ASIC mais rápido já registrado em semicondutores de alto desempenho). Especializado exclusivamente em inferência de LLMs, não serve para treinamento.

Claims em testes preliminares: ~50% mais eficiente em custo que GPUs padrão; "performance per watt substancialmente melhor que o estado da arte". Deployment inicial: fim de 2026. Escala completa: 1º semestre 2028. **Não disponível para terceiros** — uso interno OpenAI. (Fontes: openai.com; tech-insider.org; ceviu.com.br — verificado ✓, com caveat: benchmark independente ainda não publicado)

**Etched Sohu**
Abordagem radical: operações de transformer gravadas diretamente no silício (sem camada de software). Claim: 500k tokens/seg em servidor de 8 chips no Llama 70B (62.500 tokens/chip). Para comparação: H100 entrega ~700 tokens/seg no mesmo modelo. O multiplicador existe — mas a comparação deve ser feita em batch equivalente (Etched usa batch 1; H100 atinge 45.000 tok/s no batch 256).

Trade-off central: zero flexibilidade. Se a arquitetura transformer mudar, o chip não se adapta. **Ainda não disponível** para compra ou aluguel — custo por token não calculável. (Spheron, mai/2026)

**Amazon Trainium3**
Em produção e disponível via AWS. A Uber adotou em 2026 com ~50% de redução de custo vs instâncias Nvidia equivalentes. Foco em treinamento, mas com inferência. Anthropic usa Trainium para treinamento de modelos. (andrew.ooo, jun/2026)

**Padrão do mercado:** todos os grandes estão no mesmo movimento. Google (TPU Trillium, já disponível no Cloud), Meta (MTIA, interno), Microsoft (Maia, interno + Azure), Amazon (Trainium3). O mercado de silício customizado não é hype — é a resposta racional ao fato de que a NVIDIA captura 70%+ de margem bruta em cada chip vendido.

| Chip | Dono | Disponível para terceiros? | Foco | Status (jul/2026) |
|------|------|---------------------------|------|-------------------|
| Jalapeño | OpenAI + Broadcom | Não | Inferência LLM | Anunciado, deploy fim 2026 |
| Sohu | Etched | Não (racks apenas) | Inferência transformer | Pré-produção |
| Trainium3 | Amazon/AWS | Sim (AWS) | Treinamento + inferência | Em produção |
| TPU Trillium (v6e) | Google | Sim (GCP) | Treinamento + inferência | GA desde dez/2024 |
| MTIA | Meta | Não | Inferência interna | Em produção |
| H200/B200 | NVIDIA | Sim (universal) | Tudo | Padrão de mercado |

**Custo por token atual (batch 32, Llama 70B):**
- H100 SXM5: ~$0,141 por M tokens (on-demand Spheron)
- B200 SXM6: ~$0,165 por M tokens (spot) / $0,289 (on-demand)
- Sohu, Jalapeño: incalculável (sem disponibilidade pública)

### NPUs nos dispositivos: o gap entre marketing e realidade

A Computex 2026 colocou NPUs em destaque: Snapdragon X2 Elite (80 TOPS), AMD Ryzen AI Max "Strix Halo" XDNA 2 (50 TOPS), Intel Panther Lake (50 TOPS). A Microsoft exige mínimo 40 TOPS para Copilot+ PC — mais de metade dos laptops novos já atingem isso.

**O problema: TOPS não prevê velocidade de geração de tokens.**

O decode de LLM (gerar cada token da resposta) é *memory-bound*, não *compute-bound*. Para gerar 20 tokens/seg com um modelo 8B, o hardware precisa de ~100 GB/s de bandwidth. Um laptop NPU compartilha memória LPDDR5x (~120-256 GB/s com CPU e iGPU). Uma RTX 3090 tem 936 GB/s dedicados.

Resultado prático medido (RunAIHome, jun/2026):
- Snapdragon X Elite NPU (45 TOPS): ~10 tokens/seg em LLM 8B
- Intel Lunar Lake NPU: ~18-20 tokens/seg
- AMD Strix Halo iGPU (não o NPU!): ~48-61 tokens/seg
- RTX 3090 (usada, ~$1.050): ~95 tokens/seg no 7B

No AMD Ryzen AI Max: quando medido na prática, o iGPU supera o NPU de 50 TOPS para inferência de LLM. O marketing anuncia o NPU; quem faz o trabalho é a GPU integrada.

**O que os NPUs fazem bem:** prefilling (processar o prompt de entrada — fase compute-bound, NPU domina com >1.400 tokens/seg). Também: imagens, vídeo, upscaling, blur de fundo, OCR — workloads com shape fixo e determinístico. Para essas tarefas, a eficiência energética é 5-6× maior que GPU Nvidia. (Paper arxiv.org, jul/2026; MDPI, set/2025)

**Edge AI mais amplo:** mercado de $47,59B em 2026 → $385,89B em 2034 (CAGR 29,9%). Hailo-8 (26 TOPS, 2,5W, $50) demonstra que inferência local privada em modelos ≤3B é viável em Raspberry Pi — 15-25 tok/s, custo de eletricidade $3/mês vs $380/mês de cloud. (BlackRoad, mar/2026; Fortune Business Insights, jul/2026)

### A lógica econômica por trás de tudo

O núcleo da disputa de chips não é tecnológico — é financeiro. Um chip H200 custa ~$4.250 para fabricar (lógica + HBM + packaging). NVIDIA vende com 70%+ de margem bruta. Para uma empresa que gasta bilhões em inferência, construir silício próprio — mesmo com custo de NRE de dezenas de milhões por tapeout — vira racional a partir de certa escala.

A OpenAI serve ~700M usuários semanais no ChatGPT + API + Codex. A diferença de 50% em custo por token composta sobre esse volume equivale a centenas de milhões de dólares por ano. Jalapeño não é ambição tecnológica — é planilha.

---

## Tabela Comparativa: As 2 Tendências Deep Dive

| Dimensão | IA Agente e Multiagente | Hardware AI-first e Chips |
|----------|------------------------|--------------------------|
| **Maturidade atual** | Produção em empresas líderes; 85% ainda em piloto | ASICs: pré-produção/roadmap; NPUs: em todo device |
| **ROI comprovado** | Sim — BB +30%, Magalu R$100M, Azzas 5,7% vendas | Parcialmente — NPUs reduzem bateria, não rodam LLM bem |
| **Barreira principal** | Dados estruturados + governança + cultura | Software ecosystem imaturo para NPUs; ASICs não acessíveis |
| **Risco técnico** | Custo de tokens (3-10×); falhas de orquestração | Jalapeño/Sohu sem benchmark independente |
| **Relevância Brasil** | Alta — casos reais em RH, banco, varejo, moda | Média — influencia preço de APIs; NPUs chegam em qualquer laptop |
| **Horizonte de impacto** | Agora (quem tem dados prontos) | 2026-2028 (Jalapeño em escala) |
| **Tendência dominante** | Orquestrador-Trabalhador + Human-in-the-Loop | Híbrido GPU+ASIC; NPU para prefill + GPU para decode |

---

## Contradições Identificadas

1. **Sohu: 500k tokens/seg vs realidade de batch**: A Etched cita 500k tok/s para servidor de 8 chips — mas esse número é em batch 1. GPUs em batch 256 chegam a 45k tok/s *por chip*, o que reduz a vantagem aparente. A comparação justa exige mesmas condições — e a Etched não publicou dados em batch realista.

2. **NPU: marketing vs medição**: Fabricantes anunciam TOPS como proxy de velocidade para LLMs. TOPS mede throughput de operações fixas (compute-bound). Decode de LLM é memory-bound. São métricas ortogonais. O Copilot+ PC com 40+ TOPS pode gerar tokens mais lentamente que um MacBook Air de 2022 dependendo do modelo.

3. **Jalapeño 50% mais barato**: A cifra veio da Broadcom no anúncio e foi amplificada pela mídia especializada. O próprio anúncio oficial da OpenAI usa linguagem qualitativa ("substantially better performance per watt"), sem quantificar os 50%. Benchmark independente não publicado.

4. **Gartner 40% apps empresariais com agentes até 2026**: Citado amplamente, mas não encontrado com fonte primária verificável no corpus desta pesquisa. Possível dado real do Gartner — mas não confirmado.

---

## Status dos Fatos-Chave (Phase Gate)

| # | Fato | Status | Fontes | Confiança |
|---|------|--------|--------|-----------|
| 1 | Gartner: 40% apps com agentes até 2026 | ❌ Não encontrado | 0 fontes no corpus | Baixa — não usar sem fonte primária |
| 2 | NPUs evoluíram ~78% YoY (45→80 TOPS) | ⚠️ Fraco | 1 fonte (runaihome.com) | Média — o dado é real mas 1 fonte |
| 3 | Jalapeño ~50% mais barato que GPUs | ✅ Verificado* | tech-insider.org + ceviu.com.br | Média* — sem benchmark independente |
| 4 | Banco do Brasil +30% receita com agentes | ✅ Verificado | epocanegocios.globo.com + tiinside.com.br | Alta (caveat: TI Inside pode republicar press release Salesforce) |
| 5 | 15% das empresas com ROI positivo em GenAI | ⚠️ Fraco | peers.com.br (cita MIT/TEC Institute) | Média — fonte única que pode ter interesse comercial |

---

## CRAAP Scoring — Fontes Principais

| Fonte | C | R | A | A | P | Total | Tier | Nota |
|-------|---|---|---|---|---|-------|------|------|
| arxiv.org (NPU mobile, jul/2026) | 20 | 18 | 18 | 17 | 18 | **91** | **A** | Paper acadêmico, cross-layer study, 6+ autores |
| mdpi.com (NPU vs GPU servers, set/2025) | 17 | 17 | 18 | 18 | 18 | **88** | **A** | Peer-reviewed, benchmark empírico sistemático |
| epocanegocios.globo.com (BB, jul/2026) | 20 | 18 | 17 | 18 | 15 | **88** | **A** | Jornalismo de referência BR, dado declarado por executivo |
| glukhov.org (orquestração, jul/2026) | 20 | 18 | 14 | 17 | 17 | **86** | **A** | Técnico profundo, cita NeurIPS 2025 MAST, bem estruturado |
| siliconanalysts.com (ASIC economics, jul/2026) | 20 | 20 | 16 | 17 | 16 | **89** | **A** | Análise técnica detalhada com tabelas de custo verificáveis |
| openai.com (Jalapeño, jun/2026) | 20 | 20 | 20 | 12 | 10 | **82** | **A** | Fonte primária oficial — máxima autoridade, máximo bias |
| tiinside.com.br (BB/Salesforce, mai/2026) | 19 | 18 | 16 | 17 | 14 | **84** | **A** | Especializado TI BR — risco de republicar press release vendor |
| exame.com (Azzas 2154, jun/2026) | 20 | 18 | 17 | 18 | 14 | **87** | **A** | Jornalismo econômico BR sólido, metodologia A/B citada |
| exame.com (Insider IAra, jul/2026) | 20 | 18 | 17 | 17 | 14 | **86** | **A** | Mesma fonte, caso brasileiro contemporâneo |
| ceviu.com.br (chips customizados, jul/2026) | 19 | 19 | 14 | 16 | 15 | **83** | **A** | Newsletter técnica focada, síntese boa de múltiplas fontes |
| runaihome.com (NPU vs GPU, jun/2026) | 19 | 18 | 13 | 16 | 15 | **81** | **A** | Benchmarks próprios, metodologia explicada, bem calibrado |
| andrew.ooo (chips, jun/2026) | 20 | 19 | 12 | 16 | 15 | **82** | **A** | Análise independente com tabela comparativa completa |
| tech-insider.org (Jalapeño, jul/2026) | 20 | 18 | 13 | 15 | 15 | **81** | **A** | Cobertura boa mas autoridade editorial não verificada |
| spheron.network (Sohu vs NVIDIA, mai/2026) | 18 | 18 | 14 | 16 | 14 | **80** | **A/B** | Análise técnica sólida, mas empresa vende GPU cloud (interesse) |
| fortunebusinessinsights.com (edge AI, jul/2026) | 20 | 16 | 15 | 14 | 12 | **77** | **B** | Relatório de mercado — dados reais mas metodologia opaca |
| peers.com.br (ROI GenAI, jul/2026) | 20 | 18 | 14 | 14 | 13 | **79** | **B** | Consultoria com interesse em narrar baixo ROI do mercado |
| pipefy.com (AI Agents por dept, mai/2026) | 19 | 18 | 14 | 14 | 12 | **77** | **B** | Empresa vende a solução — dados podem ser curados |

---

## Recomendação: Pauta para o Blog Signal

Com base nos dados desta pesquisa, 4 temas têm alta probabilidade de tráfego orgânico e dados concretos suficientes para artigos de qualidade:

1. **"Banco do Brasil usou IA para vender 30% mais — e como funciona por dentro"**
   — Caso brasileiro verificado, dois ângulos (o agente Resume Aí + a decisão de não substituir humanos), dados concretos, narrativa de transformação. Keyword-first: "agentes de IA no banco".

2. **"Por que o NPU do seu laptop não roda IA tão bem quanto você pensa"**
   — Contradição de marketing vs realidade, dado concreto (10 tok/s vs 95 tok/s), útil para qualquer leitor que comprou Copilot+ PC. Potencial de compartilhamento alto.

3. **"OpenAI fez seu próprio chip — e isso muda o preço da IA para todo mundo"**
   — Jalapeño explicado para leigos, a lógica econômica da guerra de chips, impacto no preço das APIs. Keyword: "chip de IA OpenAI".

4. **"Como Magalu fez R$100 milhões no WhatsApp com IA (e o que todo mundo errou ao ler essa notícia)"**
   — Caso concreto + análise crítica (o sucesso não vem da IA, vem dos dados por trás). Muito compartilhável, alinhado ao estilo Signal.

---

## Metodologia e Limitações

- **Motor:** Exa (modo simples, sem filtros avançados) + análise interna Claude Sonnet 4.6
- **Buscas realizadas:** 9 queries paralelas (Níveis 1 e 3) + 1 fetch de arquivo persistido
- **Phase Gate:** subagent Explore independente — 2/5 fatos verificados com ≥2 fontes independentes
- **Período coberto:** principalmente 2025-2026 (foco em dados de julho 2026)
- **Limitações:** (1) Fato Gartner 40% não encontrado — remover ou buscar fonte primária antes de publicar; (2) Jalapeño: sem benchmark independente até jul/2026; (3) Sohu: dados de throughput sem condições de batch comparáveis; (4) 15% ROI: citação de consultoria com possível interesse comercial
- **Cobertura regional:** casos brasileiros bem representados (BB, Magalu, Azzas, Insider, Pipefy, Mitsui)
- **Não coberto nesta pesquisa:** regulação EU AI Act (sub-tópico não escolhido), quantum computing (idem), biotech/wearables (idem)
