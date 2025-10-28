import matplotlib.pyplot as plt

# DDA points (rounded)
dda_points = [(20,10),(21,11),(22,12),(23,12),(24,13),(25,14),(26,15),
              (27,16),(28,17),(29,17),(30,18)]

# Bresenham points
bres_points = [(20,10),(21,11),(22,12),(23,12),(24,13),(25,14),(26,15),
               (27,16),(28,16),(29,17),(30,18)]

# Pisahkan X dan Y
dda_x = [p[0] for p in dda_points]
dda_y = [p[1] for p in dda_points]

bres_x = [p[0] for p in bres_points]
bres_y = [p[1] for p in bres_points]

# Plot
plt.figure()
plt.plot([20,30],[10,18])               # ideal line
plt.scatter(dda_x, dda_y, marker='o', label="DDA")
plt.scatter(bres_x, bres_y, marker='x', label="Bresenham")
plt.title("Perbandingan DDA dan Bresenham\n(20,10) → (30,18)")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().invert_yaxis()  # koordinat layar
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
