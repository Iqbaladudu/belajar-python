# Membuat list
nilai = [89, 65, 64, 78, 65, 56, 43, 78, 75, 56]
# Memperbarui nilai list
nilai[6] = 50
# Append nilai dalam list
nilai.append(90)
# Insert nilai
nilai.insert(1, 100)
# Menghapus index ke-x
nilai.pop(1)
# remove method
nilai.remove(89)

# del keyword
del nilai[len(nilai)-1]
# Concatinating list
nilai2 = [67, 100]
full_nilai = nilai + nilai2
nilai.extend(nilai2)

# slicing
print(nilai)
# print(nilai[0:6])
# print(nilai[6:])
# print(nilai[5::2])

# enumerate