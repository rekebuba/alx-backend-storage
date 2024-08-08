-- Active: 1716468751032@@127.0.0.1@3306@holberton

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id
    )
    WHERE id = user_id;
END //

DELIMITER;

CALL ComputeAverageScoreForUser(2)

SELECT * FROM corrections;
