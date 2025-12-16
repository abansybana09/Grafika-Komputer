import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar lingkaran
def gambar_lingkaran(ax, x, y, radius, label='Lingkaran'):
    """
    Fungsi untuk menggambar lingkaran pada grafik
    """
    lingkaran = plt.Circle(
        (x, y),
        radius,
        fill=False,
        edgecolor='blue',
        linewidth=2,
        label=label
    )
    ax.add_patch(lingkaran)


# Fungsi untuk mencerminkan lingkaran
def pencerminan_lingkaran(x, y, radius, sumbu):
    """
    Fungsi untuk melakukan pencerminan lingkaran
    """
    if sumbu == 'X':
        # Pencerminan terhadap sumbu X
        return x, -y, radius
    elif sumbu == 'Y':
        # Pencerminan terhadap sumbu Y
        return -x, y, radius
    elif sumbu == 'ORIGIN':
        # Pencerminan terhadap titik origin
        return -x, -y, radius
    else:
        raise ValueError("Sumbu tidak valid. Pilih X, Y, atau ORIGIN.")


# ===================== INPUT DARI PENGGUNA =====================
x = float(input("Masukkan koordinat X pusat lingkaran: "))
y = float(input("Masukkan koordinat Y pusat lingkaran: "))
radius = float(input("Masukkan radius lingkaran: "))
sumbu = input("Pilih sumbu pencerminan (X, Y, atau Origin): ").strip().upper()


# ===================== MEMBUAT PLOT =====================
fig, ax = plt.subplots(figsize=(8, 8))

# Menggambar lingkaran asli
gambar_lingkaran(ax, x, y, radius, label='Lingkaran Asli')

# Menggambar lingkaran setelah pencerminan
x_baru, y_baru, radius_baru = pencerminan_lingkaran(x, y, radius, sumbu)
gambar_lingkaran(
    ax,
    x_baru,
    y_baru,
    radius_baru,
    label='Lingkaran Setelah Pencerminan'
)

# ===================== DETAIL PLOT =====================
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', adjustable='box')

# Sumbu X dan Y
ax.axhline(0, color='black', linewidth=0.5, ls='--')
ax.axvline(0, color='black', linewidth=0.5, ls='--')

# Grid, legend, dan judul
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Pencerminan Lingkaran 2D')
plt.show()
