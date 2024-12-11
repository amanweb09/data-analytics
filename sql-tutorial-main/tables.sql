-- create tables
USE tutorial;

-- show all tables
SHOW TABLES;

-- creating tables
-- NOTE: It's mandatory to given length of varchar
CREATE TABLE my_table(
    ID integer, Name varchar (100), marks integer
);

-- describe a tables (datatypes and fields)
DESCRIBE my_table;


-- inserting data
INSERT INTO my_table
VALUES (1, "aman", 100);


-- add new column
ALTER TABLE my_table
ADD teacher varchar (100);


-- drop a column
ALTER TABLE my_table
DROP teacher;