import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Buat figure dan axes
fig, ax = plt.subplots()

def gambar_persegi_panjang(lebar, tinggi):
    """
    Menggambar persegi panjang dengan lebar dan tinggi yang ditentukan.

    Parameter:
    lebar (int): lebar persegi panjang.
    tinggi (int): tinggi persegi panjang.
    """
    # Membuat kotak
    persegi_panjang = patches.Rectangle(
        (0, 0), lebar,tinggi,
        edgecolor='blue', facecolor='none', linewidth=2
    )
    ax.add_patch(persegi_panjang)

    # Atur batas sumbu
    ax.set_xlim(-10, lebar + 10)
    ax.set_ylim(-10, tinggi + 10)

    # Tambahkan grid dan buat proporsional
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Panggil fungsi di luar definisi
gambar_persegi_panjang(100,50)

