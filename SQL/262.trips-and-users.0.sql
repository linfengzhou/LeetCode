SELECT t.Request_at as Day, ROUND(COUNT(IF(t.Status like 'cancelled%',TRUE,NULL))/COUNT(*),2) AS 'Cancellation Rate'
FROM Trips as t INNER JOIN Users as u
ON t.Client_Id = u.Users_Id
WHERE t.Request_at BETWEEN '2013-10-01' and '2013-10-03' and u.Banned='No' and u.Role='client'
GROUP BY t.Request_at

