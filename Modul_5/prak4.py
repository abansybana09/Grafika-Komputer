# Import library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar lingkaran
def gambar_lingkaran(tengah, radius, warna='b', label=None):
    x, y = tengah
    theta = np.linspace(0, 2 * np.pi, 100)
    x_vals = x + radius * np.cos(theta)
    y_vals = y + radius * np.sin(theta)

    plt.plot(x_vals, y_vals, color=warna, label=label)

# Fungsi untuk melakukan translasi
def translasi(tengah, vektor):
    # Menambahkan nilai vektor translasi ke pusat lingkaran
    tengah_baru = (tengah[0] + vektor[0], tengah[1] + vektor[1])
    return tengah_baru

# Fungsi utama untuk input dinamis dan translasi
def main():
    # Input pusat lingkaran dan radius dari pengguna
    print("Masukkan pusat lingkaran (dalam format x,y):")
    x, y = map(float, input("Input Pusat Lingkaran (x, y): ").split(','))
    
    radius = float(input("Masukkan radius lingkaran: "))

    # Pusat lingkaran awal
    pusat_lingkaran_awal = (x, y)

    # Input vektor translasi dari pengguna
    print("\nMasukkan vektor translasi (dalam format dx,dy):")
    dx, dy = map(float, input("Vektor Translasi (dx, dy): ").split(','))

    # Translasi pusat lingkaran
    pusat_lingkaran_tertranslasi = translasi(pusat_lingkaran_awal, (dx, dy))

    # Plot lingkaran sebelum dan sesudah translasi
    plt.figure()

    # Gambar lingkaran awal
    gambar_lingkaran(pusat_lingkaran_awal, radius, warna='b', label='Lingkaran Awal')

    # Gambar lingkaran setelah translasi
    gambar_lingkaran(pusat_lingkaran_tertranslasi, radius, warna='r', label='Lingkaran Setelah Translasi')

    # Menampilkan grid dan setting sumbu
    plt.grid(True)

    xmin = min(pusat_lingkaran_awal[0] - radius, pusat_lingkaran_tertranslasi[0] - radius)
    xmax = max(pusat_lingkaran_awal[0] + radius, pusat_lingkaran_tertranslasi[0] + radius)
    ymin = min(pusat_lingkaran_awal[1] - radius, pusat_lingkaran_tertranslasi[1] - radius)
    ymax = max(pusat_lingkaran_awal[1] + radius, pusat_lingkaran_tertranslasi[1] + radius)

    plt.xlim(xmin - 5, xmax + 5)
    plt.ylim(ymin - 5, ymax + 5)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title('Translasi 2D Lingkaran')

    # Tampilkan plot
    plt.show()

# Panggil fungsi utama
main()
