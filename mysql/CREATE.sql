CREATE DATABASE IF NOT EXISTS gaming_db;

USE gaming_db;

CREATE TABLE Gamers (
	gamer_tag varchar(30) primary key,
    email varchar(100) unique,
    registration_date date not null,
    birth_date date
);

CREATE TABLE GamePublishers (
	publisher_id int primary key auto_increment,
    name varchar(50) not null,
    country varchar(50) not null,
    founding_date date not null
);

CREATE TABLE VideoGames (
	game_id int primary key auto_increment,
    title varchar(100) unique not null,
    release_date date not null,
    genre varchar(50) not null,
    price decimal(5, 2) not null,
    publisher_id int not null,
    FOREIGN KEY (publisher_id) REFERENCES GamePublishers(publisher_id)
);

CREATE TABLE Purchases (
    purchase_id int primary key auto_increment,
    gamer_tag varchar(30) not null,
    game_id int not null,
    purchase_date datetime not null DEFAULT CURRENT_TIMESTAMP,
    price_paid decimal(5, 2) not null,
    FOREIGN KEY (gamer_tag) REFERENCES Gamers(gamer_tag),
    FOREIGN KEY (game_id) REFERENCES VideoGames(game_id)
);

SHOW TABLES;
