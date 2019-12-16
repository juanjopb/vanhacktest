CREATE TABLE `testingjjpb`.`preferences` (
  `idpreferences` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `color` VARCHAR(45) NULL,
  `pet` VARCHAR(45) NULL,
  PRIMARY KEY (`idpreferences`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC));