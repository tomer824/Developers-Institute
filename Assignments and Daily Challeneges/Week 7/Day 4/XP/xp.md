SELECT first_name AS "FIRST NAME", last_name AS "LAST NAME" FROM employees;
SELECT * FROM employees WHERE department_id = 2
SELECT * FROM employees ORDER BY first_name ASC
SELECT first_name, last_name, salary FROM employees

SELECT employee_id, (first_name,last_name) AS name, salary FROM employees ORDER BY salary ASC

SELECT SUM(salary)
FROM employees;

SELECT MIN(salary), MAX(salary)
FROM employees

SELECT COUNT(employee_id), round(AVG(salary),2)
FROM employees

SELECT COUNT(employee_id)

SELECT COUNT(employee_id)
FROM employees

SELECT COUNT (DISTINCT job_id)
FROM employees

SELECT UPPER(first_name) FROM employees

SELECT left(first_name, 3) FROM employees

SELECT 171*214+625

SELECT (first_name, last_name) AS name FROM employees

SELECT TRIM(first_name) FROM employees

SELECT first_name, last_name, (LENGTH(first_name) + LENGTH(last_name)) AS length FROM employees

SELECT first_name FROM employees
WHERE first_name LIKE '%[^0-9]%'

SELECT * FROM employees LIMIT 10

SELECT first_name, last_name, (round(salary / 12),2) FROM employees 

CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR (50),
    region_id INTEGER,
	FOREIGN KEY (region_id) REFERENCES (regions)
);

CREATE TABLE dup_countries (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR (50),
    region_id INTEGER,
	FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

create the table as below instead of as above
SELECT * INTO dup_countries FROM countries;  

when you create the table from above include constraint null

table jobs and countries already exists from the download

CREATE TABLE job_history (
    job_id INTEGER,
	employee_id INTEGER,
    start_date DATE,
    end_date DATE,
	department_id INTEGER,
	FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

table employees already exists

RESTRICTING AND SORTING

select first_name, last_name, salary from employees WHERE salary NOT BETWEEN 10000 and 15000

select first_name, last_name, department_id from employees WHERE department_id = 30 or department_id = 100 ORDER BY department_id ASC

SELECT first_name, last_name, hire_date  FROM employees WHERE hire_date > '1987-01-01' AND hire_date < '1988-01-01';

SELECT first_name FROM employees WHERE first_name LIKE '%c%' AND first_name LIKE '%e%' ;

SELECT employees.first_name, employees.last_name, employees.job_id, employees.salary FROM employees 
INNER JOIN jobs
ON employees.job_id = jobs.job_id
WHERE jobs.job_title != 'Programmer' AND jobs.job_title != 'Shipping Clerk' AND employees.salary != 4500 OR employees.salary != 10000 OR employees.salary != 15000;

SELECT last_name FROM employees WHERE last_name LIKE '______'

SELECT last_name FROM employees WHERE last_name LIKE '__e%'



SELECT first_name, last_name, salary * 0.15 FROM employees

-- SELECT * FROM employees WHERE last_name = 'JONES' OR last_name = 'BLAKE' OR last_name = 'SCOTT' OR last_name = 'KING' OR last_name = 'FORD';