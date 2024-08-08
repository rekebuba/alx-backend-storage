-- Active: 1716468751032@@127.0.0.1@3306@holberton

DROP FUNCTION `SafeDiv`;
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;

    IF b = 0 THEN
        SET result = 0.0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END //

DELIMITER ;
