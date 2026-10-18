# Gera miniaturas leves (640px de largura, WebP) das capas dos artigos para os
# cards da home: img/<slug>.webp -> img/thumb/<slug>.webp
# So recria a miniatura quando ela nao existe ou e mais antiga que a original.
# Uso: python scripts/gerar-thumbs.py   (requer Pillow: pip install pillow)
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parent.parent
src_dir, out_dir = root / 'img', root / 'img' / 'thumb'
out_dir.mkdir(exist_ok=True)
feitas = 0
for src in sorted(src_dir.glob('*.webp')):
    out = out_dir / src.name
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        continue
    with Image.open(src) as im:
        w, h = im.size
        if w > 640:
            im = im.resize((640, round(h * 640 / w)), Image.LANCZOS)
        im.save(out, 'WEBP', quality=78, method=6)
    feitas += 1
print(f'miniaturas: {feitas} geradas/atualizadas em img/thumb/')
