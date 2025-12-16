import matplotlib.pyplot as plt

# Fungsi untuk menggambar persegi panjang
def gambar_persegi_panjang(ax, x, y, lebar, tinggi, label="Persegi Panjang"):
    persegi_panjang = plt.Rectangle(
        (x, y),
        lebar,
        tinggi,
        fill=False,
        edgecolor='blue',
        linewidth=2,
        label=label
    )
    ax.add_patch(persegi_panjang)


# Fungsi untuk mencerminkan persegi panjang
def pencerminan_persegi_panjang(x, y, lebar, tinggi, sumbu):
    if sumbu == 'X':
        # Pencerminan terhadap sumbu X
        return x, -y - tinggi, lebar, tinggi
    elif sumbu == 'Y':
        # Pencerminan terhadap sumbu Y
        return -x - lebar, y, lebar, tinggi
    elif sumbu == 'ORIGIN':
        # Pencerminan terhadap titik origin
        return -x - lebar, -y - tinggi, lebar, tinggi
    else:
        raise ValueError("Sumbu tidak valid. Gunakan X, Y, atau ORIGIN.")


# ===================== INPUT DATA =====================
x = float(input("Masukkan koordinat x sudut kiri bawah: "))
y = float(input("Masukkan koordinat y sudut kiri bawah: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
tinggi = float(input("Masukkan tinggi persegi panjang: "))
sumbu = input("Masukkan sumbu pencerminan (X, Y, atau ORIGIN): ").strip().upper()


# ===================== PLOT =====================
fig, ax = plt.subplots(figsize=(8, 8))

# Persegi panjang asli
gambar_persegi_panjang(ax, x, y, lebar, tinggi, label="Persegi Panjang Asli")

# Persegi panjang hasil pencerminan
x_baru, y_baru, lebar_baru, tinggi_baru = pencerminan_persegi_panjang(
    x, y, lebar, tinggi, sumbu
)
gambar_persegi_panjang(
    ax,
    x_baru,
    y_baru,
    lebar_baru,
    tinggi_baru,
    label="Persegi Panjang Setelah Pencerminan"
)

# ===================== DETAIL PLOT =====================
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', adjustable='box')

# Sumbu X dan Y
ax.axhline(0, color='black', linewidth=0.5, ls='--')
ax.axvline(0, color='black', linewidth=0.5, ls='--')

# Grid dan keterangan
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title("Pencerminan Persegi Panjang 2D")
plt.show()
