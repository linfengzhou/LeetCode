SELECT sum(i.TIV_2016) as TIV_2016
FROM insurance as i 
INNER JOIN (SELECT LAT,LON
		FROM insurance
		GROUP BY LAT, LON
		HAVING count(*)=1) AS ll
ON ll.LAT = i.LAT and ll.LON = i.LON
WHERE i.TIV_2015 in (
		SELECT TIV_2015
		FROM insurance 
		GROUP BY TIV_2015
		HAVING count(*)>1)
