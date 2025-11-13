# Program Diskon Bertingkat ala SmartShop

# Input total belanja
total = int(input("Masukkan total belanja: Rp "))

# Tentukan diskon berdasarkan total belanja
if total > 1000000:
    diskon = 0.30 * total     # 30% untuk di atas 1 juta
elif total > 500000:
    diskon = 0.20 * total     # 20% untuk di atas 500 ribu
elif total > 100000:
    diskon = 0.10 * total     # 10% untuk di atas 100 ribu
elif total > 50000:
    diskon = 0.05 * total     # 5% untuk di atas 50 ribu
else:
    diskon = 0                # Tidak ada diskon

# Hitung total bayar
total_bayar = total - diskon

# Cetak hasil transaksi
print("\n=== HASIL TRANSAKSI ===")
print(f"Total Belanja : Rp {total:,.0f}")
print(f"Diskon        : Rp {diskon:,.0f}")
print(f"Total Bayar   : Rp {total_bayar:,.0f}")
print("========================")
