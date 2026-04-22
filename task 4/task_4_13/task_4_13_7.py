N = int(input("Введите количество элементов массива: "))
if N < 1:
    print("Ошибка: Массив не может быть пустым")
else:
     summa = 0
i = 1
while i <= N:
        num = float(input(f"Введите элемент {i}: "))
        summa = summa + num
        i = i + 1
average = summa / N
print(f"Среднее арифметическое: {average}")