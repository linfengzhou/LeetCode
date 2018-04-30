SELECT Name
FROM Candidate AS c INNER JOIN
	(SELECT CandidateId, Count(*) as total 
	FROM Vote
	GROUP BY CandidateId
	ORDER BY total DESC
	LIMIT 1) AS t
ON c.Id = t.CandidateId
