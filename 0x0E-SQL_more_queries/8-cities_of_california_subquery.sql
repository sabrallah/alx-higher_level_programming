-- List all cities contained in the database hbtn_0d_usa

SELECT id, name 
FROM hbtn_0d_usa.cities
WHERE state_id = (
    -- Get id of California state
    SELECT id FROM hbtn_0d_usa.states
    WHERE name = 'California'
);
