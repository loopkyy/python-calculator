print("Kalkulator Sederhana")
print("Gunakan format: <angka> <operator> <angka>")
print("Operator: +  -  *  /  ^  %")
print("Ketik 'exit' untuk keluar.\n")

while True:
    expr = input("> ")

    if expr.lower() == "exit":
        print("Keluar dari kalkulator.")
        break

    parts = expr.split()
    if len(parts) != 3:
        print("Format salah! Contoh: 12 + 5")
        continue

    a, op, b = parts
    a = float(a)
    b = float(b)

    if op == '+':
        print("Hasil:", a + b)
    elif op == '-':
        print("Hasil:", a - b)
    elif op == '*':
        print("Hasil:", a * b)
    elif op == '/':
        print("Hasil:", a / b if b != 0 else "Tidak bisa dibagi 0")
    elif op == '^':
        print("Hasil:", a ** b)
    elif op == '%':
        print("Hasil:", a % b)
    else:
        print("Operator tidak dikenali:", op)
