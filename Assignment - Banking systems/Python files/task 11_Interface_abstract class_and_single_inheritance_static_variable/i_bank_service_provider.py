from abc import ABC, abstractmethod
from i_customer_service_provider import ICustomerServiceProvider

class IBankServiceProvider(ICustomerServiceProvider):
    @abstractmethod
    def create_account(self, customer, acc_no, acc_type, balance):
        pass

    @abstractmethod
    def list_accounts(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass