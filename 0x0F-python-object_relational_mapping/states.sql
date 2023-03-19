-- Create Database
CREATE DATABASE IF NOT EXISTS `hbtn_0e_0_usa`;

USE `hbtn_0e_0_usa`;

-- Create table in database
CREATE TABLE IF NOT EXISTS `states`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
	);

-- INSERT VALUSE IN THE columns
INSERT INTO `states` (`name`)
VALUES ("Carlifonia"), ("New Zealand"), ("Texas"), ("Arizona"), ("New york"), ("Nevada");
