class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User:", self.name, ", Balance:", self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


john_doe = User("John Doe", "johndoe1@gmail.com")
jane_smith = User("Jane Smith", "jsmith@yahoo.com")
bob_smith = User("Bob Smith", "bobbybsmith@gmail.com")

john_doe.make_deposit(100).make_deposit(500).make_deposit(
    50).make_withdrawal(50).display_user_balance()

jane_smith.make_deposit(200).make_deposit(
    200).make_withdrawal(300).display_user_balance()

bob_smith.make_deposit(1000).make_withdrawal(
    400).make_withdrawal(100).display_user_balance()

john_doe.transfer_money(bob_smith, 200)
john_doe.display_user_balance()
bob_smith.display_user_balance()
