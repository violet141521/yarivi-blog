# Relatório de QA — one-ui-9-quais-celulares-recebem-2026
*Gerado em 2026-10-07 pela skill validador-text*

---

## Veredicto

**Score: 95/100** — ✅ APROVADO para revisão humana

---

## 🔴 Bloqueantes (0)

*(vazio)*

---

## 🟡 Atenção (1)

- **Verificação automática de links externos falhou localmente** — o script `check_article.py`, executado no ambiente do usuário, retornou status `0` (sem resposta) para os 7 links externos, incluindo os 3 já presentes desde a versão anterior do artigo. Isso indica uma restrição de rede no ambiente local, não necessariamente links quebrados. Os dois links novos adicionados nesta revisão (4gnews e SamMobile) foram verificados manualmente via fetch e carregam normalmente com o conteúdo esperado. Os demais (Tecnoblog, Canaltech, Estado de Minas, Mundo Conectado) já constavam do artigo antes desta edição.

---

## 🟢 OK (9 itens)

- Title ≤60 chars e com "Yarivi"
- H1 ≠ Title
- Meta description presente e dentro do limite (150 chars)
- Schema FAQPage presente
- Sem placeholders no texto
- Todos os 7 links internos resolvidos no `_catalog.json`
- `article:published_time` presente (2026-09-29)
- Nenhum slug duplicado detectado
- Originalidade: Alta (0/5 frases com correspondência)

---

## Detalhamento por categoria

### Originalidade (antiplágio)
- Método: busca de frases exatas via WebSearch
- Frases testadas: 5
- Resultado: **Alta ✅ (0/5 com match)**

| Frase | Resultado |
|-------|-----------|
| "O jeito mais seguro de saber é olhar no próprio aparelho (...)" | ORIGINAL |
| "Foto inteligente: edição de imagem por comando de texto ou de voz, com comparação de antes e depois." | ORIGINAL |
| "Gravador de voz com resumo: a IA transcreve e entrega um resumo com título e até tabelas." | ORIGINAL |
| "Os assistentes estão deixando de só responder perguntas para agir por você: abrir apps, preencher formulários, mandar mensagens." | ORIGINAL |
| "É isso que o painel entrega: um registro do que a IA fez e de quais permissões ela usou." | ORIGINAL |

### Links
- Externos: 7 (3 originais + 1 já existente do rascunho anterior + 3 adicionados na auditoria de dados de hoje: 4gnews, Tecnoblog "mais celulares brasileiros", SamMobile)
- Internos: 7 (todos resolvidos no catálogo)

| Link | Status |
|------|--------|
| tecnoblog.net/.../os-primeiros-celulares-do-brasil-com-a-one-ui-9 | não verificável no ambiente local (ver nota em Atenção) |
| canaltech.com.br/.../one-ui-9-recursos-surpreendentes-para-testar | não verificável no ambiente local |
| em.com.br/.../seu-galaxy-esta-recebendo-a-one-ui-9 | não verificável no ambiente local |
| mundoconectado.com.br/.../quais-celulares-samsung-galaxy-vao-receber | não verificável no ambiente local |
| 4gnews.pt/one-ui-9-bloqueada-samsung-enfrenta-atrasos-inesperados | ✅ verificado manualmente (fetch OK) |
| tecnoblog.net/noticias/nova-samsung-one-ui-chega-a-mais-celulares-brasileiros | ✅ verificado manualmente (fetch OK) |
| sammobile.com/.../galaxy-s24-stable-one-ui-9-0-android-17-update-now-live | ✅ verificado manualmente (fetch OK) |

### SEO automático
| Check | Resultado | Detalhe |
|-------|-----------|---------|
| title_length | ✅ pass | 55 chars |
| title_yarivi | ✅ pass | — |
| h1_ne_title | ✅ pass | — |
| meta_desc_present | ✅ pass | — |
| meta_desc_length | ✅ pass | 150 chars |
| faq_schema | ✅ pass | — |
| no_placeholders | ✅ pass | — |
| internal_link_exists | ✅ pass | 7 encontrado(s) |
| published_time | ✅ pass | 2026-09-29 |

### Metadados
- Palavras no corpo: 1273
- Tempo de leitura estimado: 6 min (campo no HTML mostra "5 min" — ver recomendação)
- Title: `One UI 9: quais celulares recebem e o que muda | Yarivi` (55 chars)
- Meta description: 150 chars

---

## Recomendações

1. **Atualizar o campo visível "5 min de leitura"** no byline do artigo para "6 min", já que o script calculou 6 min com base na contagem atual de palavras (1.273, após a atualização do cronograma).
2. A edição de hoje (correção do cronograma de atraso do One UI 9) já está refletida no corpo, no FAQ (incluindo o schema JSON-LD) e no resumo em 5 pontos — consistente em todos os lugares.
3. Ao publicar, lembrar que `signal-publicador` deve atualizar `article:published_time`/`dateModified`/byline para a data real de publicação (hoje o arquivo ainda mostra 2026-09-29, correto para um rascunho).
