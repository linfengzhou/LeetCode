SELECT name
FROM salesperson
WHERE salesperson.sales_id not in 
(SELECT s.sales_id
FROM salesperson as s JOIN orders as o
on s.sales_id = o.sales_id JOIN company as c
on c.com_id = o.com_id
WHERE c.name='RED')