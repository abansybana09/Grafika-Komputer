import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

# Persegi panjang pertama (4x2)
rect1 = patches.Rectangle((0, 0), 4, 2, edgecolor='blue', facecolor='lightblue')

# Persegi panjang kedua (3x2) menempel di sisi kanan rect1
rect2 = patches.Rectangle((4, 0), 3, 2, edgecolor='green', facecolor='lightgreen')

# Tambahkan ke plot
ax.add_patch(rect1)
ax.add_patch(rect2)

# Atur tampilan
ax.set_xlim(-1, 8)
ax.set_ylim(-1, 4)
ax.set_aspect('equal')
plt.grid(True)
plt.title("Dua Persegi Panjang Menyatu")
plt.show()
