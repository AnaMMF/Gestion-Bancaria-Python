from models.bank_account import BankAccount

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: BankAccount) -> bool:
        # Busca si ya existe muestra mensaje de error y no lo añade
        if self.find_account(account.id):
            print("Account already registered.")
            return False
        
        self.accounts.append(account)
        return True

    def find_account(self, id: str) -> BankAccount:
        # Busca la cuenta por el DNI asociado y devuelve el objeto, si no lo encuentra devuelve None
        for acc in self.accounts:
            if acc.id == id:
                return acc
        return None