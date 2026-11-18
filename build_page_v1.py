#!/usr/bin/env python3
"""Build the front-page image for make.fun's news-image-20261117 entry.

Composes one 1024x1024 newspaper front page that sums up the world news of
Tuesday 17 November 2026, drawn entirely with Pillow primitives (flat
illustrations, crisp real text - no AI-generated text anywhere).
Deterministic: same input data, same bytes out.

Run:  python3 build_page.py   ->  writes assets/entry.png
The competition entrypoint main.py then copies assets/entry.png to
/output/entry.png in the grader's sandbox (standard library only).
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (26, 26, 24)
FAINT = (110, 102, 88)
RED = (178, 34, 40)
TEAL = (23, 107, 104)
NAVY = (24, 49, 83)
GOLD = (196, 138, 30)
CARD_BG = (253, 251, 245)
LINE = (201, 192, 168)

FONT_DIR = "/usr/share/fonts/truetype/noto/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


def serif(size, weight="Black"):
    return font(f"NotoSerif-{weight}.ttf", size)


def sans(size, weight="Regular"):
    return font(f"NotoSans-{weight}.ttf", size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap by pixel width."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, fill, width, leading):
    x, y = xy
    for ln in wrap(draw, text, fnt, width):
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


# ---------------------------------------------------------------- stories
# Every story below happened, or was first reported, on Tuesday
# 17 November 2026 (cross-checked against Reuters/AP/AFP/BBC/Al Jazeera
# reporting of the day). Contested claims are attributed in the wording.

LEADS = [
    dict(
        n=1, region="EUROPE · UKRAINE WAR", art="bridge",
        headline="Ukraine says a Crimean Bridge road span fell into the sea",
        summary="Second strike in two days; Zelensky hails an \u201cunprecedented\u201d hit.",
    ),
    dict(
        n=2, region="MIDDLE EAST · IRAN WAR", art="gulf",
        headline="Iran sends drones at a US radar in Bahrain; US hits back",
        summary="Bahrain says all were downed; US jets then strike Qeshm island.",
    ),
    dict(
        n=3, region="ASIA · DIPLOMACY", art="quad",
        headline="Trump holds his first Quad summit, in Manila",
        summary="Minerals deals unveiled; Putin lands in Shenzhen for Thursday.",
    ),
]

CARDS = [
    dict(
        n=4, region="AFRICA · HEALTH", art="ebola",
        headline="Ebola cases in DR Congo top 11,000, WHO says",
        summary="Cases more than doubled in three months; about 5,400 have died.",
    ),
    dict(
        n=5, region="US · BUSINESS", art="chip",
        headline="Nvidia's quarterly sales double to $115.8bn",
        summary="First results since Jensen Huang quit; the Dow fell 849 points (\u22121.6%).",
    ),
    dict(
        n=6, region="AMERICAS · HEALTH", art="measles",
        headline="US, Mexico and Bolivia lose measles-free status",
        summary="PAHO cites a year of spread; the US has 5,700+ cases in 2026.",
    ),
    dict(
        n=7, region="MIDDLE EAST · GAZA", art="gaza",
        headline="Gaza winter aid held up at crossings",
        summary="UN agencies say 1.4m face acute hunger as cold sets in.",
    ),
    dict(
        n=8, region="ASIA · DEFENCE", art="jets",
        headline="Japan scrambles jets at Russian incursion",
        summary="Two planes entered near Fukuoka; Tokyo protests, first since 2024.",
    ),
    dict(
        n=9, region="EUROPE · LABOUR", art="strike",
        headline="France struck again over the cost of living",
        summary="146,000 march nationwide (CGT: 500,000) in a second union strike.",
    ),
    dict(
        n=10, region="RUSSIA · AIR CRASH", art="crash",
        headline="Russian An-12 crash in Siberia kills all 19",
        summary="The air force plane came down near Kemerovo; a fault is suspected.",
    ),
    dict(
        n=11, region="GLOBAL · CLIMATE", art="cop",
        headline="COP31 divided over a fossil-fuel phase-out",
        summary="Nations weigh the first draft; the Antalya talks end Friday.",
    ),
]

ALSO = [
    "Russia: 1,441 drones downed overnight",
    "Kyiv: missiles hit both Dnipro bridges",
    "UN: Ukraine civilian deaths top 2025",
    "Prague: two trains collide, 46 injured",
    "Poland: Tusk survives confidence vote",
    "Moldova shuts airspace, Russian drone",
    "Turkey: police seize S\u00f6zc\u00fc TV",
    "West Bank: settlers kill a woman, 72",
    "UK: US soldier arrested in spying case",
    "Depardieu drops appeal, admits assault",
    "Pope Leo struck near eye in Peru visit",
    "US: nationwide emergency-alert test",
    "Dhaka: tear gas at garment workers",
    "Serbia: student bloc takes parliament",
    "Mongolia: president says he will resign",
    "Mozambique: opposition leader on trial",
    "India: Cyclone Akvan nears Odisha coast",
    "Darwin: M6.6 quake off Indonesia, no tsunami",
    "IMF lifts Korea 2026 growth to 3.9%",
    "Apple outage hits Pay, iCloud, App Store",
    "Deutsche Bank falls after data leak",
    "Eritrea: WHO says trachoma eliminated",
    "Bulgaria: tanker sinks, 19 crew rescued",
    "Yemen: Houthis advance toward Aden",
    "Football: Norway win 3\u20132 in Denmark",
    "Syria: 4m displaced have returned \u2014 UN",
]

TOTAL = len(LEADS) + len(CARDS) + len(ALSO)

# ------------------------------------------------------------ illustrations
# Flat scenes drawn with primitives, in the visual language of a newspaper
# spot illustration. Each takes (draw, x, y, w, h) and draws inside the box.


def art_bridge(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(203, 220, 230))
    d.rectangle([x, y + h * 0.62, x + w, y + h], fill=(64, 110, 140))
    for i in range(5):  # birds
        bx, by = x + 18 + i * 26, y + 10 + (i % 2) * 7
        d.arc([bx, by, bx + 12, by + 8], 200, 330, fill=INK, width=2)
    deck = y + h * 0.52
    d.rectangle([x, deck, x + w, deck + 7], fill=(52, 54, 58))
    for px in (0.22, 0.55, 0.85):
        d.rectangle([x + w * px, deck - 16, x + w * px + 5, deck], fill=(52, 54, 58))
    gap = x + w * 0.60
    d.polygon([(gap, deck + 7), (gap + 34, deck + 7), (gap + 26, deck + 26), (gap + 6, deck + 22)], fill=(52, 54, 58))
    cx, cy = x + w * 0.40, deck - 8  # explosion
    for dx, dy, r in [(0, 0, 13), (-14, 5, 9), (13, 4, 10), (-4, -11, 8)]:
        d.ellipse([cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r], fill=(240, 150, 40))
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(250, 210, 90))
    for sx, sy, sr in [(cx + 26, cy - 22, 11), (cx + 44, cy - 30, 14), (cx + 8, cy - 30, 9)]:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(120, 122, 126))
    d.text((x + 8, y + h - 17), "KERCH STRAIT · STRUCK FOR A SECOND DAY",
           font=sans(10, "Bold"), fill=(255, 255, 255))


def art_gulf(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 205, 160))
    d.rectangle([x, y + h * 0.66, x + w, y + h], fill=(70, 120, 150))
    d.text((x + w * 0.52, y + 6), "IRAN", font=sans(11, "Bold"), fill=INK)
    d.text((x + 10, y + h * 0.30), "BAHRAIN", font=sans(10, "Bold"), fill=INK)
    d.text((x + w * 0.78, y + h * 0.40), "QESHM", font=sans(10, "Bold"), fill=INK)
    d.text((x + w - 6, y + h * 0.70), "HORMUZ", font=sans(10, "Bold"), fill=(255, 255, 255), anchor="ra")
    # drone path
    pts = [(x + w * 0.30, y + h * 0.30), (x + w * 0.44, y + h * 0.22), (x + w * 0.58, y + h * 0.30)]
    d.line(pts, fill=RED, width=3)
    dx, dy = pts[-1]
    d.polygon([(dx, dy), (dx - 14, dy - 5), (dx - 11, dy + 6)], fill=INK)  # drone
    d.rectangle([x + w * 0.17, y + h * 0.52, x + w * 0.415, y + h * 0.615], fill=RED)
    d.text((x + w * 0.292, y + h * 0.567), "DRONES DOWNED", font=sans(10, "Bold"), fill=(255, 255, 255), anchor="mm")
    # US strike marker
    sx, sy = x + w * 0.80, y + h * 0.30
    d.line([sx - 8, sy - 8, sx + 8, sy + 8], fill=RED, width=3)
    d.line([sx - 8, sy + 8, sx + 8, sy - 8], fill=RED, width=3)
    d.rectangle([x + w * 0.585, y + h * 0.55, x + w * 0.755, y + h * 0.645], fill=NAVY)
    d.text((x + w * 0.67, y + h * 0.597), "US STRIKES", font=sans(10, "Bold"), fill=(255, 255, 255), anchor="mm")
    # tanker
    tx, ty = x + w * 0.68, y + h * 0.78
    d.polygon([(tx, ty), (tx + 62, ty), (tx + 54, ty + 10), (tx + 8, ty + 10)], fill=(40, 40, 44))
    d.rectangle([tx + 12, ty - 8, tx + 46, ty], fill=(150, 60, 50))


def _flag_us(d, x, y, w, h):
    for i in range(7):
        d.rectangle([x, y + i * h / 7, x + w, y + (i + 1) * h / 7], fill=(178, 34, 52) if i % 2 == 0 else (255, 255, 255))
    d.rectangle([x, y, x + w * 0.45, y + h * 4 / 7], fill=(36, 44, 92))


def _flag_in(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 3], fill=(240, 140, 40))
    d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(255, 255, 255))
    d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(30, 130, 60))
    d.ellipse([x + w / 2 - 4, y + h / 2 - 4, x + w / 2 + 4, y + h / 2 + 4], outline=(30, 60, 160), width=2)


def _flag_jp(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    d.ellipse([x + w / 2 - h / 6, y + h / 3, x + w / 2 + h / 6, y + 2 * h / 3], fill=(188, 0, 45))


def _flag_au(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 44, 110))
    for sx, sy in [(0.68, 0.25), (0.8, 0.55), (0.62, 0.7), (0.85, 0.2)]:
        cx, cy = x + w * sx, y + h * sy
        d.ellipse([cx - 2.5, cy - 2.5, cx + 2.5, cy + 2.5], fill=(255, 255, 255))


def art_quad(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(96, 44, 120))
    d.text((x + w / 2, y + 8), "QUAD LEADERS' SUMMIT · MANILA", font=sans(12, "Bold"),
           fill=(255, 255, 255), anchor="ma")
    fy, fw, fh = y + 34, w * 0.19, h * 0.34
    for i, (fn, label) in enumerate([(_flag_us, "US"), (_flag_in, "INDIA"), (_flag_jp, "JAPAN"), (_flag_au, "AUSTRALIA")]):
        fx = x + w * 0.06 + i * w * 0.235
        d.rectangle([fx, fy, fx + fw, fy + fh], fill=(255, 255, 255))
        fn(d, fx + 3, fy + 3, fw - 6, fh - 6)
        d.text((fx + fw / 2, fy + fh + 4), label, font=sans(10, "Bold"), fill=(255, 255, 255), anchor="ma")
    d.rectangle([x, y + h - 20, x + w, y + h], fill=(70, 30, 88))
    d.text((x + w / 2, y + h - 17), "NEW CRITICAL-MINERALS DEALS", font=sans(11, "Bold"),
           fill=(255, 255, 255), anchor="ma")


def art_ebola(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(226, 240, 246))
    cx, cy = x + w * 0.30, y + h * 0.52
    d.polygon([(cx, cy - 26), (cx + 20, cy - 14), (cx + 20, cy + 8), (cx, cy + 28),
               (cx - 20, cy + 8), (cx - 20, cy - 14)], outline=TEAL, width=3)
    d.rectangle([cx - 4, cy - 14, cx + 4, cy + 14], fill=RED)
    d.rectangle([cx - 12, cy - 4, cx + 12, cy + 4], fill=RED)
    for dx, dy in [(58, -18), (86, -12), (64, 14)]:
        vx, vy = x + w * 0.30 + dx, y + h * 0.52 + dy
        d.ellipse([vx - 10, vy - 10, vx + 10, vy + 10], outline=(90, 140, 60), width=2)
        for a in range(0, 360, 60):
            import math
            ex, ey = vx + 13 * math.cos(math.radians(a)), vy + 13 * math.sin(math.radians(a))
            d.line([vx, vy, ex, ey], fill=(90, 140, 60), width=2)
    d.rectangle([x + w * 0.60, y + h * 0.14, x + w * 0.98, y + h * 0.40], fill=RED)
    d.text((x + w * 0.79, y + h * 0.27), "11,000+ CASES", font=sans(10.5, "Bold"),
           fill=(255, 255, 255), anchor="mm")
    d.text((x + w * 0.58, y + h * 0.80), "DR CONGO · EBOLA", font=sans(10, "Bold"), fill=INK)


def art_chip(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 20, 18))
    cx, cy, s = x + w * 0.26, y + h * 0.52, h * 0.52
    d.rectangle([cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2], outline=(120, 200, 90), width=3)
    d.rectangle([cx - s / 4, cy - s / 4, cx + s / 4, cy + s / 4], outline=(120, 200, 90), width=2)
    for i in range(-1, 2):
        d.line([cx - s / 2, cy + i * s / 4, cx - s / 2 - 9, cy + i * s / 4], fill=(120, 200, 90), width=3)
        d.line([cx + s / 2, cy + i * s / 4, cx + s / 2 + 9, cy + i * s / 4], fill=(120, 200, 90), width=3)
    d.text((x + w * 0.50, y + h * 0.04), "$115.8BN", font=sans(12, "Black"), fill=(250, 210, 90))
    base = y + h * 0.86
    for i, bh in enumerate([0.22, 0.36, 0.52, 0.72]):
        bx = x + w * 0.54 + i * w * 0.085
        d.rectangle([bx, base - h * bh, bx + w * 0.055, base], fill=(120, 200, 90))
    d.line([x + w * 0.52, base - h * 0.24, x + w * 0.90, base - h * 0.58], fill=(250, 210, 90), width=3)


def art_measles(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(240, 236, 220))
    labels = [((178, 34, 52), "US"), ((20, 120, 70), "MEXICO"), ((200, 30, 45), "BOLIVIA")]
    for i, (col, name) in enumerate(labels):
        fx = x + w * (0.06 + i * 0.31)
        d.rectangle([fx, y + h * 0.18, fx + w * 0.24, y + h * 0.55], fill=col)
        d.text((fx + w * 0.12, y + h * 0.68), name, font=sans(10, "Bold"), fill=INK, anchor="ma")
    d.line([x + w * 0.08, y + h * 0.88, x + w * 0.92, y + h * 0.88], fill=INK, width=2)
    d.text((x + w / 2, y + h * 0.90), "MEASLES-FREE STATUS REVOKED", font=sans(11, "Bold"), fill=RED, anchor="ma")


def art_gaza(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 226, 234))
    gy = y + h * 0.80
    d.rectangle([x, gy, x + w, y + h], fill=(196, 178, 150))
    for i, tx in enumerate([0.08, 0.30, 0.52]):
        px = x + w * tx
        d.polygon([(px, gy), (px + w * 0.10, gy - h * 0.34), (px + w * 0.20, gy)], fill=(240, 238, 230), outline=FAINT)
    tx, ty = x + w * 0.74, gy - h * 0.30  # aid truck
    d.rectangle([tx, ty, tx + w * 0.20, ty + h * 0.30], fill=(240, 240, 240), outline=INK)
    d.rectangle([tx - w * 0.06, ty + h * 0.10, tx, ty + h * 0.30], fill=TEAL)
    d.rectangle([tx + w * 0.075, ty + h * 0.06, tx + w * 0.125, ty + h * 0.16], fill=RED)
    d.rectangle([tx + w * 0.09, ty + h * 0.09, tx + w * 0.11, ty + h * 0.13], fill=(255, 255, 255))
    for wx in (tx + w * 0.02, tx + w * 0.15):
        d.ellipse([wx, gy - 6, wx + 12, gy + 6], fill=INK)
    d.rectangle([x + w * 0.50, y + h * 0.08, x + w * 0.98, y + h * 0.32], fill=(178, 60, 40))
    d.text((x + w * 0.74, y + h * 0.20), "1.4M FACE HUNGER", font=sans(9, "Bold"),
           fill=(255, 255, 255), anchor="mm")
    d.text((x + 8, y + h - 15), "GAZA · WINTER AID HELD UP", font=sans(10, "Bold"), fill=INK)


def _jet(d, cx, cy, s, col, flip=1):
    pts = [(0, 0), (26, -6), (44, -2), (30, 4), (44, 10), (24, 10), (8, 16), (10, 8), (-6, 6), (-14, 12), (-10, 2), (-16, -4), (-6, -3), (6, -10), (10, -3)]
    d.polygon([(cx + flip * px * s, cy + py * s) for px, py in pts], fill=col)


def art_jets(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(206, 224, 238))
    d.ellipse([x + w * 0.06, y + h * 0.14, x + w * 0.20, y + h * 0.52], fill=(255, 255, 255))
    d.ellipse([x + w * 0.095, y + h * 0.24, x + w * 0.165, y + h * 0.42], fill=(188, 0, 45))
    _jet(d, x + w * 0.52, y + h * 0.40, 1.15, (40, 44, 50))
    _jet(d, x + w * 0.66, y + h * 0.62, 1.15, (150, 40, 40), flip=-1)
    d.line([x + w * 0.06, y + h * 0.85, x + w * 0.95, y + h * 0.85], fill=FAINT, width=2)
    d.text((x + w * 0.50, y + h * 0.88), "FUKUOKA · FIRST SINCE 2024", font=sans(9.5, "Bold"), fill=INK, anchor="ma")


def art_strike(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(236, 228, 208))
    d.rectangle([x + w * 0.10, y + h * 0.10, x + w * 0.90, y + h * 0.42], fill=(255, 255, 255), outline=INK, width=2)
    d.text((x + w / 2, y + h * 0.26), "146,000 MARCH", font=sans(14, "Black"), fill=RED, anchor="mm")
    d.rectangle([x + w * 0.58, y + h * 0.47, x + w * 0.96, y + h * 0.63], fill=NAVY)
    d.text((x + w * 0.77, y + h * 0.55), "CGT: 500,000", font=sans(9.5, "Bold"), fill=(255, 255, 255), anchor="mm")
    for i in range(9):
        hx = x + w * (0.10 + i * 0.10)
        hy = y + h * (0.70 + (i % 3) * 0.05)
        d.ellipse([hx - 6, hy - 6, hx + 6, hy + 6], fill=(60, 60, 66))
        d.rectangle([hx - 7, hy + 6, hx + 7, hy + 15], fill=(60, 60, 66))


def art_crash(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(210, 220, 228))
    d.rectangle([x, y + h * 0.78, x + w, y + h], fill=(240, 242, 244))
    for i, tx in enumerate([0.05, 0.16, 0.80, 0.90]):
        px = x + w * tx
        d.polygon([(px, y + h * 0.78), (px + 9, y + h * 0.52), (px + 18, y + h * 0.78)], fill=(50, 90, 70))
    cx, cy = x + w * 0.46, y + h * 0.52
    d.polygon([(cx - 37, cy + 4), (cx + 28, cy - 9), (cx + 40, cy - 2), (cx + 14, cy + 5),
               (cx + 21, cy + 12), (cx - 4, cy + 8), (cx - 24, cy + 13)], fill=(90, 94, 100))
    d.polygon([(cx - 37, cy + 4), (cx - 47, cy - 8), (cx - 38, cy - 9), (cx - 27, cy + 1)], fill=(70, 74, 80))
    for sx, sy, sr in [(cx + 38, cy - 13, 7), (cx + 50, cy - 18, 9)]:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(110, 112, 116))
    d.rectangle([x + w * 0.60, y + h * 0.08, x + w * 0.98, y + h * 0.30], fill=INK)
    d.text((x + w * 0.79, y + h * 0.19), "ALL 19 KILLED", font=sans(9.5, "Bold"),
           fill=(255, 255, 255), anchor="mm")
    d.text((x + 8, y + h - 15), "KEMEROVO · SIBERIA", font=sans(10, "Bold"), fill=INK)


def art_cop(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(224, 238, 226))
    cx, cy, r = x + w * 0.24, y + h * 0.50, h * 0.32
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(90, 150, 190))
    d.polygon([(cx - r * 0.7, cy - r * 0.3), (cx - r * 0.1, cy - r * 0.55), (cx + r * 0.1, cy - r * 0.1),
               (cx - r * 0.3, cy + r * 0.3), (cx - r * 0.75, cy + r * 0.25)], fill=(90, 160, 90))
    d.polygon([(cx + r * 0.25, cy + r * 0.35), (cx + r * 0.75, cy + r * 0.15), (cx + r * 0.8, cy + r * 0.6),
               (cx + r * 0.35, cy + r * 0.7)], fill=(90, 160, 90))
    tx = x + w * 0.60
    d.rounded_rectangle([tx, y + h * 0.14, tx + 16, y + h * 0.78], 8, outline=INK, width=2)
    d.rectangle([tx + 3, y + h * 0.40, tx + 13, y + h * 0.75], fill=RED)
    d.ellipse([tx + 2, y + h * 0.74, tx + 14, y + h * 0.90], outline=INK, width=2)
    d.rectangle([x + w * 0.72, y + h * 0.14, x + w * 0.98, y + h * 0.40], fill=TEAL)
    d.text((x + w * 0.85, y + h * 0.27), "FIRST DRAFT", font=sans(9.5, "Bold"),
           fill=(255, 255, 255), anchor="mm")
    d.text((x + w * 0.70, y + h * 0.80), "COP31 · ANTALYA", font=sans(10, "Bold"), fill=INK)


ART = {
    "bridge": art_bridge, "gulf": art_gulf, "quad": art_quad, "ebola": art_ebola,
    "chip": art_chip, "measles": art_measles, "gaza": art_gaza, "jets": art_jets,
    "strike": art_strike, "crash": art_crash, "cop": art_cop,
}


# ------------------------------------------------------------------- map
# Rough continent polygons in normalised map coords (x: lon -180..180,
# y: lat 80..-60). Deliberately simple silhouettes, newspaper-style.

LAND = [
    [(0.02, 0.20), (0.09, 0.09), (0.19, 0.06), (0.26, 0.11), (0.255, 0.21), (0.295, 0.27),
     (0.265, 0.35), (0.215, 0.33), (0.20, 0.41), (0.155, 0.37), (0.125, 0.29), (0.05, 0.29), (0.025, 0.25)],
    [(0.205, 0.44), (0.26, 0.435), (0.30, 0.52), (0.305, 0.65), (0.275, 0.79), (0.25, 0.80),
     (0.232, 0.63), (0.20, 0.53)],
    [(0.435, 0.11), (0.50, 0.065), (0.55, 0.115), (0.545, 0.20), (0.50, 0.245), (0.468, 0.20),
     (0.44, 0.225), (0.428, 0.165)],
    [(0.448, 0.305), (0.52, 0.27), (0.585, 0.30), (0.60, 0.41), (0.568, 0.56), (0.528, 0.685),
     (0.488, 0.66), (0.458, 0.50), (0.44, 0.385)],
    [(0.552, 0.085), (0.70, 0.05), (0.85, 0.075), (0.925, 0.16), (0.885, 0.26), (0.805, 0.295),
     (0.785, 0.40), (0.72, 0.375), (0.70, 0.30), (0.635, 0.335), (0.60, 0.26), (0.562, 0.20)],
    [(0.815, 0.575), (0.90, 0.555), (0.935, 0.635), (0.885, 0.725), (0.828, 0.685), (0.805, 0.615)],
]
ISLANDS = [(0.755, 0.455, 0.016), (0.79, 0.475, 0.013), (0.825, 0.46, 0.012), (0.715, 0.42, 0.010)]

# story number -> (lon, lat)
PINS = {
    1: (37, 45), 2: (50, 26), 3: (121, 14), 4: (23, -2), 5: (-74, 40), 6: (-102, 38),
    7: (34, 31), 8: (130, 33), 9: (2, 47), 10: (86, 55), 11: (30, 37),
    13: (30, 50), 29: (130, -12), 33: (39, 15),
}


def draw_map(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(233, 226, 205))
    for poly in LAND:
        pts = [(x + px * w, y + py * h) for px, py in poly]
        d.polygon(pts, fill=(206, 190, 150), outline=(150, 134, 96))
    for nx, ny, nr in ISLANDS:
        d.ellipse([x + (nx - nr) * w, y + (ny - nr) * h, x + (nx + nr) * w, y + (ny + nr) * h],
                  fill=(206, 190, 150), outline=(150, 134, 96))
    for n, (lon, lat) in PINS.items():
        px = x + (lon + 180) / 360 * w
        py = y + (80 - lat) / 140 * h
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED)
        d.text((px, py), str(n), font=sans(10, "Bold"), fill=(255, 255, 255), anchor="mm")


# ----------------------------------------------------------------- layout

def chip(d, x, y, n, r=11):
    d.ellipse([x, y, x + 2 * r, y + 2 * r], fill=RED)
    d.text((x + r, y + r), str(n), font=sans(13, "Bold"), fill=(255, 255, 255), anchor="mm")


def lead_card(d, x, y, w, h, s):
    d.rectangle([x, y, x + w, y + h], fill=CARD_BG, outline=LINE)
    ART[s["art"]](d, x + 1, y + 1, w - 2, 92)
    chip(d, x + 8, y + 8, s["n"])
    ty = y + 102
    d.text((x + 12, ty), s["region"], font=sans(11, "Bold"), fill=RED)
    ty += 17
    ty = text_block(d, (x + 12, ty), s["headline"], serif(22, "Bold"), INK, w - 24, 26)
    ty += 3
    text_block(d, (x + 12, ty), s["summary"], sans(14), (52, 50, 44), w - 24, 18)


def small_card(d, x, y, w, h, s):
    d.rectangle([x, y, x + w, y + h], fill=CARD_BG, outline=LINE)
    ART[s["art"]](d, x + 1, y + 1, w - 2, 50)
    chip(d, x + 6, y + 6, s["n"], r=9)
    ty = y + 58
    d.text((x + 9, ty), s["region"], font=sans(10, "Bold"), fill=RED)
    ty += 14
    ty = text_block(d, (x + 9, ty), s["headline"], serif(15, "Bold"), INK, w - 18, 18)
    ty += 2
    text_block(d, (x + 9, ty), s["summary"], sans(11.5), (52, 50, 44), w - 18, 14.5)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 26

    # top strip
    d.text((M, 14), "THE WORLD'S NEWS IN ONE PICTURE", font=sans(13, "Bold"), fill=RED)
    d.text((W - M, 14), f"{TOTAL} STORIES \u00b7 6 CONTINENTS \u00b7 ALL FROM TUESDAY",
           font=sans(13, "Bold"), fill=INK, anchor="ra")
    d.line([M, 38, W - M, 38], fill=INK, width=2)

    # masthead
    d.text((W / 2, 46), "Tuesday 17 November 2026", font=serif(63, "Black"), fill=INK, anchor="ma")
    d.line([M, 124, W - M, 124], fill=INK, width=4)
    d.line([M, 130, W - M, 130], fill=INK, width=1)

    # leads
    lw = (W - 2 * M - 2 * 14) / 3
    for i, s in enumerate(LEADS):
        lead_card(d, M + i * (lw + 14), 142, lw, 232, s)

    # small cards, 2 rows of 4
    cw = (W - 2 * M - 3 * 12) / 4
    for i, s in enumerate(CARDS):
        cx = M + (i % 4) * (cw + 12)
        cy = 386 + (i // 4) * (164 + 10)
        small_card(d, cx, cy, cw, 164, s)

    # bottom: map + also list
    by = 742
    d.text((M, by), "WHERE IT HAPPENED", font=sans(13, "Bold"), fill=INK)
    draw_map(d, M, by + 22, 446, 196)
    d.text((M, by + 224), "Pins: stories 1\u201311, 13, 29 and 33 \u00b7 not to scale",
           font=sans(10), fill=FAINT)

    ax = M + 446 + 24
    d.text((ax, by), "ALSO ON TUESDAY 17 NOVEMBER", font=sans(13, "Bold"), fill=INK)
    col_w = (W - M - ax - 16) / 2
    half = (len(ALSO) + 1) // 2
    f = sans(11.5)
    lead = 214 / half
    for j, item in enumerate(ALSO):
        col = 0 if j < half else 1
        row = j if col == 0 else j - half
        ix = ax + col * (col_w + 16)
        iy = by + 24 + row * lead
        n = len(LEADS) + len(CARDS) + j + 1
        d.ellipse([ix, iy + 1, ix + 15, iy + 16], fill=TEAL if col == 0 else NAVY)
        d.text((ix + 7.5, iy + 8.5), str(n), font=sans(9, "Bold"), fill=(255, 255, 255), anchor="mm")
        # one line only: shrink the wording with an ellipsis if it cannot fit
        t = item
        while d.textlength(t, font=f) > col_w - 22 and len(t) > 8:
            t = t[:-1]
        if t != item:
            t = t.rstrip(" ,;") + "\u2026"
        d.text((ix + 20, iy + 1), t, font=f, fill=(40, 38, 34))

    # footer
    d.line([M, 986, W - M, 986], fill=INK, width=2)
    d.text((M, 992), "Every story happened or was first reported on Tuesday 17 November 2026. "
                     "Contested claims are marked as claims.",
           font=sans(10.5), fill=(52, 50, 44))
    d.text((W - M, 992), "Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 BBC \u00b7 Al Jazeera \u00b7 WHO \u00b7 UN",
           font=sans(10.5), fill=(52, 50, 44), anchor="ra")
    return img


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "entry.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im = build()
    im.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")
