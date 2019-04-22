USE `*databaseName*`;
DROP procedure IF EXISTS `spGetKeywords`;

DELIMITER $$
USE `apitest`$$
CREATE PROCEDURE `spGetKeywords` (
IN P_Keyword VARCHAR(255)
)
BEGIN
SELECT
 ID,
 `name`,
 Keyword
FROM
 tbltutorial
WHERE 
 Keyword = P_Keyword;

END$$

DELIMITER ;