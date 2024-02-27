class OrderDetails:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address

class OrderCalculator:
    def calculate_total_cost(self, order_details):
        # Calculate total order cost including taxes and discounts
        total_cost = 0
        for item in order_details.items:
            total_cost += item['price']
        print(f"Total cost is: {total_cost}")

class OrderValidator:
    def validate_order(self, order_details):
        print("Order is valid.")

class OrderConfirmation:
    def send_confirmation_email(self, customer_email, order_details):
        print(f"Confirmation email sent to: {customer_email}")

class InventoryManager:
    def update_inventory(self, order_details):
        print("Inventory updated.")

class Order:
    def __init__(self, order_details):
        self.order_details = order_details
        self.id = 1  # Assign a unique ID for demonstration

    def validate_order(self):
        OrderValidator().validate_order(self.order_details)

    def send_confirmation_email(self, customer_email):
        OrderConfirmation().send_confirmation_email(customer_email, self.order_details)

    def update_inventory(self):
        InventoryManager().update_inventory(self.order_details)
    
    def calculate_total_cost(self):
        OrderCalculator().calculate_total_cost(self.order_details)


def main():
    # Sample items
    item1 = {"name": "Product A", "price": 20.00}
    item2 = {"name": "Product B", "price": 15.00}

    # Sample order details
    customer_info = {"name": "Jack Black", "email": "jBlack@hotmail.com"}
    shipping_address = "123 Main St, City, Country"

    order_details = OrderDetails(customer_info, [item1, item2], shipping_address)

    order = Order(order_details)

    order.validate_order()
    order.send_confirmation_email(customer_info['email'])
    order.update_inventory()
    order.calculate_total_cost()

if __name__ == "__main__":
    main()
