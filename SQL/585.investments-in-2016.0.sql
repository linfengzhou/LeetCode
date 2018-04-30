SELECT SUM(TIV_2016) AS TIV_2016
FROM insurance
WHERE TIV_2015 IN (
SELECT TIV_2015 
FROM insurance
GROUP BY TIV_2015
HAVING COUNT(*) > 1) and CONCAT(LAT,LON) IN (
SELECT CONCAT(LAT,LON)
FROM insurance
GROUP BY CONCAT(LAT,LON)
HAVING COUNT(*) = 1)