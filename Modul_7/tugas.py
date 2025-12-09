import numpy as np
import matplotlib.pyplot as plt

def draw_parallelogram(pts):
	poly = plt.Polygon(pts, closed=True, fill=False, edgecolor='b')
	plt.gca().add_patch(poly)

def rotate_about_centroid(pts, angle):
	rad = np.radians(angle)
	R = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
	c = pts.mean(axis=0)
	return (pts - c).dot(R.T) + c

# Input koordinat titik-titik jajargenjang
print("Masukkan koordinat 4 titik jajargenjang:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))
x4 = float(input("x4: "))
y4 = float(input("y4: "))

pts = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
angle = int(input("Masukkan sudut rotasi (derajat): "))

plt.figure(figsize=(6, 6))
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
draw_parallelogram(pts)
plt.title('Jajargenjang Sebelum Rotasi')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

rot_pts = rotate_about_centroid(pts, angle)

plt.figure(figsize=(6, 6))
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().add_patch(plt.Polygon(rot_pts, closed=True, fill=False, edgecolor='r'))
plt.title(f'Jajargenjang Setelah Rotasi ({angle} Derajat)')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()