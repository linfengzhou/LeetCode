SELECT d.dept_name, COUNT(t.student_id) as student_number
FROM department as d left join student as t
ON d.dept_id = t.dept_id
GROUP BY d.dept_id
ORDER BY student_number DESC, d.dept_name