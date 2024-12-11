-- REGEXP is a better way than LIKE clause
SELECT *
FROM users
WHERE name 
REGEXP "oku";

-- ^ symbol means that it must be present in the beginning i.e. starts with
SELECT *
FROM users
WHERE name 
REGEXP "^am";

-- $ means ends with
SELECT *
FROM users
WHERE name 
REGEXP "ku$";

--  | means or 
SELECT *
FROM users
WHERE name 
REGEXP "^G|^M";     -- starts with G or M

-- [] means range
SELECT *
FROM users
WHERE name 
REGEXP "^[a-h]"; -- begins with anywhere from a to h

SELECT *
FROM users
WHERE name 
REGEXP "^[adfgxy]";

-- all people whose name starts with a-h and ends with u
SELECT *
FROM users
WHERE name 
REGEXP "^[a-h]|u$";