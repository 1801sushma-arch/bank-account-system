#create:bank account class, deposit, withdraw, check balance, handle insufficient balance
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
        else:
            print("insufficient balance")

    def deposit (self,amount):
        self.balance+=amount

    def check_balance(self):
        return self.balance
    
n1=BankAccount("sushmitha",500)
#print(n1.name,n1.balance)
n1.deposit(300)
print("balance after depositing: ",n1.check_balance())
n1.withdraw(1000)
print("balance after withdrawing: ",n1.check_balance())
