nama_input  = input("Siapa nama kamu: ")
kedatangan = input("Jam berapa datang: ")
kedatangan_int = int(kedatangan)

if kedatangan_int == 5 or kedatangan_int == 6:
    print(f"Halo {nama_input}, kamu datangnya cepat yaa.")
if kedatangan_int > 6 and kedatangan_int <= 12:
    print(f"Halo {nama_input}, selamat! Kamu telat.")
if kedatangan_int > 12:
    print(f"Halo {nama_input}, Selamat kamu dipecat!")
