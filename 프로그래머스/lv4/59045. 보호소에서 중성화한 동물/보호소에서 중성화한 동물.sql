-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS AS A
LEFT JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE (A.SEX_UPON_INTAKE='Intact Male' OR A.SEX_UPON_INTAKE='Intact Female') 
AND (B.SEX_UPON_OUTCOME='Neutered Male' OR B.SEX_UPON_OUTCOME='Spayed Female')
ORDER BY ANIMAL_ID