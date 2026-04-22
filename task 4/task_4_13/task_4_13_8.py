N = int(input("Введите количество элементов массива: "))
if N < 1:
    print("Ошибка: Массив не может быть пустым")
else:
    count = 0
i = 1
while i <= N:
        num = float(input(f"Введите элемент {i}: "))
        if num > 0:
            count = count + 1
        i = i + 1
print(f"Количество положительных чисел: {count}")