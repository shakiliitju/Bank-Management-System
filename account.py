
class Account:
    def __init__(self,account_number,name, email,address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.tansactions = []
        self.loan_amount = 0
        self.loan_taken = 0
   
    def deposite(self, amount):
        self.balance+=amount
        self.tansactions.append(f"Deposited : {amount}")
        print(f"{amount} deposited successfully.")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance-=amount
            self.tansactions.append(f"Withdraw : {amount}")
            print(f"{amount} withdrawn successfully.")
    
    def check_balance(self):
        print(f"Current Balance = {self.balance}")

    def transaction_history(self):
        for history in self.tansactions:
            print(f"{history}")
    
    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.loan_amount+=amount
            self.balance+=amount
            self.loan_taken+=1
            self.tansactions.append(f"Loan Taken: {amount}")
            print("Loan taken successfully.")
        else:
             print("You have already taken the maximum number of loans.")
    
    def transfer(self, amount, recipient,bank):
        if amount > self.balance:
            print("Insufficient balance.")
            return
        if  recipient not in bank.users:
            print("Recipient account does not exist.")
            return
        self.balance -= amount
        recipient.balance += amount
        self.tansactions.append(f"Transferred: {amount} to {recipient.name}")
        recipient.transaction_history.append(f"Received: {amount} from {self.name}")
        print("Amount transferred successfully.")

    
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Address: {self.address}, Account Type: {self.account_type}, Account Number: {self.account_number}, Balance: {self.balance}"
