import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Buat figure dan axes
fig, ax = plt.subplots()

# 🚙 Badan mobil (persegi panjang besar)
badan_mobil = patches.Rectangle((0, 1), 6, 2, edgecolor='blue',linewidth=2, facecolor='skyblue')
ax.add_patch(badan_mobil)

# 🚙 Kabin mobil (persegi panjang kecil di atas)
kabin_mobil = patches.Rectangle((1, 2.5), 4, 1, edgecolor='blue',linewidth=2, facecolor='skyblue')
ax.add_patch(kabin_mobil)

# 🔘 Roda kiri
roda_kiri = patches.Circle((1.5, 0.5), 0.5, edgecolor='black',linewidth=2, facecolor='dimgray')
ax.add_patch(roda_kiri)

# 🔘 Roda kanan
roda_kanan = patches.Circle((4.5, 0.5), 0.5, edgecolor='black',
                             linewidth=2, facecolor='dimgray')
ax.add_patch(roda_kanan)

# 🔧 Atur tampilan
ax.set_xlim(-1, 7)
ax.set_ylim(-1, 4)
ax.set_aspect('equal')
plt.grid(True)
# plt.title("Mobil Sederhana dengan Bentuk Geometris") # Judul dihilangkan agar sama persis
plt.show()