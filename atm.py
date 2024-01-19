class Atm(object):
    """ 
     blueprint of Atm
    """
    def __init__(self, money , debitcard , bankName  ):
        self.money = money
        self.debitcard = debitcard
        self.bankName = bankName

    def withdraw(self):
        print("withdrawed Money Form Your Accont")

    def deposit(self):
        print("deposited money to your bank account")

bibek=Atm("fifty thousand","one card","State Bank Of India")
print (bibek.withdraw())
print (bibek.deposit)






    
    
        