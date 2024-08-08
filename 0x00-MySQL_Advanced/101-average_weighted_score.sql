-- Active: 1716468751032@@127.0.0.1@3306@holberton

DROP PROCEDURE ComputeAverageWeightedScoreForUsers;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE weighted_score FLOAT;

    -- Declare a cursor to iterate over all users
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- open the cursor
    OPEN user_cursor;

    user_loop: LOOP

        -- Fetch user_id from the cursor
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        SELECT IFNULL(SUM(score * weight) / SUM(weight), 0) INTO weighted_score
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        UPDATE users
        SET average_score = weighted_score
        WHERE id = user_id;

    END LOOP user_loop;

    CLOSE user_cursor;
END //

DELIMITER;

