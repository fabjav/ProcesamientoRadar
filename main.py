from PIL import Image
import numpy as np

# --- 1. Cargar la imagen de la máscara ---
# La máscara es tu imagen manual: fondo azul, DACC rojo
mask_path = "template_dacc.png"  # reemplaza con tu archivo
img = Image.open(mask_path).convert("RGB")  # asegurar que esté en RGB

# --- 2. Convertir a matriz binaria ---
# Definimos la MA como los píxeles rojos
# Ajustá el umbral según el rojo de tu imagen
red_threshold = 150
green_threshold = 100
blue_threshold = 100

# Crear matriz binaria 0/1
img_np = np.array(img)
matriz_ma = ((img_np[:, :, 0] > red_threshold) &  # R alto
             (img_np[:, :, 1] < green_threshold) &  # G bajo
             (img_np[:, :, 2] < blue_threshold)).astype(int)

# --- 3. Guardar la matriz en un archivo txt ---
np.savetxt("matriz_ma.txt", matriz_ma, fmt="%d")  # 0/1

print("Matriz de MA guardada en 'matriz_ma.txt'.")
print("Tamaño de la matriz:", matriz_ma.shape)