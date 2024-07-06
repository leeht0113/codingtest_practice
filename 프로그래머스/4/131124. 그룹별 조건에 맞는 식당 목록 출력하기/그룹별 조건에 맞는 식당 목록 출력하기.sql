-- 코드를 입력하세요
SELECT m.member_name, r.review_text, DATE_FORMAT(r.review_date, '%Y-%m-%d') AS review_date
FROM MEMBER_PROFILE AS m JOIN REST_REVIEW AS r ON m.member_id = r.member_id
WHERE m.member_name = (
SELECT m.member_name 
FROM MEMBER_PROFILE AS m JOIN REST_REVIEW AS r ON m.member_id = r.member_id
GROUP BY m.member_name
ORDER BY COUNT(REVIEW_ID) DESC
LIMIT 1
)
ORDER BY r.review_date, r.review_text