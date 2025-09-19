
history = []

print("Kalkulator Sederhana")
print("Format: <angka> <operator> <angka>")
print("Operator: +  -  *  /  ^  %")
print("Ketik 'history' untuk lihat riwayat, 'exit' untuk keluar.\n")

while True:
    expr = input("> ")

    if expr.lower() == "exit":
        print("Keluar dari kalkulator.")
        break

    if expr.lower() == "history":
        if not history:
            print("Belum ada riwayat.")
        else:
            for i, (e, h) in enumerate(history, 1):
                print(f"{i}. {e} = {h}")
        continue

    parts = expr.split()
    if len(parts) != 3:
        print("Format salah! Contoh: 12 + 5")
        continue

    a, op, b = parts
    a = float(a)
    b = float(b)

    if op == '+':
        hasil = a + b
    elif op == '-':
        hasil = a - b
    elif op == '*':
        hasil = a * b
    elif op == '/':
        hasil = a / b if b != 0 else "Tidak bisa dibagi 0"
    elif op == '^':
        hasil = a ** b
    elif op == '%':
        hasil = a % b
    else:
        print("Operator tidak dikenali:", op)
        continue

    print("Hasil:", hasil)
    history.append((expr, hasil))
