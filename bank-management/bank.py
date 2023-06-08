from user import User
from admin import Admin

class Bank:
    def __init__(self):
        self.total_balance = 100000
        self.total_loan = 0
        self.is_loan = True
        self.users = []

    def create_account(self, name, email, password):
        user = User(name, email, password)
        self.users.append(user)
        return user

    def create_admin(self, name, email, password):
        admin = Admin(name, email, password, self)
        self.users.append(admin)
        return admin
