-- Créer bd 'usa_data'  

-- Si bd existe déjà, script ne doit pas échouer

CREATE DATABASE IF NOT EXISTS usa_data;

-- Créer table 'etats' dans bd 'usa_data'  

-- id INT unique auto-généré non nul et clé primaire  

-- nom VARCHAR(256) non nul

-- Si table existe déjà, script ne doit pas échouer

CREATE TABLE IF NOT EXISTS usa_data.etats (

  id INT UNIQUE AUTO_INCREMENT NOT NULL,
  
  nom VARCHAR(256) NOT NULL,
  
  PRIMARY KEY (id)
  
);
