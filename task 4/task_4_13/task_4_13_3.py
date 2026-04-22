N = int(input("Введите число N: "))
if N < 0:
    print("Ошибка: Факториал отрицательного числа не существует")
else:
    fact = 1
    i = 1
    while i <= N:
        fact = fact * i
        i = i + 1
print(f"{N}! = {fact}")