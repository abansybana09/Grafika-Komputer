import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Buat figure dan axes
fig, ax = plt.subplots()

def gambar_lingkaran(radius):
    """
    Menggambar lingkaran dengan radius yang ditentukan oleh parameter 'radius'.

    Parameter:
    radius (int): radius lingkaran.
    """
    # Membuat kotak
    lingkaran = patches.Circle(
        (0, 0), radius,
        edgecolor='blue', facecolor='none', linewidth=2
    )
    ax.add_patch(lingkaran)

    # Atur batas sumbu
    ax.set_xlim(-radius -10, radius + 10)
    ax.set_ylim(-radius -10, radius + 10)

    # Tambahkan grid dan buat proporsional
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Panggil fungsi di luar definisi
gambar_lingkaran(50)
