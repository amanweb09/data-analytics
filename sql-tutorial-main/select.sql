-- reading
SELECT * 
FROM users;

-- selective reading
SELECT * 
FROM users 
WHERE marks=99;

SELECT name 
FROM users
WHERE marks=99;

-- Sorting
SELECT * 
FROM users 
WHERE marks=99
ORDER BY name;

-- changing the order of the columns
SELECT marks,id,name
FROM users;

-- alias
SELECT name 
AS "full_name"
FROM users;

-- operations 
SELECT (marks/5) AS "rounded_off_marks"
FROM users;