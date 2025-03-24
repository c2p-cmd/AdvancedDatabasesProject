DELIMITER //

-- show a gamer's library
DROP PROCEDURE IF EXISTS ShowGamerLibrary//
CREATE PROCEDURE ShowGamerLibrary(
	IN gamer_tag varchar(30)
)
BEGIN
	DECLARE does_exist BOOL DEFAULT FALSE;
    
    SELECT TRUE INTO does_exist FROM Gamers WHERE gamer_tag = gamer_tag LIMIT 1;
    
    IF does_exist = FALSE THEN
        SELECT 'Error: Gamer does not exist' AS message;
    ELSE
        SELECT
            v.title, v.price, v.genre
        FROM
            Purchases p
        INNER JOIN
            VideoGames v
        ON
            p.game_id = v.game_id
        WHERE
            p.gamer_tag = gamer_tag;
    END IF;
END//

-- purchase a video game
DROP PROCEDURE IF EXISTS BuyGame//
CREATE PROCEDURE BuyGame(
    IN p_gamer_tag VARCHAR(30),
    IN p_game_id INT
)
BEGIN
    DECLARE p_price DECIMAL(5, 2);

    IF NOT EXISTS (SELECT * FROM VideoGames WHERE game_id = p_game_id) THEN
        SELECT 'Error: Game does not exist' AS message;
    ELSEIF NOT EXISTS (SELECT * FROM Gamers WHERE gamer_tag = p_gamer_tag) THEN
        SELECT 'Error: Gamer does not exist' AS message;
    ELSEIF EXISTS (SELECT * FROM Purchases WHERE gamer_tag = p_gamer_tag AND game_id = p_game_id) THEN
        SELECT 'Error: Game already purchased' AS message;
    ELSE
        SELECT price INTO p_price FROM VideoGames WHERE game_id = p_game_id;
        
        INSERT INTO Purchases (gamer_tag, game_id, purchase_date, price_paid)
        VALUES (p_gamer_tag, p_game_id, NOW(), p_price);
        
        SELECT 'Purchase successful' AS message;
    END IF;
END//

-- show all gamers with their purchases
DROP PROCEDURE IF EXISTS ShowGamersWithPurchases//
CREATE PROCEDURE ShowGamersWithPurchases()
BEGIN
    SELECT 
        g.gamer_tag,
        g.email,
        COUNT(p.purchase_id) AS purchase_count,
        SUM(p.price_paid) AS total_spent
    FROM 
        Gamers g
    LEFT JOIN 
        Purchases p
    ON
        g.gamer_tag = p.gamer_tag
    GROUP BY 
        g.gamer_tag, g.email
    ORDER BY 
        purchase_count DESC;
END//

-- video games that have been purchased
DROP PROCEDURE IF EXISTS ShowPurchasedGames//
CREATE PROCEDURE ShowPurchasedGames()
BEGIN
    SELECT 
        v.title,
        v.genre,
        COUNT(p.purchase_id) AS times_purchased
    FROM 
        VideoGames v
    INNER JOIN 
        Purchases p ON v.game_id = p.game_id
    GROUP BY 
        v.title, v.genre
    ORDER BY 
        times_purchased DESC;
END//

DELIMITER ;