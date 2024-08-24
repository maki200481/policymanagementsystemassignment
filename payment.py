#creating the payment class.
class Payment:
    def __init__(self, payment_id, policyholder_id, product_id, amount, date):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.date = date

#payment management (implementing methods for payment processing, reminders, and penalties.)
 
    def process_payment(self):
        return f"Payment of {self.amount} for Product {self.product_id} processed on {self.date}."

    def send_reminder(self):
        return "Payment reminder sent."

    def apply_penalty(self):
        return "Late payment penalty applied."