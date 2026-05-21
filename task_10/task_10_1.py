# Задача 1 (учёт сырья и партий)

products = [
    {"sku": "A1", "category": "flour", "expected": 100, "actual": 95},
    {"sku": "B2", "category": "sugar", "expected": 50, "actual": 50},
    {"sku": "C3", "category": "enzyme", "expected": 10, "actual": 12},
]

# 1. Список расхождений
discrepancies = [
    (product["sku"], product["actual"] - product["expected"])
    for product in products
    if product["actual"] != product["expected"]
]

# 2. Словарь по категориям
by_category = {}
for product in products:
    by_category.setdefault(product["category"], []).append(product["sku"])

print("discrepancies:", discrepancies)
print("by_category:", by_category)