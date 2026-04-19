-- Delete table if already exists

DROP TABLE IF EXISTS student;

-- Create student table
CREATE TABLE student (
student_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
maths INTEGER,
science INTEGER,
english INTEGER
);

-- Insert sample student records (user input simulation)
INSERT INTO student (name, maths, science, english)
VALUES
('Rahul', 78, 82, 69),
('Anita', 92, 88, 95),
('Kiran', 65, 70, 60),
('Divya', 50, 55, 58);

-- Display student records
SELECT * FROM student;

-- Grade calculator query
SELECT
student_id,
name,
maths,
science,
english,

(maths + science + english) AS total,

(maths + science + english)/3 AS average,

CASE
WHEN (maths + science + english)/3 >= 90 THEN 'A+'
WHEN (maths + science + english)/3 >= 75 THEN 'A'
WHEN (maths + science + english)/3 >= 60 THEN 'B'
WHEN (maths + science + english)/3 >= 50 THEN 'C'
ELSE 'FAIL'
END AS grade

FROM student;
INSERT INTO student (name, maths, science, english)

VALUES ('Rahul', 78, 82, 69);
INSERT INTO student (name, maths, science, english)
VALUES ('Anita', 92, 88, 95);

INSERT INTO student (name, maths, science, english)
VALUES ('Kiran', 65, 70, 60);

INSERT INTO student (name, maths, science, english)
VALUES ('Divya', 50, 55, 58);
SELECT * FROM student;
SELECT
student_id,
name,
maths,
science,
english,
(maths + science + english) AS total,
(maths + science + english)/3 AS average,

CASE
WHEN (maths + science + english)/3 >= 90 THEN 'A+'
WHEN (maths + science + english)/3 >= 75 THEN 'A'
WHEN (maths + science + english)/3 >= 60 THEN 'B'
WHEN (maths + science + english)/3 >= 50 THEN 'C'
ELSE 'FAIL'
END AS grade

FROM student;
