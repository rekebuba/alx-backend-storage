-- Active: 1716468751032@@127.0.0.1@3306@hbtn_0d_tvshows
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT AUTO_INCREMENT,
    `email` VARCHAR(225) NOT NULL UNIQUE,
    `name` VARCHAR(225),
    PRIMARY KEY(`id`)
);
