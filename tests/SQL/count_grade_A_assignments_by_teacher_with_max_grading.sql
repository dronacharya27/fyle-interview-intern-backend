-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH GradingCounts AS (
    SELECT
        teacher_id,
        COUNT(*) AS graded_count
    FROM
        assignments
    WHERE
        grade = 'A' AND state = 'GRADED'
    GROUP BY
        teacher_id
    ORDER BY
        graded_count DESC
    LIMIT 1
)

SELECT
    COUNT(*) AS grade_a_count
FROM
    assignments a
JOIN
    GradingCounts gc ON a.teacher_id = gc.teacher_id
WHERE
    a.grade = 'A' AND a.state = 'GRADED';
