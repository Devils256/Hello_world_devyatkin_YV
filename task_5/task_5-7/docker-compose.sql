
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS prices;
DROP TABLE IF EXISTS products;


CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50)
);

CREATE TABLE prices (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    price NUMERIC(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    product_id INTEGER REFERENCES products(id)
);

INSERT INTO products (name, category) VALUES
('Ноутбук', 'Электроника'),
('Смартфон', 'Электроника'),
('Наушники', 'Аксессуары'),
('Монитор', 'Электроника'),
('Клавиатура', 'Аксессуары');

INSERT INTO prices (product_id, price) VALUES
(1, 55000.00),
(2, 35000.00),
(3, 2500.00),
(4, 18000.00),
(5, 1200.00);

INSERT INTO suppliers (name, product_id) VALUES
('ООО ТехноТрейд', 1),
('ИП Электроникс', 1),
('ООО ТехноТрейд', 2),
('ООО АксессуарПлюс', 3),
('ООО ТехноТрейд', 4),
('ИП Электроникс', 5);

SELECT * FROM products;
SELECT * FROM prices;
SELECT * FROM suppliers;