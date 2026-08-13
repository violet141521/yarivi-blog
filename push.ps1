Remove-Item -Force ".git\index.lock" -ErrorAction SilentlyContinue
git commit -m "fix: bugs auditoria - hamburguer mobile, links .html footer, categorias

- Adiciona menu hamburguer em nav.html (botao + toggle JS)
- Estiliza dropdown mobile em style.css (aparece abaixo do nav fixo)
- Remove .html de privacidade/termos/contato no footer
- Corrige links de categoria do footer (eram todos '#', agora '/#ultimas')
- Remove social proof falso do meta description e og:description
- Adiciona artigos/_catalog.json, favicons, og-cover, paginas legais,
  functions/api/publicar.js e novos rascunhos ao repositorio"
git push origin main
