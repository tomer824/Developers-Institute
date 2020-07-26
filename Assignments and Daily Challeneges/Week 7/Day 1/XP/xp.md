CREATE TABLE items (
	id_num SERIAL PRIMARY KEY,
    product VARCHAR (100),
    price SMALLINT,
);

CREATE TABLE customers (
	id_num SERIAL PRIMARY KEY,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (100) NOT NULL,
);

INSERT INTO items (product, price)
VALUES ('small desk', 100), ('large desk', 300), ('fan', 80);

INSERT INTO customers (first_name, last_name)
VALUES ('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');

SELECT * FROM customers
SELECT * FROM items
SELECT * FROM items WHERE price > 80
SELECT * FROM items WHERE price < 30
SELECT * FROM customers WHERE last_name = 'smith'
SELECT * FROM customers WHERE NOT first_name = 'Craig'