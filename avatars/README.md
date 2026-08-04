# avatars

Character portraits used by `../GOT.py`'s radar-chart legend.

These are **original illustrated avatars**, not photos of the actors or show
artwork — generated fully offline with [DiceBear](https://www.dicebear.com)
(`adventurer` style, MIT licensed), deterministically from each character's
name, then composited onto a flat parchment background and circle-cropped
with Pillow.

## Regenerating

```bash
npm install @dicebear/core @dicebear/collection @dicebear/converter
node generate.mjs   # writes 256x256 PNGs to ./out
```

`generate.mjs`:

```js
import { createAvatar } from "@dicebear/core";
import { adventurer } from "@dicebear/collection";
import { toPng } from "@dicebear/converter";
import { writeFileSync, mkdirSync } from "fs";

const OUT_DIR = "./out";
mkdirSync(OUT_DIR, { recursive: true });

const CHARACTERS = [
  "Jon Snow", "Tywin Lannister", "Lord Varys",
  "Arya Stark", "Sansa Stark", "Daenerys Targaryen",
];

const slug = (name) => name.toLowerCase().replace(/^lord\s+/, "").replace(/\s+/g, "_");

for (const name of CHARACTERS) {
  const avatar = createAvatar(adventurer, { seed: name, size: 256 });
  const png = await toPng(avatar.toString(), { size: 256 });
  writeFileSync(`${OUT_DIR}/${slug(name)}.png`, Buffer.from(await png.toArrayBuffer()));
}
```

Then composite onto parchment and circle-crop with Pillow:

```python
from PIL import Image, ImageDraw
import pathlib

BG = (245, 235, 210, 255)
for f in pathlib.Path("out").glob("*.png"):
    fg = Image.open(f).convert("RGBA")
    canvas = Image.new("RGBA", fg.size, BG)
    canvas.alpha_composite(fg)
    mask = Image.new("L", fg.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0, *fg.size), fill=255)
    canvas.putalpha(mask)
    canvas.save(f"../avatars/{f.name}")
```
