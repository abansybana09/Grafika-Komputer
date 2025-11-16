# Import library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar segitiga
def gambar_segitiga(titik, warna='b', label=None):
    segitiga = np.array(titik)
    # Tambahkan titik pertama ke akhir untuk menutup segitiga
    segitiga = np.vstack([segitiga, segitiga[0]])
    plt.plot(segitiga[:, 0], segitiga[:, 1], color=warna, label=label)

# Fungsi untuk melakukan translasi
def translasi(titik, vektor):
    titik_baru = [(x + vektor[0], y + vektor[1]) for x, y in titik]
    return titik_baru

# Titik-titik awal segitiga
segitiga_awal = [(1, 2), (3, 5), (6, 2)]

# Vektor translasi
vektor_translasi = (2, 3)

# Translasi segitiga
segitiga_tertranslasi = translasi(segitiga_awal, vektor_translasi)

# Plot segitiga sebelum dan sesudah translasi
plt.figure()

# Gambar segitiga awal
gambar_segitiga(segitiga_awal, warna='b', label='Segitiga Awal')

# Gambar segitiga setelah translasi
gambar_segitiga(segitiga_tertranslasi, warna='r', label='Segitiga Setelah Translasi')

# Menampilkan grid dan setting sumbu
plt.grid(True)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title('Translasi 2D Segitiga')

# Tampilkan plot
plt.show()
