-- Print full description of first_table
USE DATABASE_NAME;

SELECT 
  TABLE_NAME AS `Table`,
  COLUMN_NAME AS `Field`,
  COLUMN_TYPE AS `Type`,
  IS_NULLABLE AS `Null`,
  COLUMN_KEY AS `Key`,
  COLUMN_DEFAULT AS `Default`,
  EXTRA AS `Extra` 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'first_table'
ORDER BY ORDINAL_POSITION;
