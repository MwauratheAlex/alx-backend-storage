-- creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users
	JOIN (
		SELECT corrections.user_id,
			SUM(corrections.score * projects.weight) / SUM(projects.weight) AS new_weighted_avg
		FROM corrections
		JOIN projects
		ON corrections.project_id = projects.id
		GROUP BY corrections.user_id
	) AS derived_table
	ON users.id = derived_table.user_id
	SET users.average_score = derived_table.new_weighted_avg;
END$$

DELIMITER ;
