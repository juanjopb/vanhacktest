CREATE TABLE IF NOT EXISTS `preferences` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`name` varchar(50) NOT NULL UNIQUE,
  	`color` varchar(255) NOT NULL,
  	`pet` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;