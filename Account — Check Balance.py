class Account:

    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def show_balance(self):
        print("Account No:", self.account_no)
        print("Balance:", self.balance)

acc1 = Account("12345", 10000)
acc1.show_balance()

acc2 = Account("67567", 60000)
acc2.show_balance()