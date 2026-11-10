#!/usr/bin/env python3
"""
Genera assets/xp-profile.svg (diseño Windows XP para el README de GitHub).

Uso:
    python build.py                 -> avatar placeholder
    python build.py avatar.png      -> embebe tu foto (png/jpg) dentro del SVG

Por qué embeber la foto: un SVG cargado con <img> en GitHub NO puede cargar
imágenes externas, así que la foto debe ir como data-URI dentro del SVG.
"""
import base64
import mimetypes
import sys
from pathlib import Path

# ----------------------------- DATOS EDITABLES -----------------------------
FULL_NAME_LINES = ["Jandy José Peña", "Vásquez"]
USERNAME = "(BlurTrace)"
SUBTITLE_LINES = ["Junior Frontend Developer", "in Training"]
EMAIL = "jandyjpv@gmail.com"
PHONE = "+57 314 845 7565"
INSTAGRAM = "@blurtrace"
EXPLORER_TITLE = r"BlurTrace - Explorer [C:\Tech Stack]"
EXPLORING = ["Software Architecture, REST APIs,", "Advanced Patterns & Cloud"]
CLOCK = "12:00 PM"

TECH = [  # (nombre, badge, color fondo, color texto)
    ("HTML", "HTML5", "#E34F26", "#fff"),
    ("CSS", "CSS3", "#1572B6", "#fff"),
    ("JS", "JS", "#F7DF1E", "#000"),
    ("React", "React", "#61DAFB", "#000"),
    ("NextJs", "Next.js", "#000000", "#fff"),
    ("Docker", "Docker", "#2496ED", "#fff"),
    ("AWS", "AWS", "#FF9900", "#000"),
    ("Vite", "Vite", "#646CFF", "#fff"),
    ("npm", "npm", "#CB3837", "#fff"),
    ("VSC", "VS Code", "#007ACC", "#fff"),
    ("PostgreSQL", "Postgres", "#4169E1", "#fff"),
    ("Prisma", "Prisma", "#2D3748", "#fff"),
    ("TypeScript", "TS", "#3178C6", "#fff"),
    ("CI/CD", "CI/CD", "#2088FF", "#fff"),
    ("MySQL", "MySQL", "#4479A1", "#fff"),
]
# ---------------------------------------------------------------------------

W, H = 1200, 640
FONT = "Tahoma, Verdana, 'Segoe UI', Arial, sans-serif"


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def avatar_markup(path: str | None) -> str:
    """Contenido dentro del marco del avatar (70x70 -> interior 58x58)."""
    if path:
        mime = mimetypes.guess_type(path)[0] or "image/png"
        b64 = base64.b64encode(Path(path).read_bytes()).decode()
        return (
            f'<image x="0" y="0" width="58" height="58" '
            f'preserveAspectRatio="xMidYMid slice" '
            f'href="data:{mime};base64,{b64}" clip-path="url(#avClip)"/>'
        )
    # placeholder: silueta
    return (
        '<rect width="58" height="58" fill="#dbe9fb"/>'
        '<circle cx="29" cy="22" r="11" fill="#7aa7e0"/>'
        '<path d="M6 58 C8 40 20 36 29 36 C38 36 50 40 52 58 Z" fill="#7aa7e0"/>'
    )


def flag_paths(tx=0, ty=0, s=1.0) -> str:
    return (
        f'<g transform="translate({tx} {ty}) scale({s})">'
        '<path d="M12 18 C 30 14, 42 28, 48 26 L 48 50 C 42 51, 28 38, 12 42 Z" fill="#eb3c00"/>'
        '<path d="M54 26 C 66 23, 78 30, 92 24 L 92 48 C 76 53, 66 48, 54 50 Z" fill="#4fa800"/>'
        '<path d="M12 46 C 28 42, 42 55, 48 54 L 48 78 C 42 79, 30 66, 12 70 Z" fill="#0080ff"/>'
        '<path d="M54 54 C 66 52, 78 57, 92 52 L 92 76 C 78 81, 66 76, 54 78 Z" fill="#ffb900"/>'
        "</g>"
    )


