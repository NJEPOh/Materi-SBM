total = int(input("Masukkan total belanja: "))
if total > 200000:
    diskon = total * 0.15
    total_bayar = total - diskon
else:
    total_bayar = total
print("Total yang harus dibayar:", total_bayar)
