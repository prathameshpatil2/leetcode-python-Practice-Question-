class Account:

    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount
        print("Balance", self.balance)

acc1 = Account(12323, 10000)
acc1.debit(2000)

acc2 = Account(12345, 20000)
acc2.debit(5000)