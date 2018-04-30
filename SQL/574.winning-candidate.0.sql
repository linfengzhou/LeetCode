SELECT Name
FROM Candidate 
WHERE Id = 
	(SELECT CandidateId
	FROM Vote
	GROUP BY CandidateId
	ORDER BY Count(*) DESC
	LIMIT 1)