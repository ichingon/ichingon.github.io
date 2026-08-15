import os
import re
from pathlib import Path

CONTENT_DIR = Path("content/hexagramas")

def standardize_markdown(content):
    # 1. Separar Frontmatter del cuerpo
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not fm_match:
        return content

    yaml_frontmatter, body = fm_match.groups()

    # 2. Limpiar tooltips manteniendo su texto interior
    body = re.sub(r'\{\{<\s*tooltip\s+[^>]*>\}\}(.*?)\{\{<\s*/tooltip\s*>\}\}', r'\1', body, flags=re.DOTALL)

    # 3. Normalizar encabezados principales a nivel H2 (##)
    body = re.sub(r'\n#{2,4}\s+(El Dictamen)', r'\n## \1', body, flags=re.IGNORECASE)
    body = re.sub(r'\n#{2,4}\s+(La Imagen)', r'\n## \1', body, flags=re.IGNORECASE)
    body = re.sub(r'\n#{2,4}\s+(Las Líneas Individuales|Las Líneas)', r'\n## Las Líneas Individuales', body, flags=re.IGNORECASE)
    body = re.sub(r'\n#{2,4}\s+(Enlaces de Consulta)', r'\n## \1', body, flags=re.IGNORECASE)

    # 4. Normalizar subencabezados de líneas individuales a nivel H3 (###)
    lines_split = re.split(r'\n##\s+Las Líneas Individuales', body, flags=re.IGNORECASE)
    if len(lines_split) > 1:
        before_lines = lines_split[0]
        lines_and_after = lines_split[1]

        # Separar si hay enlaces de consulta o bloque nostr después de las líneas
        footer_split = re.split(r'\n##\s+Enlaces de Consulta|\n\*\*🔐\s+VERIFICACIÓN', lines_and_after, maxsplit=1, flags=re.IGNORECASE)
        lines_body = footer_split[0]
        footer_body = lines_and_after[len(lines_body):] if len(footer_split) > 1 else ""

        # Estandarizar cualquier #### a ### dentro del bloque de líneas
        lines_body = re.sub(r'\n####\s+', r'\n### ', lines_body)

        body = f"{before_lines}\n## Las Líneas Individuales{lines_body}{footer_body}"

    # 5. Limpieza de separadores horizontales duplicados y espacios
    body = re.sub(r'\n{3,}', '\n\n', body)
    body = re.sub(r'\n---\n\s*\n##', r'\n\n##', body)

    # 6. Reconstruir archivo markdown
    return f"---\n{yaml_frontmatter.strip()}\n---\n\n{body.strip()}\n"

def main():
    if not CONTENT_DIR.exists():
        print(f"[!] No existe la carpeta {CONTENT_DIR}")
        return

    archivos_procesados = 0

    for n in range(1, 65):
        hex_dir = CONTENT_DIR / f"hex{n:02d}"
        if not hex_dir.exists():
            hex_dir = CONTENT_DIR / f"hex{n}"
        if not hex_dir.exists():
            continue

        for filename in ["_index.md", "index.md"]:
            md_path = hex_dir / filename
            if md_path.exists():
                with open(md_path, "r", encoding="utf-8") as f:
                    original = f.read()

                normalized = standardize_markdown(original)

                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(normalized)

                archivos_procesados += 1
                break

    print(f"[✓] {archivos_procesados} archivos .md en español normalizados con éxito.")

if __name__ == "__main__":
    main()