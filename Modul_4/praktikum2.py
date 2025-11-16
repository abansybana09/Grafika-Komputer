import matplotlib.pyplot as plt

def midpoint_circle(h, k, r):
    """
    Menghasilkan daftar titik (x, y) pada lingkaran dengan algoritma midpoint circle.
    h, k: koordinat pusat lingkaran
    r: jari-jari (radius)
    """
    x = 0         # mulai dari titik paling kanan pada sumbu x relatif ke pusat (0, r)
    y = r         # mulai dari titik paling atas relatif ke pusat
    points = []

    # Inisialisasi keputusan p sesuai algoritma midpoint circle
    p = 1 - r

    # Tambahkan titik awal (h + 0, k + r)
    points.append((x + h, y + k))

    # Iterasi sampai x < y (menggambar sampai sudut 45 derajat, sisanya simetri)
    while x < y:
        x += 1
        # Jika p < 0 berarti titik di dalam lingkaran -> gunakan piksel sebelah kanan
        # Pembaruan p untuk kasus ini: p = p + 2*x + 1
        if p < 0:
            p += 2 * x + 1
        else:
            # Jika p >= 0 berarti titik berada di luar/tepat di batas -> geser ke bawah (y-1)
            y -= 1
            # Pembaruan p untuk kasus ini: p = p + 2*(x - y) + 1
            p += 2 * x - 2 * y + 1

        # Karena lingkaran simetris terhadap 8 oktaf, tambahkan semua titik simetris
        points.extend([
            (h + x, k + y),  # kuadran kanan-atas relatif
            (h - x, k + y),  # kiri-atas
            (h + x, k - y),  # kanan-bawah
            (h - x, k - y),  # kiri-bawah
            (h + y, k + x),  # rotasi 90 derajat dari (x,y)
            (h - y, k + x),
            (h + y, k - x),
            (h - y, k - x)
        ])
    return points

# Input dari pengguna
center_x = int(input("Masukkan koordinat x pusat lingkaran: "))
center_y = int(input("Masukkan koordinat y pusat lingkaran: "))
radius = int(input("Masukkan jari-jari lingkaran: "))

# Dapatkan daftar titik lingkaran menggunakan fungsi di atas
circle_points = midpoint_circle(center_x, center_y, radius)

# Plot hasilnya menggunakan matplotlib
plt.figure(figsize=(8,8))
for point in circle_points:
    plt.plot(point[0], point[1], 'bo')  # 'bo' = blue circle marker

plt.title('Lingkaran menggunakan algoritma Midpoint Circle')
# Atur batas sumbu agar lingkaran muat pada tampilan
plt.xlim(center_x - radius - 1, center_x + radius + 1)
plt.ylim(center_y - radius - 1, center_y + radius + 1)

# Tambahkan sumbu bantu dan grid
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')  # aspek rasio 1:1 agar lingkaran tidak terdistorsi
plt.show()