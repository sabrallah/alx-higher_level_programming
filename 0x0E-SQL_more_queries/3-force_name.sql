-- Create table 'force_name'
-- The table should have two columns: id (INT) and name (VARCHAR(256)) which cannot be null
-- If the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
