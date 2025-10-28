import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Buat figure dan axes
fig, ax = plt.subplots()

# Panjang sisi segitiga
sisi = 10
tinggi = np.sqrt(3) / 2 * sisi

# Titik-titik segitiga sama sisi
titik = [[0, 0], [sisi, 0], [sisi/2, tinggi]]

# Tambahkan segitiga ke plot
segitiga = patches.Polygon(titik, closed=True, edgecolor='red', facecolor='none', linewidth=2)
ax.add_patch(segitiga)

# Atur tampilan
ax.set_xlim(-1, sisi + 1)
ax.set_ylim(-1, tinggi + 1)
ax.set_aspect('equal')
plt.grid(True)
plt.title("Segitiga Sama Sisi (sisi = 10)")
plt.show()
