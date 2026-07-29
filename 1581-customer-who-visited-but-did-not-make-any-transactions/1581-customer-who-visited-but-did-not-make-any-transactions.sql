# Write your MySQL query statement below
SELECT customer_id,count(visit_id) AS count_no_trans FROM Visits
WHERE visit_id not in (select visit_id from Transactions)
group by customer_id;