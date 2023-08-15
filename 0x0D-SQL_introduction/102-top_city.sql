-- Displays the top city with the highest average temperature 
SELECT city FROM temperatures 
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 1;
