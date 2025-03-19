-- adding a null registration date
INSERT INTO Gamers (gamer_tag, email, birth_date)
VALUES ('unknown_gamer', 'somegamer@gmail.com', '2000-10-03');

SELECT * FROM Gamers where gamer_tag = 'unknown_gamer';

-- adding a negative price (should fail)
UPDATE VideoGames SET price = -10 WHERE title = 'Mario Tennis Aces';

-- deleting a publisher with games
-- fail
DELETE FROM GamePublishers WHERE publisher_id = 3;

-- success
DELETE FROM GamePublishers where publisher_id = 11;
