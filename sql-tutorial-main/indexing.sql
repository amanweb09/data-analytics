-- add index to a column with a specific name
ALTER TABLE my_table
ADD INDEX my_index (name, marks);

-- add primary key
ALTER TABLE my_table
ADD PRIMARY KEY (id)

-- removing primary key
ALTER TABLE my_table
DROP PRIMARY KEY;

