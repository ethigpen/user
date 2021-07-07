
class User:
#     class attributes get defined in the class 
    bank_name = "First National Dojo"
#     now our method has 2 parameters!
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0

    def make_deposit(self, amount):	
        # takes an argument that is the amount of the deposit
        self.account_balance += amount	
        # the specific user's account increases by the amount of the value 

    # have this method decrease the user's balance by the amount specified
    def make_withdrawal(self,amount):
        # needs argument that is amount of withdrawal
        self.account_balance -= amount

    # have this method print the user's name and account balance to the terminal
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: ${self.account_balance}')

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

emile = User("Emile Thigpen", "et@python.com")
monty = User("Monty Python", "mp@python.com")
belle = User("Belle Moose-Goose", "bm@python.com")

emile.make_deposit(500)
emile.make_deposit(200)
emile.make_deposit(75)
emile.make_withdrawal(150)     
emile.display_user_balance()    #output:625
monty.make_deposit(200)
monty.make_deposit(200)
monty.make_withdrawal(50)
monty.make_withdrawal(50)
monty.display_user_balance()    #output: 300
belle.make_deposit(20)
belle.make_withdrawal(5)
belle.make_withdrawal(7)
belle.make_withdrawal(3)    
belle.display_user_balance()    #output: 5
emile.transfer_money(belle,50)
emile.display_user_balance()    #575
belle.display_user_balance()    #55