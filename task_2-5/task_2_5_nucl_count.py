#Ввод данных

sequence = input("Введите последовательность ДНК: ");

#Обработка данных

sequence_upper = sequence.upper();

#Вывод первичных данных

print(f"\n=== Анализ последовательности ДНК ===\nПоследовательность в верхнем регистре: {sequence_upper}\n");

#Подсчет данных

count_A = sequence_upper.count("A");
count_T = sequence_upper.count("T");
count_G = sequence_upper.count("G");
count_C = sequence_upper.count("C");

# Длина последовательности

length = len(sequence_upper);

print(f"Подсчёт нуклеотидов:\nA: {count_A}\nT: {count_T}\nG: {count_G}\nC: {count_C}\n");
print(f"Общая длина: {length} нуклеотидов\n");

# Вывод вторичных данных

print("Процентное содержание нуклеотидов:")
print(f"A: {count_A / length * 100:.2f}%\nT: {count_T / length * 100:.2f}%\nG: {count_G / length * 100:.2f}%\nC: {count_C / length * 100:.2f}%");