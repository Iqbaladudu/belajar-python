# x = 1
# while x <= 10:
#     print(x)
#     x = x + 1

# list = [5,8,1,3,2]
# lanjut = True
# while lanjut == True:
#     lanjut = False
#     for i in range(len(list) - 1):
#         if list[i] > list[i+1]:
#             list[i], list[i+1] = list[i+1], list[i]
#             lanjut = True
# print(list)



# nikah = False
# jodoh = False
# waktu = 0
# while nikah == False:
#     print("Mencari jodoh")
#     if jodoh == False:
#         waktu = waktu + 1
#         print(waktu)
#         if waktu == 20:
#             print("Jodoh ditemukan")
#             jodoh = True
#             nikah = True

# number_input = int(input("Masukkan Angka yang akan dicari: "))
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(f"Mencari angka {number_input} ....")
#     if number_input == number:
#         print(f"Angka {number_input} ditemukan.")
#         break

numbers           = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 3:
        continue
    print(number)

