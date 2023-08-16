-- Create table 'id_not_null'
-- id INT default value 1, name VARCHAR(256)
-- Should not fail if table exists

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
