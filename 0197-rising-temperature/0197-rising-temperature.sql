# Write your MySQL query statement below
select m1.id 
from Weather m1 join Weather m2
    on datediff(m1.recordDate, m2.recordDate) =1
where m1.temperature > m2.temperature;