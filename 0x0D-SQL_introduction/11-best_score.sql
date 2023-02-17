-- Print all scores and name so far the score >= 10
SELECT `score`, `name` FROM `second_table`
WHEN `score` >= 10
ORDER BY `score` DESC;
