# Import library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar persegi panjang
def gambar_persegi_panjang(titik, warna='b', label=None):
  persegi_panjang = np.array(titik)
  # Tambahkan titik pertama ke akhir untuk menutup persegi panjang
  persegi_panjang = np.vstack([persegi_panjang, persegi_panjang[0]])
  plt.plot(persegi_panjang[:, 0], persegi_panjang[:, 1], color=warna, label=label)

# Fungsi untuk melakukan translasi
def translasi(titik, vektor):
  # Menambahkan vektor translasi ke semua titik persegi panjang
  titik_baru = [[x + vektor[0], y + vektor[1]] for x, y in titik]
  return titik_baru

# Fungsi utama untuk input dinamis dan translasi
def main():
  # Input titik persegi panjang dari pengguna
  print("Masukkan koordinat persegi panjang (dalam format x, y):")
  x1, y1 = map(float, input("Titik 1 (x1, y1): ").split(','))
  x2, y2 = map(float, input("Titik 2 (x2, y2): ").split(','))
  x3, y3 = map(float, input("Titik 3 (x3, y3): ").split(','))
  x4, y4 = map(float, input("Titik 4 (x4, y4): ").split(','))

  # Titik persegi panjang awal
  persegi_panjang_awal = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

  # Input vektor translasi dari pengguna
  print("Masukkan vektor translasi (dalam format dx, dy):")
  dx, dy = map(float, input("Vektor Translasi (dx, dy): ").split(','))

  # Translasi persegi panjang
  persegi_panjang_tertranslasi = translasi(persegi_panjang_awal, (dx, dy))

  # Plot persegi panjang sebelum dan sesudah translasi
  plt.figure()

  # Gambar persegi panjang awal
  gambar_persegi_panjang(persegi_panjang_awal, warna='b', label='Persegi Panjang Awal')

  # Gambar persegi panjang setelah translasi
  gambar_persegi_panjang(persegi_panjang_tertranslasi, warna='r', label='Persegi Panjang Setelah Translasi')

  # Menampilkan grid dan setting sumbu
  plt.grid(True)
  
  # Mengumpulkan semua koordinat x dan y untuk mengatur batas plot
  semua_x = [x1, x2, x3, x4] + [titik[0] for titik in persegi_panjang_tertranslasi]
  semua_y = [y1, y2, y3, y4] + [titik[1] for titik in persegi_panjang_tertranslasi]
  
  plt.xlim(min(semua_x) - 10, max(semua_x) + 10)
  plt.ylim(min(semua_y) - 10, max(semua_y) + 10)
  
  # Note: Baris xlim/ylim di gambar asli hanya menggunakan titik awal, 
  # yang mungkin tidak optimal jika hasil translasinya jauh.
  # Versi gambar asli:
  # plt.xlim(min(x1, x2, x3, x4) - 10, max(x1, x2, x3, x4) + 10)
  # plt.ylim(min(y1, y2, y3, y4) - 10, max(y1, y2, y3, y4) + 10)

  plt.gca().set_aspect('equal', adjustable='box')
  plt.legend()
  plt.title('Translasi 2D Persegi Panjang')

  # Tampilkan plot
  plt.show()

# Panggil fungsi utama
main()