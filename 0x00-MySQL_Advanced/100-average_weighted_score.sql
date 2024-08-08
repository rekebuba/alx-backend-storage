-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser,
-- that computes and store the average weighted score for a student.

-- drop if exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- change delimiter temporarily
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    -- weighted_score to tore the value
    DECLARE weighted_score FLOAT;

    -- get and seat the score by joining correction and projects table
    SELECT SUM((score * weight)) / SUM(weight) INTO weighted_score
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    AND corrections.user_id = user_id;

    -- update average_score column
    UPDATE users
    SET average_score = weighted_score
    WHERE id = user_id;
END //

-- change back to default
DELIMITER ;
