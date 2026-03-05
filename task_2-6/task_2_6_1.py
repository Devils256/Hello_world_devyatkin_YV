pH = int(input("Введите pH среды:"))
if pH < 7:
    print("Кислая среда")
elif pH > 7:
    print("Щелочная среда")
else:
    print("Нейтральная среда")