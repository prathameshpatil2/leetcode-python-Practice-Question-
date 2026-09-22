class Account:

    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount
        print("Balance", self.balance)

