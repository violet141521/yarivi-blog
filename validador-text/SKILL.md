---
name: validador-text
description: >
  Valida a qualidade de um artigo do blog Yarivi antes da revisão humana (QA v2).
  Calcula nota 0-100 com rubrica ponderada (dados e fontes, originalidade, SEO, links, estilo, utilidade),
  exige nota >= 90 e zero bloqueantes, e repete corrigir -> refazer QA até passar.
  Use SEMPRE que: um rascunho acabou de ser escrito, a usuária pedir "valida o artigo [slug]",
  "roda o QA", "verifica os links", "checa plágio", antes de apresentar ou aprovar qualquer rascunho.
  Também é chamada automaticamente pela skill signal-seo-writer ao finalizar cada artigo.
---

# validador-text (v2)

Regra permanente da Mi (14/11/2026): **nenhum artigo é apresentado com nota abaixo de 90**.
Se ficar abaixo, corrige-se o artigo e refaz-se o QA, quantas rodadas forem necessárias.

Blog: `C:\Repositorio\ClaudeProject\Aula1\BlogTI`
Artigo: `rascunhos/{slug}.html` (ou `artigos/` para reauditar publicado)
Relatório: `rascunhos/qa-{slug}.md` · histórico de rodadas: `rascunhos/qa-{slug}.rodadas.json`
Script: `validador-text/scripts/check_article.py` · Spec: `docs/validador-text-spec.md`

## Rubrica (100 pontos)

| Categoria | Pts | O que mede |
|---|---|---|
| Dados e fontes | 25 | ≥3 fontes; fonte com ≤1 ano e com data no rótulo; número com atribuição no texto; dado sem fonte/citação sem origem (auditoria 2.6) |
| Originalidade | 15 | 5 de 5 frases testadas no antiplágio (2 delas com dado/número); cópia exata desconta; 3+ = bloqueante |
| SEO técnico | 15 | title ≤60 com marca, H1≠title, meta 110–155, FAQPage, published_time, palavra-chave no title/meta/100 primeiras palavras/H2 |
| Links | 10 | externos verificados (4xx/5xx = bloqueante), links internos válidos, **link interno para data posterior = bloqueante**, «Leia também» |
| Estilo Yarivi | 20 | frases curtas (média ≤20), poucas >30 palavras, jargão explicado, ação concreta no fim, lead ≤60 palavras |
| Utilidade ao leitor | 15 | lead entrega a resposta, ≥4 H2, FAQ ≥3, imagem/prompt/alt, 900–2.200 palavras, sem canibalização com outro artigo |

**Aprovado = nota ≥ 90 e zero 🔴.** Qualquer outro caso = REPROVADO → loop de correção.
Bloqueantes: link quebrado, cópia (3+ frases), link interno para artigo de data posterior, placeholder no texto.

## Fluxo (loop até passar)

### 1. Identificar o slug
Sem slug: ler `rascunhos/fila.json`, listar `aguardando-revisao` e perguntar.

### 2. Rodada de QA
a) Rodar o script sem manual para obter `frases_antiplagio`, `links_externos`, `links_pendentes`:
```bash
python -I validador-text/scripts/check_article.py {slug}
```
b) **Antiplágio — as 5 frases sempre**: WebSearch de cada frase entre aspas (o script já escolhe 2 com dado/número). Match só conta se a frase completa e específica aparecer.
c) **Links**: o script checa HTTP; se o PC estiver sem rede, `links_pendentes` volta preenchido — verificar cada URL com WebFetch (ou pelo ambiente em nuvem) e anotar o status em `links_verificados`. Não deixar link sem verificação.
d) **Auditoria de dados (passo 2.6 do CLAUDE.md)**: conferir cada número/data/citação contra a fonte. Anotar `mantidos`, `removidos`, `sem_fonte_remanescentes`, `citacoes_sem_origem`.
e) **Julgamento editorial** (o que o script não vê): o primeiro parágrafo responde à pergunta de busca? O texto cobre a intenção do leitor? Tom Yarivi (analogia antes do jargão)? Se não, registrar `ajustes` com pontos negativos e **motivo**.
f) Gravar o JSON manual em `rascunhos/qa-manual-{slug}.json` (formato no cabeçalho do script) e rodar:
```bash
python -I validador-text/scripts/check_article.py {slug} --manual rascunhos/qa-manual-{slug}.json --write
```
O script calcula a nota, grava `qa-{slug}.md` e registra a rodada no histórico.

### 3. Decisão
- `aprovado: true` → apresentar o artigo à Mi com nota, resumo da auditoria de dados e quantas rodadas foram necessárias.
- `aprovado: false` → **não apresentar**. Corrigir no próprio HTML cada item 🔴/🟡 que tirou pontos (adicionar data nas fontes, atribuir números à fonte, encurtar lead e frases longas, explicar jargão, adicionar ação final, trocar fonte antiga por recente etc.), listar o que foi feito em `correcoes_rodada` e voltar ao passo 2 (nova rodada). Repetir até ≥ 90. Dado sem fonte verificável continua sendo removido e a frase reescrita, nunca inventado.
- Se após 4 rodadas a nota não chegar a 90, parar e dizer à Mi o que impede (ex.: fonte recente inexistente), em vez de relaxar a regra.

### 4. Resumo no chat
```
📋 QA — [manchete]
Nota final: XX/100 (rodadas: N) | ✅ aprovado
Dados e fontes XX/25 · Originalidade XX/15 · SEO XX/15 · Links XX/10 · Estilo XX/20 · Utilidade XX/15
Correções feitas: [lista curta]  |  Dados removidos: [lista curta]
Relatório: rascunhos/qa-{slug}.md
```

## Observações
- Recência: fonte com mais de 1 ano é tratada como dado sem fonte (regra do CLAUDE.md), salvo fato histórico fixo.
- A nota v2 é mais exigente que a v1: artigos antigos que tiravam 95–100 podem cair; reauditar publicados usa o mesmo comando (lê de `artigos/`).
- Backups da v1: `SKILL.v1.bak.md`, `scripts/check_article.v1.bak.py`, `references/qa-template.v1.bak.md`.
