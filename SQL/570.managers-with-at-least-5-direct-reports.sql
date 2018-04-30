SELECT Name 
FROM Employee AS e INNER JOIN (SELECT ManagerId
FROM Employee
GROUP BY ManagerId
HAVING COUNT(*) >= 5) AS t 
on e.Id = t.ManagerId