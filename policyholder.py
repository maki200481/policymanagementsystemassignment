#creating the policyholders class.
class Policyholder:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.status = "active"
        
#policyholder management (implementing methods to register, suspend, and reactivate policyholders)
    def register(self):
        return f"Policyholder {self.name} registered with email {self.email}."

    def suspend(self):
        self.status = "suspended"
        return f"Policyholder {self.name} is now suspended."

    def reactivate(self):
        self.status = "active"
        return f"Policyholder {self.name} is now active again."  