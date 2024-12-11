-- ORDER BY is used for sorting

-- sorting by name
SELECT *
FROM users
ORDER BY name;

-- descending order
SELECT *
FROM users
ORDER BY marks
DESC;

-- multiple level sorting i.e. first sort as per marks, then by name
SELECT *
FROM users
ORDER BY marks DESC, name;