-- Displays the average temperature of all temperature readings 
SELECT city, AVG(value) AS avg_temp
FROM temperatures 
GROUP BY city
ORDER BY avg_temp DESC;
