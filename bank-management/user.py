class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0
        self.transaction_history = []
        self.loan = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(('Deposit', amount))

    def withdraw(self, amount, bank):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(('Withdraw', amount))
            bank.total_balance -= amount
            return True
        elif bank.total_balance < amount:
            print("Bank is bankrupt!")
            return False
        else:
            print("You have inadequate balance!")
            return False

    def check_balance(self):
        return self.balance

    def transfer(self, amount, recipient, bank):
        if self.withdraw(amount, bank):
            recipient.deposit(amount)
            self.transaction_history.append(('Transfer', amount, recipient.name))

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, loan_amount, bank):
        max_loan_amount = self.balance * 2
        if bank.is_loan and loan_amount <= max_loan_amount:
            self.loan += loan_amount
            self.balance += loan_amount
            bank.total_loan += loan_amount
            self.transaction_history.append(('Loan', loan_amount))
        else:
            print("You cant take more than twice of your balance!")