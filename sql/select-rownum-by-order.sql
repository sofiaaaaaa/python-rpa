-- 참조 https://gent.tistory.com/170

-- order by 된 결과에 순번을 매기는 방법. 
SELECT ROW_NUMBER() OVER(ORDER BY a.job, a.ename) row_num
     , a.*
  FROM emp a
 ORDER BY a.job, a.ename
