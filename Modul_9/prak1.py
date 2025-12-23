# Import library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar belah ketupat sebelum dan sesudah shear
def plot_belah_ketupat(original_points, sheared_points):
    # Gambar belah ketupat sebelum shear
    plt.figure(figsize=(6, 6))
    plt.subplot(1, 2, 1)
    plt.plot(*zip(*original_points, original_points[0]), marker='o')
    plt.title('Belah Ketupat Asli')
    plt.grid(True)

    # Gambar belah ketupat setelah shear
    plt.subplot(1, 2, 2)
    plt.plot(*zip(*sheared_points, sheared_points[0]), marker='o')
    plt.title('Belah Ketupat Setelah Shear')
    plt.grid(True)

    plt.show()

# Fungsi untuk melakukan shear pada objek belah ketupat
def shear_belah_ketupat(points, shear_x, shear_y):
    # Matriks transformasi shear
    shear_matrix = np.array([[1, shear_x],
                             [shear_y, 1]])

    # Mengalikan setiap titik dengan matriks shear
    sheared_points = []
    for point in points:
        new_point = np.dot(shear_matrix, point)
        sheared_points.append(new_point)

    return sheared_points

# Input dinamis dari user
print("Masukkan faktor shear horizontal (Shear X): ")
shear_x = float(input()) # Shear X (horizontal)
print("Masukkan faktor shear vertikal (Shear Y): ")
shear_y = float(input()) # Shear Y (vertikal)

# Koordinat asli belah ketupat
belah_ketupat_points = np.array([[0, 2], [2, 0], [0, -2], [-2, 0]])

# Lakukan transformasi shear
sheared_points = shear_belah_ketupat(belah_ketupat_points, shear_x, shear_y)

# Plot hasilnya
plot_belah_ketupat(belah_ketupat_points, sheared_points)
