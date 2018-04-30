SET @prev:=NUll;
SELECT min(t2.distance) as shortest
FROM(
SELECT IF(@prev is NULL, NULL, t1.x-@prev) as distance, @prev:=t1.x
FROM (SELECT * 
FROM point
ORDER BY x) 
as t1) 
as t2