def folder_grid() -> str:
    out = []
    cols, x0, y0 = 5, 14, 88
    cw, rh = 104.8, 96
    n = len(TECH)
    cycle = n * 1.4
    for i, (name, badge, bg, fg) in enumerate(TECH):
        r, c = divmod(i, cols)
        cx = x0 + c * cw + cw / 2
        top = y0 + r * rh
        bw = max(30, len(badge) * 6 + 10)
        out.append(
            f'<g transform="translate({cx:.1f} {top})">'
            # resaltado animado (como el hover de XP)
            f'<rect class="sel" x="-44" y="0" width="88" height="82" rx="4" '
            f'fill="#eef3fa" stroke="#b6d0f6" style="animation-delay:{i*1.4:.1f}s;'
            f'animation-duration:{cycle:.1f}s"/>'
            '<use href="#folder" x="-29" y="6"/>'
            f'<rect x="{-bw/2:.1f}" y="40" width="{bw}" height="13" rx="3" fill="{bg}" '
            'stroke="rgba(0,0,0,.35)" stroke-width=".6"/>'
            f'<text x="0" y="49.8" text-anchor="middle" font-size="9" font-weight="700" '
            f'fill="{fg}">{esc(badge)}</text>'
            f'<text x="0" y="72" text-anchor="middle" font-size="11" fill="#000">{esc(name)}</text>'
            "</g>"
        )
    return "\n".join(out)


