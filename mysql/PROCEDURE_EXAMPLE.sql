-- Show Users
SELECT * FROM Gamers;

-- See Rainbow Archer's Library
Call ShowGamerLibrary('RainbowArcher');

-- Purchase a game
Call BuyGame('RainbowArcher', 22);

-- Show All Gamers with their purchases
CALL ShowGamersWithPurchases();

-- Video games that been purchased
CALL ShowPurchasedGames();
