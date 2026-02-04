class BankAccount:
    def __init__(self,account_no,balance=0.0):
        self.account_no = account_no
        self.balance = balance
    def deposite(self,amount):
        if amount >= 0:
            self.balance+=amount
            print(f"Deposited:Rs{amount},New Balance:{self.balance}")
        else:
            print("Deposited amount be positive")
    def withdrawal(self,amount):
        if amount >= 0:
            if amount <= self.balance:
                self.balance-= amount
                print(f"Withdrawn:Rs{amount}, Remaining Balance:Rs{self.balance}")
            else:
                print("Insufficient balance")
        else :
            print("Withdrawal amount must be positive.")
    def check_balance(self):
        print(f"Account No:{self.account_no}")

account=BankAccount("SBI1234",10000)
account.deposite(500)
account.withdrawal(100)
account.check_balance()