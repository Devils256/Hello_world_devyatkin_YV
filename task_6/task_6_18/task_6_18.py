import pandas as pd
from sqlalchemy import create_engine, text

# Параметры подключения
host = "localhost"
port = "5435"
user = "postgres"
password = "student"
database = "student_task"

engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

# 1. Проверка соединения
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("✓ Подключение к PostgreSQL установлено")
except Exception as e:
    print(f"Ошибка подключения: {e}")
    exit()

# 2. JOIN-запрос с правильными именами колонок
query = """
SELECT 
    p.name AS product_name,
    p.category,
    pr.price
FROM prices pr
JOIN products p ON pr.product_id = p.id
"""
df = pd.read_sql(query, engine)

print("\nПервые 5 строк полученных данных:")
print(df.head())
print(f"\nВсего записей: {len(df)}")
print(f"Уникальных товаров: {df['product_name'].nunique()}")
print(f"Уникальных категорий: {df['category'].nunique()}")

# 3. Основные статистики по цене
print("\n=== Статистика по цене ===")
print(f"Среднее значение: {df['price'].mean():.2f} руб.")
print(f"Медиана:          {df['price'].median():.2f} руб.")
print(f"Станд. отклонение:{df['price'].std():.2f} руб.")
print(f"Минимальная цена: {df['price'].min():.2f} руб.")
print(f"Максимальная цена:{df['price'].max():.2f} руб.")

# 4. Квартили и товары с ценой выше Q3
Q1 = df['price'].quantile(0.25)
Q2 = df['price'].quantile(0.50)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

print("\n=== Квартили и IQR ===")
print(f"Q1 (25%): {Q1:.2f} руб.")
print(f"Q2 (50%): {Q2:.2f} руб.")
print(f"Q3 (75%): {Q3:.2f} руб.")
print(f"Межквартильный размах (IQR): {IQR:.2f} руб.")

high_price = df[df['price'] > Q3]
print("\n=== Товары с ценой выше Q3 ===")
if high_price.empty:
    print("Нет товаров с ценой выше Q3.")
else:
    for _, row in high_price.iterrows():
        print(f"{row['product_name']} ({row['category']}): {row['price']:.2f} руб.")

# 5. Группировка по категориям
grouped = df.groupby('category')['price'].agg(
    count='count',
    mean_price='mean',
    median_price='median',
    std_price='std'
).round(2).sort_values('mean_price', ascending=False)

print("\n=== Статистика по категориям (сортировка по убыванию средней цены) ===")
print(grouped.to_string())

# 6. Топ-5 товаров с наибольшим разбросом цен
price_range = df.groupby('product_name')['price'].agg(['min', 'max'])
price_range['diff'] = price_range['max'] - price_range['min']
top5 = price_range.nlargest(5, 'diff')

print("\n=== Топ-5 товаров с наибольшим разбросом цен ===")
if top5.empty:
    print("Нет данных.")
else:
    for product, row in top5.iterrows():
        print(f"{product}: min = {row['min']:.2f} руб., max = {row['max']:.2f} руб., разброс = {row['diff']:.2f} руб.")


