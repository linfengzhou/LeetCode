# Write your MySQL query statement below
select p.FirstName, p.LastName, a.City, a.state
from Person as p LEFT JOIN Address as a
on p.PersonId = a.PersonId