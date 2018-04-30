set @max := (SELECT CandidateId
	FROM Vote
	GROUP BY CandidateId
	ORDER BY Count(*) DESC
	LIMIT 1);
SELECT Name
FROM Candidate
WHERE Id = @max