import numpy as np
import matplotlib.pyplot as plt

# Originalbilden som en matris
bild = np.array([
    [25, 25, 25, 250, 250, 250, 250, 25, 25, 25],
    [25, 25, 25, 225, 225, 225, 225, 25, 25, 25],
    [25, 25, 25, 200, 200, 200, 200, 25, 25, 25],
    [25, 25, 25, 175, 175, 175, 175, 25, 25, 25],
    [150, 150, 150, 150, 150, 150, 150, 150, 150, 150],
    [25, 125, 125, 125, 125, 125, 125, 125, 125, 25],
    [25, 25, 100, 100, 100, 100, 100, 100, 25, 25],
    [25, 25, 25, 75, 75, 75, 75, 25, 25, 25],
    [25, 25, 25, 50, 50, 50, 50, 25, 25, 25],
    [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
], dtype=float)

print("Originalbild:")
print(bild.astype(int))

# Hitta minsta och största värdet i bilden
min_varde = np.min(bild)
max_varde = np.max(bild)

# Räkna ut värden för kontrastjustering
a = 255 / (max_varde - min_varde)
b = -a * min_varde

print("\nKontrastjustering:")
print("Minvärde:", min_varde)
print("Maxvärde:", max_varde)
print("a =", round(a, 3))
print("b =", round(b, 3))

# Skapa ny bild med förbättrad kontrast
ny_bild = a * bild + b

# Se till att alla värden hamnar mellan 0 och 255
ny_bild = np.clip(np.round(ny_bild), 0, 255).astype(int)

print("\nEfter kontrastjustering:")
print(ny_bild)

# Rotera bilden 180 grader
roterad_bild = np.flipud(np.fliplr(ny_bild))

print("\nRoterad bild:")
print(roterad_bild)

# Skapa negativ bild
negativ_bild = 255 - roterad_bild

print("\nNegativ bild:")
print(negativ_bild)

# Visa alla steg
fig, axlar = plt.subplots(1, 4, figsize=(14, 4))

axlar[0].imshow(bild, cmap="gray", vmin=0, vmax=255)
axlar[0].set_title("Original")
axlar[0].axis("off")

axlar[1].imshow(ny_bild, cmap="gray", vmin=0, vmax=255)
axlar[1].set_title("Kontrast")
axlar[1].axis("off")

axlar[2].imshow(roterad_bild, cmap="gray", vmin=0, vmax=255)
axlar[2].set_title("Rotation")
axlar[2].axis("off")

axlar[3].imshow(negativ_bild, cmap="gray", vmin=0, vmax=255)
axlar[3].set_title("Negativ")
axlar[3].axis("off")

plt.tight_layout()
plt.show()