-- alias to table
SELECT *
FROM users u    -- we can use u instead of users 
WHERE u.name = "goku"

-- alias to columns
SELECT name AS student_name, marks AS marks_in_maths
FROM users 