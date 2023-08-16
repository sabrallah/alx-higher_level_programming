-- Lists all cities contained in the database hbtn_0d_usa 
-- Cities are grouped by states and ordered by cities.id

SELECT cities.id, cities.name, states.name 
FROM hbtn_0d_usa.cities 
INNER JOIN hbtn_0d_usa.states 
ON cities.state_id = states.id
ORDER BY cities.id;
