SELECT first_name, last_name FROM student;

SELECT instructor_id FROM instructor WHERE tenured = 1;

SELECT s.first_name AS student_first_name, s.last_name AS student_last_name, 
       i.first_name AS advisor_first_name, i.last_name AS advisor_last_name
FROM student AS s 
JOIN instructor AS i ON s.advisor_id = i.instructor_id 
WHERE s.advisor_id IS NOT NULL;

SELECT i.instructor_id, i.first_name, i.last_name
FROM instructor i
LEFT JOIN student s ON i.instructor_id = s.advisor_id
WHERE s.advisor_id IS NULL;

SELECT 
  i.first_name, 
  i.last_name, 
  SUM(c.num_credits) AS total_credits 
FROM 
  instructor i 
  JOIN course c ON i.instructor_id = c.instructor_id 
GROUP BY 
  i.instructor_id;

-- Website: https://www.w3schools.com/sql/sql_like.asp
-- The LIKE operator in this query means that it will return any course code that starts with 3 and can end with any number.

SELECT course.course_code, instructor.first_name, instructor.last_name, course.num_credits
FROM course
JOIN instructor ON course.instructor_id = instructor.instructor_id
JOIN student_schedule ON course.course_id = student_schedule.course_id
WHERE student_schedule.student_id = 1;

SELECT course_code, course_name
FROM course
WHERE course_code LIKE '3__%'
