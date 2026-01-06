# Import library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar persegi panjang sebelum dan sesudah shear
def plot_persegi_panjang(original_points, sheared_points):
    plt.figure(figsize=(6, 8))

    # Gambar persegi panjang asli
    plt.subplot(2, 1, 1)
    original_closed = np.vstack([original_points, original_points[0]])
    plt.plot(original_closed[:, 0], original_closed[:, 1], marker='o')
    plt.title('Persegi Panjang Asli')
    plt.grid(True)

    # Gambar persegi panjang setelah shear
    plt.subplot(2, 1, 2)
    sheared_closed = np.vstack([sheared_points, sheared_points[0]])
    plt.plot(sheared_closed[:, 0], sheared_closed[:, 1], marker='o')
    plt.title('Persegi Panjang Setelah Shear')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Fungsi untuk melakukan shear pada persegi panjang
def shear_persegi_panjang(points, shear_x, shear_y):
    shear_matrix = np.array([[1, shear_x],
                             [shear_y, 1]])
    sheared_points = []
    for point in points:
        new_point = np.dot(shear_matrix, point)
        sheared_points.append(new_point)
    return np.array(sheared_points)

# Input faktor shear dari pengguna
print("Masukkan faktor shear horizontal (Shear X): ")
shear_x = float(input())
print("Masukkan faktor shear vertikal (Shear Y): ")
shear_y = float(input())

# Koordinat persegi panjang (misalnya 4 titik sudut)
persegi_panjang_points = np.array([[0, 0], [4, 0], [4, 2], [0, 2]])

# Lakukan shear
sheared_points = shear_persegi_panjang(persegi_panjang_points, shear_x, shear_y)

# Tampilkan hasil
plot_persegi_panjang(persegi_panjang_points, sheared_points)
