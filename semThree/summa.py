# Base class
class PaymentMethod:
    def process_payment(self, amount):
        pass

# Derived class for Credit Card
class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print("Hello")
        return f"Processing credit card payment of {amount}"

# Derived class for PayPal
class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print("Hai")
        return f"Processing PayPal payment of {amount}"

# Function to demonstrate polymorphism
def process_order(payment_method, amount):
    amt = payment_method.process_payment(amount)
    print(amt)
