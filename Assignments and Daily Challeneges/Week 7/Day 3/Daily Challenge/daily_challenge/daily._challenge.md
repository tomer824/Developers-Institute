-- create table car 
-- (car_id serial, 
-- brand varchar(50),
-- PRIMARY KEY (car_id)
-- )



-- ONE to MANY
-- create table owner 
-- (owner_id serial,
--  name varchar(50),
-- 	car_id integer,
-- PRIMARY KEY (owner_id),
-- FOREIGN KEY (car_id) references car (car_id)
-- )

-- ONE TO ONE
-- create table adresses
-- (owner_id integer not null unique,
-- address varchar(50),
-- Foreign KEY (owner_id) references owner (owner_id)
-- )

-- create table colors
-- (color_id serial,
-- color_name varchar(50),
-- Primary key (color_id)
-- )

-- MANY TO MANY
-- create table car_color 
-- (car_id integer,
-- color_id integer,
-- FOREIGN KEY (car_id) references car (car_id),
-- FOREIGN KEY (color_id) references colors (color_id)
-- )
