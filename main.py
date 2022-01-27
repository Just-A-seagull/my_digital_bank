import datetime

class Account:
    auto_account_number = 1234567890
    
    def __init__(self, currency: str, initial_balance: float = 0):
        self.account_number = Account.auto_account_number
        Account.auto_account_number += 1
        self.currency = currency
        self.initial_balance = initial_balance
        self.timestamp = datetime.datetime.now()

class Client: 
    def __init__(self, name: str):
        self.name = name
        self.timestamp = datetime.datetime.now()
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)
    
    def print_accounts(self):
        print(f"printing accounts of client {self.name}")
        for acc in self.accounts:
            print(f"{acc.account_number} ({acc.currency} {acc.initial_balance})")

class transactions:
    def __init__(self, value: float = 0, note: str = ""):
        self.value = value
        self.note = note
        self.timestamp = datetime.datetime.now()
        
    def print_transaction():
        pass
    
    def add_money():
        pass


clients = []
clients.append(Client('Anna'))
clients.append(Client('Jenifer'))
clients.append(Client('Miki'))

clients[0].add_account(Account('EUR', 200))
clients[0].add_account(Account('USD', 150))
clients[0].add_account(Account('CAD', 300))

clients[1].add_account(Account('CAD', 300))
clients[1].add_account(Account('USD', 500))

clients[2].add_account(Account('CAD', 400))

clients[0].print_accounts()
