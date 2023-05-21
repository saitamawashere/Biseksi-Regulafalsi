def fungsi(x):
    # Definisikan fungsi yang ingin dihitung di sini
    return x**2 - 4

def biseksi(a, b, toleransi):
    # Metode Biseksi
    if fungsi(a) * fungsi(b) >= 0:
        print("Tidak terdapat akar pada rentang ini.")
        return None

    iterasi = 0
    while (b - a) >= toleransi:
        iterasi += 1
        c = (a + b) / 2
        if fungsi(c) == 0.0:
            break
        if fungsi(c) * fungsi(a) < 0:
            b = c
        else:
            a = c

    print("Metode Biseksi:")
    print("Jumlah iterasi:", iterasi)
    print("Akar yang ditemukan:", c)

def regulafalsi(a, b, toleransi):
    # Metode Regula Falsi
    if fungsi(a) * fungsi(b) >= 0:
        print("Tidak terdapat akar pada rentang ini.")
        return None

    iterasi = 0
    while abs(b - a) >= toleransi:
        iterasi += 1
        c = (a * fungsi(b) - b * fungsi(a)) / (fungsi(b) - fungsi(a))
        if fungsi(c) == 0.0:
            break
        if fungsi(c) * fungsi(a) < 0:
            b = c
        else:
            a = c

    print("Metode Regula Falsi:")
    print("Jumlah iterasi:", iterasi)
    print("Akar yang ditemukan:", c)

# Input rentang dan toleransi dari user
a = float(input("Masukkan batas bawah rentang: "))
b = float(input("Masukkan batas atas rentang: "))
toleransi = float(input("Masukkan toleransi: "))

# Hitung menggunakan metode Biseksi
biseksi(a, b, toleransi)

# Hitung menggunakan metode Regula Falsi
regulafalsi(a, b, toleransi)