# Import library untuk operasi array dan plotting
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menggambar segi enam
def gambar_segi_enam(titik):
	# Menambahkan titik pertama di akhir untuk menutup bentuk
	titik_plot = np.vstack([titik, titik[0]])
	plt.plot(titik_plot[:,0], titik_plot[:,1], label='Segi Enam', color='b')

# Fungsi untuk melakukan rotasi titik-titik
def rotasi(titik, sudut):
	radian = np.radians(sudut)
	# Matriks rotasi 2D
	rotasi_matrix = np.array([[np.cos(radian), -np.sin(radian)], [np.sin(radian), np.cos(radian)]])
	# Mengalikan titik dengan matriks rotasi
	titik_rotated = np.dot(titik, rotasi_matrix.T)
	return titik_rotated

# Input koordinat 6 titik segi enam dari user
print('Masukkan koordinat titik-titik segi enam (x, y):')
titik = []
for i in range(6):
	x = float(input(f'Koordinat x titik {i+1}: '))
	y = float(input(f'Koordinat y titik {i+1}: '))
	titik.append([x, y])
# Konversi list ke numpy array
titik = np.array(titik)
# Input sudut rotasi dari user
sudut_rotasi = float(input('Masukkan sudut rotasi (dalam derajat): '))

# Visualisasi segi enam sebelum rotasi
plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
gambar_segi_enam(titik)
plt.title('Segi Enam Sebelum Rotasi')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()

# Melakukan rotasi pada titik-titik segi enam
titik_rotated = rotasi(titik, sudut_rotasi)

# Visualisasi segi enam setelah rotasi
plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
gambar_segi_enam(titik_rotated)
plt.title(f'Segi Enam Setelah Rotasi ({sudut_rotasi} Derajat)')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()