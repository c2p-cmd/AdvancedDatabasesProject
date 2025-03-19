-- Analytics good for the businesses


-- 5 most popular games
SELECT 
    v.title,
    v.genre,
    COUNT(gp.purchase_id) AS times_purchased
FROM
    VideoGames v
INNER JOIN
    Purchases gp ON v.game_id = gp.game_id
GROUP BY
    v.title, v.genre
ORDER BY
    times_purchased DESC
LIMIT 5;


-- gamers with most purchases
SELECT 
    g.gamer_tag,
    g.email,
    COUNT(gp.purchase_id) AS games_purchased,
    SUM(gp.price_paid) AS total_spent
FROM
    Gamers g
INNER JOIN
    Purchases gp ON g.gamer_tag = gp.gamer_tag
GROUP BY
    g.gamer_tag, g.email
ORDER BY
    games_purchased DESC;


-- gamers with max spending
SELECT 
    g.gamer_tag,
    g.email,
    COUNT(gp.purchase_id) AS games_purchased,
    SUM(gp.price_paid) AS total_spent
FROM
    Gamers g
INNER JOIN
    Purchases gp ON g.gamer_tag = gp.gamer_tag
GROUP BY
    g.gamer_tag, g.email
ORDER BY
    total_spent DESC;


-- gamers with 0 spending
SELECT 
    g.gamer_tag,
    g.email
FROM
    Gamers g
LEFT JOIN
    Purchases p ON g.gamer_tag = p.gamer_tag
WHERE
    p.purchase_id IS NULL
GROUP BY
    g.gamer_tag;
    

-- games that have not been purchased
SELECT 
	v.game_id,
    v.title,
    v.genre
FROM
    VideoGames v
LEFT JOIN
    Purchases gp ON v.game_id = gp.game_id
WHERE
    gp.purchase_id IS NULL;


-- top 5 most expensive games
SELECT 
    v.title,
    v.genre,
    v.price
FROM
    VideoGames v
ORDER BY
    v.price DESC
LIMIT 5;


-- top 5 cheapest games
SELECT 
    v.title,
    v.genre,
    v.price
FROM
    VideoGames v
ORDER BY
    v.price
LIMIT 5;


-- publishers with their game count
SELECT 
    gp.publisher_id,
    gp.name,
    gp.country,
    COUNT(v.game_id) AS games_published
FROM
    GamePublishers gp
INNER JOIN
    VideoGames v ON gp.publisher_id = v.publisher_id
GROUP BY
    gp.publisher_id
ORDER BY
    games_published DESC;
