import json
import os

# 1. Recolectar todos los textos posibles de tus JSON
textos_totales = ""
idiomas = ["es", "en", "de"]
for lang in idiomas:
    path = f"hexagramas.{lang}.json"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            def extraer_strings(obj):
                global textos_totales
                if isinstance(obj, str):
                    textos_totales += obj
                elif isinstance(obj, dict):
                    for v in obj.values():
                        extraer_strings(v)
                elif isinstance(obj, list):
                    for item in obj:
                        extraer_strings(item)
            extraer_strings(data)

# 2. Agregar caracteres latinos, puntuación, pinyin, trigramas y símbolos base
extras = " ☰☷☳☴☵☲☶☱0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúüñÁÉÍÓÚÜÑäöüßÄÖÜßāēīōūǖǎěǐǒǔǚàèìòùǜńňǖǘǚǜ.,;:?!-_/()[]{}""«»%#@+=*°–—黛灵娜"
textos_totales += extras

# 3. AGREGAR AUTOMÁTICAMENTE EL RANGO DE LOS 64 HEXAGRAMAS (U+4DC0 a U+4DFF)
hexagramas_unicode = "".join([chr(code) for code in range(0x4DC0, 0x4E00)])
textos_totales += hexagramas_unicode

# 4. Eliminar duplicados y guardar
caracteres_unicos = "".join(sorted(set(textos_totales)))

with open("caracteres_completos.txt", "w", encoding="utf-8") as f:
    f.write(caracteres_unicos)

print(f"¡Listo! Se extrajeron {len(caracteres_unicos)} caracteres únicos (incluyendo los 64 hexagramas).")