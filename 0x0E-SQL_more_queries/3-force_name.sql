-- Creates the table force_name on database hbtn_0d_2
-- with specific requirements for id, name fields
CREATE TABLE IF NOT EXISTS `hbtn_0d_2`.`force_name` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB; 

-- Inserts a new row with null value for name (should fail)
INSERT INTO `hbtn_0d_2`.`force_name` (`id`, `name`) VALUES (89, NULL);

-- Inserts a new row with non-null value for name 
INSERT INTO `hbtn_0d_2`.`force_name` (`id`, `name`) VALUES (91, 'Holberton School');

-- Prints the name column from force_name table 
SELECT `name` FROM `hbtn_0d_2`.`force_name` WHERE `id` = 89;

SELECT `name` FROM `hbtn_0d_2`.`force_name` WHERE `id` = 91;
