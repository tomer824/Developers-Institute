UPDATE film
SET language_id = 2
WHERE title = 'Date Speed' or title = 'Amadeus Holy' or title ='Arabia Dogma';

INSERT INTO address (address, district, city_id, postal_code, phone, last_update) VALUES
('Menachem Begin 48', 'Tel Aviv', '533', '44660', '585556636', '2020-07-28'),
('Menachem Begin 58', 'Tel Aviv', '533', '44660', '585556636', '2020-07-28'),
('Menachem Begin 68', 'Tel Aviv', '533', '44660', '585556636', '2020-07-28')

INSERT INTO customer (store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active) VALUES
(1, 'Tomer', 'Goldstein', 'tomer@gmail.com', 606, 'True', '2020-07-28', '2020-07-28', 1),
(2, 'Chaim', 'Wiesner', 'chaim@gmail.com', 607, 'True', '2020-07-28', '2020-07-28', 1),
(1, 'Jason', 'Kipp', 'jason@gmail.com', 608, 'True', '2020-07-28', '2020-07-28', 1)

process of #3 same as #2

we never created customer_review (thats in the ninja assignment, did not do it) - but you wouldnt be able to delete the table because it is reliant on other tables and has foreign keys

SELECT actor.first_name, actor.last_name, film.title, film.description
FROM actor
INNER JOIN film_actor
ON actor.actor_id = film_actor.actor_id
INNER JOIN film
ON film.film_id = film_actor.film_id
WHERE actor.last_name = 'Monroe' AND actor.first_name = 'Penelope' AND film.description LIKE '%Sumo%';

SELECT film.title, film.rating, film.length, category.name
FROM film
INNER JOIN film_category
ON film_category.film_id = film.film_id
INNER JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = 'Documentary' AND film.length < 60;

SELECT film.title, film.rental_rate, rental.return_date, customer.customer_id, film.description
FROM customer
INNER JOIN rental
ON customer.customer_id = rental.customer_id
INNER JOIN inventory
ON rental.inventory_id = inventory.inventory_id
INNER JOIN film
ON inventory.film_id = film.film_id
WHERE rental.return_date BETWEEN '2005-07-28' AND '2005-08-01' AND film.rental_rate > 4.00 AND rental.customer_id = 323;

SELECT film.title, customer.first_name, customer.last_name, film.description, film.cheap_expensive
FROM rental
INNER JOIN customer
ON customer.customer_id = rental.customer_id
INNER JOIN inventory
ON rental.inventory_id = inventory.inventory_id
INNER JOIN film
ON inventory.film_id = film.film_id
WHERE  rental.customer_id = 323 AND film.description LIKE '%Boat%' AND film.cheap_expensive = 'expensive';

SELECT DISTINCT film.title, actor.first_name, actor.last_name
FROM actor
INNER JOIN film_actor
ON actor.actor_id = film_actor.actor_id
INNER JOIN film
ON film_actor.film_id = film.film_id
INNER JOIN inventory
ON inventory.film_id = film.film_id
INNER JOIN film_category
ON film.film_id = film_category.film_id
INNER JOIN category
ON film_category.category_id = category.category_id
WHERE  category.name = 'Action' AND actor.first_name = 'Joe' AND actor.last_name = 'Swank';

INSERT INTO rental (rental_date, inventory_id, customer_id, staff_id, last_update)VALUES 
('2020-07-28', 254, 600, 1, '2020-07-28'),
('2020-07-28', 300, 600, 2, '2020-07-28' ),
('2020-07-28', 1000, 600, 1, '2020-07-28' );

UPDATE rental
SET return_date = '2020-07-28'
WHERE customer_id = 600 AND  rental_id = 254 

UPDATE rental
SET return_date = '2020-07-28'
WHERE customer_id = 600 AND rental_id = 300;

