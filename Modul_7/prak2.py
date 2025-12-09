import numpy as np
import matplotlib.pyplot as plt

def gambar_persegi_panjang(titik):
    persegi_panjang = plt.Polygon(titik, closed=True, fill=None, edgecolor='r')
    plt.gca().add_patch(persegi_panjang)

def rotasi(titik, sudut):
    # Konversi derajat ke radian
    radian = np.radians(sudut)
    
    # Matriks rotasi 2D
    rotasi_matrix = np.array([[np.cos(radian), -np.sin(radian)],
                              [np.sin(radian), np.cos(radian)]])
    
    # Mengalikan titik dengan matriks rotasi
    titik_rotated = np.dot(titik, rotasi_matrix)
    return titik_rotated

x1 = float(input("Masukkan koordinat x1: "))
y1 = float(input("Masukkan koordinat y1: "))
x2 = float(input("Masukkan koordinat x2: "))
y2 = float(input("Masukkan koordinat y2: "))
x3 = float(input("Masukkan koordinat x3: "))
y3 = float(input("Masukkan koordinat y3: "))
x4 = float(input("Masukkan koordinat x4: "))
y4 = float(input("Masukkan koordinat y4: "))

# Menyimpan koordinat 4 titik persegi panjang dalam array
titik_asli = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])

sudut_rotasi = float(input("Masukkan sudut rotasi (dalam derajat): "))

# Visualisasi persegi panjang sebelum rotasi
plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

gambar_persegi_panjang(titik_asli)
plt.title('Persegi Panjang Sebelum Rotasi')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# Melakukan rotasi pada titik-titik persegi panjang
titik_rotated = rotasi(titik_asli, sudut_rotasi)

# Visualisasi persegi panjang setelah rotasi
plt.figure(figsize=(8, 8))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

gambar_persegi_panjang(titik_rotated)
plt.title(f'Persegi Panjang Setelah Rotasi {sudut_rotasi} Derajat')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()