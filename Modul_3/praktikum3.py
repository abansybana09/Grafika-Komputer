import matplotlib.pyplot as plt

# Fungsi untuk menggambar garis menggunakan algoritma Bresenham
def bresenham_algorithm(x0, y0, x1, y1):
    # Inisialisasi variabel
    x, y = x0, y0
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1 # penambahan untuk x
    sy = 1 if y0 < y1 else -1 # penambahan untuk y
    err = dx - dy

    x_points = [x]
    y_points = [y]

    while x != x1 or y != y1:
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
        x_points.append(x)
        y_points.append(y)

    # Menggambar garis menggunakan matplotlib
    plt.plot(x_points, y_points, marker='o', color='r')
    plt.title(f"Garis Bresenham dari ({x0}, {y0}) ke ({x1}, {y1})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Meminta input dari pengguna untuk titik awal dan titik akhir
x0 = int(input("Masukkan koordinat x0 (titik awal): "))
y0 = int(input("Masukkan koordinat y0 (titik awal): "))
x1 = int(input("Masukkan koordinat x1 (titik akhir): "))
y1 = int(input("Masukkan koordinat y1 (titik akhir): "))

# Memanggil fungsi untuk menggambar garis dengan algoritma Bresenham
bresenham_algorithm(x0, y0, x1, y1)