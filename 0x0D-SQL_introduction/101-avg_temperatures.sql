-- displays the average temperature (Fahrenheit) by 
-- city ordered by temperature (descending)
SELECT `city`, ARG(`value`) AS `arg_temp`
FROM `first_table`
GROUP BY `city`
ORDER BY `arg_temp` DESC
