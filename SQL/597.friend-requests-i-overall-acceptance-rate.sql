SELECT ROUND(IFNULL(((SELECT COUNT(DISTINCT requester_id, accepter_id)
		FROM request_accepted AS ac) / 
(SELECT COUNT(DISTINCT sender_id, send_to_id)
		FROM friend_request AS rq)), 0), 2) AS accept_rate
