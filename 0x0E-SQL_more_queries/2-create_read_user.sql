-- Creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- Creates the user user_0d_2 with password 
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grants ability to connect to server
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- Grants SELECT privilege to user_0d_2 on database hbtn_0d_2 
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
