# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menggambar lingkaran sebelum dan sesudah shear
def plot_lingkaran(original_points, sheared_points):
    # Gambar lingkaran sebelum shear
    plt.figure(figsize=(6, 6))
    plt.subplot(1, 2, 1)
    plt.plot(original_points[0], original_points[1], label='Lingkaran Asli')
    plt.title('Lingkaran Asli')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    # Gambar lingkaran setelah shear
    plt.subplot(1, 2, 2)
    plt.plot(sheared_points[0], sheared_points[1], label='Lingkaran Setelah Shear')
    plt.title('Lingkaran Setelah Shear')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    plt.show()

# Fungsi untuk melakukan shear pada lingkaran
def shear_lingkaran(points, shear_x, shear_y):
    # Matriks transformasi shear
    shear_matrix = np.array([[1, shear_x],
                             [shear_y, 1]])

    # Mengalikan setiap titik lingkaran dengan matriks shear
    sheared_points = np.dot(shear_matrix, points)

    return sheared_points

# Input dinamis dari user
print("Masukkan faktor shear horizontal (Shear X): ")
shear_x = float(input())  # Shear X (horizontal)
print("Masukkan faktor shear vertikal (Shear Y): ")
shear_y = float(input())  # Shear Y (vertikal)

# Menghasilkan koordinat lingkaran asli
theta = np.linspace(0, 2 * np.pi, 100)  # Sudut lingkaran
radius = 5  # Jari-jari lingkaran
x = radius * np.cos(theta)  # Koordinat X lingkaran
y = radius * np.sin(theta)  # Koordinat Y lingkaran

# Gabungkan koordinat X dan Y menjadi matriks
lingkaran_points = np.array([x, y])

# Lakukan transformasi shear
sheared_points = shear_lingkaran(lingkaran_points, shear_x, shear_y)

# Plot hasilnya
plot_lingkaran(lingkaran_points, sheared_points)
