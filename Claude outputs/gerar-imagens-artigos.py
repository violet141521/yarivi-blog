#!/usr/bin/env python3
"""
Script para gerar/organizar imagens dos 5 artigos Yarivi
Opções:
  1. Placeholder minimalista (PIL)
  2. Stock images (Unsplash API)
  3. IA generativa (DALL-E, remoto)
"""

import os
import json
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# ============================================================================
# CONFIGURAÇÃO DOS ARTIGOS
# ============================================================================

ARTIGOS = {
    "banco-digital-vs-tradicional-2026": {
        "titulo": "Banco Digital vs Banco Tradicional",
        "categoria": "Fintech",
        "cor_primaria": "#34D399",  # Teal
        "cor_fundo": "#0F172A",     # Dark blue
        "emoji": "🏦",
        "palavras_chave": "banco, segurança, pix, digital, fintech",
        "descricao_alt": "Comparação visual entre banco digital e banco tradicional - segurança e tecnologia"
    },
    "vicio-redes-sociais-algoritmo-dopamina-2026": {
        "titulo": "Por que TikTok vicia",
        "categoria": "Bem-estar Digital",
        "cor_primaria": "#F59E0B",  # Amber
        "cor_fundo": "#0F172A",
        "emoji": "🧠",
        "palavras_chave": "tiktok, dopamina, redes sociais, vício, psicologia",
        "descricao_alt": "Visualização do ciclo de vício em redes sociais - dopamina e algoritmos"
    },
    "lgpd-ia-regulacao-brasil-2026": {
        "titulo": "LGPD e IA: Regulação Brasil",
        "categoria": "IA & Privacidade",
        "cor_primaria": "#8B5CF6",  # Violet
        "cor_fundo": "#0F172A",
        "emoji": "⚖️",
        "palavras_chave": "lgpd, ia, regulação, privacidade, brasil",
        "descricao_alt": "Símbolo de regulação e privacidade em IA - compliance e segurança de dados"
    },
    "ia-open-source-llama-mistral-2026": {
        "titulo": "Open Source IA: Llama e Mistral",
        "categoria": "Software",
        "cor_primaria": "#10B981",  # Emerald
        "cor_fundo": "#0F172A",
        "emoji": "🤖",
        "palavras_chave": "llama, mistral, open source, ia, grátis",
        "descricao_alt": "Logo representando IA open source - Llama, Mistral, DeepSeek"
    },
    "tutor-ia-homeschooling-vs-reforco-2026": {
        "titulo": "Tutor IA vs Reforço",
        "categoria": "Educação",
        "cor_primaria": "#EC4899",  # Pink
        "cor_fundo": "#0F172A",
        "emoji": "📚",
        "palavras_chave": "educação, homeschooling, tutor ia, aprendizado",
        "descricao_alt": "Tutor de IA auxiliando em educação - homeschooling e aprendizado personalizado"
    }
}

# ============================================================================
# FUNÇÃO 1: Gerar Placeholder com PIL (Minimalista)
# ============================================================================

