-- query inside a query

SELECT *
FROM users 
WHERE name = (
    SELECT name
    FROM users 
    WHERE id = 2;
);

-- find who scores the max marks
SELECT name, id, marks
FROM users
WHERE marks = (SELECT MAX(marks) FROM users);

-- ques: i have a car name BMW 5 series. find all the cars that are expensive than it
-- i need to first get the price of BMW then compare other cars with it
SELECT *
FROM cars 
WHERE price > (
    SELECT price 
    FROM cars 
    WHERE name = "BMW 5 series";
);

-- find all cars that are expensive than the average of all cars
SELECT *
FROM cars
WHERE price > (
    SELECT AVG(price)
    FROM cars;
);

-- find all the customers who haven't placed an order
SELECT *
FROM customers 
WHERE customerNumber NOT IN (
    SELECT DISTINCT customerNumber
    FROM customers;
);


-- --------------------
--      ALL
-- --------------------
-- compares a value with every value in a list
-- useful when we are getting more than 1 element from a subquery
SELECT *
FROM users
WHERE marks > ALL(25, 75, 80)

SELECT *
FROM users
WHERE marks > ALL(
    SELECT marks 
    FROM users
    WHERE name = "aman" -- we have 2 entries with name aman
)


-- ---------------------------
--            ANY
-- ---------------------------
-- match with any of the entry appearing in the list from a subquery
SELECT *
FROM users
WHERE marks > ANY (25, 75, 80)

SELECT *
FROM users
WHERE marks > ANY(
    SELECT marks 
    FROM users
    WHERE name = "aman" -- we have 2 entries with name aman
)

-- ---------------------------
--     Correlated subquery
-- ---------------------------
-- when inner query depends on the outer query (upar ulta tha)
-- eg. select all the products whose price is > the average in the respective category
-- i.e find the most expensive car, most expensive truck, etc. 
SELECT *
FROM products p
WHERE price > (
    SELECT AVG(price)
    FROM products
    WHERE category = p.category
)


-- ---------------------------
--            EXISTS
-- ---------------------------
-- find all the customers who have made an order
SELECT *
FROM users u
WHERE EXISTS (  --where exists a customer with the following condition
    SELECT is_paid
    FROM fees f
    WHERE f.studentID = u.id
)

-- --------------------------------------
-- Subquery in the SELECT clause
-- --------------------------------------
SELECT *, 
(SELECT AVG(amount) FROM payments) AS average_payment,
amount-average_payment AS avg_difference
FROM payments;


-- --------------------------------------
-- Subquery in the FROM clause
-- --------------------------------------
SELECT studentID
FROM (SELECT * FROM fees WHERE is_paid=1)
