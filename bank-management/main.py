from bank import Bank

def main():
    bank = Bank()
    # Create users
    user1 = bank.create_account('User1', 'user1@phitron.com', '123')
    user2 = bank.create_account('User2', 'user2@phitron.com', '456')
    # Create admin
    admin = bank.create_admin('Admin', 'admin@phitron.com', '789')

    # deposit, transfer, withdraw, loan
    user1.deposit(50000)
    user2.withdraw(10000, bank)
    user1.transfer(10000, user2, bank)
    print(user2.check_balance())
    user1.withdraw(5000, bank)
    user2.take_loan(30000, bank)
    print(user1.check_transaction_history())
    print(user2.check_transaction_history())

    # balance check
    print(admin.check_total_balance())
    print(admin.check_total_loan())

if __name__ == "__main__":
    main()
