-- grouping categorical variables


-- --------------------------------------
--      SELECTING UNIQUE VALUES
-- --------------------------------------
SELECT 
    DISTINCT name
FROM users;


-- --------------------------------------
--              GROUPING
-- --------------------------------------
SELECT name
FROM users
GROUP BY name;


-- --------------------------------------
--        Aggregation with grouping
-- --------------------------------------
-- correct syntax:
--  SELECT c1, c2,..cn,  aggregation
--  FROM table
--  WHERE condition
--  GROUP BY c1,c2,..,cn
-- i.e. jo jo  columns upar, vo vo columns niche

SELECT 
    name,
    marks,
    count(*) AS name_count  -- how many students have same name
FROM users
GROUP BY name, marks;

-- NOTE: we can't select * if use GROUP BY clause


-- -----------------------
--      HAVING clause
-- -----------------------
-- we cant use WHERE clause for filtering groups/agg columns thus we will use HAVING
-- i.e. group all but show only those values whose marks are more than 70
SELECT 
    name,
    marks,
    count(*) AS name_count  -- how many students have same name
FROM users
GROUP BY name, marks;
HAVING marks > 70;

-- WHERE clause filters before grouping while HAVING filters after grouping

SELECT 
    country, 
    COUNT(*) AS totalOrders
FROM orders
JOIN customers 
    USING (customerNumber)
WHERE country   -- as we are filtering it before grouping 
    IN ("France", "USA", "Japan")
GROUP BY country
HAVING totalOrders > 20; -- as it is an aggregate column


-- show the total amount paid by each customer after 10-12-2023
SELECT 
customerNumber, 
SUM(amount) AS order_count
FROM payments
WHERE orderDate > "10-12-2023"
GROUP BY customerNumber

-- ques: find total amount of order placed by each unique customer and sort by total amount
-- total value = price * qty
SELECT customerNumber, 
SUM(quantityOrdered*priceOfEach) as totalAmount
FROM orders
GROUP BY customerNumber;    -- gives unique customer ID as all ids will be grouped
ORDER BY totalAmount DESC
