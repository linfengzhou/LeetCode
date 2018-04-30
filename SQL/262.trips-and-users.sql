SELECT t.Request_at as Day, ROUND(COUNT(IF(t.Status='cancelled_by_client' or t.Status='cancelled_by_driver',TRUE,NULL))/COUNT(*),2) AS 'Cancellation Rate'
FROM Trips as t
WHERE t.Request_at BETWEEN '2013-10-01' and '2013-10-03' and t.Client_Id in (SELECT Users_Id FROM Users WHERE Banned='No' and Role='client')
GROUP BY t.Request_at

