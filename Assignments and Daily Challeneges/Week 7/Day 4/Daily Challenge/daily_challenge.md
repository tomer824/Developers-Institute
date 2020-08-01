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


-- INSERT INTO orders (persons_name, item_id) VALUES 
-- ('Tomer', 1),('Tomer', 2), ('Chaim', 1), ('Adam', 3), ('Adam', 1)

CREATE TABLE order_total (
total_price NUMERIC,
items_id INTEGER,
order_id INTEGER,
FOREIGN KEY (items_id) REFERENCES items (id),
FOREIGN KEY (order_id) REFERENCES orders (order_id)
);

INSERT INTO order_total (items_id, order_id)
VALUES (1,2),(1,3),(2,1),(2,3),(2,2),(3,3),(1,2),(1,2),(2,1),(3, 1),(2,2);

SELECT SUM(items.price)
FROM orders
JOIN order_total ON orders.order_id = order_total.order_id
JOIN items ON order_total.items_id = items.id
WHERE orders.order_id = 2;