#!/usr/bin/env python3
"""Build the GTA 6 meme for the make.fun bounty gta6-meme-x-01.

Composites the AI-generated two-panel scene with the official make.fun
ghost badge (press kit mark) and bold meme captions. Deterministic:
same inputs always produce the same meme.png.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SCENE = HERE / "assets" / "media-generation-meme-scene-0-bd0af5d9-f293-46c6-a654-490d06791ce1.png"
MARK = HERE / "assets" / "mark-1024.png"
OUT = HERE / "meme.png"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

W = 1024
TOP_BAR_H = 100
BOTTOM_BAR_H = 150


def fit_font(draw, text, max_width, start_size):
    """Largest bold font (<= start_size) whose text fits max_width."""
    size = start_size
    while size > 10:
        font = ImageFont.truetype(FONT_PATH, size)
        if draw.textlength(text, font=font) <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(FONT_PATH, 10)


def centered(draw, text, font, cx, cy, fill="white"):
    draw.text((cx, cy), text, font=font, fill=fill, anchor="mm")


def main():
    scene = Image.open(SCENE).convert("RGB")
    if scene.size != (W, W):
        scene = scene.resize((W, W), Image.LANCZOS)
    img = scene.copy()
    draw = ImageDraw.Draw(img)

    # Top caption bar over the dull waiting room.
    draw.rectangle([0, 0, W, TOP_BAR_H], fill="black")
    top_text = "STILL WAITING FOR GTA VI SINCE 2013…"
    font = fit_font(draw, top_text, W - 40, 54)
    centered(draw, top_text, font, W // 2, TOP_BAR_H // 2)

    # The make.fun ghost badge, sitting in the gamer's chair (bottom panel).
    mark = Image.open(MARK).convert("RGBA")
    badge = 340
    mark = mark.resize((badge, badge), Image.LANCZOS)
    chair_cx, badge_cy = 315, 690
    img.paste(mark, (chair_cx - badge // 2, badge_cy - badge // 2), mark)
    draw = ImageDraw.Draw(img)

    # Bottom caption bar with the punchline / advert.
    draw.rectangle([0, W - BOTTOM_BAR_H, W, W], fill="black")
    line1 = "MEANWHILE, THE MAKE.FUN GHOST"
    line2 = "IS EARNING REAL USDC FROM BOUNTIES"
    f1 = fit_font(draw, line1, W - 40, 46)
    f2 = fit_font(draw, line2, W - 40, 46)
    base = W - BOTTOM_BAR_H
    centered(draw, line1, f1, W // 2, base + 42)
    centered(draw, line2, f2, W // 2, base + 102)

    img.save(OUT)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
