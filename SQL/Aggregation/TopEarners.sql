SELECT (SALARY * MONTHS) AS EARNINGS, COUNT(*) FROM EMPLOYEE
GROUP BY 1
ORDER BY EARNINGS DESC LIMIT 1