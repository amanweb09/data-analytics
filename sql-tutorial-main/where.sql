-- All comparison operators can be used with where

SELECT marks
FROM users 
WHERE marks != 99;

SELECT marks
FROM users 
WHERE name = "goku";


-- ***** Logical operators - AND , OR , NOT *****

-- AND always has higher preference than OR so make sure to use ()

SELECT marks 
FROM users
WHERE marks > 50 AND marks < 80

SELECT marks 
FROM users
WHERE name = "aman" OR (marks > 50 AND marks < 80)

-- all marks except the condition ones
SELECT marks 
FROM users
WHERE NOT (marks > 50 AND marks < 80)

-- NOTE: logical operators also work with dates

-- ********* IN Operator *********
SELECT * 
FROM users
WHERE name IN ("goku", "gohan", "vegeta")

SELECT * 
FROM users
WHERE name NOT IN ("goku", "gohan", "vegeta")

-- ************ BETWEEN clause ************
-- specifying a range of values

SELECT * 
FROM users
WHERE marks BETWEEN 40 AND 60;

-- also works with dates
SELECT * 
FROM users
WHERE date_of_test BETWEEN '2024-1-10' AND '2024-3-15';

-- ********** LIKE clause ***********
-- suppose we dont know the exact word eg sale/sales/Sale/Sales/sales-manager/salesperson
SELECT *
FROM users
WHERE name LIKE "%sale%";    -- % here means that any chars after/before sale (similarly _ means 1 letter)

-- finding all the people whose name ends with n
SELECT *
FROM users
WHERE name LIKE "%n";

-- finding whose name has 4 letters and ends with u
SELECT *
FROM users
WHERE name LIKE "____u"; -- _ means 1 character