def build(avatar_path: str | None) -> str:
    SEL_PCT = 100 / len(TECH)
    left_cx = 300
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">
<title>BlurTrace - Windows XP profile</title>
<defs>
  <style>
    .sel{{opacity:0;animation-name:sel;animation-iteration-count:infinite;animation-timing-function:steps(1,end)}}
    @keyframes sel{{0%{{opacity:1}}{SEL_PCT:.2f}%{{opacity:0}}100%{{opacity:0}}}}
    .pulse{{animation:pulse 2.4s ease-in-out infinite}}
    @keyframes pulse{{0%,100%{{opacity:.25}}50%{{opacity:1}}}}
    .stripes{{animation:slide 1.2s linear infinite}}
    @keyframes slide{{to{{transform:translate(17px,0)}}}}
  </style>

  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1f5fd6"/><stop offset=".6" stop-color="#6aa8f5"/><stop offset="1" stop-color="#bcdcff"/>
  </linearGradient>
  <linearGradient id="hill" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#6fc23a"/><stop offset="1" stop-color="#2f7d17"/>
  </linearGradient>
  <radialGradient id="logon" cx=".18" cy=".38" r=".9">
    <stop offset="0" stop-color="#5a91ed"/><stop offset=".55" stop-color="#1545aa"/><stop offset="1" stop-color="#082987"/>
  </radialGradient>
  <linearGradient id="barTop" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#092c74"/><stop offset="1" stop-color="#00194e"/></linearGradient>
  <linearGradient id="barBot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#092c74"/><stop offset="1" stop-color="#01143c"/></linearGradient>
  <linearGradient id="divider" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".3" stop-color="#fff" stop-opacity=".7"/>
    <stop offset=".7" stop-color="#fff" stop-opacity=".7"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="avFrame" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1aa3e8"/><stop offset="1" stop-color="#0550c6"/></linearGradient>
  <linearGradient id="power" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e63920"/><stop offset="1" stop-color="#a41906"/></linearGradient>
  <linearGradient id="title" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0058ee"/><stop offset=".12" stop-color="#3593ff"/><stop offset=".2" stop-color="#126dff"/>
    <stop offset=".4" stop-color="#034fe4"/><stop offset=".85" stop-color="#004fe4"/><stop offset="1" stop-color="#002e9a"/>
  </linearGradient>
  <linearGradient id="btnBlue" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b70f0"/><stop offset="1" stop-color="#1545aa"/></linearGradient>
  <linearGradient id="btnRed" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e36a52"/><stop offset="1" stop-color="#ba290f"/></linearGradient>
  <linearGradient id="fBack" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe680"/><stop offset="1" stop-color="#f2b41c"/></linearGradient>
  <linearGradient id="fFront" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff2aa"/><stop offset="1" stop-color="#f8be22"/></linearGradient>
  <linearGradient id="taskbar" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1f2f86"/><stop offset=".1" stop-color="#3168d5"/><stop offset=".4" stop-color="#2456c3"/>
    <stop offset=".8" stop-color="#1e45a9"/><stop offset="1" stop-color="#17368a"/>
  </linearGradient>
  <linearGradient id="startBtn" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#388e3c"/><stop offset=".15" stop-color="#43a047"/><stop offset=".8" stop-color="#2e7d32"/><stop offset="1" stop-color="#1b5e20"/>
  </linearGradient>
  <linearGradient id="tray" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0d9ff4"/><stop offset=".15" stop-color="#086bb9"/><stop offset="1" stop-color="#0d5a9d"/>
  </linearGradient>
  <linearGradient id="task" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3c82f0"/><stop offset="1" stop-color="#1c52b8"/></linearGradient>
  <pattern id="warn" width="17" height="17" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">
    <rect width="8.5" height="17" fill="#f5b300"/><rect x="8.5" width="8.5" height="17" fill="#2b2b2b"/>
  </pattern>

  <clipPath id="avClip"><rect width="58" height="58" rx="6"/></clipPath>
  <filter id="shadow" x="-10%" y="-10%" width="120%" height="125%"><feDropShadow dx="4" dy="6" stdDeviation="7" flood-color="#000" flood-opacity=".55"/></filter>
  <filter id="tshadow" x="-10%" y="-30%" width="120%" height="170%"><feDropShadow dx="1" dy="2" stdDeviation="1.5" flood-color="#000" flood-opacity=".7"/></filter>

  <!-- Icono de carpeta XP reutilizable (58x47) -->
  <g id="folder" transform="scale(.725)">
    <path d="M4 10 L26 10 L34 18 L74 18 A4 4 0 0 1 78 22 L78 58 A4 4 0 0 1 74 62 L4 62 A4 4 0 0 1 0 58 L0 14 A4 4 0 0 1 4 10 Z" fill="url(#fBack)" stroke="#bd8a0a" stroke-width="1.2"/>
    <path d="M0 24 L78 24 L74 60 A4 4 0 0 1 70 64 L6 64 A4 4 0 0 1 2 60 Z" fill="url(#fFront)" stroke="#c69512" stroke-width="1"/>
  </g>
</defs>

<!-- ============ FONDO (Bliss en vectores) ============ -->
<rect width="{W}" height="604" fill="url(#sky)"/>
<ellipse cx="900" cy="90" rx="150" ry="28" fill="#fff" opacity=".55"/>
<ellipse cx="1010" cy="115" rx="120" ry="22" fill="#fff" opacity=".45"/>
<ellipse cx="760" cy="140" rx="90" ry="16" fill="#fff" opacity=".4"/>
<path d="M0 470 C 250 380, 520 360, 760 410 C 940 445, 1080 420, 1200 380 L1200 604 L0 604 Z" fill="url(#hill)"/>
<path d="M0 540 C 300 480, 600 500, 1200 470 L1200 604 L0 604 Z" fill="#2c7314" opacity=".55"/>

<!-- ============ LADO IZQUIERDO: LOGON ============ -->
<rect x="0" y="0" width="600" height="604" fill="url(#logon)"/>
<rect x="0" y="0" width="600" height="52" fill="url(#barTop)"/>
<rect x="0" y="50" width="600" height="2" fill="#ef6900"/>
<rect x="0" y="540" width="600" height="64" fill="url(#barBot)"/>
<rect x="0" y="540" width="600" height="2" fill="#ef6900"/>
<rect x="598" y="0" width="2" height="604" fill="#ff9900"/>

