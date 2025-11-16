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
    dx, dy = vektor
    titik_baru = [(x + dx, y + dy) for x, y in titik]
    return titik_baru

# Fungsi utama untuk input dinamis dan translasi
def main():
    # Input titik segitiga dari pengguna
    print("Masukkan koordinat segitiga (dalam format x,y):")
    x1, y1 = map(float, input("Titik 1 (x1, y1): ").split(','))
    x2, y2 = map(float, input("Titik 2 (x2, y2): ").split(','))
    x3, y3 = map(float, input("Titik 3 (x3, y3): ").split(','))

    segitiga_awal = [(x1, y1), (x2, y2), (x3, y3)]

    # Input vektor translasi
    print("\nMasukkan vektor translasi (dalam format dx,dy):")
    dx, dy = map(float, input("Vektor Translasi (dx, dy): ").split(','))

    # Translasi segitiga
    segitiga_tertranslasi = translasi(segitiga_awal, (dx, dy))

    # Plot segitiga sebelum dan sesudah translasi
    plt.figure()

    # Gambar segitiga awal
    gambar_segitiga(segitiga_awal, warna='b', label='Segitiga Awal')

    # Gambar segitiga setelah translasi
    gambar_segitiga(segitiga_tertranslasi, warna='r', label='Segitiga Setelah Translasi')

    # Menampilkan grid dan setting sumbu
    plt.grid(True)
    plt.xlim(min(x1, x2, x3) - 10, max(x1, x2, x3) + 10)
    plt.ylim(min(y1, y2, y3) - 10, max(y1, y2, y3) + 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title('Translasi 2D Segitiga')

    plt.show()

# Panggil fungsi utama
main()
