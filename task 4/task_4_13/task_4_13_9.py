N = int(input("Введите количество элементов массива: "))
if N < 1:
    print("Ошибка: Массив не может быть пустым")
else:
    summa = 0
i = 1
while i <= N:
        num = int(input(f"Введите элемент {i}: "))
        if num % 2 != 0:  # Проверка на нечетность
            summa = summa + num
        i = i + 1
print(f"Сумма нечетных элементов: {summa}")