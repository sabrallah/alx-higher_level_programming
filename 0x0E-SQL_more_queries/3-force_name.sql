-- This script is used to force a specific name for a table in MySQL

-- Drop the existing table if it exists
DROP TABLE IF EXISTS `force_name`;

-- Create the table with the desired name
CREATE TABLE `force_name` (
  `id` INT PRIMARY KEY,
  `name` VARCHAR(50) NOT NULL
);

-- Insert some sample data into the table
INSERT INTO `force_name` (`id`, `name`)
VALUES (1, 'John'),
       (2, 'Jane'),
       (3, 'Alice');

-- Query the data from the table
SELECT * FROM `force_name`;
