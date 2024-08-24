#creating the product class.
class Product:
    def __init__(self, product_id, name, description, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.status = "available"

#product management (implementing methods for creating, updating, and removing/suspending policy products.)
    def create(self):
        return f"Product {self.name} created with ID {self.product_id}."

    def update_details(self, new_details):
        self.description = new_details
        return f"Product {self.name} updated."

    def suspend(self):
        self.status = "suspended"
        return f"Product {self.name} is now suspended."