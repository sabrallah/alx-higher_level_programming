-- create table for  `unique_id`
-- `id` INT default 1 unique, `name` VARCHAR(256)
-- if the table exists,the  script shouldn't fail

CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE, 
  name VARCHAR(256)
);
