CREATE DATABASE  IF NOT EXISTS `rpgpython` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `rpgpython`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: rpgpython
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `inimigos`
--

DROP TABLE IF EXISTS `inimigos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inimigos` (
  `idmonstro` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  `hab` tinyint(4) DEFAULT NULL,
  `ener` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`idmonstro`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inimigos`
--

LOCK TABLES `inimigos` WRITE;
/*!40000 ALTER TABLE `inimigos` DISABLE KEYS */;
INSERT INTO `inimigos` VALUES (1,'Corcel Demônio',8,10),(2,'Thassaloss Maior',10,15),(3,'Mastin',7,7),(4,'Névoa Vampira',7,9),(5,'Morcego Vampiro Chifrudo',8,7),(6,'Zumbi 1',6,6),(7,'Zumbi 2',7,6),(8,'Thassaloss Menor',8,11),(9,'Ghoul Imenso',8,11),(10,'Homem da Floresta',10,7),(11,'Corvo Gigante',7,6),(12,'Zumbi 3',6,5),(13,'Zumbi 4',7,5),(14,'Lobo 1',6,5),(15,'Lobo 2',7,6),(16,'Katarina Heydrich',10,10),(17,'Gnomo',8,6),(18,'Golem de Madeira',8,6),(19,'Lobo 3',7,8),(20,'Ghul Fedorento',8,9),(21,'Rato Grande',7,8),(22,'Armadura Animada',8,9),(23,'Aparição',8,9),(24,'Tapete de Pele de Tigre',7,7),(25,'Cobra do Rio',6,6),(26,'Baobhan Sith',9,9),(27,'Zumbi 5',7,7),(28,'Urso Marrom',7,8),(29,'Guarda Florestal',10,9),(30,'Espectro',10,14),(31,'Geléia Necrótica',7,9),(32,'Wilhelm Heydrich',8,7),(33,'Homúnculo',8,5),(34,'Lothar',9,10),(35,'Conde Reiner Heydrich',13,21),(36,'Sombra',8,6);
/*!40000 ALTER TABLE `inimigos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-22 14:40:59
