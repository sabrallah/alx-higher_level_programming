-- creates the user user_0d_1 with password user_0d_1_pwd 
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'; 

-- grants SELECT privilege to user_0d_1 on database hbtn_0d_tvshows
GRANT SELECT ON `hbtn_0d_tvshows`.* TO 'user_0d_1'@'localhost';
