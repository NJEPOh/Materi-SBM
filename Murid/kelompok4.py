# Program Diskon Tambahan untuk Pelanggan Tetap

# Input total belanja
total = int(input("Masukkan total belanja: Rp "))

# Tanya apakah pelanggan tetap
pelanggan_tetap = input("Apakah pelanggan tetap? (y/n): ").lower() == 'y'

# Hitung diskon utama
if total > 300000:
    diskon_utama = 0.10 * total
else:
    diskon_utama = 0

# Diskon tambahan khusus pelanggan tetap
if pelanggan_tetap:
    diskon_tambahan = 0.05 * total
else:
    diskon_tambahan = 0

# Total diskon keseluruhan
total_diskon = diskon_utama + diskon_tambahan
total_bayar = total - total_diskon

# Cetak hasil transaksi
print("\n=== HASIL TRANSAKSI ===")
print(f"Total Belanja     : Rp {total:,.0f}")
print(f"Diskon Utama (10%): Rp {diskon_utama:,.0f}")
print(f"Diskon Tambahan   : Rp {diskon_tambahan:,.0f}")
print(f"Total Diskon      : Rp {total_diskon:,.0f}")
print(f"Total Bayar       : Rp {total_bayar:,.0f}")
print("========================")
