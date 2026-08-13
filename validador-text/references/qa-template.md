# Relatório de QA — {slug}
*Gerado em {data} pela skill validador-text*

---

## Veredicto

**Score: {score}/100** — {veredicto}

---

## 🔴 Bloqueantes ({n_bloqueantes})

{lista_bloqueantes}
*(vazio se nenhum)*

---

## 🟡 Atenção ({n_atencao})

{lista_atencao}
*(vazio se nenhum)*

---

## 🟢 OK ({n_ok} itens)

{lista_ok}

---

## Detalhamento por categoria

### Originalidade (antiplágio)
- Método: busca de frases exatas via WebSearch
- Frases testadas: 5
- Resultado: {originalidade_resultado}

| Frase | Resultado |
|-------|-----------|
{tabela_frases}

### Links
- Externos verificados: {n_externos}
- Internos verificados: {n_internos}

{tabela_links}

### SEO automático
| Check | Resultado | Detalhe |
|-------|-----------|---------|
{tabela_seo}

### Metadados
- Palavras no corpo: {word_count}
- Tempo de leitura estimado: {reading_time} min
- Title: `{title}` ({title_len} chars)
- Meta description: {meta_desc_len} chars

---

## Recomendações

{recomendacoes}
