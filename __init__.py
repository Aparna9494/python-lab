class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def Deposit(self, deposit):
        print("Current balance:", self.balance)
        if deposit > 0:
            self.balance += deposit
            print("Deposited: $" + str(deposit) + " | New balance: $" + str(self.balance))
        else:
            print("Deposit amount must be positive.")

    def Withdraw(self, withdraw):
        if withdraw > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= withdraw
            print("Withdrew: $" + str(withdraw) + " | New balance: $" + str(self.balance))

    def get_balance(self):
        return self.balance

    def accountinfo(self):
        print("Account Number: " + str(self.account_number))
        print("Account Holder: " + self.name)
        print("Account Type: " + self.account_type)
        print("Balance: $" + str(self.balance))



account1 = BankAccount(785492, "Fida", "Savings", 40)


account1.accountinfo()


account1.Deposit(345555555)


account1.Withdraw(2)


print("Current balance: $" + str(account1.get_balance()))
