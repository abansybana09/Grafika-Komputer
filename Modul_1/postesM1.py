# Import modul math untuk operasi matematika
import math

# Mendefinisikan fungsi untuk menghitung luas lingkaran
def hitung_luas_lingkaran(radius):
    # Menghitung luas menggunakan rumus pi * r^2
    luas = math.pi * radius ** 2
    # Mengembalikan nilai luas yang telah dihitung
    return luas

# Mendefinisikan fungsi untuk menghitung keliling lingkaran
def hitung_keliling_lingkaran(radius):
    # Menghitung keliling menggunakan rumus 2 * pi * r
    keliling = 2 * math.pi * radius
    # Mengembalikan nilai keliling yang telah dihitung
    return keliling

# Nilai jari-jari lingkaran
radius = 5

# Memanggil fungsi hitung_luas_lingkaran dan menyimpan hasilnya
luas = hitung_luas_lingkaran(radius)
# Memanggil fungsi hitung_keliling_lingkaran dan menyimpan hasilnya
keliling = hitung_keliling_lingkaran(radius)

# Menampilkan hasil perhitungan luas lingkaran
print(f"Luas lingkaran dengan jari-jari {radius} adalah: {luas:.2f}")
# Menampilkan hasil perhitungan keliling lingkaran
print(f"Keliling lingkaran dengan jari-jari {radius} adalah: {keliling:.2f}")
