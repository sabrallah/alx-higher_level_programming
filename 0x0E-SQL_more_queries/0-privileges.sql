-- List privileges of user_0d_1 on localhost
SELECT * FROM information_schema.user_privileges
WHERE grantee LIKE '%user\_0d\_1%' AND host='localhost';

-- List privileges of user_0d_2 on localhost  
SELECT * FROM information_schema.user_privileges
WHERE grantee LIKE '%user\_0d\_2%' AND host='localhost';
