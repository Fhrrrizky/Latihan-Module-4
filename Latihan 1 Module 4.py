harga = int(input("Masukkan Harga Belanja: Rp "))

if harga >= 250000:
    diskon = harga * 50 / 100
    total_diskon = harga - diskon
    print("Diskon Yang Anda Dapatkan: Rp {:,.2f}".format(diskon))
    print("Total Pembayaran Setelah Diskon: Rp {:,.2f}".format(total_diskon))
else:
    print("Belanjaan Tidak Mendapat Diskon. Total Pembayaran: Rp {:,.2f}".format(harga))