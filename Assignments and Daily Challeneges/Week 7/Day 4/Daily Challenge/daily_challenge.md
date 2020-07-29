CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    persons_name VARCHAR (50),
    item_id integer,
    FOREIGN KEY (item_id) REFERENCES items (id)
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
	name VARCHAR (50),
    price NUMERIC
);


INSERT INTO items (food, price) VALUES ('Hotdog', '1.00'), ('Pizza', '2.50'), ('Fries', '1.50');


