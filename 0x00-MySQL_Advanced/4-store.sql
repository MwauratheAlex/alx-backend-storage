-- creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER decrease_qty_after_order
AFTER INSERT
ON orders
UPDATE TABLE items
SET quantity = items.quantity - NEW.quantity
WHERE items.name = NEW.name
