-- --------------------------
--      INNER JOIN 
-- --------------------------
-- inner join only returns the rows that have a common element in the other table
-- for ex. we wont get the row in the output if there is no row for student with ID 2 in the fees table

SELECT *
FROM users u
JOIN fees f
    ON u.id = f.studentID;


SELECT u.id as studentID, name, fees_paid
FROM users u
JOIN fees f 
    ON u.id = f.studentID;


-- *********  JOINING Multiple Tables ********
SELECT u.id AS studentID, u.name AS student_name, fd.name as father_name, marks, fees_paid
FROM users u
JOIN fees f
    ON u.id = f.studentID
JOIN fatherdetails fd
    ON fd.studentID = u.id;


-- ************* IMPLICIT JOIN **************
-- in implicit join, we dont use JOIN keyword (above ones are explicit joins)
SELECT *
FROM users u, fees f
WHERE u.id = f.studentID;    -- WHERE is used for joining


-- ---------------------------
--      OUTER JOIN
-- ---------------------------
-- Outer join solves the problem of inner join
-- Outer join will return all the elements 
-- if there no corresponding element in the 2nd table, it will return null

-- 2 types of outer joins: LEFT and RIGHT
-- LEFT join retains all the columns of the left table

SELECT *
FROM users u
LEFT JOIN fees f
ON u.id = f.studentID;

SELECT *
FROM users u
RIGHT JOIN fees f
ON u.id = f.studentID;


-- ---------------------------
--      NATURAL JOIN
-- ---------------------------
-- no need to specify ON property as columns with same name will be joined automatically
SELECT *
FROM fees f
NATURAL JOIN fatherdetails fd   -- there is a common row studentID thus it will be joined using studentID


-- ---------------------------
--      USING clause
-- ---------------------------
-- if the column name is same, we can simply use USING clause
SELECT *
FROM fees f
JOIN fatherdetails fd
USING (studentID)


-- ---------------------------
--      CROSS JOIN
-- ---------------------------
-- joins each row of table each row in table 
-- for eg. row  has 10 rows and 2 has 20 rows, then total rows in output will be 200
SELECT * 
FROM users u
CROSS JOIN fees f 
ON u.id = f.studentID;