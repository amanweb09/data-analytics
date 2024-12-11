-- -----------------------
--      MAX, MIN, AVG, SUM
-- -----------------------
SELECT 
    MAX(marks) AS max_marks,
    MIN(marks) AS min_marks,
    AVG(marks) AS avg_marks,
    SUM(marks) AS total_marks
FROM users; 

-- max min also works with strings and dates (returns the most recent date)
SELECT 
    MAX(admission_date)
FROM users;

-- in string, a<b<C.. (as per dictionary)
SELECT
    MAX(name)
FROM users;


-- -----------------------
--      COUNT
-- -----------------------
-- COUNT counts only non-null values
SELECT COUNT(marks) AS total_student
from users;

-- count all non-null values in the rows
SELECT COUNT(*)
from users;

-- conditional counting
SELECT COUNT(*)
from users u
WHERE u.marks > 50;