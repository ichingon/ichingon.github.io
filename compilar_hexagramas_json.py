import os
import re
import json
import yaml
from pathlib import Path

CONTENT_DIR = Path("content/hexagramas")
OUTPUT_DIR = Path("static/data")

LANG_CONFIG = {
    "es": {
        "files": ["_index.md", "index.md"],
        "url_prefix": "https://elichingon.com/hexagramas"
    },
    "en": {
        "files": ["_index.en.md", "index.en.md"],
        "url_prefix": "https://elichingon.com/en/hexagrams"
    },
    "de": {
        "files": ["_index.de.md", "index.de.md"],
        "url_prefix": "https://elichingon.com/de/hexagramme"
    }
}

HEX_CANONICAL = {
    1: {"hanzi": "乾", "pinyin": "Qián", "binary": "111111", "above": "Qián", "below": "Qián"},
    2: {"hanzi": "坤", "pinyin": "Kūn", "binary": "000000", "above": "Kūn", "below": "Kūn"},
    3: {"hanzi": "屯", "pinyin": "Zhūn", "binary": "100010", "above": "Kǎn", "below": "Zhèn"},
    4: {"hanzi": "蒙", "pinyin": "Méng", "binary": "010001", "above": "Gèn", "below": "Kǎn"},
    5: {"hanzi": "需", "pinyin": "Xū", "binary": "111010", "above": "Kǎn", "below": "Qián"},
    6: {"hanzi": "訟", "pinyin": "Sòng", "binary": "010111", "above": "Qián", "below": "Kǎn"},
    7: {"hanzi": "師", "pinyin": "Shī", "binary": "010000", "above": "Kūn", "below": "Kǎn"},
    8: {"hanzi": "比", "pinyin": "Bǐ", "binary": "000010", "above": "Kǎn", "below": "Kūn"},
    9: {"hanzi": "小畜", "pinyin": "Xiǎo Chù", "binary": "111011", "above": "Xùn", "below": "Qián"},
    10: {"hanzi": "履", "pinyin": "Lǚ", "binary": "110111", "above": "Qián", "below": "Duì"},
    11: {"hanzi": "泰", "pinyin": "Tài", "binary": "111000", "above": "Kūn", "below": "Qián"},
    12: {"hanzi": "否", "pinyin": "Pǐ", "binary": "000111", "above": "Qián", "below": "Kūn"},
    13: {"hanzi": "同人", "pinyin": "Tóng Rén", "binary": "101111", "above": "Qián", "below": "Lí"},
    14: {"hanzi": "大有", "pinyin": "Dà Yǒu", "binary": "111101", "above": "Lí", "below": "Qián"},
    15: {"hanzi": "謙", "pinyin": "Qiān", "binary": "001000", "above": "Kūn", "below": "Gèn"},
    16: {"hanzi": "豫", "pinyin": "Yù", "binary": "000100", "above": "Zhèn", "below": "Kūn"},
    17: {"hanzi": "隨", "pinyin": "Suí", "binary": "100110", "above": "Duì", "below": "Zhèn"},
    18: {"hanzi": "蠱", "pinyin": "Gǔ", "binary": "011001", "above": "Gèn", "below": "Xùn"},
    19: {"hanzi": "臨", "pinyin": "Lín", "binary": "110000", "above": "Kūn", "below": "Duì"},
    20: {"hanzi": "觀", "pinyin": "Guān", "binary": "000011", "above": "Xùn", "below": "Kūn"},
    21: {"hanzi": "噬嗑", "pinyin": "Shì Kè", "binary": "100101", "above": "Lí", "below": "Zhèn"},
    22: {"hanzi": "賁", "pinyin": "Bì", "binary": "101001", "above": "Gèn", "below": "Lí"},
    23: {"hanzi": "剝", "pinyin": "Bō", "binary": "000001", "above": "Gèn", "below": "Kūn"},
    24: {"hanzi": "復", "pinyin": "Fù", "binary": "100000", "above": "Kūn", "below": "Zhèn"},
    25: {"hanzi": "無妄", "pinyin": "Wú Wàng", "binary": "100111", "above": "Qián", "below": "Zhèn"},
    26: {"hanzi": "大畜", "pinyin": "Dà Chù", "binary": "111001", "above": "Gèn", "below": "Qián"},
    27: {"hanzi": "頤", "pinyin": "Yí", "binary": "100001", "above": "Gèn", "below": "Zhèn"},
    28: {"hanzi": "大過", "pinyin": "Dà Guò", "binary": "011110", "above": "Duì", "below": "Xùn"},
    29: {"hanzi": "坎", "pinyin": "Kǎn", "binary": "010010", "above": "Kǎn", "below": "Kǎn"},
    30: {"hanzi": "離", "pinyin": "Lí", "binary": "101101", "above": "Lí", "below": "Lí"},
    31: {"hanzi": "咸", "pinyin": "Xián", "binary": "001110", "above": "Duì", "below": "Gèn"},
    32: {"hanzi": "恆", "pinyin": "Héng", "binary": "011100", "above": "Zhèn", "below": "Xùn"},
    33: {"hanzi": "遯", "pinyin": "Dùn", "binary": "001111", "above": "Qián", "below": "Gèn"},
    34: {"hanzi": "大壯", "pinyin": "Dà Zhuàng", "binary": "111100", "above": "Zhèn", "below": "Qián"},
    35: {"hanzi": "晉", "pinyin": "Jìn", "binary": "000101", "above": "Lí", "below": "Kūn"},
    36: {"hanzi": "明夷", "pinyin": "Míng Yí", "binary": "101000", "above": "Kūn", "below": "Lí"},
    37: {"hanzi": "家人", "pinyin": "Jiā Rén", "binary": "101011", "above": "Xùn", "below": "Lí"},
    38: {"hanzi": "睽", "pinyin": "Kuí", "binary": "110101", "above": "Lí", "below": "Duì"},
    39: {"hanzi": "蹇", "pinyin": "Jiǎn", "binary": "001010", "above": "Kǎn", "below": "Gèn"},
    40: {"hanzi": "解", "pinyin": "Xiè", "binary": "010100", "above": "Zhèn", "below": "Kǎn"},
    41: {"hanzi": "損", "pinyin": "Sǔn", "binary": "110001", "above": "Gèn", "below": "Duì"},
    42: {"hanzi": "益", "pinyin": "Yì", "binary": "100011", "above": "Xùn", "below": "Zhèn"},
    43: {"hanzi": "夬", "pinyin": "Guài", "binary": "111110", "above": "Duì", "below": "Qián"},
    44: {"hanzi": "姤", "pinyin": "Gòu", "binary": "011111", "above": "Qián", "below": "Xùn"},
    45: {"hanzi": "萃", "pinyin": "Cuì", "binary": "000110", "above": "Duì", "below": "Kūn"},
    46: {"hanzi": "升", "pinyin": "Shēng", "binary": "011000", "above": "Kūn", "below": "Xùn"},
    47: {"hanzi": "困", "pinyin": "Kùn", "binary": "010110", "above": "Duì", "below": "Kǎn"},
    48: {"hanzi": "井", "pinyin": "Jǐng", "binary": "011010", "above": "Kǎn", "below": "Xùn"},
    49: {"hanzi": "革", "pinyin": "Gé", "binary": "101110", "above": "Duì", "below": "Lí"},
    50: {"hanzi": "鼎", "pinyin": "Dǐng", "binary": "011101", "above": "Lí", "below": "Xùn"},
    51: {"hanzi": "震", "pinyin": "Zhèn", "binary": "100100", "above": "Zhèn", "below": "Zhèn"},
    52: {"hanzi": "艮", "pinyin": "Gèn", "binary": "001001", "above": "Gèn", "below": "Gèn"},
    53: {"hanzi": "漸", "pinyin": "Jiàn", "binary": "001011", "above": "Xùn", "below": "Gèn"},
    54: {"hanzi": "歸妹", "pinyin": "Guī Mèi", "binary": "110100", "above": "Zhèn", "below": "Duì"},
    55: {"hanzi": "豐", "pinyin": "Fēng", "binary": "101100", "above": "Zhèn", "below": "Lí"},
    56: {"hanzi": "旅", "pinyin": "Lǚ", "binary": "001101", "above": "Lí", "below": "Gèn"},
    57: {"hanzi": "巽", "pinyin": "Xùn", "binary": "011011", "above": "Xùn", "below": "Xùn"},
    58: {"hanzi": "兌", "pinyin": "Duì", "binary": "110110", "above": "Duì", "below": "Duì"},
    59: {"hanzi": "渙", "pinyin": "Huàn", "binary": "010011", "above": "Xùn", "below": "Kǎn"},
    60: {"hanzi": "節", "pinyin": "Jié", "binary": "110010", "above": "Kǎn", "below": "Duì"},
    61: {"hanzi": "中孚", "pinyin": "Zhōng Fú", "binary": "110011", "above": "Xùn", "below": "Duì"},
    62: {"hanzi": "小過", "pinyin": "Xiǎo Guò", "binary": "001100", "above": "Zhèn", "below": "Gèn"},
    63: {"hanzi": "既濟", "pinyin": "Jì Jì", "binary": "101010", "above": "Kǎn", "below": "Lí"},
    64: {"hanzi": "未濟", "pinyin": "Wèi Jì", "binary": "010101", "above": "Lí", "below": "Kǎn"}
}

