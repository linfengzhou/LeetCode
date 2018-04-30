set @prevName:=null;

SELECT id, student FROM (SELECT s1.id, CASE 
WHEN s1.id%2=1 and t.student is not null THEN t.student
WHEN s1.id%2=1 and t.student is null THEN s1.student
ELSE @prevName
END student, @prevName:=s1.student
FROM seat s1 left join (SELECT s1.id, s2.student
FROM seat s1 left join seat s2
on s1.id + 1 = s2.id) t
on s1.id = t.id) t2
