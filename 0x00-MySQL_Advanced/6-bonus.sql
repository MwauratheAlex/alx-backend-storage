-- creates a stored procedure AddBonus that adds a new correction for a student.
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$

CREATE PROCEDURE AddBonus (
	IN user_id INT,
	project_name VARCHAR(255),
	score FLOAT
)
BEGIN
	DECLARE project_id INT;
	SET project_id = (SELECT id FROM projects WHERE name = project_name);
	IF project_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET project_id = LAST_INSERT_ID();
		INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
	ELSE
		UPDATE corrections
		SET score = score
		WHERE corrections.user_id = user_id
		AND corrections.project_id = project_id;
	END IF
END$$

DELIMITER ;