<rect x="{left_cx}" y="130" width="1" height="330" fill="url(#divider)"/>

<!-- Marca -->
<g filter="url(#tshadow)">{flag_paths(212, 184, .6)}</g>
<g filter="url(#tshadow)" text-anchor="end">
  <text x="272" y="266" fill="#fff" font-size="14" font-style="italic">Microsoft</text>
  <text x="236" y="296" fill="#fff" font-size="32" font-weight="700">Windows</text>
  <text x="274" y="296" fill="#ff6a00" font-size="26" font-weight="700" font-style="italic">xp</text>
</g>
<text x="272" y="322" text-anchor="end" fill="#d1e2fc" font-size="15" filter="url(#tshadow)">To begin, click your user name</text>

<!-- Tarjeta de usuario -->
<rect x="318" y="252" width="272" height="90" rx="10" fill="#1246b4" fill-opacity=".85"/>
<rect class="pulse" x="318" y="252" width="272" height="90" rx="10" fill="none" stroke="#27c4fe" stroke-width="2"/>
<g transform="translate(330 262)">
  <rect width="70" height="70" rx="10" fill="url(#avFrame)" stroke="#57adff" stroke-width="2"/>
  <rect x="3" y="3" width="64" height="64" rx="8" fill="#fff" stroke="#ffaf02" stroke-width="2"/>
  <g transform="translate(6 6)">{avatar_markup(avatar_path)}</g>
</g>
<g filter="url(#tshadow)" fill="#fff">
  <text x="412" y="276" font-size="15" font-weight="700">{esc(FULL_NAME_LINES[0])}</text>
  <text x="412" y="293" font-size="15" font-weight="700">{esc(FULL_NAME_LINES[1])}</text>
</g>
<text x="412" y="310" font-size="12" font-weight="700" fill="#e2eeff">{esc(USERNAME)}</text>
<text x="412" y="324" font-size="10" fill="#9eccff">{esc(SUBTITLE_LINES[0])}</text>
<text x="412" y="336" font-size="10" fill="#9eccff">{esc(SUBTITLE_LINES[1])}</text>
<!-- bandera de Colombia -->
<g transform="translate(486 328)">
  <rect width="16" height="10" fill="#fcd116"/><rect y="5" width="16" height="2.5" fill="#003893"/><rect y="7.5" width="16" height="2.5" fill="#ce1126"/>
</g>

<!-- Barra inferior del logon -->
<g transform="translate(28 556)">
  <rect width="28" height="28" rx="5" fill="url(#power)" stroke="#ff7b63"/>
  <path d="M14 6 V15 M8.8 9 A8 8 0 1 0 19.2 9" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
</g>
<text x="66" y="575" fill="#fff" font-size="13">Turn off computer</text>
<text x="572" y="565" text-anchor="end" fill="#9cbfe8" font-size="10">After you log on, you can add or change accounts.</text>
<text x="572" y="579" text-anchor="end" fill="#9cbfe8" font-size="10">Just go to Control Panel and click User Accounts.</text>

<!-- ============ LADO DERECHO: EXPLORER ============ -->
<g transform="translate(624 22)" filter="url(#shadow)">
  <rect width="552" height="560" rx="8" fill="#fbfbf7" stroke="#0055ea" stroke-width="3"/>
