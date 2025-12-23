# Import library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar segitiga sebelum dan sesudah shear
def plot_segitiga(original_points, sheared_points):
    # Gambar segitiga sebelum shear
    plt.figure(figsize=(6, 6))
    plt.subplot(1, 2, 1)
    # Tambahkan titik pertama di akhir untuk menutup segitiga
    original_closed = np.vstack([original_points, original_points[0]])
    plt.plot(original_closed[:, 0], original_closed[:, 1], marker='o')
    plt.title('Segitiga Asli')
    plt.grid(True)

    # Gambar segitiga setelah shear
    plt.subplot(1, 2, 2)
    # Tambahkan titik pertama di akhir untuk menutup segitiga
    sheared_closed = np.vstack([sheared_points, sheared_points[0]])
    plt.plot(sheared_closed[:, 0], sheared_closed[:, 1], marker='o')
    plt.title('Segitiga Setelah Shear')
    plt.grid(True)

    plt.show()

# Fungsi untuk melakukan shear pada objek segitiga
def shear_segitiga(points, shear_x, shear_y):
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
shear_x = float(input())  # Shear X (horizontal)
print("Masukkan faktor shear vertikal (Shear Y): ")
shear_y = float(input())  # Shear Y (vertikal)

# Koordinat asli segitiga
segitiga_points = np.array([[0, 0], [4, 0], [2, 3]])

# Lakukan transformasi shear
sheared_points = shear_segitiga(segitiga_points, shear_x, shear_y)

# Plot hasilnya
plot_segitiga(segitiga_points, sheared_points)
