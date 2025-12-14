try:
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    operator = input("Masukkan operator (+, -, *, /): ")

    if operator == "+":
        hasil = a + b
    elif operator == "-":
        hasil = a - b
    elif operator == "*":
        hasil = a * b
    elif operator == "/":
        hasil = a / b  # bisa memicu ZeroDivisionError
    else:
        raise Exception("Operator tidak valid! Gunakan +, -, *, atau /")

    print("Hasil:", hasil)

except ValueError:
    print("Error: Input harus berupa angka.")
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol.")
except Exception as e:
    print("Error:", e)