</g>
<g transform="translate(624 22)">
  <!-- Barra de título -->
  <path d="M0 8 A8 8 0 0 1 8 0 H544 A8 8 0 0 1 552 8 V30 H0 Z" fill="url(#title)"/>
  <path d="M8 8 L14 8 L16 10 L24 10 A1.5 1.5 0 0 1 25.5 11.5 V20 A1.5 1.5 0 0 1 24 21.5 H9.5 A1.5 1.5 0 0 1 8 20 Z" fill="#ffcc00"/>
  <text x="32" y="19.5" fill="#fff" font-size="12" font-weight="700" filter="url(#tshadow)">{esc(EXPLORER_TITLE)}</text>
  <g transform="translate(468 4)">
    <rect width="21" height="21" rx="3" fill="url(#btnBlue)" stroke="#fff"/><rect x="6" y="14" width="9" height="2.4" fill="#fff"/>
    <g transform="translate(24 0)"><rect width="21" height="21" rx="3" fill="url(#btnBlue)" stroke="#fff"/><rect x="5.5" y="5.5" width="10" height="10" fill="none" stroke="#fff" stroke-width="1.8"/></g>
    <g transform="translate(48 0)"><rect width="21" height="21" rx="3" fill="url(#btnRed)" stroke="#fff"/><path d="M6 6 L15 15 M15 6 L6 15" stroke="#fff" stroke-width="2" stroke-linecap="round"/></g>
  </g>

  <!-- Barra de menús -->
  <rect y="30" width="552" height="22" fill="#ece9d8"/><rect y="51" width="552" height="1" fill="#d4cfbe"/>
  <g font-size="11" fill="#000"><text x="10" y="45">File</text><text x="42" y="45">Edit</text><text x="76" y="45">View</text><text x="114" y="45">Favorites</text><text x="170" y="45">Help</text></g>
  <g transform="translate(526 33)"><rect width="8" height="8" fill="#e73827"/><rect x="10" width="8" height="8" fill="#7ac142"/><rect y="10" width="8" height="8" fill="#00a4ef"/><rect x="10" y="10" width="8" height="8" fill="#ffba08"/></g>

  <!-- Barra de dirección -->
  <rect y="52" width="552" height="24" fill="#ece9d8"/><rect y="75" width="552" height="1" fill="#d4cfbe"/>
  <text x="10" y="68" font-size="11" fill="#555">Address</text>
  <rect x="58" y="55" width="484" height="18" fill="#fff" stroke="#7f9db9"/>
  <text x="66" y="68" font-size="11" fill="#000">C:\\Tech Stack</text>

  <!-- Cuerpo -->
  <rect y="76" width="552" height="460" fill="#fff"/>
  {folder_grid()}

  <!-- Fila inferior -->
  <line x1="14" y1="388" x2="538" y2="388" stroke="#ccc" stroke-dasharray="1 2"/>

  <g transform="translate(14 400)">
    <rect width="252" height="100" rx="6" fill="#fffdf2" stroke="#ffcc00"/>
    <g transform="translate(10 18)">
      <path d="M4 6 L22 6 L28 13 L58 13 A3 3 0 0 1 61 16 L61 44 A3 3 0 0 1 58 47 L4 47 A3 3 0 0 1 1 44 L1 9 A3 3 0 0 1 4 6 Z" fill="#ffd451" stroke="#c99718" stroke-width="1.2"/>
      <clipPath id="stripeClip"><rect x="5" y="20" width="52" height="24" rx="2"/></clipPath>
      <g clip-path="url(#stripeClip)"><g class="stripes"><rect x="-20" y="14" width="100" height="40" fill="url(#warn)"/></g></g>
      <rect x="5" y="20" width="52" height="24" rx="2" fill="none" stroke="#735100"/>
    </g>
    <text x="84" y="40" font-size="13" font-weight="700" fill="#000">Currently exploring</text>
    <text x="84" y="58" font-size="10" fill="#666">{esc(EXPLORING[0])}</text>
    <text x="84" y="71" font-size="10" fill="#666">{esc(EXPLORING[1])}</text>
  </g>

  <g transform="translate(284 400)">
    <text x="0" y="12" font-size="13" font-weight="700" fill="#111">Let's Connect!</text>
    <!-- email -->
    <g transform="translate(0 24)">
      <rect width="22" height="22" rx="4" fill="#3b82f6"/>
      <rect x="4.5" y="6.5" width="13" height="9" rx="1" fill="none" stroke="#fff" stroke-width="1.5"/><path d="M5 7.5 L11 12.5 L17 7.5" fill="none" stroke="#fff" stroke-width="1.5"/>
      <text x="30" y="15" font-size="11" fill="#000"><tspan font-weight="700">Email</tspan>: {esc(EMAIL)}</text>
    </g>
    <!-- teléfono -->
    <g transform="translate(0 52)">
      <rect width="22" height="22" rx="4" fill="#22c55e"/>
      <rect x="7.5" y="4" width="7" height="14" rx="1.5" fill="none" stroke="#fff" stroke-width="1.5"/><circle cx="11" cy="15.3" r=".9" fill="#fff"/>
      <text x="30" y="15" font-size="11" fill="#000"><tspan font-weight="700">Business Number</tspan>: {esc(PHONE)}</text>
    </g>
    <!-- instagram -->
    <g transform="translate(0 80)">
      <rect width="22" height="22" rx="4" fill="#dd2a7b"/>
      <rect x="4.5" y="4.5" width="13" height="13" rx="4" fill="none" stroke="#fff" stroke-width="1.5"/><circle cx="11" cy="11" r="3" fill="none" stroke="#fff" stroke-width="1.5"/><circle cx="14.7" cy="7.3" r=".9" fill="#fff"/>
      <text x="30" y="15" font-size="11" fill="#000"><tspan font-weight="700">Instagram</tspan>: {esc(INSTAGRAM)}</text>
    </g>
  </g>

  <!-- Barra de estado -->
  <rect y="536" width="552" height="24" fill="#ece9d8"/><rect y="536" width="552" height="1" fill="#d4cfbe"/>
  <text x="10" y="552" font-size="11" fill="#000">{len(TECH)} object(s)</text>
  <text x="542" y="552" text-anchor="end" font-size="11" fill="#000">My Computer</text>
