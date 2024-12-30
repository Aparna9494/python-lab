class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def Deposit(self,deposit):
            self.balance+=deposit
            print("deposit:",str(deposit),"balance:",str(self.balance))
    def Withdraw(self,withdraw):
        if(withdraw>self.balance):
            print("insufficient balance" )
        else:
            self.balance=self.balance-withdraw
            print("withdrawal amount:",str(withdraw),"balance:",str(self.balance))
    def get_balance(self):
        return self.balance
    def account_info(self):
        print("Account Number: " , str(self.account_number))
        print("Account Holder: " ,self.name)
        print("Account Type: " , self.account_type)
        print("Balance: " , str(self.balance))
account1=BankAccount(785492,"fida","savings",40)
account1.account_info()
account1.Deposit(345555555)
account1.Withdraw(2)
print("Current balance: " + str(account1.get_balance()))



