SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person as p LEFT JOIN Address as a 
ON p.PersonId=a.PersonId