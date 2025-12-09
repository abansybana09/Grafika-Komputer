import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menggambar segitiga
def gambar_segitiga(titik):
    segitiga = plt.Polygon(titik, closed=True, fill=False, edgecolor='b')
    plt.gca().add_patch(segitiga)

# Fungsi untuk rotasi titik menggunakan matriks rotasi
def rotasi(titik, sudut):
    radian = np.radians(sudut)
    # Matriks rotasi 2D
    rotasi_matrix = np.array([[np.cos(radian), -np.sin(radian)], [np.sin(radian), np.cos(radian)]])
    # Perkalian matriks untuk transformasi rotasi
    titik_rotated = np.dot(titik, rotasi_matrix.T)
    return titik_rotated

# Input koordinat titik-titik segitiga
x1 = float(input('Masukkan koordinat x1: '))
y1 = float(input('Masukkan koordinat y1: '))
x2 = float(input('Masukkan koordinat x2: '))
y2 = float(input('Masukkan koordinat y2: '))
x3 = float(input('Masukkan koordinat x3: '))
y3 = float(input('Masukkan koordinat y3: '))
sudut_rotasi = float(input('Masukkan sudut rotasi (dalam derajat): '))

# Buat array numpy dari titik-titik segitiga
titik_asli = np.array([[x1, y1], [x2, y2], [x3, y3]])

# Gambar segitiga sebelum rotasi
plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
gambar_segitiga(titik_asli)
plt.title('Segitiga Sebelum Rotasi')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# Proses rotasi segitiga
titik_rotated = rotasi(titik_asli, sudut_rotasi)

plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
# Gambar segitiga hasil rotasi dengan warna merah
seg = plt.Polygon(titik_rotated, closed=True, fill=False, edgecolor='r')
plt.gca().add_patch(seg)
plt.title(f'Segitiga Setelah Rotasi ({sudut_rotasi} Derajat)')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()