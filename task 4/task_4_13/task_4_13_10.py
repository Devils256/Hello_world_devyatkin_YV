N = int(input("Введите количество элементов массива: "))
if N < 1:
    print("Ошибка: Массив не может быть пустым")
else:
    summa = 0
for i in range(1, N + 1):
        num = float(input(f"Введите элемент {i}: "))
        if i % 2 != 0:
            summa = summa + num
print(f"Сумма элементов с нечётными индексами: {summa}")