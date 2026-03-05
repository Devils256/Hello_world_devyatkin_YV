#Ввод данных

name = input("Введите имя оператора:");
value = input("Введите текущее значение датчика давления");
name_processed = name.strip().upper();
value_processed = value.strip().upper();
text = (f"Имя оператора:\t\t\t{name_processed}\nТекущее давление:\t\t\t{value_processed}")

# Запись данных
with open("sensor_log.txt", "w", encoding="utf-8") as card:
    card.write(f"{text}")

# Вывод данных

print("\nДанные успешно сохранены в sensor_log.txt")
