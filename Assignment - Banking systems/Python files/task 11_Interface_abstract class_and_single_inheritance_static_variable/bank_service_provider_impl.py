from i_bank_service_provider import IBankServiceProvider
from customer_service_provider_impl import CustomerServiceProviderImpl
from account import Account
from savings_account import SavingsAccount
from current_account import CurrentAccount
from zero_balance_account import ZeroBalanceAccount

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self):
        super().__init__()
        self.account_list = []
        self.branch_name = ""
        self.branch_address = ""

    def create_account(self, customer, acc_type, balance):
        if acc_type == "Savings":
            account = SavingsAccount(customer, balance)
        elif acc_type == "Current":
            account = CurrentAccount(customer, balance, overdraft_limit=1000) # default overdraft limit set to 1000
        else:
            account = ZeroBalanceAccount(customer)

        self.accounts[account.acc_no] = account
        return account.acc_no

    def list_accounts(self):
        return self.accounts.values()

    def calculate_interest(self):
        for acc in self.accounts.values():
            if isinstance(acc, SavingsAccount):
                # Calculate and update interest
                pass