import matplotlib.pyplot as plt

def plot_circle(x_center, y_center, x, y):
    """
    Gambarkan titik-titik simetris untuk satu pasangan koordinat (x, y)
    relatif terhadap pusat lingkaran (x_center, y_center).

    Param:
    - x_center, y_center: koordinat pusat lingkaran
    - x, y: koordinat titik pada kuadran pertama yang akan dipantulkan
    """
    # Gambar 8 titik simetris berdasarkan pasangan (x, y)
    plt.plot(x_center + x, y_center + y, 'ro')
    plt.plot(x_center - x, y_center + y, 'ro')
    plt.plot(x_center + x, y_center - y, 'ro')
    plt.plot(x_center - x, y_center - y, 'ro')
    plt.plot(x_center + y, y_center + x, 'ro')
    plt.plot(x_center - y, y_center + x, 'ro')
    plt.plot(x_center + y, y_center - x, 'ro')
    plt.plot(x_center - y, y_center - x, 'ro')

def bresenham_circle(x_center, y_center, radius):
    """
    Implementasi algoritma Bresenham untuk menggambar lingkaran.

    Algoritma ini menggunakan parameter keputusan 'd' untuk menentukan
    apakah koordinat y harus dikurangi pada langkah berikutnya.
    Fungsi memanggil plot_circle pada setiap langkah untuk menggambar
    semua titik simetris lingkaran.

    Param:
    - x_center, y_center: koordinat pusat lingkaran
    - radius: jari-jari lingkaran (integer)
    """
    # Titik awal pada sumbu y (x = 0, y = radius)
    x = 0
    y = radius
    # Nilai awal fungsi keputusan (konstanta untuk lingkaran)
    d = 3 - 2 * radius

    # Gambar titik awal (beserta simetrisnya)
    plot_circle(x_center, y_center, x, y)
    
    # Iterasi sampai y menjadi negatif (selesai menggambar kuadran)
    while y >= 0:
        x += 1
        # Jika d > 0, geser y ke dalam (decrement) dan perbarui d sesuai kasus
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            # Jika d <= 0, hanya perbarui d tanpa mengubah y
            d = d + 4 * x + 6
        # Gambar titik hasil iterasi saat ini (beserta simetrisnya)
        plot_circle(x_center, y_center, x, y)

# Input pengguna untuk pusat lingkaran dan jari-jari
x_center = int(input("Masukkan koordinat x pusat lingkaran: "))
y_center = int(input("Masukkan koordinat y pusat lingkaran: "))
radius = int(input("Masukkan jari-jari lingkaran: "))

# Panggil fungsi untuk menggambar lingkaran
bresenham_circle(x_center, y_center, radius)

# Atur aspek, tampilkan grid, dan tampilkan plot
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()