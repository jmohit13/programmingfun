/*
Enter your query here.
*/
SELECT
    s.hacker_id, h.name, s.score, c.difficulty_level, d.score, COUNT(s.submission_id)
FROM Submissions s
left join Challenges c
on s.challenge_id = c.challenge_id
left join Difficulty d
on d.difficulty_level = c.difficulty_level
left join Hackers h
on h.hacker_id = s.hacker_id
WHERE s.score = d.score
GROUP BY h.name
ORDER BY s.score DESC, d.score DESC;
