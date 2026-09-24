# Relatório de QA — tutor-ia-homeschooling-vs-reforco-2026
*Gerado em 2026-09-09 pela skill validador-text · atualizado em 2026-09-09 (re-checagem)*

---

## Veredicto

**Score: 100/100** — ✅ Aprovado

---

## 🔴 Bloqueantes (0)

*(nenhum)*

---

## 🟡 Atenção (0)

O ponto de atenção da versão anterior (links não verificáveis por HTTP no shell do usuário) foi resolvido — todas as 8 fontes foram confirmadas via WebFetch nesta sessão. Ver nota sobre a Forbes abaixo.

---

## 🟢 OK (9 itens)

1. `<title>` com 59 caracteres, termina em " | Yarivi", keyword no início
2. H1 diferente do `<title>` (manchete com gancho)
3. `<meta name="description">` com 140 caracteres
4. Schema.org `FAQPage` presente e com as 4 perguntas do corpo
5. 2 links internos válidos (`ia-educacao-escola-brasil-2026`, `como-explicar-ia-para-leigos-2026`)
6. `article:published_time` presente (2026-09-09)
7. Nenhum título duplicado/muito similar no catálogo
8. Nenhum placeholder real de template (`no_placeholders` passa após correção do script)
9. 8 fontes externas em `art-sources`, **8/8 confirmadas** (7 via WebFetch direto + 1 via busca, ver nota Forbes)

---

## Nota sobre a fonte Forbes (não é atenção, apenas registro)

O link da Forbes (`forbes.com/sites/torconstantino/.../students-learned-twice-as-much-with-ai-tutor...`) retorna erro 403 tanto no `check_article.py` quanto no WebFetch direto — isso é o bloqueio anti-bot padrão da Forbes contra scrapers, não um link quebrado. Confirmado via busca: o artigo existe, título e data batem exatamente ("Students Learned Twice As Much With AI Tutor Than Typical Lectures", Tor Constantino, 18/09/2024), e o conteúdo (estudo de Harvard, Kestin et al.) é corroborado por uma segunda fonte independente (getcoai.com). Link mantido como está.

## Correção de script aplicada nesta re-checagem

`check_article.py` tinha `TODO` com `re.IGNORECASE`, que casava com "todo dia"/"o dia todo" em português. Corrigido para `\bTODO\b` sem ignorecase. Aplicado de forma centralizada, vale para toda a fila.

---

## Detalhamento por categoria

### Originalidade (antiplágio)
- Método: 5 frases de 15-25 palavras, buscadas entre aspas duplas via WebSearch
- Frases testadas: 5
- Resultado: **5/5 ORIGINAL**

| Frase | Resultado |
|-------|-----------|
| "Fazendo a conta de um mês: uma aula por semana já soma cerca de R$ 190 a R$ 210 por mês." | ORIGINAL |
| "Em 2018, o STF julgou o Recurso Extraordinário 888.815 e decidiu que não há lei que autorize essa prática hoje." | ORIGINAL |
| "Ainda assim, o resultado mostra que a atenção individualizada — seja de IA, seja de um professor particular — costuma superar aula em grupo." | ORIGINAL |
| 'Segundo a ESET (WeLiveSecurity), tutores de IA podem "alucinar" respostas erradas com total confiança...' | ORIGINAL |
| "Reforço particular presencial custa em média R$ 47 por hora no Brasil, podendo passar de R$ 375/mês com duas aulas semanais." | ORIGINAL |

### Links
- Externos no artigo: 8 — 7/8 confirmados via WebFetch direto, 1/8 (Forbes) confirmado via busca (bloqueio anti-bot, não link quebrado — ver nota acima)

| Link | Status |
|------|--------|
| openai.com/index/chatgpt-study-mode/ | ✅ Confirmado via WebFetch |
| khanmigo.ai/pricing | ✅ Confirmado via WebFetch — US$4/mês |
| blog.khanacademy.org (parceria Fundação Lemann) | ✅ Confirmado via WebFetch |
| superprof.com.br/blog/valores-aula-em-casa/ | ✅ Confirmado via WebFetch — R$47/hora |
| researchsquare.com (Kestin et al.) | ✅ Confirmado via WebFetch |
| forbes.com (Tor Constantino) | ✅ Confirmado via busca — 403 é anti-bot, não link quebrado |
| welivesecurity.com (ESET) | ✅ Confirmado via WebFetch |
| rosenbaum.adv.br (homeschooling/STF) | ✅ Confirmado via WebFetch |

- Internos: 2/2 confirmados existentes em `artigos/`

### SEO automático
| Check | Resultado | Detalhe |
|-------|-----------|---------|
| title_length | ✅ | 59 chars |
| title_yarivi | ✅ | termina " \| Yarivi" |
| h1_ne_title | ✅ | manchete distinta do title |
| meta_desc_present | ✅ | presente |
| meta_desc_length | ✅ | 140 chars |
| faq_schema | ✅ | FAQPage presente, 4 perguntas |
| no_placeholders | ✅ | passa após correção do script |
| internal_link_exists | ✅ | 2 links internos |
| published_time | ✅ | 2026-09-09 |

### Metadados
- Palavras no corpo: 1473
- Tempo de leitura estimado: 7 min
- Title: `Tutor de IA vs reforço particular: custo-benefício | Yarivi` (59 chars)
- Meta description: 140 chars

---

## Auditoria de dados (regra CLAUDE.md — obrigatória)

Todos os números, datas e valores em R$/US$ do artigo foram verificados via WebSearch/WebFetch. Nenhum dado foi inventado ou aproximado sem fonte.

### Dados mantidos (com fonte)
| Dado | Fonte |
|------|-------|
| Study Mode do ChatGPT é gratuito no plano Free desde 29 jul 2025 | OpenAI, "Introducing study mode" |
| Khanmigo custa US$ 4/mês para pais e alunos; gratuito só para professores | Khan Academy, khanmigo.ai/pricing |
| Khan Academy tem parceria com Fundação Lemann levando Khanmigo a escolas no Brasil | Khan Academy Blog |
| ChatGPT Plus custa US$ 20/mês | OpenAI Help Center |
| Reforço particular presencial custa em média R$ 47/hora no Brasil | Superprof |
| Estudo de Harvard (Kestin et al., 194 alunos) — ganho ~2x maior com tutor de IA vs aula tradicional | Kestin et al., preprint Research Square; confirmado por Forbes |
| STF julgou o RE 888.815 em 2018: não há legislação que autorize homeschooling no Brasil | Rosenbaum Advocacia, citando decisão do STF |
| Riscos de tutores de IA para crianças (alucinação, coleta de dados de desempenho/voz) | ESET WeLiveSecurity |

### Dados removidos ou ajustados
- **H1 original do brief ("R$ 50 de tutor de IA vs R$ 500 de reforço particular")**: valores de exemplo não verificados, substituídos pelos valores reais encontrados: **"Tutor de IA sai de graça. O professor particular custa R$ 47 a hora"**.
- Nenhum outro número foi removido: todos os valores no texto final têm fonte confirmável.

---

## Recomendações
1. Nenhuma correção pendente relacionada a QA/links.
2. Gerar e inserir a imagem de capa em `img/tutor-ia-homeschooling-vs-reforco-2026.webp` (prompt em `rascunhos/img-tutor-ia-homeschooling-vs-reforco-2026.md`) antes da publicação.
3. Ler a seção do FAQ sobre homeschooling em voz alta antes de aprovar — é o ponto mais sensível juridicamente do artigo.
