class InsufficientFundsException(Exception):
    def __init__(self, account_number, balance, withdrawal_amount):
        self.account_number = account_number
        self.balance = balance
        self.withdrawal_amount = withdrawal_amount
        super().__init__(
            f"Insufficient funds in account {account_number}. Balance: {balance}. Attempted withdrawal: {withdrawal_amount}.")


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException(self.account_number, self.balance,
                                             amount)
        self.balance -= amount


try:
    account = BankAccount('123456789', 1000)
    account.withdraw(1500)
except InsufficientFundsException as ex:
    print("Error:", str(ex))
