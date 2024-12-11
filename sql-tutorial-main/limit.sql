
-- give first 10 records
SELECT *
FROM users
LIMIT 10;

-- give records from 20 to 30
SELECT *
FROM users
LIMIT 20,30;    -- skip 20 records and then give next 30 records

-- getting the top scorer
SELECT *
FROM users
ORDER BY marks DESC
LIMIT 1;