TRIGRAM_META = {
    "Qián": {"glyph": "☰", "es": "Cielo", "en": "Heaven", "de": "Himmel"},
    "Kūn":  {"glyph": "☷", "es": "Tierra", "en": "Earth", "de": "Erde"},
    "Zhèn": {"glyph": "☳", "es": "Trueno", "en": "Thunder", "de": "Donner"},
    "Kǎn":  {"glyph": "☵", "es": "Agua", "en": "Water", "de": "Wasser"},
    "Gèn":  {"glyph": "☶", "es": "Montaña", "en": "Mountain", "de": "Berg"},
    "Xùn":  {"glyph": "☴", "es": "Viento / Madera", "en": "Wind / Wood", "de": "Wind / Holz"},
    "Lí":   {"glyph": "☲", "es": "Fuego", "en": "Fire", "de": "Feuer"},
    "Duì":  {"glyph": "☱", "es": "Lago", "en": "Lake", "de": "See"}
}

def clean_markdown_text(text):
    if not text:
        return ""
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # 1. Reemplazar SVG de la torre por ⛩
    text = re.sub(r'<svg\b[^>]*>.*?</svg>', '⛩', text, flags=re.DOTALL)
    
    # 2. Remover etiquetas HTML generales
    text = re.sub(r'<p\b[^>]*>.*?</p>', '', text, flags=re.DOTALL)
    text = re.sub(r'</?[a-zA-Z0-9_-]+[^>]*>', '', text)
    
    # 3. Remover tooltips manteniendo su texto interior[cite: 8]
    text = re.sub(r'\{\{<\s*tooltip\s+[^>]*>\}\}(.*?)\{\{<\s*/tooltip\s*>\}\}', r'\1', text, flags=re.DOTALL)
    
    # 4. Remover shortcodes y notas al pie por completo[cite: 6, 7, 8]
    text = re.sub(r'\{\{<[^>]+>\}\}', '', text)
    text = re.sub(r'\[\^\d+\]:?.*', '', text)
    
    # 5. Remover enlaces markdown [Texto](url) -> Texto
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # 6. Remover prefijos de blockquote '>' y sangrías de citas poéticas[cite: 8]
    text = re.sub(r'^[ \t]*>[ \t]?', '', text, flags=re.MULTILINE)
    
    # 7. Remover formato Markdown inline
    text = re.sub(r'\*{2,}(.*?)\*{2,}', r'\1', text)
    text = re.sub(r'_{2,}(.*?)_{2,}', r'\1', text)
    text = re.sub(r'\*([^*\n]+)\*', r'\1', text)
    text = re.sub(r'_([^_\n]+)_', r'\1', text)
    text = re.sub(r'`([^`\n]+)`', r'\1', text)
    text = re.sub(r'~~(.*?)~~', r'\1', text)
    
    # 8. Remover separadores horizontales (---, ***, ___)[cite: 8]
    text = re.sub(r'^[ \t]*[-*_]{3,}[ \t]*$', '', text, flags=re.MULTILINE)
    
    # 9. Normalizar saltos de línea
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def extract_quote_and_commentary(section_body):
    lines = section_body.replace('\r\n', '\n').splitlines()
    quote_lines = []
    commentary_lines = []
    in_quote = True

    for line in lines:
        stripped = line.strip()
        if in_quote:
            if stripped.startswith(">"):
                quote_lines.append(re.sub(r"^>\s*", "", stripped))
            elif not stripped and not quote_lines:
                continue
            else:
                in_quote = False
                commentary_lines.append(line)
        else:
            commentary_lines.append(line)

    raw_quote = clean_markdown_text(" ".join(quote_lines).strip())
    raw_commentary = clean_markdown_text("\n".join(commentary_lines).strip())

    if not raw_quote and raw_commentary:
        parts = raw_commentary.split("\n\n", 1)
        raw_quote = parts[0].strip()
        raw_commentary = parts[1].strip() if len(parts) > 1 else ""

    return {
        "text": raw_quote,
        "commentary": raw_commentary
    }

