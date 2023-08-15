-- Displays the top 3 cities with the highest average temperatures
SELECT city FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3;
