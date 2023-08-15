-- Lists all records of second_table with a name and orders by score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
