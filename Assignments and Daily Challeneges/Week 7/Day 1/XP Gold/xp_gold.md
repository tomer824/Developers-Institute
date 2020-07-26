CREATE TABLE students (
	id_num SERIAL PRIMARY KEY,
    last_name VARCHAR (100),
    first_name VARCHAR (50),
    birth_date TIMESTAMP
);

INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Marc', 'Dupont', '1998-11-02'), ('Yoan', 'Durant', '2010-03-12'), ('Lea', 'Martin', '1987-07-24'), ('Sarah', 'Benichou', '1996-04-07'), ('lea', 'Dupont', '2003-04-16'), ('Omer', 'Simpson', '1980-03-10'), ('Tomer', 'Goldstein', '1987-08-24'), ('Chaim', 'Wiesner', '1993-11-02'), ('Tzivia', 'Druin', '1998-11-02');

SELECT * FROM students
SELECT first_name, last_name FROM students
SELECT first_name, last_name FROM students WHERE id_num = 2
SELECT first_name, last_name FROM students WHERE last_name = 'Dupont' AND first_name = 'Marc'
SELECT first_name, last_name FROM students WHERE last_name = 'Dupont' OR first_name = 'Marc'
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%'
SELECT first_name, last_name FROM students WHERE first_name LIKE 'a%'
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a'
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a_'
SELECT first_name, last_name FROM students WHERE id_num = 1 or id_num = 3
SELECT first_name, last_name FROM students WHERE birth_date >= '2000-01-01'