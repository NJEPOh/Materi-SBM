total = int(input("Masukkan total belanja: "))
if total > 100000:
    diskon = total * 0.1
    total_bayar = total - diskon
else:
    total_bayar = total
print("Total yang harus dibayar:", total_bayar)
