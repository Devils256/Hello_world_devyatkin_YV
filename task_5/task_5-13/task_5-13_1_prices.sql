UPDATE prices
SET price = price * 1.1
WHERE price < 1000;

SELECT * FROM prices WHERE price < 1000;
ROLLBACK;