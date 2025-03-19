DELIMITER //

-- Prevent deletion of a publisher with games
CREATE TRIGGER before_publisher_delete
BEFORE DELETE ON GamePublishers
FOR EACH ROW
BEGIN
    DECLARE game_count INT;
    
    SELECT COUNT(*) INTO game_count
    FROM VideoGames
    WHERE publisher_id = OLD.publisher_id;
    
    IF game_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete publisher with associated games';
    END IF;
END//

-- Auto-add registration_date if not provided
CREATE TRIGGER default_registration_date
BEFORE INSERT ON Gamers
FOR EACH ROW
BEGIN
    IF NEW.registration_date IS NULL THEN
        SET NEW.registration_date = CURDATE();
    END IF;
END//

-- Prevent negative prices for games
CREATE TRIGGER prevent_negative_game_price
BEFORE INSERT ON VideoGames
FOR EACH ROW
BEGIN
    IF NEW.price < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Game price cannot be negative';
    END IF;
END//


CREATE TRIGGER prevent_negative_game_price_update
BEFORE UPDATE ON VideoGames
FOR EACH ROW
BEGIN
    IF NEW.price < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Game price cannot be negative';
    END IF;
END//

DELIMITER ;