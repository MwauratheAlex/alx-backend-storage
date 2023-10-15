-- creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	-- calculate average
	DECLARE weighted_avg FLOAT;

	SET weighted_avg = (
		SELECT SUM(corrections.score / projects.weight) / SUM (projects.weight)
		FROM corrections
		JOIN projects
		ON corrections.project_id = projects.id
		WHERE corrections.user_id = user_id;	
	);

	-- update users table
	UPDATE users
	SET average_score = weighted_avg
	WHERE users.id = user_id;
END$$

DELIMITER ;
