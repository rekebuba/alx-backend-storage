-- SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order.

-- drop if exists
DROP TRIGGER IF EXISTS monitor_order;

-- create trigger
CREATE TRIGGER monitor_order
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
