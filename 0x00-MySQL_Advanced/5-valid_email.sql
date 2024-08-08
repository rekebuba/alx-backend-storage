-- SQL script that creates a trigger that resets the attribute valid_email
-- only when the email has been changed.

-- drop if exists
DROP TRIGGER IF EXISTS reset_email;

-- change delimiter temporarily
DELIMITER //
CREATE TRIGGER reset_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //

-- change back to default
DELIMITER ;
