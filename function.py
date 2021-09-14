# Fungsi

def operasi_bilangan(first_num, second_num, operator):
    result = None
    if operator == "+":
        result = first_num + second_num
    elif operator == "-":
        result = first_num - second_num
    elif operator == "x":
        result = first_num * second_num
    elif operator == ":":
        result = first_num / second_num
    print(result)
#
# operasi_bilangan(10, 5, "+")
# operasi_bilangan(30, 15, "+")
# operasi_bilangan(50, 2, ":")
# operasi_bilangan(45, 5, "-")
def bayar(harga, duit):
    if duit < harga:
        print("Uang kamu ngga cukup, silahkan ngepet lagi!")
    elif duit >= harga:
        result = duit - harga
        if result == 0:
            print("Uang kamu pas, kalo mau beli lagi, ngepet lagi!")
        elif result > 0:
            print(f"Kamu berhasil membeli makanan yang kamu pilih.\nSisa uang kamu adalah {result} EGP")
def tentukan_harga(nomor_menu):
    harga = None
    if nomor_menu == 1:
        harga = 25
    elif nomor_menu == 2:
        harga = 30
    elif nomor_menu == 3:
        harga = 18
    elif nomor_menu == 4:
        harga = 20
    elif nomor_menu == 5:
        harga = 10
    else:
        print("Masukkan input yang benar")
    return harga

def beli_makanan():
    input_nama = input("Masukkan Nama Kamu: ")
    input_menu = int(input(f" Halo {input_nama}\nPilih Nomor makanan: "))
    input_duit = int(input("Jumlah uang kamu: "))
    harga = tentukan_harga(nomor_menu = input_menu)
    bayar(harga, input_duit)
    
# print("======== [ Selamat Datang di Toko Kopi ] ========")
# print("""
#             1. Seblak - 25 EGP
#             2. Baso Aci - 30 EGP
#             3. Cimol - 18 EGP
#             4. Cireng - 20 EGP
#             5. Bakso Goreng - 10 EGP
# """)