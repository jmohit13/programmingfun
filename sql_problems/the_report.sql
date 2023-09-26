/*
Enter your query here.
*/

SELECT CASE
         WHEN (SELECT g.grade
               FROM   grades g
               WHERE  s.marks >= g.min_mark
                      AND s.marks <= g.max_mark) < 8 THEN NULL
         ELSE s.NAME
       END                                AS StudentName,
       (SELECT g.grade
        FROM   grades g
        WHERE  s.marks >= g.min_mark
               AND s.marks <= g.max_mark) AS Grade,
       s.marks
FROM   students s
ORDER  BY grade DESC,
          CASE
            WHEN grade >= 8 THEN studentname
            ELSE grade
          END ASC,
          CASE
            WHEN grade < 8 THEN s.marks
          END ASC