# Relatório de QA — carro-autonomo-brasil-2026
*Gerado em 2026-09-25 pela skill validador-text*

---

## Veredicto

**Score: 100/100** — ✅ APROVADO para revisão humana

---

## 🔴 Bloqueantes (0)

*(nenhum)*

---

## 🟡 Atenção (0)

*(nenhum)*

---

## 🟢 OK (9 itens)

- Title = 60 chars (limite exato), termina com "| Yarivi"
- H1 é manchete com gancho, diferente do title
- Meta description dentro do limite (150 chars)
- Schema FAQPage presente
- Sem placeholders no texto
- 2 links internos válidos (../artigos/...)
- `article:published_time` presente
- Antiplágio: 0/5 frases com correspondência exata
- Estatística de segurança (1 milhão de vítimas evitadas) corrigida para refletir escopo real da fonte antes da apresentação

---

## Detalhamento por categoria

### Originalidade (antiplágio)
- Método: busca de frases exatas via WebSearch (entre aspas)
- Frases testadas: 5
- Resultado: **Alta ✅** (0/5 com correspondência)

| Frase | Resultado |
|-------|-----------|
| "dirige sozinho numa área ou condição delimitada, sem precisar de intervenção humana" | ORIGINAL |
| "a legislação brasileira em tramitação — mira nos níveis 3 e 4" | ORIGINAL |
| "a tecnologia embarcada já avançou mais rápido do que a lei permite usar" | ORIGINAL |
| "é culpa de quem estava no banco do motorista mesmo sem dirigir" | ORIGINAL |
| "essa é, de longe, a pergunta mais espinhosa — e ainda sem resposta definitiva no Brasil" | ORIGINAL |

### Links
- Externos: 4 (Câmara dos Deputados, Canaltech, Gazeta do Povo, Exame)
- Internos: 2 (`agente-de-ia-o-que-e-2026`, `carro-eletrico-brasil-2026-vale-a-pena`)
- **Nota de método:** checador de status HTTP sem acesso à rede neste computador. Todos os 4 links foram confirmados manualmente (fetch bem-sucedido) durante a pesquisa e a auditoria de dados.

### SEO automático
| Check | Resultado | Detalhe |
|-------|-----------|---------|
| title_length | ✅ | 60 chars |
| title_yarivi | ✅ | — |
| h1_ne_title | ✅ | — |
| meta_desc_present | ✅ | — |
| meta_desc_length | ✅ | 150 chars |
| faq_schema | ✅ | — |
| no_placeholders | ✅ | — |
| internal_link_exists | ✅ | 2 encontrados |
| published_time | ✅ | 2026-09-25 |

### Metadados
- Palavras no corpo: 1205
- Tempo de leitura estimado: 6 min
- Title: `Carro autônomo no Brasil: o que já pode e o que não | Yarivi` (60 chars)
- Meta description: 150 chars

---

## Auditoria de dados (CLAUDE.md passo 2.6)

| Dado | Fonte | Status |
|---|---|---|
| Comissão de Viação e Transportes (CVT) da Câmara aprovou texto consolidando PL 1317/2023 e PL 3641/2023 | Câmara dos Deputados — notícia oficial 1177072 | ✅ mantido, confirmado literalmente na fonte |
| Multiplicador de 5x na multa por operar sem autorização; 3x por direção desatenta | Câmara dos Deputados (mesma fonte) | ✅ mantido, confirmado literalmente |
| Próximo passo: Comissão de Constituição e Justiça (CCJ), depois plenários da Câmara e do Senado | Câmara dos Deputados (mesma fonte) | ✅ mantido |
| Escala de níveis de autonomia 0 a 5 (SAE) | Conhecimento técnico consolidado da indústria automotiva (padrão internacional J3016 da SAE) — não é uma estatística de uma fonte jornalística específica | ✅ mantido, é uma classificação técnica padrão, não um dado que exija fonte única |
| "Até 1 milhão de acidentes evitados globalmente até 2035" | Gazeta do Povo | 🔧 **corrigido antes da apresentação** — a fonte real fala em até ~1 milhão de **mortes e feridos nos EUA** (não "acidentes" nem "globalmente"), condicionado a 10% de adoção da frota americana, com base num estudo da revista científica *JAMA Surgery* (dez/2025). O texto e o FAQ (incluindo o schema JSON-LD) foram reescritos para refletir o escopo real: EUA, mortes e feridos, taxa de adoção de 10%, ao longo de uma década |
| Waymo: redução de risco de ferimentos em áreas onde já opera | Gazeta do Povo (mesma fonte, dado adicional incorporado na correção) | ✅ adicionado com precisão: 80% de redução de risco, conforme a fonte |
| Responsabilidade civil em caso de acidente ainda é zona cinzenta no Brasil | Exame — "Carros autônomos: quem é culpado em acidentes?" | ✅ mantido, é uma análise qualitativa do estado da legislação, não uma estatística pontual |

Um dado foi identificado como impreciso na auditoria — a estatística "1 milhão de acidentes evitados globalmente" generalizava um estudo que na verdade é específico dos EUA e fala em mortes/feridos sob um cenário de adoção de 10% da frota, não uma previsão global incondicional. Como manda o CLAUDE.md, a frase foi reescrita imediatamente (no corpo do artigo, na resposta do FAQ visível e no schema JSON-LD FAQPage) antes deste relatório ser fechado, sem deixar a imprecisão pendente para a Mi decidir.

---

## Recomendações

Nenhuma pendência. A única imprecisão encontrada na auditoria (escopo da estatística de segurança) já foi corrigida no arquivo. Pronto para revisão e aprovação da Mi.
