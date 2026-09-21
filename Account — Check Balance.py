class Account:

    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def show_balance(self):
        print("Account No:", self.account_no)
        print("Balance:", self.balance)
