# LeetCode DataBase
## Nth Highest
### 176 Second Highest Salary
Solution 1(subquery):

```
SELECT(  
SELECT DISTINCT Salary  
FROM Employee  
ORDER BY Salary DESC  
LIMIT 1 OFFSET 1
) AS SecondHighestSalary
```

Solution 2(Trick):

```
SELECT max(Salary) As SecondHighestSalary  
FROM Employee  
WHERE Salary != (SELECT MAX(Salary) FROM Employee)
```

### 177 Nth Highest Salary
```
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE M INT;
    SET M = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary
      FROM Employee
      ORDER BY Salary DESC
      LIMIT M, 1
      
  );
END
```

# 181 
```
# Write your MySQL query statement below
SELECT e2.Name as Employee
FROM Employee AS e1 INNER JOIN Employee AS e2
ON e1.Id = e2.ManagerId 
WHERE e1.Salary < e2.Salary 

```
# 182
```
# Write your MySQL query statement below
SELECT Email
FROM Person
GROUP BY Email
Having COUNT(Email) > 1;
```
# 183
Without Subquery
 
```
SELECT c.Name as Customers
FROM Customers as c LEFT JOIN Orders AS o
ON c.id = o.CustomerId 
WHERE o.ID is NULL  
```

With Subquery

```
SELECT c.Name as Customers
FROM Customers as c
WHERE c.Id not in (SELECT CustomerId FROM Orders)
```

# 196 
Without Subquery

```
DELETE p1
FROM Person as p1, Person as p2
WHERE p1.Email = p2.Email and p1.Id > p2.Id
```

With Subquery

```
DELETE 
FROM Person 
WHERE Id NOT IN (
SELECT A.Id FROM (
SELECT MIN(Id) AS Id 
FROM Person 
GROUP BY Email
) 
AS A
)
```

# 197
```
SELECT w1.Id as Id
FROM Weather w1 INNER JOIN Weather w2
on DATEDIFF(w1.Date, w2.Date) = 1 and w1.temperature > w2.temperature;
```

Using Variable Solution??? (to do)
