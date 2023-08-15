-- Displays the top 3 cities with the highest avg temps in July and August
SELECT city, MONTH(date) AS month, AVG(value) AS avg_temp
FROM temperatures
WHERE month(date) IN (7, 8)  
GROUP BY city, month
ORDER BY month, avg_temp DESC;
LIMIT 3;
