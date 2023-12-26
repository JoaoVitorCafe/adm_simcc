INSERT INTO institution (name, acronym, email_user, PASSWORD)
VALUES
    ('University A', 'UA', 'ua@example.com', 'password123'),
    ('University B', 'UB', 'ub@example.com', 'password456');
	
SELECT * FROM institution;
DELETE FROM institution WHERE institution_id = 3;

INSERT INTO researcher (name, lattes_id, institution_id)
VALUES
    ('John Doe', 'JD123', 1),
    ('Jane Smith', 'JS456', 2);
	
	
SELECT * FROM researcher;


INSERT INTO graduate_program (code, name, area, modality, TYPE, rating, institution_id)
VALUES
    ('GP001', 'Computer Science', 'Computer Science', 'Master', 'MSc', 'A', 1),
    ('GP002', 'Electrical Engineering', 'Engineering', 'PhD', 'PhD', 'B', 2);
	
	
SELECT * FROM graduate_program;

INSERT INTO graduate_program_researcher (graduate_program_id, researcher_id, year, type_)
VALUES
    (1, 1, 2022, 'Supervisor'),
    (2, 2, 2021, 'Co-Supervisor');
	
	
SELECT * FROM graduate_program_researcher;
	