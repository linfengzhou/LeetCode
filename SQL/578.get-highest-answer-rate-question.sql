SELECT question_id as survey_log
FROM survey_log
GROUP BY question_id
ORDER BY count(answer_id) / count(distinct q_num) DESC
LIMIT 1