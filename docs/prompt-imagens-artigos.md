# Prompt padrão — imagem de artigo (Yarivi)

Baseado nas 6 imagens já publicadas em `img/` (carro-eletrico, gerenciador-de-senhas,
golpes-app-banco-pix, ia-consumo-energia, o-que-fazer-celular-velho, vpn). Objetivo: gerar,
para qualquer artigo novo, um prompt de imagem consistente com essa identidade visual —
sem precisar redescobrir o estilo a cada vez.

## Estilo já estabelecido (observado nas 6 imagens)

- **Render cinematográfico escuro** — fundo quase preto/noturno, luz dramática, aparência de
  still de CGI de alta produção (não flat design, não ícone, não infográfico)
- **Uma única cena/metáfora literal central** — um objeto ou ação que representa o conceito do
  artigo de forma direta (anzol fisgando a tela do celular = golpe; túnel de luz conectando
  laptop ao globo = VPN; carro branco carregando = carro elétrico). Nunca colagem de ícones soltos
- **Teal neon (`#34D399`-ish, turquesa/ciano)** como cor de destaque primária em quase todas —
  luz, brilho, cabo, portal, ícone
- **Cor secundária de contraste conforme o tom do artigo**: vermelho/laranja para ameaça ou perigo
  (golpe, servidor "pegando fogo"); dourado/âmbar para valor ou solução (chave mestra do
  gerenciador de senhas); mantém só o teal quando o tom é neutro/positivo (carro elétrico, VPN)
- **Sem texto, sem logotipos de marca, sem watermark** na imagem
- **Formato**: 1536×1024 (paisagem 3:2 — tamanho nativo do GPT-Image-1) na maioria; aceitável
  redimensionar para algo próximo de 16:9 quando necessário
- **Sem pessoas com rosto identificável** (quando há figuras humanas, aparecem em silhueta/capuz,
  como no exemplo de vigilância da VPN)

## O prompt (colar em Claude, ChatGPT ou direto no gerador de imagem)

```
Você é o diretor de arte do blog de tecnologia Yarivi. Sua tarefa é escrever o prompt de
geração de imagem (em inglês) e o alt-text (em português) para a imagem de capa de UM artigo,
seguindo exatamente o estilo visual já estabelecido nas imagens publicadas do blog.

ESTILO OBRIGATÓRIO (não se desvie):
- Render cinematográfico, fundo escuro/noturno, iluminação dramática, qualidade de still de
  CGI/3D de alta produção — nunca flat design, ícone plano, infográfico ou colagem de ícones
- UMA cena central com uma metáfora visual literal e direta do conceito do artigo (um objeto
  ou uma ação, não vários símbolos soltos)
- Cor de destaque primária: teal/turquesa neon (#34D399), usada como luz, brilho, cabo, portal
  ou contorno
- Cor de destaque secundária conforme o tom do artigo:
  - vermelho/laranja para golpe, ameaça, risco, perigo
  - dourado/âmbar para solução, chave, proteção, valor
  - só teal (sem segunda cor) quando o tom é neutro ou positivo
- Proibido: texto, letras, números, logotipos de marcas reais, watermark, rostos humanos
  identificáveis (se houver figura humana, usar silhueta ou capuz)
- Formato paisagem 3:2 (1536x1024)

ENTRADA (preencher por artigo):
- Título do artigo: [TÍTULO]
- Slug: [slug-do-artigo]
- Resumo/lead do artigo (1-2 frases): [RESUMO]
- Tom: [ameaça/golpe | solução/proteção | neutro/informativo | comparação vale-a-pena]

SAÍDA (sempre as três partes, nesse formato):

1. **Metáfora central escolhida**: uma frase explicando o objeto/cena e por que representa o
   artigo.

2. **Prompt de geração (inglês)**: um parágrafo único, direto, no padrão dos exemplos abaixo —
   descreve a cena, a luz, as cores, o enquadramento e termina com "cinematic lighting, dark
   background, high detail, 3:2 landscape, no text, no logos".

3. **Alt-text (português, para o atributo `alt` da tag `<img>`)**: descreve a cena em poucas
   palavras + travessão + o tema do artigo. Padrão: "[cena central em poucas palavras] —
   [ilustração de/tema do artigo]". Máximo ~20 palavras, sem repetir literalmente o H1.

Exemplos de referência (não copiar, só calibrar o nível de detalhe e o tom):
- "A white electric sedan charging at night, glowing teal charging cable snaking from a
  futuristic charging pillar to the car, Brazilian city skyline with a mountain silhouette and
  palm trees in the background, starry night sky, cinematic lighting, dark background, high
  detail, 3:2 landscape, no text, no logos"
  → alt: "Carro elétrico branco carregando com cabo teal luminoso, palmeiras e skyline
  brasileira ao fundo — vale a pena comprar carro elétrico no Brasil"
- "A glowing red fishing hook piercing through a smartphone screen showing a banking app
  interface, dark moody background, sparks of orange light, faint ghosted QR code pattern
  behind, cinematic lighting, dark background, high detail, 3:2 landscape, no text, no logos"
  → alt: "Smartphone com gancho de pesca luminoso vermelho perfurando a tela — ilustração de
  golpes em apps de banco e Pix"
```

## Onde encaixar no fluxo editorial

Sugestão: novo passo **2.7** em `signal-seo-writer/SKILL.md`, logo após a auditoria de dados
(2.6) e antes de apresentar o rascunho à Mi — gerar a metáfora + prompt + alt-text para cada
artigo aprovado, junto com o rascunho.

## Depois de gerar a imagem

1. Salvar como `img/[slug].webp` (mesmo slug do arquivo em `artigos/` ou `rascunhos/`)
2. Inserir logo após `</header>`, antes de `<article class="art-body">`:

```html
<img src="../img/[slug].webp" alt="[ALT-TEXT]" width="1536" height="1024" style="width:100%;height:auto;border-radius:8px;margin-bottom:2rem;display:block;" loading="eager">
```

3. Ajustar `width`/`height` se a imagem final tiver outra proporção (ex.: 1088x608, como em
   `o-que-fazer-celular-velho-descarte-2026`)

## Nota sobre a tentativa anterior

`Claude outputs/PROMPTS-DALLE.md` (8 set 2026) descreve um estilo diferente — flat/abstrato,
1200x630, cores por categoria — que não é o padrão que acabou entrando no ar. Este documento
substitui aquele como referência de estilo para novas imagens.
