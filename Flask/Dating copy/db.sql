-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: dating
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `man`
--

DROP TABLE IF EXISTS `man`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `man` (
  `idman` int NOT NULL AUTO_INCREMENT,
  `created` datetime NOT NULL,
  `nationality` varchar(45) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `length` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `color` varchar(45) DEFAULT NULL,
  `jobstatus` varchar(45) DEFAULT NULL,
  `qabila` varchar(45) DEFAULT NULL,
  `smokingstatus` tinyint DEFAULT NULL,
  `martialstatus` varchar(45) DEFAULT NULL,
  `area` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `origin` varchar(45) DEFAULT NULL,
  `qualifications` varchar(45) DEFAULT NULL,
  `marriagetype` varchar(45) DEFAULT NULL,
  `anothernationality` tinyint DEFAULT NULL,
  `about` longtext,
  `requirments` longtext,
  `userid` int NOT NULL,
  `gender` varchar(45) NOT NULL,
  PRIMARY KEY (`idman`),
  UNIQUE KEY `idman_UNIQUE` (`idman`),
  KEY `userid_idx` (`userid`),
  CONSTRAINT `man_userid` FOREIGN KEY (`userid`) REFERENCES `user` (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `man`
--

LOCK TABLES `man` WRITE;
/*!40000 ALTER TABLE `man` DISABLE KEYS */;
INSERT INTO `man` VALUES (4,'2023-01-25 02:36:52','سعودي',34,122,90,'أسود','مدير','-',1,'متزوج','','مطروح','','مهندس','شرعي',0,'---- ---- ----','---- ---- ----',2,'ذكر'),(5,'2023-01-25 02:38:57','سعودي',34,122,90,'أسود','مدير','-',1,'متزوج','','مطروح','','مهندس','شرعي',0,'---- ---- ----','---- ---- ----',1,'ذكر'),(6,'2023-01-25 02:38:57','سوري',33,128,60,'قوقازي','عامل سباكة','-',0,'أعزب','منوف','القاهرة','المنوفية','تجارة','سري',1,'---- ---- ----','---- ---- ----',1,'ذكر'),(7,'2023-01-25 02:38:57','سوداني',56,159,64,'أسمر','نجار','-',1,'متزوج','الجيزة','الإسماعيلية','القاهرة','محامي','علني',1,'---- ---- ----','---- ---- ----',1,'ذكر'),(8,'2023-01-25 02:38:57','سعودي',22,149,74,'أسود','رجل أعمال','-',1,'مطلق','حلوان','حلوان','دمنهور','ليسانس آداب','مؤقت',1,'---- ---- ----','---- ---- ----',1,'ذكر'),(9,'2023-01-25 02:38:57','مصري',19,139,94,'أبيض','لا أعمل','-',0,'غير متزوج','دمنهور','المنصورة','القاهرة','معلم','مسيار',0,'---- ---- ----','---- ---- ----',1,'ذكر'),(10,'2023-01-25 02:38:57','عراقي',23,160,100,'أسمر','أعمل','-',0,'متزوج','','الإسكندرية','المنصورة','','شرعى',0,'---- ---- ----','---- ---- ----',1,'ذكر'),(11,'2023-01-25 02:38:57','كويتي',45,190,80,'أبيض','لا أعمل','-',1,'أرمل','مدينتي','القاهرة','الإسماعيلية','','مسيار',0,'---- ---- ----','---- ---- ----',1,'ذكر'),(12,'2023-01-25 02:38:57','مصرية',40,165,95,'بيضاء','أعمل','-',0,'غير متزوجه','مدينتي','القاهرة','الإسماعيلية','بكالوريوس هندسة','مسيار',1,'---- ---- ----','---- ---- ----',1,'أنثى'),(13,'2023-01-25 02:38:58','سعوديه',34,122,90,'سوداء','معلمة','-',1,'عزباء','','مطروح','','مهندس','شرعي',0,'---- ---- ----','---- ---- ----',1,'أنثى'),(14,'2023-01-25 02:38:58','سورية',33,128,60,'قوقازية','مدرسة','-',0,'غير متزوجة','منوف','القاهرة','المنوفية','تجارة','سري',0,'---- ---- ----','---- ---- ----',1,'أنثى'),(15,'2023-01-25 02:38:58','سودانية',56,159,64,'سمراء','ممرضة','-',1,'مطلقة','الجيزة','الإسماعيلية','القاهرة','محامي','علني',0,'---- ---- ----','---- ---- ----',1,'أنثى'),(16,'2023-01-25 02:38:58','سعودية',22,149,74,'سوداء','سيدة أعمال','-',1,'غير متزوج','حلوان','حلوان','دمنهور','ليسانس آداب','مؤقت',1,'---- ---- ----','---- ---- ----',1,'أنثى'),(17,'2023-01-25 02:38:58','مصرية',19,139,94,'بيضاء','لا أعمل','-',0,'غير متزوج','دمنهور','المنصورة','القاهرة','معلم','مسيار',1,'---- ---- ----','---- ---- ----',1,'أنثى'),(18,'2023-01-25 02:38:58','عراقيه',23,160,100,'سمراء','أعمل','-',0,'أرملة','','الإسكندرية','المنصورة','','شرعى',1,'---- ---- ----','---- ---- ----',1,'أنثى'),(19,'2023-01-25 02:38:58','كويتية',45,190,80,'سوداء','لا أعمل','-',1,'','مدينتي','القاهرة','الإسماعيلية','','مسيار',1,'---- ---- ----','---- ---- ----',1,'أنثى'),(22,'2023-01-28 23:57:59','',18,160,70,'','','',1,'','','','','','',1,'','',4,'ذكر');
/*!40000 ALTER TABLE `man` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request`
--

DROP TABLE IF EXISTS `request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request` (
  `idmatch` int NOT NULL AUTO_INCREMENT,
  `idrequester` int NOT NULL,
  `idtarget` int NOT NULL,
  `requestdate` datetime NOT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idmatch`),
  UNIQUE KEY `idmatch_UNIQUE` (`idmatch`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request`
--

LOCK TABLES `request` WRITE;
/*!40000 ALTER TABLE `request` DISABLE KEYS */;
INSERT INTO `request` VALUES (1,2,1,'2023-01-26 05:12:13','تم الإرسال');
/*!40000 ALTER TABLE `request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `iduser` int NOT NULL AUTO_INCREMENT,
  `fullname` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `phoneno` varchar(45) NOT NULL,
  PRIMARY KEY (`iduser`),
  UNIQUE KEY `iduser_UNIQUE` (`iduser`),
  UNIQUE KEY `phoneno_UNIQUE` (`phoneno`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Administrator','sha256$eoN8OUQAKajoSozT$32512340baa95f142dba43e267d7763b3a07d81684a2de69ce3bdf9ce3e122d2','00201026655008'),(2,'محمد أحمد زيادة','sha256$of8v06Dps3syeifN$e6689dce2030e256a05b7ab8f766442b0084273a92fbc915df99c7cb3a2c597f','00201555250555'),(4,'Administrator','sha256$zdI6cIQ4Szs6KqCz$47bea0eb33ec75d30edcb74194d3645410ac439fd0838fee697060dd1b7086ae','0000000');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-29  0:14:23
