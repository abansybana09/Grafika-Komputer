import numpy as np
import cv2

# Membuat canvas abu-abu muda
canvas = np.ones((400, 600, 3), dtype=np.uint8) * 240  # Warna abu-abu muda

# Mendefinisikan warna dalam format BGR
BLUE = (255, 0, 0)      # Biru
GREEN = (0, 255, 0)     # Hijau
RED = (0, 0, 255)       # Merah
YELLOW = (0, 255, 255)  # Kuning
WHITE = (255, 255, 255) # Putih

# Koordinat titik-titik persegi panjang
points = [
    (100, 100),  # Kiri atas
    (500, 100),  # Kanan atas
    (500, 300),  # Kanan bawah
    (100, 300)   # Kiri bawah
]

# Menggambar garis penghubung titik dengan warna gradien
colors = [BLUE, GREEN, RED, YELLOW]
for i in range(len(points)):
    # Warna akan diambil dari titik awal setiap garis
    cv2.line(canvas, points[i], points[(i+1)%4], colors[i], 2)

# Menggambar titik pada setiap sudut dengan warna berbeda
colors = [BLUE, GREEN, RED, YELLOW]
labels = ['A', 'B', 'C', 'D']

for i, (point, color, label) in enumerate(zip(points, colors, labels)):
    # Menggambar lingkaran besar
    cv2.circle(canvas, point, 10, color, -1)
    # Menambahkan outline putih
    cv2.circle(canvas, point, 10, WHITE, 2)
    # Menambahkan label
    cv2.putText(canvas, label, (point[0]-10, point[1]-15), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

# Menampilkan gambar
cv2.imshow('Persegi Panjang dengan Titik Berwarna', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
