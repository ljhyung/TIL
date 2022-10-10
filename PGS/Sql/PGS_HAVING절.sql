SELECT NAME, COUNT(NAME) FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME)>1 ORDER BY NAME;
-- where은 기본적인 조건절로서 우선적으로 모든 필드를 조건에 둘 수 있다. 
-- 하지만 having은 group by 된 이후 특정한 필드로 그룹화 되어진 새로운 테이블에 조건을 줄 수 있다