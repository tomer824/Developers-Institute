# 1.

UPDATE students
SET first_name = 'Lea' 
WHERE id_num = 5;

UPDATE students
SET birth_date = '1998-02-11' 
WHERE last_name = 'Dupont'

DELETE FROM students WHERE first_name = 'Lea' and last_name = 'Dupont';

SELECT COUNT(*)
FROM students

SELECT COUNT(*)
FROM students
WHERE birth_date > '2000-01-01'

ALTER TABLE students
ADD math_grade SMALLINT NOT NULL DEFAULT 0;

UPDATE students
SET math_grade = 80
WHERE id_num = 1;

UPDATE students
SET math_grade = 90
WHERE id_num = 2 or id_num = 4;

UPDATE students
SET math_grade = 100
WHERE id_num = 6;

SELECT COUNT(*)
FROM students
WHERE math_grade > 83;

INSERT INTO students (last_name, first_name, birth_date, math_grade)
VALUES ('Simpson', 'Omer', '1980-03-10', 70);

SELECT first_name, last_name, COUNT(math_grade) AS total_grade
FROM students
GROUP BY first_name, last_name;

SELECT SUM(math_grade)
FROM students

# 2.

SELECT * FROM public.items
ORDER BY price ASC 

SELECT * FROM public.items
WHERE price > 80
ORDER BY price DESC

SELECT first_name, last_name 
FROM public.customers
ORDER BY first_name ASC
LIMIT 3

SELECT first_name, last_name 
FROM public.customers
ORDER BY first_name DESC
LIMIT 2

SELECT last_name 
FROM public.customers
ORDER BY last_name DESC

CREATE TABLE purchases (
    customer_id SMALLINT,
    item_id SMALLINT
);

no it doesnt work, cant leave the field blank

INSERT INTO purchases (customer_id, item_id) VALUES
((SELECT id_num from customers WHERE id_num = 1),2),
((SELECT id_num from customers WHERE id_num = 2),3),
((SELECT id_num from customers WHERE id_num = 3),1),
((SELECT id_num from customers WHERE id_num = 4),1),
((SELECT id_num from customers WHERE id_num = 5),2);
**mitchel - did I get the above right? please confirm for me.

select * from purchases
this isnt very useful - to see customer number but not names it doesnt really tell me who they are

select item_id, customers.* 
from purchases
inner join customers
on purchases.customer_id = customers.id_num;

select item_id , customers.*
from purchases
inner join customers
on purchases.customer_id = customers.id_num
where customers.id_num = 4;

select item_id, customers.*
from purchases
inner join customers
on purchases.customer_id = customers.id_num
where purchases.item_id = 1 or purchases.item_id = 2;

INSERT INTO items (product, price)
VALUES ('hard drive', 50);

INSERT INTO purchases (customer_id, item_id)
VALUES (3, 4)

DELETE FROM customers WHERE first_name = 'scott';

SELECT customers.first_name, customers.last_name, items.product
FROM purchases
INNER JOIN customers ON purchases.customer_id = customers.id_num
INNER JOIN items ON purchases.item_id = items.id_num;