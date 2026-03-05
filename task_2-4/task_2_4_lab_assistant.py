#Ввод данных

volume = int(input("Введите нужный объем раствора (в мл): "));

#Подсчет данных

salt_mass = volume * 0.009;
water_volume = volume;

#Ввод данных в текстовой файл

with open("recipe2.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли:  {salt_mass:.2f} г\n")
    file.write(f"Объем воды:  {water_volume} мл\n");

#Вывод данных

print("Рецепт записан в recipe.txt");