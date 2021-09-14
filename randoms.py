import random

# nums = random.randint(1, 10)
# print(nums)
nama_depan = [
    "Muhammad",
    "Joko",
    "Asep",
    "Siti",
    "Iwan",
]
nama_belakang = [
    "Izzuddin",
    "Irsyad",
    "Iqbal",
    "Sultan",
    "Rian"
]
# for i in range(len(nama_depan)):
#     for x in range(len(nama_belakang)):
#             full_name = f"{nama_depan[i]} {nama_belakang[x]}"
#             print(full_name)


def getName():
    nama_depan_random = random.randint(0, len(nama_depan) - 1)
    nama_belakang_random = random.randint(0, len(nama_belakang) - 1)
    full_name = f"{nama_depan[nama_depan_random]} {nama_belakang[nama_belakang_random]}"
    print(full_name)

getName()