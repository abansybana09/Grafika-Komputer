import matplotlib.pyplot as plt

def midpoint_circle(h, k, r):
    # Mulai dari titik teratas pada lingkaran relatif terhadap pusat (0, r)
    x = 0
    y = r
    points = []
    
    # Parameter keputusan awal untuk algoritma midpoint
    p = 1 - r
    
    # Tambahkan titik awal (sudah digeser ke pusat (h, k))
    points.append((x + h, y + k))
    
    # Ulangi sampai x mencapai atau melewati y (hanya men-generate satu oktaf lalu cermin)
    while x < y:
        x += 1  # naikkan x satu langkah
        # Jika p < 0, titik selanjutnya tetap pada y, hanya update p berdasarkan x
        if p < 0:
            p += 2 * x - 2 * + 1
        else:
            # Jika p >= 0, turunkan y satu langkah dan update p berdasarkan perbedaan x dan y
            y -= 1
            p += 2*x - 2*y + 1
            
        # Karena simetri lingkaran, tambahkan 8 titik yang merupakan cermin dari (x, y)
        points.extend([
            (x + h, y + k),
            (h - x, k + y),
            (h + x, k - y),
            (h - x, k - y),
            (h + y, k + x),
            (h - y, k + x),
            (h + y, k - x),
            (h - y, k - x)
        ])
    return points

# Koordinat pusat dan jari-jari lingkaran yang ingin digambar
center_x = 0
center_y = 0
radius = 10

# Dapatkan titik-titik lingkaran dari fungsi midpoint_circle
circle_points = midpoint_circle(center_x, center_y, radius)

# Visualisasi menggunakan matplotlib
plt.figure(figsize=(8,8))
for point in circle_points:
    # Gambar setiap titik sebagai titik biru ('bo')
    plt.plot(point[0], point[1], 'bo')
    
    # Judul plot (diletakkan di dalam loop pada kode asli; cukup satu kali juga bisa)
    plt.title('lingkaran dengan menggunkan algoritma midpoint circle')

# Atur batas sumbu agar lingkaran terlihat penuh
plt.xlim(-radius-1, radius+1)
plt.ylim(-radius-1, radius+1)

# Gambar garis koordinat (sumbu x dan y) dengan style tipis dan putus-putus
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')

# Tampilkan grid dan pastikan aspek sama (agar lingkaran tidak terdistorsi)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()