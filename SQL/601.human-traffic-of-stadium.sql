SELECT DISTINCT(s1.id), s1.date, s1.people
FROM stadium as s1, stadium as s2, stadium as s3
WHERE (
    (s1.id-s2.id = 1 and s1.id-s3.id = 2) or
    (s1.id-s2.id = 1 and s1.id-s3.id = -1) or
    (s1.id-s2.id = -1 and s1.id-s3.id = -2 )) AND 
    s1.people >= 100 and 
    s2.people >= 100 and 
    s3.people >= 100 
ORDER BY s1.id