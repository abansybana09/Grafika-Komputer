import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Buat figure dan axes
fig, ax = plt.subplots()

def gambar_segitiga(panjang_sisi):
    
    t1 = (0, 0)
    t2 = (panjang_sisi, 0)
    t3 = (panjang_sisi / 2, (panjang_sisi * (3**0.5)) / 2)
    # Membuat kotak
    segitiga = patches.Polygon(
        [t1, t2, t3], closed=True, edgecolor='blue', facecolor='none', linewidth=2)
    ax.add_patch(segitiga)

    # Atur batas sumbu
    ax.set_xlim(-10, panjang_sisi + 10)
    ax.set_ylim(-10, (panjang_sisi * (3**0.5)) / 2 + 10)

    # Tambahkan grid dan buat proporsional
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Panggil fungsi di luar definisi
gambar_segitiga(100)
