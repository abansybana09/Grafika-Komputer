import matplotlib.pyplot as plt

# Fungsi untuk menggambar garis menggunakan algoritma DDA
def dda_algorithm(x0, y0, x1, y1):
    # Inisialisasi titik awal
    x, y = x0, y0
    
    # Menghitung perbedaan koordinat
    dx = x1 - x0
    dy = y1 - y0

    # Menentukan jumlah langkah berdasarkan jarak terpanjang (steps)
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Menghitung penambahan x dan y per langkah
    x_inc = dx / steps
    y_inc = dy / steps

    # Menyimpan titik-titik hasil algoritma DDA
    x_points = [x]
    y_points = [y]

    # Loop untuk menghitung titik-titik sepanjang garis
    # Loop berjalan sebanyak 'steps' kali
    for _ in range(int(steps)):
        x += x_inc
        y += y_inc
        
        # Menyimpan koordinat dengan pembulatan ke integer terdekat
        x_points.append(round(x))
        y_points.append(round(y))
        
    # Menggambar garis menggunakan matplotlib
    # Note: plt.plot() dalam dda_algorithm hanya menambahkan satu segmen garis ke plot aktif.
    plt.plot(x_points, y_points, marker="o", color="b") 

# Fungsi untuk menggambar rumah
def draw_house():
    # Inisialisasi plot dengan ukuran tertentu
    plt.figure(figsize=(6, 6))

    # Dinding rumah (persegi)
    # Garis Kiri
    dda_algorithm(2, 2, 2, 6) 
    # Garis Atas
    dda_algorithm(2, 6, 6, 6) 
    # Garis Kanan
    dda_algorithm(6, 6, 6, 2) 
    # Garis Bawah
    dda_algorithm(6, 2, 2, 2) 

    # Atap rumah (segitiga)
    # Kiri ke puncak
    dda_algorithm(2, 6, 4, 8) 
    # Puncak ke kanan
    dda_algorithm(4, 8, 6, 6) 

    # Pintu (persegi kecil)
    # Kiri
    dda_algorithm(3, 2, 3, 4) 
    # Atas
    dda_algorithm(3, 4, 4, 4) 
    # Kanan
    dda_algorithm(4, 4, 4, 2) 
    
    # Jendela (persegi kecil)
    # Kiri
    dda_algorithm(5, 4, 5, 5) 
    # Atas
    dda_algorithm(5, 5, 6, 5) 
    # Kanan
    dda_algorithm(6, 5, 6, 4) 
    # Bawah
    dda_algorithm(6, 4, 5, 4) 

    # Menampilkan hasil gambar rumah
    plt.title("Gambar Rumah dengan Algoritma DDA")
    # Batasan sumbu X
    plt.xlim(0, 8)
    # Batasan sumbu Y
    plt.ylim(0, 10)
    # Mengatur aspek rasio agar x dan y memiliki skala yang sama (persegi)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

# Memanggil fungsi untuk menggambar rumah
draw_house()