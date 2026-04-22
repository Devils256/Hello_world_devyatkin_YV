N = int(input("Введите количество чисел: "))
if N < 1:
    print("Ошибка: N должно быть больше или равно 1")
else:
     max_value = float(input("Введите число 1: "))
i = 2
while i <= N:
        num = float(input(f"Введите число {i}: "))
        if num > max_value:
            max_value = num
        i = i + 1
print(f"Максимальное число: {max_value}")