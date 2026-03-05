#Ввод данных

total_capsules = int(input("Введите общее количество произведенных капсул: "));
package_size = int(input("Введите количество капсул в одной упаковке: "));

#Подсчет данных

full_packages = total_capsules // package_size
remaining_capsules = total_capsules % package_size

# Вывод данных

print(f"\n--- Отчет фасовочного цеха ---\nПолных упаковок:\t{full_packages}\nОстаток капсул:\t\t{remaining_capsules}");