import random
from account import Account
from admin import Admin
class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.users = []
        self.admin = Admin()
        self.loan_feature  = True
    
    def create_account(self,name,email,address,account_type):
        account_number = random.randint(1000,100000)
        account = Account(account_number,name,email,address,account_type)
        self.users.append(account)
        print(f"{account_number} created successfuly")
        return account
    
    def delete_account(self,account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print(f"{account_number} deleted successfully")
                return
        print(f"{account_number} not found")

    def get_all_accounts(self):
        for user in self.users:
            print(user)
    def total_available_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print(f"Total balance: = {total_balance}")

    def total_loan_amount(self):
        total_loan = sum(user.loan_amount for user in self.users)
        print(f"Total loan = {total_loan}")
    
    def on_loan_feature(self):
        self.loan_feature=True
        print("Loan Feature is now Enabled")

    def off_loan_feature(self):
        self.loan_feature = False
        print("Loan feature is now disabled")
    
        
