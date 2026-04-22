a = float(input("Введите первое число (a): "))
b = float(input("Введите второе число (b): "))
c = float(input("Введите третье число (c): "))
d = float(input("Введите четвёртое число (d): "))
min_value = a
if b < min_value:
    min_value = b
if c < min_value:
    min_value = c
if d < min_value:
    min_value = d
print("Минимальное число:", min_value)