-- SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student.

-- drop if exists

DROP PROCEDURE IF EXISTS AddBonus;

-- change delimiter temporarily

DELIMITER //
-- create stored procedure AddBonus
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    SET @project_id = NULL;

    SELECT id INTO @project_id FROM projects
    WHERE projects.name = project_name;

    IF @project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET @project_id = LAST_INSERT_ID();
    END IF;


    INSERT INTO corrections VALUES(user_id, @project_id, score);
END //

-- change back to default
DELIMITER ;
