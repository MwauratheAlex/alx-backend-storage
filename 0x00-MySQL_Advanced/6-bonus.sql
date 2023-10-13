-- creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER $$
CREATE PROCEDURE AddBonus
(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score FLOAT
)
BEGIN
	DECLARE project_id INT;

	-- Check if the project already exists, if not create a new project
	SET project_id = (SELECT id FROM projects WHERE name = project_name);

	IF project_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET project_id = LAST_INSERT_ID();
	END IF;
	
	UPDATE corrections
	SET score = score
	WHERE user_id = user_id AND user_id = user_id


END$$
DELIMITER ;

