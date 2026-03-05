#Ввод данных

protein = int(input("Масса белка(г):"));
jir = int(input("Масса жира(г):"));
uglevod = int(input("Масса углеводов(г):"));

#Подсчет данных

count = (protein * 4) + (jir * 9) + (uglevod * 4);

#Вывод данных

print(f"Калорийность =", count);