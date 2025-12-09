# Import library untuk operasi matematika dan plotting
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menggambar lingkaran
def gambar_lingkaran(radius, center):
	# Membuat 200 titik untuk menggambar lingkaran
	theta = np.linspace(0, 2 * np.pi, 200)
	# Konversi koordinat polar ke kartesian
	x = radius * np.cos(theta) + center[0]
	y = radius * np.sin(theta) + center[1]
	plt.plot(x, y, label='Lingkaran', color='b')

# Fungsi untuk merotasi lingkaran
def rotasi(center, radius, sudut):
	theta = np.linspace(0, 2 * np.pi, 200)
	# Konversi derajat ke radian
	rad = np.radians(sudut)
	# Rotasi lingkaran dengan menambahkan sudut rotasi pada theta
	x_rot = radius * np.cos(theta + rad) + center[0]
	y_rot = radius * np.sin(theta + rad) + center[1]
	return x_rot, y_rot

# Input data dari user
center_x = float(input('Masukkan koordinat pusat x: '))
center_y = float(input('Masukkan koordinat pusat y: '))
radius = float(input('Masukkan radius lingkaran: '))
sudut_rotasi = float(input('Masukkan sudut rotasi (dalam derajat): '))

# Visualisasi lingkaran sebelum rotasi
plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
gambar_lingkaran(radius, (center_x, center_y))
plt.title('Lingkaran Sebelum Rotasi')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()

# Melakukan rotasi pada lingkaran
x_rot, y_rot = rotasi((center_x, center_y), radius, sudut_rotasi)

# Visualisasi lingkaran setelah rotasi
plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.plot(x_rot, y_rot, label='Lingkaran Rotasi', color='r')
plt.title(f'Lingkaran Setelah Rotasi ({sudut_rotasi} Derajat)')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()