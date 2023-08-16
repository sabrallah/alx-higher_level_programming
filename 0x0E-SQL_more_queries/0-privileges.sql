-- Grant all privileges to a new user named 'myuser' on the 'mydatabase' database
GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'localhost';

-- Grant only SELECT privileges to a new user named 'readonly' on the 'mydatabase' database
GRANT SELECT ON mydatabase.* TO 'readonly'@'localhost';

-- Grant only INSERT privileges to a new user named 'insertuser' on the 'mytable' table
GRANT INSERT ON mydatabase.mytable TO 'insertuser'@'localhost';
