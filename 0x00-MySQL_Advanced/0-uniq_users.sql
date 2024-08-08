-- SQL script that creates a table users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(225) NOT NULL UNIQUE,
    name VARCHAR(225),
    PRIMARY KEY(id)
);
