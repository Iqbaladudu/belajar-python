def pengumuman(jumlah_infak, nama = "Hamba Allah"):
    print(f"Bapak {nama} berinfak sebanyak {jumlah_infak} EGP")
def sapa(nama, ucapan, jam):
    ucapan_split = ucapan.split()
    print(f"Halo {nama}, {ucapan}, sekarang pukul {jam} {ucapan_split[1]}")

def tambah(bil1, bil2):
    result = bil1 + bil2
    return result

def profil(**profil_data):
    for i, k in enumerate(profil_data):
        print(k, profil_data[k], sep=": ")
profil_data = {
    "Nama Depan": "Muhammad",
    "Nama Belakang": "Iqbal",
    "Alamat": "darosah",
    "Email": "iqbal.adudu@gmail.com"
}
profil(**profil_data)