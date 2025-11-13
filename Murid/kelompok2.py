# Program Diskon 25% untuk Belanja di atas Rp500.000

# Input total belanja
total = int(input("Masukkan total belanja: Rp "))

# Hitung diskon
if total > 500000:
    diskon = 0.25 * total
else:
    diskon = 0

# Hitung total bayar
total_bayar = total - diskon

# Cetak hasil transaksi
print("\n=== HASIL TRANSAKSI ===")
print(f"Total Belanja : Rp {total:,.0f}")
print(f"Diskon (25%)  : Rp {diskon:,.0f}")
print(f"Total Bayar   : Rp {total_bayar:,.0f}")
print("========================")
