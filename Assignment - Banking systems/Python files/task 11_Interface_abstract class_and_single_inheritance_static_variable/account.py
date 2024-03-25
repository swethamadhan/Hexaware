class Account:
    last_acc_no = 0

    def __init__(self, customer, acc_type, balance):
        Account.last_acc_no += 1
        self.acc_no = Account.last_acc_no
        self.customer = customer
        self.acc_type = acc_type
        self.balance = balance