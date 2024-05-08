class Admin:
    def __init__(self):
        pass

    def create_account(self, bank, name, email, address, account_type):
        return bank.create_account(name, email, address, account_type)

    def delete_account(self, bank, account_number):
        bank.delete_account(account_number)

    def get_all_accounts(self, bank):
        bank.get_all_accounts()

    def get_total_balance(self, bank):
        bank.total_available_balance()

    def get_total_loan_amount(self, bank):
        bank.total_loan_amount()

