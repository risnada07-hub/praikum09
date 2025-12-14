# praikum09
# Latihan Exception Handling Python

Repository ini berisi latihan mandiri untuk memahami **Exception Handling** pada bahasa pemrograman **Python**, khususnya penggunaan `try-except` dalam menangani error agar program tetap berjalan dengan aman.

---

##  Latihan 1: Kalkulator Aman

### Deskripsi
Program kalkulator sederhana yang meminta:
- Dua buah angka
- Satu operator aritmatika (`+`, `-`, `*`, `/`)

Program dirancang agar mampu menangani kesalahan input dan error runtime.

### Fitur
- Menangani input bukan angka (`ValueError`)
- Menangani pembagian dengan nol (`ZeroDivisionError`)
- Menampilkan pesan error khusus jika operator tidak valid

### Contoh Kode
```python
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
        hasil = a / b
    else:
        raise Exception("Operator tidak valid!")

    print("Hasil:", hasil)

except ValueError:
    print("Error: Input harus berupa angka.")
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol.")
except Exception as e:
    print("Error:", e)
