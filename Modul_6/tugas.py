import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ============================================================
# FUNGSI UNTUK MENGGAMBAR TABUNG
# ============================================================
def draw_cylinder(radius, height, title, ax):
    """
    Menggambar tabung 3D menggunakan jaring-jaring mesh.
    radius : jari-jari tabung
    height : tinggi tabung
    title  : judul tampilan
    ax     : axes untuk plot 3D
    """

    # Membuat grid theta (sudut) dan z (tinggi)
    z = np.linspace(0, height, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    theta, z = np.meshgrid(theta, z)

    # Rumus koordinat silinder
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Plot permukaan tabung
    ax.plot_surface(x, y, z, color='gray', edgecolor='black', linewidth=0.3)

    # Judul di tengah
    ax.set_title(title, pad=20, fontsize=12)

    # Mengatur batas sumbu agar proporsional
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([0, 10])

    # Label sumbu
    ax.set_xlabel("X", labelpad=10)
    ax.set_ylabel("Y", labelpad=10)
    ax.set_zlabel("Z", labelpad=10)

    # Grid menyala
    ax.grid(True)



# ============================================================
# INPUT DATA DARI USER
# ============================================================
radius = float(input("Masukkan radius tabung        : "))
height = float(input("Masukkan tinggi tabung        : "))
scale_factor = float(input("Masukkan faktor penskalaan    : "))

# Hasil skala
new_radius = radius * scale_factor
new_height = height * scale_factor



# ============================================================
# MENAMPILKAN GAMBAR
# ============================================================
fig = plt.figure(figsize=(13, 6))

# Plot tabung asli
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
draw_cylinder(radius, height, "Tabung Asli", ax1)

# Plot tabung setelah penskalaan
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
draw_cylinder(new_radius, new_height, 
              f"Tabung Setelah Penskalaan\n(Faktor Skala: {scale_factor})", ax2)

# Mengatur tata letak
plt.tight_layout()
plt.show()
