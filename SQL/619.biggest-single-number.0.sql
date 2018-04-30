SELECT MAX(NUM) as num FROM(
SELECT num
FROM number
GROUP BY num 
Having COUNT(*) = 1 ) as t