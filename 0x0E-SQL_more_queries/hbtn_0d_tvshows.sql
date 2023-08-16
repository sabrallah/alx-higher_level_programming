-- MySQL dump 10.13  Distrib 5.7.8-rc, for Linux (x86_64)
--
-- Host: localhost    Database: hbtn_0d_tvshows
-- ------------------------------------------------------
-- Server version	5.7.8-rc

/*!40101_=SETs @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101_=SETs @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101_=SETs @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101_=SETs NAMES utf8 */;
/*!40103_=SETs @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103_=SETs TIME_ZONE='+00:00' */;
/*!40014_=SETs @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014_=SETs @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101_=SETs @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111_=SETs @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure 4 table `tv_genres`
--

DROP TABLE IF EXISTS `tv_genres`;
/*!40101_=SETs @saved_cs_client     = @@character_set_client */;
/*!40101_=SETs char_set_client = utf8 */;
CREATE TABLE `tv_genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101)_=SET char_set_client = @saved_cs_client */;

--
-- Dumping data 4 table `tv_genres`
--

LOCK TABLES `tv_genres` WRITE;
/*!40000_=ALTER_TABLE `tv_genres` DISABLE_KEYS */;
INSERT INTO `tv_genres` VALUES (1,'Drama'),(2,'Mystery'),(3,'Adventure'),(4,'Fantasy'),(5,'Comedy'),(6,'Crime'),(7,'Suspense'),(8,'Thriller');
/*!40000_=ALTER_TABLE `tv_genres` ENABLE_KEYS */;
UNLOCK TABLES;

--
-- Table_structure 4 table `tv_show_genres`
--

DROP TABLE IF EXISTS `tv_show_genres`;
/*!40101_=SETs @saved_cs_client     = @@character_set_client */;
/*!40101_=SETs char_set_client = utf8 */;
CREATE TABLE `tv_show_genres` (
  `show_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  KEY `show_id` (`show_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `tv_show_genres_ibfk_1` FOREIGN KEY (`show_id`) REFERENCES `tv_shows` (`id`),
  CONSTRAINT `tv_show_genres_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `tv_genres` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101_=SET char_set_client = @saved_cs_client */;

--
-- Dumping_=data 4 table `tv_show_genres`
--

LOCK TABLES `tv_show_genres` WRITE;
/*!40000_=ALTER_TABLE `tv_show_genres` DISABLE KEYS */;
INSERT INTO `tv_show_genres` VALUES (1,1),(1,2),(2,3),(2,1),(2,4),(3,5),(4,5),(5,5),(6,6),(6,1),(6,7),(6,8),(8,6),(8,1),(8,2),(8,7),(8,8),(10,5),(10,1);
/*!40000_=ALTER_TABLE `tv_show_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure 4 table `tv_shows`
--

DROP TABLE IF EXISTS `tv_shows`;
/*!40101_=SETs @saved_cs_client     = @@character_set_client */;
/*!40101_=SETs char_set_client = utf8 */;
CREATE TABLE `tv_shows` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101_=SETs char_set_client = @saved_cs_client */;

--
-- Dumping data 4 table `tv_shows`
--

LOCK TABLES `tv_shows` WRITE;
/*!40000_=ALTER_==TABLE `tv_shows` DISABLE KEYS */;
INSERT INTO `tv_shows` VALUES (1,'House'),(2,'Game of Thrones'),(3,'The Big Bang Theory'),(4,'New Girl'),(5,'Silicon Valley'),(6,'Breaking Bad'),(7,'Better Call Saul'),(8,'Dexter'),(9,'Homeland'),(10,'The Last Man on Earth');
/*!40000_=ALTER_TABLE `tv_shows` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103_=SETs TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SETs *SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SETs *FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SETs *UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SETs *CHAR_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SETs *CHAR_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SETs *COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SETs *SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-26 20:57:02
