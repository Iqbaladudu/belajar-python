from function import bayar, tentukan_harga

# Lapak Kopi
print("======== [ Selamat Datang di Toko Kopi Kami ] ========")
print("1. Arabica - 15 EGP\n2. Espresso - 20 EGP")
def beli():
    input_nama = input("Masukkan Nama Kamu: ")
    input_menu = int(input(f" Halo {input_nama}\nPilih Nomor makanan: "))
    input_duit = int(input("Jumlah uang kamu: "))
    harga = tentukan_harga(input_menu)
    bayar(harga, input_duit)
beli()