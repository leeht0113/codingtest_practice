-- 코드를 입력하세요
WITH review_count AS (
SELECT MEMBER_ID, COUNT(REVIEW_ID) AS review_cnt
FROM REST_REVIEW
GROUP BY MEMBER_ID
)
SELECT m.member_name, r.review_text, DATE_FORMAT(r.review_date, '%Y-%m-%d') AS review_date
FROM MEMBER_PROFILE AS m JOIN REST_REVIEW AS r ON m.member_id = r.member_id
WHERE m.member_id IN (SELECT MEMBER_ID 
                      FROM review_count 
                      WHERE review_cnt = (SELECT MAX(review_cnt) FROM review_count))
ORDER BY review_date, r.review_text
