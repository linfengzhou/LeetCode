SELECT distinct(c1.seat_id)
FROM cinema as c1 JOIN cinema as c2 
on abs(c1.seat_id - c2.seat_id) = 1
WHERE c1.free=1 and c2.free=1
ORDER BY c1.seat_id