def criar_placeholder_pil(slug, config, largura=1200, altura=630):
    """
    Cria imagem placeholder minimalista com design Yarivi
    Dimensões ideais: 1200x630px (OG image)
    """

    # Criar imagem com fundo gradiente simulado
    img = Image.new('RGB', (largura, altura), config["cor_fundo"])
    draw = ImageDraw.Draw(img)

    # Desenhar retângulo com cor primária (topo)
    rect_height = 200
    draw.rectangle(
        [(0, 0), (largura, rect_height)],
        fill=config["cor_primaria"]
    )

    # Adicionar emoji grande
    emoji_y = 100
    emoji_x = largura // 2 - 50

    try:
        # Tentar usar fonte, se não disponível usar padrão
        fonte_grande = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 120)
        fonte_titulo = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 60)
        fonte_subtitulo = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 40)
    except:
        fonte_grande = ImageFont.load_default()
        fonte_titulo = ImageFont.load_default()
        fonte_subtitulo = ImageFont.load_default()

    # Emoji (simulado com texto)
    emoji_text = config["emoji"]
    draw.text(
        (largura // 2 - 40, emoji_y - 60),
        emoji_text,
        fill="white",
        font=fonte_grande
    )

    # Título principal
    titulo = config["titulo"]
    titulo_y = rect_height + 100
    draw.text(
        (50, titulo_y),
        titulo,
        fill="white",
        font=fonte_titulo
    )

    # Categoria
    categoria_text = f"📍 {config['categoria']}"
    draw.text(
        (50, titulo_y + 80),
        categoria_text,
        fill=config["cor_primaria"],
        font=fonte_subtitulo
    )

    # Frase curta
    frase = "Yarivi — Tech sem jargão"
    draw.text(
        (50, altura - 80),
        frase,
        fill="#94A3B8",  # Gray
        font=fonte_subtitulo
    )

    # Salvar
    output_path = f"imagens/{slug}.png"
    os.makedirs("imagens", exist_ok=True)
    img.save(output_path)
    print(f"✅ Criado: {output_path}")
    return output_path

# ============================================================================
# FUNÇÃO 2: Script para baixar de Stock Images (Unsplash/Pexels)
# ============================================================================

def gerar_script_unsplash():
    """
    Gera script bash para baixar imagens de Unsplash
    (Requer chave API ou URL direto)
    """

    script = """#!/bin/bash
# Script para baixar imagens dos artigos Yarivi via Unsplash

mkdir -p imagens

# Banco Digital vs Tradicional
curl -s "https://source.unsplash.com/1200x630/?bank,finance,security" -o imagens/banco-digital-vs-tradicional-2026.png

# TikTok e Vício
curl -s "https://source.unsplash.com/1200x630/?phone,social,media,dopamine" -o imagens/vicio-redes-sociais-algoritmo-dopamina-2026.png

# LGPD e IA
curl -s "https://source.unsplash.com/1200x630/?privacy,security,ai,regulation" -o imagens/lgpd-ia-regulacao-brasil-2026.png

# Open Source IA
curl -s "https://source.unsplash.com/1200x630/?ai,robot,code,opensource" -o imagens/ia-open-source-llama-mistral-2026.png

# Educação e Tutor
curl -s "https://source.unsplash.com/1200x630/?education,learning,laptop,student" -o imagens/tutor-ia-homeschooling-vs-reforco-2026.png

echo "✅ Imagens baixadas em ./imagens/"
ls -lh imagens/
"""

    with open("baixar-imagens-unsplash.sh", "w") as f:
        f.write(script)
    os.chmod("baixar-imagens-unsplash.sh", 0o755)
    print("✅ Script criado: baixar-imagens-unsplash.sh")
    return "baixar-imagens-unsplash.sh"

# ============================================================================
# FUNÇÃO 3: Gerar Instruções para DALL-E
# ============================================================================

def gerar_prompts_dalle():
    """
    Gera prompts otimizados para DALL-E/Midjourney
    """

    prompts = {
        "banco-digital-vs-tradicional-2026": {
            "en": "Split screen illustration: left side shows a modern smartphone with a glowing digital banking app interface in teal and blue, right side shows a traditional bank building with security vault. Minimalist design, professional, blog header image 1200x630",
            "pt": "Ilustração de tela dividida: lado esquerdo mostra smartphone moderno com app de banco digital brilhante em verde-teal e azul, lado direito mostra prédio de banco tradicional com cofre. Design minimalista, profissional, imagem para blog 1200x630"
        },
        "vicio-redes-sociais-algoritmo-dopamina-2026": {
            "en": "Abstract visualization of brain with dopamine molecules and TikTok/Instagram logo, connected to smartphone screen with infinite feed. Neon amber and violet colors, modern neuroscience illustration, 1200x630 blog header",
            "pt": "Visualização abstrata de cérebro com moléculas de dopamina e logo TikTok/Instagram, conectado a tela de smartphone com feed infinito. Cores neon âmbar e roxo, ilustração moderna de neurociência, cabeçalho blog 1200x630"
        },
        "lgpd-ia-regulacao-brasil-2026": {
            "en": "Symbol of regulation and privacy: scales of justice combined with AI chip/neural network, Brazilian flag subtle in background, lock icon representing data protection. Violet and teal colors, legal/compliance aesthetic, 1200x630",
            "pt": "Símbolo de regulação e privacidade: balança da justiça combinada com chip de IA/rede neural, bandeira brasileira sutil ao fundo, ícone de cadeado representando proteção de dados. Cores roxo e teal, estética legal/compliance, 1200x630"
        },
        "ia-open-source-llama-mistral-2026": {
            "en": "Stylized llama and comet/star symbols representing Llama and Mistral AI models, surrounded by code snippets and open-source symbols (github logo subtle), green and emerald colors, tech illustration, 1200x630 blog header",
            "pt": "Símbolos estilizados de lhama e cometa representando modelos Llama e Mistral, cercados por fragmentos de código e símbolos open-source (logo github sutil), cores verde e esmeralda, ilustração tech, cabeçalho blog 1200x630"
        },
        "tutor-ia-homeschooling-vs-reforco-2026": {
            "en": "Split screen: left shows student with AI tutor bot on laptop at home (homeschooling), right shows student in traditional classroom with teacher. Warm pink and emerald colors, education illustration, hopeful mood, 1200x630",
            "pt": "Tela dividida: esquerda mostra estudante com tutor IA em laptop em casa (homeschooling), direita mostra estudante em sala de aula tradicional com professor. Cores rosa quente e esmeralda, ilustração educação, mood esperançoso, 1200x630"
        }
    }

    with open("prompts-dalle.json", "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)

    print("✅ Prompts DALL-E gerados: prompts-dalle.json")

    # Também gerar versão txt legível
    with open("PROMPTS-DALLE.md", "w", encoding="utf-8") as f:
        f.write("# Prompts para Gerar Imagens (DALL-E / Midjourney)\n\n")
        f.write("Use esses prompts em https://openai.com/dall-e-3 ou https://www.midjourney.com\n\n")
        for slug, texts in prompts.items():
            f.write(f"## {slug}\n\n")
            f.write(f"**Português:**\n{texts['pt']}\n\n")
            f.write(f"**English:**\n{texts['en']}\n\n")
            f.write("---\n\n")

    print("✅ Prompts legíveis: PROMPTS-DALLE.md")

# ============================================================================
# FUNÇÃO 4: Gerar Código HTML para Inserir Imagens
# ============================================================================

def gerar_html_imagens():
    """
    Gera snippets HTML para inserir imagens nos artigos
    """

    html_snippets = {}

    for slug, config in ARTIGOS.items():
        # Versão OG Meta
        og_meta = f'''<!-- Open Graph / Social Media -->
<meta property="og:image" content="https://yarivi.com/imagens/{slug}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:image" content="https://yarivi.com/imagens/{slug}.png">'''

        # Versão Hero Image (topo do artigo)
        hero_image = f'''<!-- Imagem Hero (antes do H1) -->
<figure class="art-hero">
    <img
        src="../imagens/{slug}.png"
        alt="{config['descricao_alt']}"
        loading="lazy"
        decoding="async"
    >
    <figcaption style="font-size: 0.85rem; color: var(--text-3); margin-top: 0.5rem;">
        Ilustração: {config['categoria']}
    </figcaption>
</figure>'''

        # Versão Inline (dentro do artigo)
        inline_image = f'''<figure class="art-inline-img" style="margin: 2rem 0; text-align: center;">
    <img
        src="../imagens/{slug}.png"
        alt="{config['descricao_alt']}"
        loading="lazy"
        style="max-width: 100%; height: auto; border-radius: var(--radius-lg);"
    >
    <figcaption style="font-size: 0.8rem; color: var(--text-3); margin-top: 0.75rem;">
        Figura: {config['categoria']}
    </figcaption>
</figure>'''

        html_snippets[slug] = {
            "og_meta": og_meta,
            "hero_image": hero_image,
            "inline_image": inline_image
        }

    with open("snippets-html-imagens.json", "w", encoding="utf-8") as f:
        json.dump(html_snippets, f, ensure_ascii=False, indent=2)

    print("✅ Snippets HTML: snippets-html-imagens.json")

    # Também gerar markdown
    with open("INSERIR-IMAGENS-HTML.md", "w", encoding="utf-8") as f:
        f.write("# Como Inserir Imagens nos Artigos HTML\n\n")

        for slug, snippets in html_snippets.items():
            f.write(f"## {slug}\n\n")
            f.write("### 1. Meta Tags (no <head>)\n```html\n")
            f.write(snippets["og_meta"])
            f.write("\n```\n\n")
            f.write("### 2. Hero Image (topo do artigo)\n```html\n")
            f.write(snippets["hero_image"])
            f.write("\n```\n\n")
            f.write("### 3. Inline Image (dentro do artigo)\n```html\n")
            f.write(snippets["inline_image"])
            f.write("\n```\n\n")
            f.write("---\n\n")

    print("✅ Guia de inserção: INSERIR-IMAGENS-HTML.md")

# ============================================================================
# FUNÇÃO 5: Gerar CSS para Imagens
# ============================================================================

def gerar_css_imagens():
    """
    Estilos CSS para imagens responsivas
    """

    css = """/* =========================================================================
   ESTILOS PARA IMAGENS NOS ARTIGOS
   ========================================================================= */

/* Imagem Hero (topo do artigo) */
.art-hero {
    margin: 0 0 2.5rem 0;
    padding: 0;
    text-align: center;
}

.art-hero img {
    max-width: 100%;
    height: auto;
    border-radius: var(--radius-lg);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    display: block;
    margin: 0 auto;
}

/* Imagem inline (dentro do artigo) */
.art-inline-img {
    margin: 2rem 0;
    padding: 0;
    text-align: center;
}

.art-inline-img img {
    max-width: 100%;
    height: auto;
    border-radius: var(--radius-lg);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Legenda de figura */
.art-inline-img figcaption,
.art-hero figcaption {
    font-size: 0.8rem;
    color: var(--text-3);
    margin-top: 0.75rem;
    line-height: 1.5;
}

/* Galeria de imagens (para múltiplas imagens) */
.art-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.art-gallery img {
    max-width: 100%;
    height: auto;
    border-radius: var(--radius-lg);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Responsivo: mobile */
@media (max-width: 640px) {
    .art-hero {
        margin: 0 0 1.5rem 0;
    }

    .art-inline-img {
        margin: 1.5rem 0;
    }

    .art-gallery {
        grid-template-columns: 1fr;
        gap: 1rem;
    }
}

/* Dark mode: ajustes sutis */
@media (prefers-color-scheme: dark) {
    .art-hero img,
    .art-inline-img img {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }
}
"""

    with open("estilos-imagens.css", "w") as f:
        f.write(css)

    print("✅ Estilos CSS: estilos-imagens.css")

# ============================================================================
# FUNÇÃO 6: Relatório JSON (metadados)
# ============================================================================

def gerar_metadados_imagens():
    """
    Gera JSON com metadados de todas as imagens
    """

    metadata = {
        "gerado_em": datetime.now().isoformat(),
        "total_artigos": len(ARTIGOS),
        "especificacoes": {
            "formato": "PNG",
            "largura": 1200,
            "altura": 630,
            "dpi": 72,
            "tamanho_maximo": "200KB",
            "notas": "Otimizado para redes sociais (OG image) e blog"
        },
        "artigos": {}
    }

    for slug, config in ARTIGOS.items():
        metadata["artigos"][slug] = {
            "titulo": config["titulo"],
            "categoria": config["categoria"],
            "arquivo": f"{slug}.png",
            "url_publica": f"https://yarivi.com/imagens/{slug}.png",
            "alt_text": config["descricao_alt"],
            "cor_primaria": config["cor_primaria"],
            "emoji": config["emoji"],
            "palavras_chave": config["palavras_chave"].split(", ")
        }

    with open("metadata-imagens.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print("✅ Metadados: metadata-imagens.json")

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 70)
    print("GERADOR DE IMAGENS - ARTIGOS YARIVI 2026-09-08")
    print("=" * 70)

    print("\n📊 Opções disponíveis:\n")
    print("1. Gerar PLACEHOLDERS (PIL) — Rápido, minimalista")
    print("2. Gerar SCRIPT Unsplash — Baixar stock images")
    print("3. Gerar PROMPTS DALL-E — Para IA generativa")
    print("4. Gerar SNIPPETS HTML — Código para inserir")
    print("5. Gerar CSS — Estilos responsivos")
    print("6. Gerar METADADOS — JSON com config")
    print("7. TODOS os itens acima\n")

    opcao = input("Escolha uma opção (1-7): ").strip()

    if opcao in ["1", "7"]:
        print("\n🎨 Criando placeholders com PIL...")
        for slug, config in ARTIGOS.items():
            criar_placeholder_pil(slug, config)

    if opcao in ["2", "7"]:
        print("\n📥 Gerando script Unsplash...")
        gerar_script_unsplash()

    if opcao in ["3", "7"]:
        print("\n🤖 Gerando prompts DALL-E...")
        gerar_prompts_dalle()

    if opcao in ["4", "7"]:
        print("\n📝 Gerando snippets HTML...")
        gerar_html_imagens()

    if opcao in ["5", "7"]:
        print("\n🎨 Gerando CSS...")
        gerar_css_imagens()

    if opcao in ["6", "7"]:
        print("\n📋 Gerando metadados...")
        gerar_metadados_imagens()

    print("\n" + "=" * 70)
    print("✅ CONCLUÍDO!")
    print("=" * 70)
    print("\n📁 Arquivos gerados:")
    print("   - imagens/                      (pasta com imagens)")
    print("   - prompts-dalle.json            (prompts para IA)")
    print("   - PROMPTS-DALLE.md              (versão legível)")
    print("   - snippets-html-imagens.json    (código HTML)")
    print("   - INSERIR-IMAGENS-HTML.md       (guia completo)")
    print("   - estilos-imagens.css           (CSS responsivo)")
    print("   - metadata-imagens.json         (metadados)")
    print("   - baixar-imagens-unsplash.sh    (script bash)")
    print("\n💡 Próximos passos:")
    print("   1. Escolha um método de imagens (PIL, Unsplash, ou DALL-E)")
    print("   2. Execute o script correspondente")
    print("   3. Copie o HTML dos snippets para cada artigo")
    print("   4. Teste no navegador\n")

if __name__ == "__main__":
    main()
