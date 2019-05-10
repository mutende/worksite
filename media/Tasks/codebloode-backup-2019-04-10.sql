-- MySQL dump 10.16  Distrib 10.1.29-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: codebloode
-- ------------------------------------------------------
-- Server version	10.1.29-MariaDB-6

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointment` (
  `appId` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `time` time NOT NULL,
  `eTime` time NOT NULL,
  `counsNo` varchar(12) DEFAULT NULL,
  `regNo` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`appId`),
  KEY `foreign key` (`regNo`),
  CONSTRAINT `foreign key` FOREIGN KEY (`regNo`) REFERENCES `student` (`regNo`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES (2,'2019-02-12','08:00:00','08:45:00','counsellor1','K11/08100/18'),(5,'2019-02-15','08:45:00','09:30:00','counsellor8','K11/08100/18'),(6,'2019-02-15','08:45:00','09:30:00','counsellor1','K11/08100/18'),(7,'2019-02-15','09:30:00','10:15:00','counsellor1','K11/08100/18'),(8,'2019-04-10','14:21:00','15:06:00','counsellor1','K11/08100/18');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `counsellor`
--

DROP TABLE IF EXISTS `counsellor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `counsellor` (
  `counsNo` varchar(12) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phoneNo` varchar(13) NOT NULL,
  `gender` char(1) NOT NULL,
  `password` varchar(75) NOT NULL,
  `salt` varchar(75) NOT NULL,
  `day` datetime NOT NULL,
  PRIMARY KEY (`counsNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `counsellor`
--

LOCK TABLES `counsellor` WRITE;
/*!40000 ALTER TABLE `counsellor` DISABLE KEYS */;
INSERT INTO `counsellor` VALUES ('counsellor1','Peter Keter','keter@gmail.com','0712131415','M','ytSc7X4leVhg+wa6tEdX7iNKTM95QfK0PGQ2SojIMSM=','4dM0svX1TGWmrBa8Hl4KrUzu386tBW','2019-02-18 13:36:11'),('counsellor2','Keton Philip','philip@gmail.com','0712234567','M','Z87dFryeO2UN9HMoK+PtMqIUjAZk9P5+1K1q0bNqNeg=','zmUYE2UfZmlZPao8qy8Vf79XE0a9AR','2019-02-19 07:28:11'),('counsellor4','Jane Kraig','jane@gmail.com','0790876543','F','KTKIf/bwXPl1wZaRPyPwo9NygsyFcDjXRZ/4cRmiM6Y=','2XjmWPm3efZe1YPV4kav7HpUDKm2Y5','2019-02-19 07:26:20'),('counsellor8','Craig Couns','craig@gmail.com','0790876543','M','AIHyYiWOt7hukguY8YGwO0MWyhCDEzDglnoLca7P7rw=','4JkrEBK1sxcWAMPaBYZkvzlhPjhEaQ','2019-02-19 08:52:02');
/*!40000 ALTER TABLE `counsellor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dean`
--

DROP TABLE IF EXISTS `dean`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dean` (
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `uName` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phoneNo` varchar(13) NOT NULL,
  `password` varchar(75) NOT NULL,
  `salt` varchar(75) NOT NULL,
  `day` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dean`
--

LOCK TABLES `dean` WRITE;
/*!40000 ALTER TABLE `dean` DISABLE KEYS */;
INSERT INTO `dean` VALUES ('Justine','Omwoyo','dean','deaneu@gmail.com','0712234567','RqZK9bA+tuWKRZovXLy9gUx2kgPEEtlZRnv5bYsGiHY=','OpwPXOMqs3qD3FAYKrFWuwl4oqLS1u','2019-02-18 13:28:44');
/*!40000 ALTER TABLE `dean` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheduling`
--

DROP TABLE IF EXISTS `scheduling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scheduling` (
  `scheduleId` int(11) NOT NULL AUTO_INCREMENT,
  `counsNo` varchar(12) NOT NULL,
  `dateAway` date NOT NULL,
  `timeAway` time NOT NULL,
  `dateBack` date NOT NULL,
  `timeBack` time NOT NULL,
  `reason` varchar(150) NOT NULL,
  `approval` varchar(3) NOT NULL,
  PRIMARY KEY (`scheduleId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheduling`
--

LOCK TABLES `scheduling` WRITE;
/*!40000 ALTER TABLE `scheduling` DISABLE KEYS */;
INSERT INTO `scheduling` VALUES (1,'counsellor1','2019-02-19','15:30:00','2019-02-20','18:30:00',' wedding','no'),(2,'counsellor1','2019-02-18','17:02:00','2019-02-19','17:02:00','Off Day','no'),(3,'counsellor1','2019-02-21','09:00:00','2019-02-26','14:00:00',' wedding','no'),(4,'counsellor1','2019-02-02','05:45:00','2019-02-04','08:45:00',' personal','no'),(7,'counsellor1','2019-02-20','13:00:00','2019-02-23','13:30:00','burial','yes'),(8,'Counsellor1','2019-04-15','08:30:00','2019-04-17','10:30:00',' personal reasons','yes');
/*!40000 ALTER TABLE `scheduling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `regNo` varchar(15) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `phoneNo` varchar(13) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(75) NOT NULL,
  `salt` varchar(75) NOT NULL,
  `day` datetime NOT NULL,
  PRIMARY KEY (`regNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('K11/08100/18','James','Smith','0712131415','myem@gmail.com','0eif4p9mmuPtAhM3V1R9nOAbr49bmpGYAQy78CNURMw=','BJzRrmGsI5WlGxsB3HBQuoupRyqUIN','2019-02-18 12:55:46'),('S13/09722/15','John','Kraig','0711687880','kraig@gmail.com','PX76ikQewqYw4fYfEQc/FDXpRw44EzmDdrqpLfq9rtQ=','QZkFbyYjkeE1TEBjleq72TupqIco7l','2019-02-19 07:01:27');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-10  9:56:29
