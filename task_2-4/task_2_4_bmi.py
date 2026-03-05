#Ввод данных

mass = float(input("Вес(кг):"));
height = float(input("Рост(м):"));

#Подсчет данных

bmi = mass / (height ** 2)

#Вывод данных

print(f"--- Отчет о состоянии здоровья ---\nВес:\t{mass:.2f}\nРост:\t{height:.2f}\nИндекс массы тела пациента: {bmi:.2f}")