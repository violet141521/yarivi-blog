# 🖼️ Sistema de Imagens para Artigos Yarivi

**Data:** 8 de setembro de 2026  
**Status:** ✅ Script completo com 3 opções de imagens + placeholders prontos

---

## 📦 O que você tem

### Arquivos Entregues

1. **`gerar-imagens-artigos.py`** — Script Python principal
   - 6 funções para gerar/organizar imagens
   - Suporte a PIL, Unsplash, DALL-E
   - Interativo (menu de opções)

2. **Placeholders Minimalistas** (5 PNG)
   - 1200x630px (tamanho ideal OG image)
   - Design responsivo com cores Yarivi
   - Pronto para usar ou substituir

3. **Guias de Implementação**
   - `PROMPTS-DALLE.md` — Prompts para IA generativa
   - `INSERIR-IMAGENS-HTML.md` — Código HTML para cada artigo
   - `estilos-imagens.css` — CSS responsivo
   - `snippets-html-imagens.json` — JSON com todos os snippets

4. **Metadados**
   - `metadata-imagens.json` — Config de todas as imagens

5. **Script Automático**
   - `baixar-imagens-unsplash.sh` — Bash script para baixar stock images

---

## 🎨 3 Opções para as Imagens

### Opção 1️⃣: Usar Placeholders (O que você tem agora)

**Prós:**
- ✅ Rápido: já estão prontas
- ✅ Profissional: design minimalista Yarivi
- ✅ Funciona imediatamente

**Contras:**
- ❌ Genérico (sem foto/ilustração real)

**Ação:**
```bash
# Copiar placeholders para rascunhos/
cp -r imagens/ rascunhos/
```

---

### Opção 2️⃣: Baixar Stock Images (Unsplash)

**Prós:**
- ✅ Imagens reais de alta qualidade
- ✅ Grátis
- ✅ Automatizado

**Contras:**
- ⚠️ Requer internet
- ⚠️ Resultado pode variar

**Ação:**
```bash
# Execute o script gerado
chmod +x baixar-imagens-unsplash.sh
./baixar-imagens-unsplash.sh

# Resultado: 5 imagens em ./imagens/
ls -lh imagens/
```

---

### Opção 3️⃣: IA Generativa (DALL-E / Midjourney)

**Prós:**
- ✅ Personalizado 100%
- ✅ Prompts otimizados já prontos
- ✅ Máxima qualidade visual

**Contras:**
- ⚠️ Pago (DALL-E: $0.04/imagem)
- ⚠️ Manual (copiar/colar prompts)

**Ação:**

1. Abrir `PROMPTS-DALLE.md`
2. Copiar um prompt (português ou inglês)
3. Ir para https://openai.com/dall-e-3
4. Colar o prompt
5. Gerar imagem
6. Salvar como `{slug}.png` em `imagens/`

**Exemplo:**
```
Ilustração de tela dividida: lado esquerdo mostra smartphone moderno 
com app de banco digital brilhante em verde-teal e azul, lado direito 
mostra prédio de banco tradicional com cofre. Design minimalista, 
profissional, imagem para blog 1200x630
```

---

## 📝 Como Inserir Imagens nos Artigos

Abra `INSERIR-IMAGENS-HTML.md` — tem 3 opciones para cada artigo:

### Opção A: Meta Tags (OG Image)
```html
<!-- No <head> do artigo -->
<meta property="og:image" content="https://yarivi.com/imagens/banco-digital-vs-tradicional-2026.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

### Opção B: Hero Image (Topo do artigo)
```html
<!-- Após o <header>, antes do <article> -->
<figure class="art-hero">
    <img
        src="../imagens/banco-digital-vs-tradicional-2026.png"
        alt="Comparação visual entre banco digital e banco tradicional"
        loading="lazy"
    >
</figure>
```

### Opção C: Inline Image (Dentro do artigo)
```html
<!-- Dentro de <article class="art-body"> -->
<figure class="art-inline-img">
    <img
        src="../imagens/banco-digital-vs-tradicional-2026.png"
        alt="Banco digital vs tradicional"
        loading="lazy"
    >
    <figcaption>Figura: Fintech</figcaption>
