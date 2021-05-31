class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance=0, interest_rate=0.015)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print("User:", self.name, ", Balance:", self.account)
        return self

    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount

# -----------------------------------------------------------------------


class BankAccount:
    def __init__(self, balance=0, interest_rate=0.015):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.interest_rate
            self.balance += interest
            return self


john_doe = BankAccount()
jane_smith = BankAccount(balance=50)

john_doe.deposit(100).deposit(100).deposit(
    100).withdraw(200).yield_interest().display_account_info()

jane_smith.deposit(1000).deposit(1000).withdraw(200).withdraw(
    200).withdraw(200).withdraw(200).yield_interest().display_account_info()
