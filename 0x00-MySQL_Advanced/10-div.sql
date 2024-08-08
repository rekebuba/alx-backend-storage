-- SQL script that creates a function SafeDiv that divides (and returns),
-- the first by the second number or returns 0 if the second number is equal to 0.

-- drop if exists
DROP FUNCTION `SafeDiv`;

-- change delimiter temporarily
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
DETERMINISTIC -- the output will always be the same given the same input
BEGIN
    DECLARE result FLOAT;

    IF b = 0 THEN
        SET result = 0.0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END //

-- change back to default
DELIMITER ;