</g>

<!-- ============ BARRA DE TAREAS ============ -->
<rect y="604" width="{W}" height="36" fill="url(#taskbar)"/><rect y="604" width="{W}" height="1" fill="#3c7bf6"/>
<path d="M0 604 H96 A14 18 0 0 1 96 640 H0 Z" fill="url(#startBtn)"/>
{flag_paths(14, 611, .22)}
<text x="42" y="628" fill="#fff" font-size="15" font-style="italic" font-weight="700" filter="url(#tshadow)">start</text>
<g transform="translate(118 608)">
  <rect width="170" height="28" rx="3" fill="url(#task)" stroke="#143e8c"/>
  <g transform="translate(8 7)"><path d="M0 2 H5 L7 4 H14 V13 H0 Z" fill="#ffcc00" stroke="#c99718" stroke-width=".6"/></g>
  <text x="30" y="18" fill="#fff" font-size="12">C:\\Tech Stack</text>
</g>
<rect x="1056" y="604" width="144" height="36" fill="url(#tray)"/><rect x="1056" y="604" width="1" height="36" fill="#13467c"/>
<g fill="#fff"><path d="M1074 618 h4 l5 -4 v16 l-5 -4 h-4 Z"/><path d="M1087 616 q4 6 0 12" fill="none" stroke="#fff" stroke-width="1.4"/></g>
<path d="M1106 614 l8 3 v7 q0 5 -8 8 q-8 -3 -8 -8 v-7 Z" fill="#fff" opacity=".9" transform="translate(-4 0)"/>
<text x="1186" y="626" text-anchor="end" fill="#fff" font-size="11">{CLOCK}</text>
</svg>
"""
    return svg


if __name__ == "__main__":
    avatar = sys.argv[1] if len(sys.argv) > 1 else None
    out = Path(__file__).parent / "assets" / "xp-profile.svg"
    out.parent.mkdir(exist_ok=True)
    out.write_text(build(avatar), encoding="utf-8")
    print(f"OK -> {out}  ({out.stat().st_size/1024:.1f} KB)")
