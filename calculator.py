
print("Kalkulator Sederhana")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")
print("6. Modulus")

pilihan = int(input("Pilih operasi (1-6): "))
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

if pilihan == 1:
    print("Hasil:", a + b)
elif pilihan == 2:
    print("Hasil:", a - b)
elif pilihan == 3:
    print("Hasil:", a * b)
elif pilihan == 4:
    print("Hasil:", a / b if b != 0 else "Tidak bisa dibagi 0")
elif pilihan == 5:
    print("Hasil:", a ** b)
elif pilihan == 6:
    print("Hasil:", a % b)
else:
    print("Pilihan tidak valid")
