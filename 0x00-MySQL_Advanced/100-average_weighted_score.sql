-- Active: 1716468751032@@127.0.0.1@3306@holberton

DROP PROCEDURE ComputeAverageWeightedScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE weighted_score FLOAT;
    SET weighted_score = (
        SELECT SUM((score * weight)) / SUM(weight)
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        AND corrections.user_id = user_id
        );
    UPDATE users
    SET average_score = weighted_score
    WHERE id = user_id;
END //

DELIMITER;
