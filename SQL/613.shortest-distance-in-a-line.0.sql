SELECT MIN(ABS(p1.x - p2.x)) as shortest
FROM point p1 INNER JOIN point p2
ON p1.x <> p2.x