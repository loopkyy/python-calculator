a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

print("Hasil penjumlahan:", a + b)
print("Hasil pengurangan:", a - b)
print("Hasil perkalian:", a * b)

if b != 0:
    print("Hasil pembagian:", a / b)
else:
    print("Tidak bisa dibagi 0")

print("Hasil pangkat:", a ** b)
print("Hasil modulus:", a % b)
