-- Lists all cities contained in the database hbtn_0d_usa
-- Display: cities.id - cities.name - states.name
-- Results sorted in ascending order by cities.id
-- You can use only one SELECT statement

SELECT cities.id, cities.name, states.name 
FROM hbtn_0d_usa.cities
INNER JOIN hbtn_0d_usa.states 
ON cities.state_id = states.id
ORDER BY cities.id;
