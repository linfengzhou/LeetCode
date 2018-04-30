set @row_number=1, @last_dep=NULL;

SELECT d.Name as Department, t1.Name as Employee, t1.Salary
FROM Department as d join 
(SELECT Name, Salary, DepartmentId, CASE
WHEN @last_dep is NULL or @last_dep <> DepartmentId THEN  @row_number:=1
ELSE @row_number := @row_number + 1
END as row_number, @last_dep:=DepartmentId
FROM (SELECT * FROM Employee ORDER BY DepartmentId, Salary DESC) as t) AS t1
on d.Id=t1.DepartmentId
WHERE t1.row_number <= 3
