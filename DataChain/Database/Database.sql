-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: swami
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.21.10.3

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
-- Table structure for table `model6`
--

DROP TABLE IF EXISTS `model6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `model6` (
  `modelid` int NOT NULL AUTO_INCREMENT,
  `owner` varchar(50) DEFAULT NULL,
  `method` varchar(30) DEFAULT NULL,
  `learning` varchar(100) DEFAULT NULL,
  `rating` int DEFAULT NULL,
  `bounty` double DEFAULT NULL,
  `target` int DEFAULT NULL,
  `reached` int DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `sdesc` text,
  `ldesc` text,
  `tags` text,
  `private` tinyint(1) DEFAULT NULL,
  `datasetsell` tinyint(1) DEFAULT NULL,
  `modelsell` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`modelid`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model6`
--

LOCK TABLES `model6` WRITE;
/*!40000 ALTER TABLE `model6` DISABLE KEYS */;
INSERT INTO `model6` VALUES (59,'0x032b8f531dafec4af731ba6d0eb87a4b3b08b2d5','Softmax Regression','Incremental Learning',0,0.5,1000,0,'Iris Datase','This is desc','Panaoidfgaoiefhboidfjboij','ragh,kb,',0,0,0);
/*!40000 ALTER TABLE `model6` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model7`
--

DROP TABLE IF EXISTS `model7`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `model7` (
  `modelid` int NOT NULL,
  `owner` varchar(50) DEFAULT NULL,
  `mschema` longtext,
  `predict` text,
  `filter` longblob,
  `actual` longblob,
  PRIMARY KEY (`modelid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model7`
--

LOCK TABLES `model7` WRITE;
/*!40000 ALTER TABLE `model7` DISABLE KEYS */;
INSERT INTO `model7` VALUES (59,'0x032b8f531dafec4af731ba6d0eb87a4b3b08b2d5','{\'sepal length (cm)\': \'float\', \'sepal width (cm)\': \'float\', \'petal length (cm)\': \'float\', \'petal width (cm)\': \'float\', \'target\': \'int\'}','target',_binary '€•…\0\0\0\0\0\0Œriver.compose.pipeline”ŒPipeline”“”)”}”Œsteps”Œcollections”ŒOrderedDict”“”)R”(ŒStandardScaler”Œriver.preprocessing.scale”h\n“”)”}”(Œwith_std”ˆŒcounts”hŒCounter”“”}”…”R”Œmeans”hŒdefaultdict”“”Œbuiltins”Œfloat”“”…”R”Œvars”hh…”R”ubŒSoftmaxRegression”Œ\Zriver.linear_model.softmax”h!“”)”}”(Œ	optimizer”Œriver.optim.sgd”ŒSGD”“”)”}”(Œlr”Œriver.optim.schedulers”ŒConstant”“”)”}”Œ\rlearning_rate”G?„z\áG®{sbŒn_iterations”K\0ubŒ\noptimizers”hŒ	functools”Œpartial”“”Œcopy”Œdeepcopy”“”…”R”(h:h*…”}”Nt”b…”R”Œloss”Œriver.optim.losses”ŒCrossEntropy”“”)”}”Œclass_weight”}”sbŒl2”K\0Œweights”hh7h…”R”(hh…”}”Nt”b…”R”ubusb.',_binary '€•…\0\0\0\0\0\0Œriver.compose.pipeline”ŒPipeline”“”)”}”Œsteps”Œcollections”ŒOrderedDict”“”)R”(ŒStandardScaler”Œriver.preprocessing.scale”h\n“”)”}”(Œwith_std”ˆŒcounts”hŒCounter”“”}”…”R”Œmeans”hŒdefaultdict”“”Œbuiltins”Œfloat”“”…”R”Œvars”hh…”R”ubŒSoftmaxRegression”Œ\Zriver.linear_model.softmax”h!“”)”}”(Œ	optimizer”Œriver.optim.sgd”ŒSGD”“”)”}”(Œlr”Œriver.optim.schedulers”ŒConstant”“”)”}”Œ\rlearning_rate”G?„z\áG®{sbŒn_iterations”K\0ubŒ\noptimizers”hŒ	functools”Œpartial”“”Œcopy”Œdeepcopy”“”…”R”(h:h*…”}”Nt”b…”R”Œloss”Œriver.optim.losses”ŒCrossEntropy”“”)”}”Œclass_weight”}”sbŒl2”K\0Œweights”hh7h…”R”(hh…”}”Nt”b…”R”ubusb.');
/*!40000 ALTER TABLE `model7` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `signature` varchar(255) DEFAULT NULL,
  `balance` double DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (32,'Swami','0xfa746ff52266504857ce6b83f90b0e769b1063db','0xbc8bc2d68600b0b86f3123477c5c15ebe20ceb89808839bc0a0adf2c572694b750fe0ca9ea49917633c700e378a0cb7045c483c63e21f836896cff6b76c5edb91c',0),(33,'174414','0x032b8f531dafec4af731ba6d0eb87a4b3b08b2d5','0x2a7405b793cc4b6807fafe5fc25606616c1d279d3a0bf6ac2bfc14865c06286f54d9c3a1edfcc526bb7e46f146f0d36b9cf048cb96d079af1525917a2d176b281b',0),(34,'SLT','0xb64c573b9e277dd5d056110096ef3d1d885788ea','0xebd4bd5b568e72533c69d9bb7946a87206c389f6b58dfb470da9c52563851d166e459c9795c3c798eb8b43ee6a8823ed723c433f77e865db10735c3849b9091b1b',0),(35,'sai','0x1732e538ba35876183fc57e864cc1700c19e2d7b','0x306818306e1d834dbddb850e29832a931af775dfb97f3127399bc49dacde6fb214a0af6a0c3f7f7e0a246f0bce0f9a62b21ec25274bc89945ff03778041412a81c',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-25 11:11:17
