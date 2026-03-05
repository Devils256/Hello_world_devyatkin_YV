# Данные

chem_element = input("Название хим. элемента:");
amount_element = input("Количество(целое число):");
processed_chem = chem_element.strip().upper();
processed_amount = amount_element.strip().upper();
text_print = (f"Реактив {processed_chem} поступил на склад в количестве {processed_amount} шт..")

# Вывод данных в текстовый файл

f = open("inventory.txt", "w", encoding="utf-8");
print(f"{text_print}", file=f);
f.close();

# Вывод данных оператору

print(f"{text_print}");