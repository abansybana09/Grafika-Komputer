# Import library
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Fungsi untuk membuat objek limas
def create_pyramid(base_length, height):
    # Titik-titik sudut dasar limas
    base_x = np.array([0, base_length, base_length, 0])
    base_y = np.array([0, 0, base_length, base_length])
    base_z = np.zeros(4)

    # Titik puncak limas
    apex = np.array([[base_length / 2, base_length / 2, height]])

    # Menggabungkan semua titik
    x = np.concatenate((base_x, apex[:, 0]))
    y = np.concatenate((base_y, apex[:, 1]))
    z = np.concatenate((base_z, apex[:, 2]))

    return x, y, z, apex


# Fungsi untuk menerapkan penskalaan pada objek
def scale_pyramid(x, y, z, scale_x, scale_y, scale_z):
    # Matriks penskalaan
    scale_matrix = np.array([scale_x, scale_y, scale_z])

    # Mengubah koordinat
    scaled_x = x * scale_matrix[0]
    scaled_y = y * scale_matrix[1]
    scaled_z = z * scale_matrix[2]

    return scaled_x, scaled_y, scaled_z


# Parameter geometri objek
base_length = 4
height = 4

# Pengambilan input faktor penskalaan
scale_x = float(input("Masukkan faktor penskalaan pada sumbu X: "))
scale_y = float(input("Masukkan faktor penskalaan pada sumbu Y: "))
scale_z = float(input("Masukkan faktor penskalaan pada sumbu Z: "))

# Membuat objek limas
x, y, z, apex = create_pyramid(base_length, height)

# Melakukan penskalaan
scaled_x, scaled_y, scaled_z = scale_pyramid(x, y, z, scale_x, scale_y, scale_z)

# Visualisasi objek
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Objek asli
ax.add_collection3d(
    Poly3DCollection(
        [list(zip(x[:4], y[:4], z[:4]))],
        color='gray',
        alpha=0.5,
        label='Asli'
    )
)

# Objek setelah skala
ax.add_collection3d(
    Poly3DCollection(
        [list(zip(scaled_x[:4], scaled_y[:4], scaled_z[:4]))],
        color='red',
        alpha=0.5,
        label='Skala'
    )
)

# Label sumbu dan legenda
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Penskalaan 3D Objek Limas dengan Input Dinamis')
ax.legend()

#menentukan batas sumbu
ax.set_xlim([0, base_length * scale_x])
ax.set_ylim([0, base_length * scale_y])
ax.set_zlim([0, height * scale_z])
plt.show()
