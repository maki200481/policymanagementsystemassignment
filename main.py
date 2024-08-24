from policyholder import PolicyHolder
from product import Product
from payment import Payment

#function to display policyholder account details
def display_account_details(policyholder, payment):
    status = 'Active' if policyholder.active else 'Inactive'
    print(f"Policyholder ID: {policyholder.policyholder_id}, Name: {policyholder.name}")
    print(f"Email: {policyholder.contact_info}, Status: {status}")
    payment.process_payment()

# Create instances of PolicyHolder
policyholder1 = PolicyHolder(policyholder_id=1, name="Amaka John", contact_info="amaka.john@gmail.com")
policyholder2 = PolicyHolder(policyholder_id=2, name="Brie Smith", contact_info="brie.smith@gmail.com")

# Registering the policyholders
policyholder1.register()
policyholder2.register()

# Create an instance of a Product
product1 = Product(product_id=101, name="Health Insurance", description="Comprehensive health coverage", price=500)

# Process payments for each policyholder
payment1 = Payment(payment_id=201, policyholder_id=policyholder1.policyholder_id, product_id=product1.product_id, amount=product1.price)
payment2 = Payment(payment_id=202, policyholder_id=policyholder2.policyholder_id, product_id=product1.product_id, amount=product1.price)

# Displaying the details of each policyholder and their payment status
display_account_details(policyholder1, payment1)
display_account_details(policyholder2, payment2)
