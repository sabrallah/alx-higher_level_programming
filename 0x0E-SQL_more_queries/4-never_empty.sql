-- creates the table id_not_null with a column id that will never be empty
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1 UNIQUE
);

-- insert a row if table is empty
INSERT INTO id_not_null (id)
SELECT 1 FROM id_not_null
WHERE NOT EXISTS (SELECT 1 FROM id_not_null);
