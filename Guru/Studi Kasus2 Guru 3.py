total = int(input("Masukkan total belanja: "))
if total > 300000:
    diskon = total * 0.2
elif total >= 200000:
    diskon = total * 0.1
else:
    diskon = 0
total_bayar = total - diskon
print("Total yang harus dibayar:", total_bayar)
