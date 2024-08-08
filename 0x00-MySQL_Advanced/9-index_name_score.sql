-- Active: 1716468751032@@127.0.0.1@3306@holberton
ALTER TABLE names
DROP INDEX idx_name_first;

CREATE INDEX idx_name_first_score ON names((LEFT(name, 1)), score);

