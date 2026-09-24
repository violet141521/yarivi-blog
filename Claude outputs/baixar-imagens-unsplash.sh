#!/bin/bash
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
