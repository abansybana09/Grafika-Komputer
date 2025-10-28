import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Buat figure dan axes
fig, ax = plt.subplots()

def gambar_kotak(ukuran: int):
    """
    Menggambar kotak dengan panjang sisi yang ditentukan oleh parameter 'ukuran'.

    Parameter:
    ukuran (int): Panjang sisi kotak.
    """
    # Membuat kotak
    kotak = patches.Rectangle(
        (0, 0), ukuran, ukuran,
        edgecolor='blue', facecolor='none', linewidth=2
    )
    ax.add_patch(kotak)

    # Atur batas sumbu
    ax.set_xlim(-10, ukuran + 10)
    ax.set_ylim(-10, ukuran + 10)

    # Tambahkan grid dan buat proporsional
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Panggil fungsi di luar definisi
gambar_kotak(100)
