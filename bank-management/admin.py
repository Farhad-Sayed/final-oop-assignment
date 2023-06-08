from user import User

class Admin(User):
    def __init__(self, name, email, password, bank):
        super().__init__(name, email, password)
        self.bank = bank

    def check_total_balance(self):
        return self.bank.total_balance

    def check_total_loan(self):
        return self.bank.total_loan
