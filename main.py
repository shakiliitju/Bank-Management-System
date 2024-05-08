from account import Account
from admin import Admin
from bank import Bank

bank = Bank("Bangladesh")
admin = Admin()
current_user = None
while True:
    print(f"\n.....Welcome to {bank.name} bank........\n")
    print("1.Admin")
    print("2.User")
    print("3.Exit")

    choise = int(input("Enter your option = "))

    if choise==1:
       while True:
            print("\n-------Admin Options---------\n")
            print("1.Create Account")
            print("2.Delete Account")
            print("3.View All  Account")
            print("4.Check Total Amount")
            print("5.Check Total Loan Amount")
            print("6.On Loan Feature")
            print("7.Off Loan Feature")
            print("8.Go to main pages")

            ch = int(input("Enter your Option = "))

            if ch==1:
                name = input("Name = ")
                email = input("Email = ")
                address = input("Address = ")
                type = input("Type = ")
                current_user=admin.create_account(bank,name,email,address,type)
            elif ch==2:
                account  = int(input("Account Number = "))
                admin.delete_account(bank,account_number=account)
            elif ch==3:
                admin.get_all_accounts(bank)
            elif ch==4:
                admin.get_total_balance(bank)
            elif ch==5:
                admin.get_total_loan_amount(bank)
            elif ch==6:
                bank.on_loan_feature()
            elif ch==7:
                bank.off_loan_feature()
            elif ch==8:
                break
            else:
                print("Invalid Option")
        

    elif choise==2:
        while True:
            print("\n---------User Option---------\n")
            print("1.Create Account")
            print("2.Deposite Amount")
            print("3.Withdraw Amount")
            print("4.Check available balance")
            print("5.Check Transfer History")
            print("6.Take Loan")
            print("7.Transfer Money")
            print("8.Go to main pages")


            ch = int(input("\nEnter your Option = "))

            if ch==1:
                name = input("Name = ")
                email = input("Email = ")
                address = input("Address = ")
                type = input("Type = ")
                current_user = bank.create_account(name,email,address,address)
                
            elif ch==2:
                deposite_amount = int(input("Amount = "))
                current_user.deposite(deposite_amount)
                
            elif ch==3:
                withdraw_amount = int(input("Amount = "))
                current_user.withdraw(withdraw_amount)
                
            elif ch==4:
                current_user.check_balance()
            elif ch==5:
                current_user.transaction_history()
            elif ch==6:
                amount = int(input("Amount  = "))
                current_user.take_loan(amount)
            elif ch==7:
                print("\nEnter receiver info: \n")
                account_number = int(input("Account Number = "))
                name = input("Name = ")
                email = input("Email = ")
                address = input("Address = ")
                type = input("Type = ")
                receiver=Account(account_number,name,email,address,type)
                amount = int(input("Amount  = "))
                current_user.transfer(amount,receiver,bank)
            elif ch==8:
                break
            else:
                print("Invalid Option")
    elif choise==3:
        break
    else:
        print("Invalid Option!")
 

