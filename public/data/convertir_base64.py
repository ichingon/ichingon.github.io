import base64

# Lee tu fuente optimizada en modo binario
with open("fuente-iching-optimizada.ttf", "rb") as f:
    encoded_string = base64.b64encode(f.read()).decode("utf-8")

# Guarda el resultado en un archivo de texto plano
with open("fuente_base64.txt", "w") as f:
    f.write(encoded_string)

print("¡Conversión completada! Revisa el archivo fuente_base64.txt")