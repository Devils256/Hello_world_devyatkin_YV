N = int(input("Введите число N: "))
if N < 1:
    print("Ошибка: N должно быть больше или равно 1")
else:
    summa = 0
    i = 1
    while i <= N:
        summa = summa + i
        i = i + 1
print(f"Сумма чисел от 1 до {N}: {summa}")