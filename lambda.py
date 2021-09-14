def addition(num1, num2):
    return num1 + num2
name = "Iqbal"
addition = lambda num1, num2: num1 + num2
# print(addition(10, 10))

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
genap = list(map(lambda x: , li))

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
genap = list(filter(lambda x: (x % 2 == 0), li))
print(genap)
