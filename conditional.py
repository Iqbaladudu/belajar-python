print("==========[ Selamat Datang di Program Pemesanan Kopi ]==========")
nama = input("Masukkan Nama Kamu: ")
menu_input = input(
    f"Halo {nama}, Kamu mau pesan apa?:\n1.Kopi Arabica - 10 EGP\n2.Kopi Robusta - 15 EGP\n3.Espresso - 7 EGP\n4.Late - 17 EGP\nKamu pilih nomor berapa: ")
menu_input_int = int(menu_input)
uang = input("Berapa uang kamu yang kamu kasih: ")
uang_int = int(uang)

if menu_input_int == 1:
    print("Kamu akan membeli Arabica seharga 10 EGP")
    if uang_int == 10:
        print("Uang kamu pas.")
    elif uang_int > 10:
        kembalian = uang_int - 10
        print(f"Kamu memberikan uang {uang} EGP, kembaliannya {kembalian} EGP")
    elif uang_int < 10:
        print("Uang kamu ga cukup.\nCari lagi.")

