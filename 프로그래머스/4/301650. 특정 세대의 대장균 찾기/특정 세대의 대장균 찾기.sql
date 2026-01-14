WITH RECURSIVE ecoli_gen AS (
    -- 1세대
    SELECT
        ID,
        PARENT_ID,
        1 AS generation
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL

    UNION ALL

    -- 다음 세대
    SELECT
        e.ID,
        e.PARENT_ID,
        g.generation + 1
    FROM ECOLI_DATA e
    JOIN ecoli_gen g
      ON e.PARENT_ID = g.ID
)
SELECT ID
FROM ecoli_gen
WHERE generation = 3
ORDER BY ID;
