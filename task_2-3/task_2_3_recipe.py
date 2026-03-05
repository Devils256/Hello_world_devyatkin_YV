#Ввод данных

eat = input("Название питательной среды:");
concentration = input ("Концентрация агара(%):");
temp = input("Температура стерилизации(°C):")
eat_processed = eat.strip().upper();
concentration_processed = concentration.strip().upper();
temp_processed = temp.strip().upper();
text = (f"Введите название питательной среды:\t{eat_processed}\nВведите концентрацию агара (%):\t{concentration_processed}\nВведите температуру стерилизации (°C):\t{temp_processed}")

#Запись данных

with open("recipe.txt", "w", encoding="utf-8") as card:
    card.write(f"{text}")

#Вывод данных

print("\n Файл recipe.txt успешно сформирован!")