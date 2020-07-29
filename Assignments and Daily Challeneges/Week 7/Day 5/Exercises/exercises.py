import sqlite as sl

conn = sl.connect('example.db')

CREATE TABLE employees
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT,
  last_name TEXT,
  pin_number TEXT,
  salary NUMERIC
);
INSERT INTO employees
(first_name, last_name, pin_number, salary)
VALUES
('Adam', 		'Adamson',	'aaa', 20000),
('Bobby', 	'Brown', 	'bbb', 25000),
('Charlie', 	'Chaplain', 'ccc', 33000),
('Davey', 	'Dobson', 	'ddd', 17000),
('Eli', 		'Emmerson', 'eee', 12000),
('Freddie', 	'Farrah', 	'fff', 22000)


c = conn.cursor()

query = input("what is your query? ")

c.execute("SELECT * FROM employees")

results - c.fetchall()
conn.close()

for item in results:
    print(item)