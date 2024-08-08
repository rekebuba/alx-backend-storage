-- Active: 1716468751032@@127.0.0.1@3306@holberton

DROP TRIGGER IF EXISTS monitor_order;
CREATE TRIGGER monitor_order
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
