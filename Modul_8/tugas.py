import matplotlib.pyplot as plt

# Input titik belah ketupat dari pengguna
titik_belah_ketupat_asli = []
print("Masukkan koordinat belah ketupat (format: x,y). Harus 4 titik:")
for i in range(4):
    x, y = map(float, input(f"Titik {i+1}: ").split(","))
    titik_belah_ketupat_asli.append([x, y])

# Pilih sumbu pencerminan
sumbu = input("Masukkan sumbu pencerminan (x, y, origin): ").strip().lower()

# Fungsi pencerminan umum
def pencerminan(titik_asli, sumbu):
    if sumbu == 'x':
        return [[x, -y] for x, y in titik_asli]
    elif sumbu == 'y':
        return [[-x, y] for x, y in titik_asli]
    elif sumbu == 'origin':
        return [[-x, -y] for x, y in titik_asli]
    else:
        raise ValueError("Sumbu tidak valid. Pilih 'x', 'y', atau 'origin'.")

# Terapkan pencerminan
titik_belah_ketupat_pencerminan = pencerminan(titik_belah_ketupat_asli, sumbu)

# Input offset opsional
offset_y = float(input("Masukkan offset Y (misalnya 0.9): "))
offset_x = float(input("Masukkan offset X (misalnya 0): "))
titik_belah_ketupat_pencerminan = [[x + offset_x, y + offset_y] for x, y in titik_belah_ketupat_pencerminan]

# Fungsi menggambar objek
def gambar_objek(titik, label_teks, warna, z_order):
    x_coords = [p[0] for p in titik] + [titik[0][0]]
    y_coords = [p[1] for p in titik] + [titik[0][1]]
    plt.fill(x_coords, y_coords, color=warna, alpha=0.9, label=label_teks, zorder=z_order)

# Plot
plt.figure(figsize=(8, 8))
plt.title("Pencerminan Belah Ketupat 2D")

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

gambar_objek(titik_belah_ketupat_asli, 'Belah Ketupat Asli', '#555555', 1)
gambar_objek(titik_belah_ketupat_pencerminan, 'Belah Ketupat Setelah Pencerminan', '#778899', 2)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')

plt.legend(loc='upper right')
plt.show()
