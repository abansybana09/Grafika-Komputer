import matplotlib.pyplot as plt

def draw_square(vertices, title):
    x, y = zip(*vertices)
    x += (x[0],)
    y += (y[0],)

    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def scale_square(vertices, scale_factor):
    scaled_vertices = [(x * scale_factor, y * scale_factor) for x, y in vertices]
    return scaled_vertices

print("Masukkan titik-titik persegi (x1 y1), (x2 y2), (x3 y3), (x4 y4):")
x1, y1 = map(float, input("Titik 1: ").split())
x2, y2 = map(float, input("Titik 2: ").split())
x3, y3 = map(float, input("Titik 3: ").split())
x4, y4 = map(float, input("Titik 4: ").split())

square_vertices = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
scale_factor = float(input("Masukkan faktor skala: "))

draw_square(square_vertices, "Persegi Asli")

scaled_square_vertices = scale_square(square_vertices, scale_factor)
draw_square(scaled_square_vertices, f"Persegi Setelah Penskalaan (Faktor Skala = {scale_factor})")