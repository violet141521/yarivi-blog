# Template do relatório de QA (v2)

O relatório `rascunhos/qa-{slug}.md` agora é **gerado pelo script** (`check_article.py --write`), não preenchido à mão.
Estrutura gerada:

1. Veredicto: nota X/100 + ✅ APROVADO / 🔴 REPROVADO, tabela de pontos por categoria
2. 🔴 Bloqueantes · 🟡 Atenção (com pontos descontados) · 🟢 OK
3. Auditoria de dados (mantidos com fonte / removidos ou reescritos) — vem de `dados` no JSON manual
4. Originalidade: tabela das frases testadas e resultado
5. Fontes com data e precisão (dia/mês/ano)
6. Metadados (palavras, leitura, title, meta, palavra-chave)
7. Histórico de rodadas: nota por rodada e correções aplicadas antes de cada uma

Entrada manual: `rascunhos/qa-manual-{slug}.json` (campos em `scripts/check_article.py`, cabeçalho).
