SELECT Name 
FROM Employee
WHERE Id in 
(SELECT ManagerId 
FROM Employee
GROUP BY ManagerId
HAVING COUNT(*) >= 5)