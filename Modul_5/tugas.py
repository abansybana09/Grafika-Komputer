import matplotlib.pyplot as plt
import numpy as np

def gambar_persegi_panjang(titik, warna='b', label=None):
  bentuk = np.array(titik)
  bentuk_tertutup = np.vstack([bentuk, bentuk[0]])
  plt.plot(bentuk_tertutup[:, 0], bentuk_tertutup[:, 1], color=warna, label=label, linewidth=2)

def translasi(titik, vektor):
  titik_baru = [[x + vektor[0], y + vektor[1]] for x, y in titik]
  return titik_baru

persegi_panjang_awal = [
  (10, 10),
  (40, 10),
  (50, 20),
  (20, 20)
]

vektor = (10, 10)
persegi_panjang_tertranslasi = translasi(persegi_panjang_awal, vektor)

plt.figure(figsize=(10, 5.5))
gambar_persegi_panjang(persegi_panjang_awal, warna='blue', label='Persegi Panjang Awal')
gambar_persegi_panjang(persegi_panjang_tertranslasi, warna='red', label='Persegi Panjang Setelah Translasi')
plt.xlim(0, 60)
plt.ylim(0, 30)
plt.xticks(np.arange(0, 61, 10))
plt.yticks(np.arange(0, 31, 5))
plt.grid(True)
plt.legend()
plt.title("Latihan Translasi Jajargenjang")
plt.gca().set_aspect('auto', adjustable='box')
plt.show()
