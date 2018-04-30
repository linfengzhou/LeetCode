SELECT name
FROM salesperson
WHERE salesperson.sales_id not in 
(SELECT o.sales_id
FROM rders as o
JOIN company as c
on c.com_id = o.com_id
WHERE c.name='RED')