-- creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER after_order_insert
AFTER INSERT
ON orders
UPDATE items
SET quantity = quantity - NEW.quantity
WHERE items.name = NEW.name
