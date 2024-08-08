-- Active: 1716468751032@@127.0.0.1@3306@holberton

DROP TRIGGER IF EXISTS reset_email;
DELIMITER //
CREATE TRIGGER reset_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;
