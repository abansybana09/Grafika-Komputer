import matplotlib.pyplot as plt

# Fungsi untuk menggambar segitiga
def gambar_segitiga(titik):
    # Menyusun titik segitiga
    x = [titik[0][0], titik[1][0], titik[2][0], titik[0][0]]
    y = [titik[0][1], titik[1][1], titik[2][1], titik[0][1]]

    # Menggambar segitiga
    plt.plot(x, y, marker='o')
    plt.fill(x, y, alpha=0.3)  # Mengisi segitiga dengan warna transparan


# Fungsi untuk melakukan pencerminan
def pencerminan(titik, sumbu):
    # Melakukan pencerminan berdasarkan sumbu
    if sumbu == 'x':
        # Pencerminan terhadap sumbu x
        return [(x, -y) for (x, y) in titik]
    elif sumbu == 'y':
        # Pencerminan terhadap sumbu y
        return [(-x, y) for (x, y) in titik]
    elif sumbu == 'origin':
        # Pencerminan terhadap origin
        return [(-x, -y) for (x, y) in titik]
    else:
        raise ValueError("Sumbu tidak valid. Pilih 'x', 'y', atau 'origin'.")


# Input titik segitiga
titik_segitiga = []
print("Masukkan koordinat titik segitiga (format: x,y):")
for i in range(3):
    koordinat = input(f"Titik {i+1}: ")
    x, y = map(float, koordinat.split(','))
    titik_segitiga.append((x, y))


# Input jenis sumbu pencerminan
sumbu = input("Masukkan sumbu pencerminan ('x', 'y', atau 'origin'): ")

# Menggambar segitiga asli
plt.figure(figsize=(8, 8))
plt.title("Pencerminan Segitiga 2D")
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Gambar segitiga asli
gambar_segitiga(titik_segitiga)

# Pencerminan segitiga
titik_segitiga_pencerminan = pencerminan(titik_segitiga, sumbu)

# Menggambar segitiga setelah pencerminan
gambar_segitiga(titik_segitiga_pencerminan)

# Menambahkan legend dan menampilkan plot
plt.legend(['Segitiga Asli', 'Segitiga Pencerminan'])
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
