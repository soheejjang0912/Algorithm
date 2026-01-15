SELECT
    GRADE,
    ID,
    EMAIL
FROM (
    SELECT
        CASE
            WHEN
                (d.SKILL_CODE & fe.FE_CODE) > 0
                AND (d.SKILL_CODE & py.CODE) > 0
            THEN 'A'
            WHEN
                (d.SKILL_CODE & cs.CODE) > 0
            THEN 'B'
            WHEN
                (d.SKILL_CODE & fe.FE_CODE) > 0
            THEN 'C'
        END AS GRADE,
        d.ID,
        d.EMAIL
    FROM DEVELOPERS d
    CROSS JOIN (
        SELECT SUM(CODE) AS FE_CODE
        FROM SKILLCODES
        WHERE CATEGORY = 'Front End'
    ) fe
    CROSS JOIN (
        SELECT CODE
        FROM SKILLCODES
        WHERE NAME = 'Python'
    ) py
    CROSS JOIN (
        SELECT CODE
        FROM SKILLCODES
        WHERE NAME = 'C#'
    ) cs
) t
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID;
