-- creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER $$
CREATE PROCEDURE AddBonus
(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score FLOAT
)
BEGIN
	UPDATE corrections
	SET corrections.score = score
	WHERE project_id = (SELECT id FROM projects WHERE name = (SELECT name FROM users WHERE id = user_id));
END$$
DELIMITER ;

