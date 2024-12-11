-- finding all null values
SELECT * 
FROM users 
WHERE marks IS NULL;

-- finding all non null values
SELECT * 
FROM users 
WHERE marks IS NOT NULL;