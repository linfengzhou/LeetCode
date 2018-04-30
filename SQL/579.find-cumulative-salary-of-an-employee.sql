SELECT e1.Id as id, e1.Month as month, e1.Salary + IFNULL(e2.Salary,0) + IFNULL(e3.Salary,0) as Salary
FROM Employee as e1 LEFT JOIN Employee as e2 
ON e1.Id = e2.Id and e1.Month - 2 = e2.Month
LEFT JOIN Employee as e3
ON e1.Id = e3.Id and e1.Month - 1 = e3.Month
JOIN (SELECT Id, MAX(MONTH) as Month FROM
     Employee GROUP BY Id) as t1
     ON e1.Id = t1.Id and e1.Month != t1.Month
ORDER BY e1.Id, e1.Month DESC