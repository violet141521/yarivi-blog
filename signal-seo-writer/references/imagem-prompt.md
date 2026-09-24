# Prompt de imagem de capa — padrão Yarivi

Estilo já estabelecido nas imagens publicadas em `img/` (carro-eletrico, gerenciador-de-senhas,
golpes-app-banco-pix, ia-consumo-energia, o-que-fazer-celular-velho, vpn). Use este documento
para gerar a imagem de capa de qualquer artigo novo, mantendo consistência visual.

## Estilo obrigatório

- Render cinematográfico, fundo escuro/noturno, iluminação dramática, qualidade de still de
  CGI/3D de alta produção — nunca flat design, ícone plano, infográfico ou colagem de ícones
- UMA cena central com metáfora visual literal e direta do conceito do artigo (um objeto ou
  uma ação, não vários símbolos soltos)
- Cor de destaque primária: teal/turquesa neon (`#34D399`), como luz, brilho, cabo, portal ou
  contorno
- Cor de destaque secundária conforme o tom do artigo:
  - vermelho/laranja → golpe, ameaça, risco, perigo
  - dourado/âmbar → solução, chave, proteção, valor
  - só teal (sem segunda cor) → tom neutro ou positivo
- Proibido: texto, letras, números, logotipos de marcas reais, watermark, rostos humanos
  identificáveis (figura humana só em silhueta/capuz)
- Formato paisagem 3:2 (1536×1024 — tamanho nativo do GPT-Image-1)

## O que gerar, para cada artigo

1. **Metáfora central**: uma frase dizendo o objeto/cena escolhida e por que representa o artigo
2. **Prompt de geração (inglês)**: um parágrafo único descrevendo cena, luz, cores e
   enquadramento, terminando com "cinematic lighting, dark background, high detail, 3:2
   landscape, no text, no logos"
3. **Alt-text (português)**: "[cena central em poucas palavras] — [tema do artigo]",
   até ~20 palavras, sem repetir literalmente o H1

### Exemplos de referência (calibrar tom/detalhe, não copiar)

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

## Entrega

Salvar como `rascunhos/img-{{SLUG}}.md` com as 3 partes acima, mais o snippet HTML pronto
(placeholder até a imagem existir):

```html
<img src="../img/{{SLUG}}.webp" alt="{{ALT_TEXT}}" width="1536" height="1024" style="width:100%;height:auto;border-radius:8px;margin-bottom:2rem;display:block;" loading="eager">
```

Depois que a imagem for gerada (fora do Claude, num gerador de imagem) e salva como
`img/{{SLUG}}.webp`, esse `<img>` entra no HTML do artigo logo após `</header>`, antes de
`<article class="art-body">`. Se a imagem final sair com outra proporção, ajustar `width`/
`height` de acordo (ex.: 1088×608).
