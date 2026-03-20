from PIL import Image
import numpy as np

# --- 1. Cargar la matriz desde el TXT ---
matriz_path = "matriz_ma.txt"  # tu archivo
matriz_ma = np.loadtxt(matriz_path, dtype=int)

# --- 2. Convertir la matriz binaria a imagen RGB ---
# Definimos colores:
# 0 = fondo azul
# 1 = DACC rojo
alto, ancho = matriz_ma.shape
img_rgb = np.zeros((alto, ancho, 3), dtype=np.uint8)

# Fondo azul
img_rgb[matriz_ma == 0] = [0, 0, 255]  # azul puro
# DACC rojo
img_rgb[matriz_ma == 1] = [255, 0, 0]  # rojo puro

# --- 3. Crear la imagen y guardar como PNG ---
img = Image.fromarray(img_rgb)
img.save("matriz_ma_reconstruida.png")

print("Imagen reconstruida guardada como 'matriz_ma_reconstruida.png'.")