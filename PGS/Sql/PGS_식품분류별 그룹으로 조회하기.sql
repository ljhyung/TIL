SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME FROM FOOD_PRODUCT WHERE CATEGORY IN ('과자','국','김치','식용유') AND PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY) GROUP BY CATEGORY ORDER BY MAX_PRICE DESC;

-- 그룹별로 조회하는데 그냥 조회하면 제품이름이 제품가격 MAX인 제품의 이름을 가져오지 않아서 WHERE조건절에 가격 조건을 넣었다