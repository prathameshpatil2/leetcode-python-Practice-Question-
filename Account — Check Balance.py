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

acc3 = Account("87678", 70000)
acc3.show_balance()

acc4 = Account("76898", 90000)
acc4.show_balance()

acc5 = Account("67876", 60000)
acc5.show_balance()

acc6 = Account("98789", 50000)
acc6.show_balance()

acc7 = Account("56789", 40000)
acc7.show_balance()

acc8 = Account("34567", 30000)
acc8.show_balance()

acc9 = Account("23456", 20000)
acc9.show_balance()

acc10 = Account("12345", 10000)
acc10.show_balance()

acc11 = Account("98765", 50000)
acc11.show_balance()