def parse_hexagram_md(file_path, hex_number, lang):
    with open(file_path, "r", encoding="utf-8") as f:
        raw_content = f.read().replace('\r\n', '\n').replace('\r', '\n')

    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw_content, re.DOTALL)
    if not fm_match:
        return None

    yaml_str, body = fm_match.groups()
    try:
        frontmatter = yaml.safe_load(yaml_str) or {}
    except Exception:
        frontmatter = {}

    # Descartar enlaces de pie y bloque Nostr[cite: 10]
    body = re.split(r'\n#{2,4}\s+(?:Enlaces de Consulta|Reference links|Referenzlinks)', body, flags=re.IGNORECASE)[0]
    body = re.split(r'\n\*\*🔐\s+VERIFICACIÓN', body, flags=re.IGNORECASE)[0]

    yt_match = re.search(r'\{\{<\s*youtube-short\s+"([^"]+)"', body)
    youtube_id = yt_match.group(1) if yt_match else ""

    # Trigramas descriptivos[cite: 10]
    tri_above_raw = ""
    tri_below_raw = ""
    tri_above_match = re.search(r'\*\s*(?:\*\*Arriba:\*\*|Above:|oben)\s*(.*)', body, re.IGNORECASE)
    tri_below_match = re.search(r'\*\s*(?:\*\*Abajo:\*\*|Below:|unten)\s*(.*)', body, re.IGNORECASE)
    if tri_above_match:
        tri_above_raw = clean_markdown_text(tri_above_match.group(1))
    if tri_below_match:
        tri_below_raw = clean_markdown_text(tri_below_match.group(1))

    # Segmentación de secciones[cite: 10]
    dictamen_split = re.split(r'\n#{2,4}\s+(?:El Dictamen|The Judgment|The Judgement|Das Urteil).*?\n', body, flags=re.IGNORECASE)
    intro_raw = dictamen_split[0] if len(dictamen_split) > 1 else ""
    rest_after_dict = dictamen_split[1] if len(dictamen_split) > 1 else body

    imagen_split = re.split(r'\n#{2,4}\s+(?:La Imagen|The Image|Das Bild).*?\n', rest_after_dict, flags=re.IGNORECASE)
    dictamen_raw = imagen_split[0] if len(imagen_split) > 1 else ""
    rest_after_img = imagen_split[1] if len(imagen_split) > 1 else ""

    lineas_split = re.split(r'\n#{2,4}\s+.*?(?:Líneas|Lines|Linien).*?\n', rest_after_img, flags=re.IGNORECASE)
    imagen_raw = lineas_split[0] if len(lineas_split) > 1 else rest_after_img
    lines_body = lineas_split[1] if len(lineas_split) > 1 else ""

    # Limpieza de Intro[cite: 10]
    intro_cleaned = re.sub(r'#{2,3}\s*Trigram[a-z]*.*?\n\n', '', intro_raw, flags=re.DOTALL | re.IGNORECASE)
    intro_text = clean_markdown_text(intro_cleaned)

    # Extracción de Dictamen e Imagen[cite: 10]
    dictamen_data = extract_quote_and_commentary(dictamen_raw)
    imagen_data = extract_quote_and_commentary(imagen_raw)

    # Extracción de Líneas[cite: 10]
    subsections = re.split(r'\n#{3,4}\s+', "\n" + lines_body)
    lineas_dict = {}
    valid_subsections = [s.strip() for s in subsections if s.strip()]

    for idx, sec in enumerate(valid_subsections, start=1):
        lines_in_sec = sec.splitlines()
        header = clean_markdown_text(lines_in_sec[0].strip())
        content = "\n".join(lines_in_sec[1:]).strip()

        line_key = str(idx) if idx <= 6 else "all"

        extracted = extract_quote_and_commentary(content)
        extracted["title"] = header
        lineas_dict[line_key] = extracted

    canon = HEX_CANONICAL.get(hex_number, {})
    unicode_code = 0x4DC0 + (hex_number - 1)
    unicode_glyph = chr(unicode_code)
    unicode_hex = f"{unicode_code:04X}"

    above_key = canon.get("above", "Qián")
    below_key = canon.get("below", "Qián")
    above_meta = TRIGRAM_META.get(above_key, {})
    below_meta = TRIGRAM_META.get(below_key, {})

    raw_title = frontmatter.get("title", "")
    name_cleaned = raw_title
    if "/" in raw_title:
        name_cleaned = raw_title.split("/")[-1].strip()
    elif "-" in raw_title:
        name_cleaned = raw_title.split("-")[-1].strip()

    url_prefix = LANG_CONFIG.get(lang, {}).get("url_prefix", "https://elichingon.com/hexagramas")
    hex_url = f"{url_prefix}/hex{hex_number:02d}/"

    return {
        "id": hex_number,
        "url": hex_url,
        "binary": canon.get("binary", ""),
        "unicode_glyph": unicode_glyph,
        "unicode_hex": unicode_hex,
        "hanzi": canon.get("hanzi", ""),
        "pinyin": canon.get("pinyin", ""),
        "name": name_cleaned,
        "title": raw_title,
        "description": frontmatter.get("description", ""),
        "youtube_id": youtube_id,
        "trigrams": {
            "above": {
                "pinyin": above_key,
                "element": above_meta.get(lang, above_key),
                "glyph": above_meta.get("glyph", ""),
                "text": tri_above_raw
            },
            "below": {
                "pinyin": below_key,
                "element": below_meta.get(lang, below_key),
                "glyph": below_meta.get("glyph", ""),
                "text": tri_below_raw
            }
        },
        "intro": intro_text,
        "dictamen": dictamen_data,
        "imagen": imagen_data,
        "lines": lineas_dict
    }

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for lang, config in LANG_CONFIG.items():
        compiled_hexes = {}
        candidates = config["files"]
        print(f"Procesando idioma '{lang}'...")

        for n in range(1, 65):
            hex_dir = CONTENT_DIR / f"hex{n:02d}"
            if not hex_dir.exists():
                hex_dir = CONTENT_DIR / f"hex{n}"

            file_path = None
            for filename in candidates:
                cand_path = hex_dir / filename
                if cand_path.exists():
                    file_path = cand_path
                    break

            if not file_path:
                continue

            hex_data = parse_hexagram_md(file_path, n, lang)
            if hex_data:
                compiled_hexes[str(n)] = hex_data

        out_path = OUTPUT_DIR / f"hexagramas.{lang}.json"
        with open(out_path, "w", encoding="utf-8") as f_out:
            json.dump(compiled_hexes, f_out, ensure_ascii=False, indent=2)

        print(f"  -> Generado: {out_path} ({len(compiled_hexes)}/64 hexagramas)")

if __name__ == "__main__":
    main()