-- 각그룹별로 한명씩 착출하고 싶을 때 
-- 참조 : https://blogs.oracle.com/sql/post/how-to-select-the-top-n-rows-per-group-with-sql-in-oracle-database

with rws as (
  select o.*, row_number () over (
           partition by customer_id
           order by order_datetime desc
         ) rn
  from   co.orders o
)
  select * from rws
  where  rn <= 1
  order  by customer_id, order_datetime desc;