</figure>
```

---

## 🎯 Passo a Passo Recomendado

### Hoje (8 set 2026)
1. ✅ **Escolher método:** Placeholder, Unsplash, ou DALL-E?
2. ✅ **Organizar imagens:** Colocar em `imagens/`

### Amanhã (9 set 2026)
3. **Adicionar Meta Tags** (OG Image)
   - Copiar de `INSERIR-IMAGENS-HTML.md`
   - Colar no `<head>` de cada artigo HTML

4. **Adicionar Hero Image** (opcional, mas recomendado)
   - Copiar snippet
   - Colar após `</header>`

### Depois (quando publicar)
5. **Upload das imagens** para Cloudflare Pages
   - `git add imagens/`
   - `git commit -m "Add article images"`
   - `git push`

6. **Verificar no navegador**
   - Testar responsividade
   - Verificar OG image (Share no Twitter/Facebook)

---

## 📐 Especificações Técnicas

| Especificação | Valor |
|---|---|
| **Formato** | PNG |
| **Resolução** | 1200 × 630px |
| **DPI** | 72 |
| **Tamanho máximo** | 200KB |
| **Uso principal** | Open Graph (OG image) + Blog |

**Por que 1200×630?**
- Padrão ideal para redes sociais (Twitter, Facebook, WhatsApp)
- Renderiza bem em previews de compartilhamento
- 16:9 (wide format)
- Otimizado para celular + desktop

---

## 💻 Como Rodar o Script Novamente

Se você precisa gerar as imagens de novo ou de outra forma:

```bash
# Instalar PIL (se não tiver)
pip install pillow

# Executar o script
python3 gerar-imagens-artigos.py

# Escolher uma opção:
# 1 = Placeholders
# 2 = Script Unsplash
# 3 = Prompts DALL-E
# 4 = Snippets HTML
# 5 = CSS
# 6 = Metadados
# 7 = TODOS
```

---

## 🎨 Paleta de Cores Usada

| Artigo | Cor Primária | RGB | Uso |
|---|---|---|---|
| Banco Digital | Teal | #34D399 | Destaque |
| Bem-estar | Amber | #F59E0B | Destaque |
| LGPD/IA | Violet | #8B5CF6 | Destaque |
| Open Source | Emerald | #10B981 | Destaque |
| Educação | Pink | #EC4899 | Destaque |
| Fundo | Dark Blue | #0F172A | Base |

---

## 📄 Estrutura de Arquivos Final

```
yarivi/
├── artigos/
│   ├── banco-digital-vs-tradicional-2026.html
│   ├── vicio-redes-sociais-algoritmo-dopamina-2026.html
│   ├── lgpd-ia-regulacao-brasil-2026.html
│   ├── ia-open-source-llama-mistral-2026.html
│   └── tutor-ia-homeschooling-vs-reforco-2026.html
├── imagens/                          ← NOVO
│   ├── banco-digital-vs-tradicional-2026.png
│   ├── vicio-redes-sociais-algoritmo-dopamina-2026.png
│   ├── lgpd-ia-regulacao-brasil-2026.png
│   ├── ia-open-source-llama-mistral-2026.png
│   └── tutor-ia-homeschooling-vs-reforco-2026.png
├── style.css                         ← Adicionar CSS de imagens
└── [...]
```

---

## ✅ Checklist de Implementação

- [ ] Escolher método de imagens (Placeholder/Unsplash/DALL-E)
- [ ] Organizar imagens em `imagens/`
- [ ] Adicionar `estilos-imagens.css` ao `style.css` ou arquivo separado
- [ ] Copiar Meta Tags para `<head>` de cada artigo
- [ ] Copiar Hero Image ou Inline Image para cada artigo
- [ ] Testar no navegador (desktop + mobile)
- [ ] Testar OG image (compartilhar no Twitter/WhatsApp)
- [ ] Fazer commit e push para Cloudflare
- [ ] Verificar imagens live no site

---

## 🚀 Próximas Melhorias

- [ ] Adicionar WebP (formato mais leve)
- [ ] Lazy loading nativo (já está no HTML)
- [ ] Otimizar compressão PNG
- [ ] Srcset para diferentes resoluções (1x, 2x)
- [ ] Criar thumbnails 400×210px para listagens

---

## 📞 Suporte

**Erro ao rodar o script?**
- Verificar se PIL está instalado: `pip install pillow`
- Verificar permissões: `chmod +x *.sh`
- Verificar Internet (se usando Unsplash)

**Imagens não aparecem no site?**
- Verificar caminho relativo (`../imagens/`)
- Verificar permissões de arquivo (755)
- Verificar cache do navegador (Ctrl+Shift+Delete)

**OG image não aparece no compartilhamento?**
- Usar validator: https://www.opengraphprotocol.org/
- Limpar cache: https://developers.facebook.com/tools/debug
- Aguardar 24h para cache atualizar

---

**Criado:** 8 set 2026  
**Versão:** 1.0  
**Status:** ✅ Pronto para usar
