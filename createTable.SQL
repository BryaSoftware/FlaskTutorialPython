CREATE TABLE `*databaseName*`.`tbltutorial` (
 `ID` INT NOT NULL AUTO_INCREMENT,
 `name` VARCHAR(255) NULL,
 `Keyword` VARCHAR(255) NULL,
 PRIMARY KEY (`ID`),
 INDEX `index1` (`Keyword` ASC) VISIBLE);
 
/*insert records*/
INSERT INTO tblTutorial (
 `name`,
 keyword
)
VALUES (
 'Zac',
 'Developer'
);

/*insert records*/
INSERT INTO tblTutorial (
 `name`,
 keyword
)
VALUES (
 'Jackie',
 'Writer'
);

/*insert records*/
INSERT INTO tblTutorial (
 `name`,
 keyword
)
VALUES (
 'Sarah',
 'Writer'
);
