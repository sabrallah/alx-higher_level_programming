-- Create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table cities
-- id INT unique, auto generated, can't be null and is a primary key
-- state_id INT, foreign key that references to id of the states table
-- name VARCHAR(256) can't be null
-- If table exists, script should not fail

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL
);
