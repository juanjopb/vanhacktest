CREATE TABLE IF NOT EXISTS`testingjjpb`.`preferences` (
  `idpreferences` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `color` VARCHAR(45) NULL,
  `pet` VARCHAR(45) NULL,
  PRIMARY KEY (`idpreferences`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC));
