import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar bentuk 4-sisi (dari kode Anda)
def gambar_persegi_panjang(titik, warna='b', label=None):
  """
  Menggambar sebuah poligon 4-sisi tertutup.
  """
  bentuk = np.array(titik)
  # Menambahkan titik pertama ke akhir untuk menutup bentuk
  bentuk_tertutup = np.vstack([bentuk, bentuk[0]])
  # Plot garis
  plt.plot(bentuk_tertutup[:, 0], bentuk_tertutup[:, 1], color=warna, label=label, linewidth=2)

# Fungsi untuk melakukan translasi (dari kode Anda)
def translasi(titik, vektor):
  # Menambahkan vektor translasi ke semua titik
  titik_baru = [[x + vektor[0], y + vektor[1]] for x, y in titik]
  return titik_baru

# --- Data dan Logika Latihan ---

# 1. Titik-titik untuk Jajargenjang Awal (dari grid)
persegi_panjang_awal = [
    (10, 10), 
    (40, 10), 
    (50, 20), 
    (20, 20)
]

# 2. Tentukan Vektor Translasi
# Kita asumsikan vektornya (10, 10), berdasarkan perpindahan
# titik pertama (10, 10) menjadi (20, 20) di gambar.
vektor = (10, 10)

# 3. Hitung Jajargenjang hasil translasi
persegi_panjang_tertranslasi = translasi(persegi_panjang_awal, vektor)

# --- Membuat Plot ---

plt.figure(figsize=(10, 5.5)) # Ukuran disesuaikan agar rasio mirip gambar

# Gambar Jajargenjang Awal
gambar_persegi_panjang(persegi_panjang_awal, warna='blue', label='Persegi Panjang Awal')

# Gambar Jajargenjang Setelah Translasi (Hasil Perhitungan)
gambar_persegi_panjang(persegi_panjang_tertranslasi, warna='red', label='Persegi Panjang Setelah Translasi')

# --- Pengaturan Tampilan Plot (Sesuai Gambar) ---

# Mengatur rentang sumbu
plt.xlim(0, 60)
plt.ylim(0, 30)

# Mengatur 'ticks' (penanda) pada sumbu
plt.xticks(np.arange(0, 61, 10)) # Sumbu X dari 0-60, interval 10
plt.yticks(np.arange(0, 31, 5))  # Sumbu Y dari 0-30, interval 5

# Menampilkan grid
plt.grid(True)

# Menampilkan legenda
plt.legend()

# Memberi judul plot
plt.title("Latihan Translasi Jajargenjang")

# Mengatur aspek rasio
plt.gca().set_aspect('auto', adjustable='box') 

# Tampilkan plot
plt.show()