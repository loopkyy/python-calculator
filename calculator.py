# calculator.py
expr = input("Masukkan operasi (contoh: 12 + 5): ")

# pecah input jadi angka dan operator
parts = expr.split()
if len(parts) != 3:
    print("Format salah! gunakan contoh: 12 + 5")
else:
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
