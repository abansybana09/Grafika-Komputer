import matplotlib.pyplot as plt
import numpy as np

# tentukan ukuran canvas
canvas_width = 10
canvas_height = 10

# membuat canvas kosong dengan latar belakang putih
canvas = plt.figure(figsize=(canvas_width, canvas_height))
ax = canvas.add_subplot(111)

# matikan axis (sumbu)
ax.axis('off')

# buat beberapa titik dengan warna berbeda membentuk pola
colors = ['ro', 'bo', 'go', 'mo', 'co']  # red, blue, green, magenta, cyan
points = [
    (3, 3), (3, 7), (7, 3), (7, 7),  # sudut-sudut
    (5, 5)  # tengah
]

# gambar titik-titik
for point, color in zip(points, colors):
    ax.plot(point[0], point[1], color, markersize=10)

# tambahkan garis penghubung antar titik
for i in range(len(points)-1):
    x = [points[i][0], points[i+1][0]]
    y = [points[i][1], points[i+1][1]]
    ax.plot(x, y, '--k', alpha=0.5)  # garis putus-putus hitam dengan transparansi

# tampilkan canvas
plt.show()
