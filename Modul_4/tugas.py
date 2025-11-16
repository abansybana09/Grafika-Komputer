import matplotlib.pyplot as plt

def midpoint_circle(h, k, r):
    x = 0
    y = r
    points = set()
    
    p = 1 - r

    # tambahkan semua 8 simetri untuk titik awal
    points.update([
        (x + h, y + k),
        (h - x, k + y),
        (h + x, k - y),
        (h - x, k - y),
        (h + y, k + x),
        (h - y, k + x),
        (h + y, k - x),
        (h - y, k - x)
    ])
    
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
            
        points.update([
            (x + h, y + k),
            (h - x, k + y),
            (h + x, k - y),
            (h - x, k - y),
            (h + y, k + x),
            (h - y, k + x),
            (h + y, k - x),
            (h - y, k - x)
        ])
    return list(points)

center_x = 0
center_y = 0
radius = 10

circle_points = midpoint_circle(center_x, center_y, radius)

# ubah titik menjadi dua list untuk plotting
xs = [p[0] for p in circle_points]
ys = [p[1] for p in circle_points]

plt.figure(figsize=(8,8))
plt.scatter(xs, ys, s=30, color='blue')  # gunakan scatter untuk kontrol ukuran titik

# set padding per sisi (kanan, kiri, atas, bawah)
pad_right  = 0.2
pad_left   = 0.2
pad_top    = 0.2
pad_bottom = 0.2

x_min = center_x - radius - pad_left
x_max = center_x + radius + pad_right
y_min = center_y - radius - pad_bottom
y_max = center_y + radius + pad_top

ax = plt.gca()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

plt.title('lingkaran dengan menggunakan algoritma midpoint circle')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
ax.set_aspect('equal', adjustable='box')
plt.show()