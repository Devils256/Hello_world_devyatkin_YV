fio = input("ФИО исследователя:");
date = input("Дата:");
name = input("Эксперимент:")
conclusion = input("Вывод:")
fio_processed = fio.strip().upper();
date_processed = date.strip().upper();
name_processed = name.strip().upper();
conclusion_processed = conclusion.strip().upper();
text = (f"______________________________________________\nЭлектронный лабораторный журнал\n______________________________________________\nФИО исследователя:\t{fio_processed}\nДата:\t{date_processed}\nЭксперимент:\t{name_processed}\nВывод:\t{conclusion_processed}\n______________________________________________")

# Запись данных в текстовой файл

with open("journal.txt", "w", encoding="utf-8") as card:
    card.write(f"{text}")

# Вывод данных оператору

print("\nФайл 'journal.txt' успешно сформирован!")