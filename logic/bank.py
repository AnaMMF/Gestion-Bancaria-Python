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

    def list_accounts(self):
        # Imprime la lista de cuentas registradas usando el método __str__ de la clase BankAccount
        return [str(acc) for acc in self.accounts]

    def deposit(self, id: str, amount: float) -> bool:
        # Busca la cuenta por el DNI asociado y si la encuentra añade el importe al saldo, devuelve True si se ha realizado el ingreso o False si no se ha encontrado la cuenta
        #TODO: Devolver un mensaje de error si el importe es negativo o cero y si la cuenta no se ha encontrado
        if amount <= 0:
            print("Invalid deposit amount. Please enter a positive value.")
            return False

        account = self.find_account(id)
        if account:
            account.amount += amount
            return True
        return False

    def withdraw(self, id: str, amount: float) -> bool:
        # Busca la cuenta por el DNI asociado y si la encuentra resta el importe al saldo, devuelve True si se ha realizado el retiro o False si no se ha encontrado la cuenta o si el saldo es insuficiente
        #TODO: Devolver un mensaje de error si no se encuentramla cuenta

        account = self.find_account(id)
        if account:
            if account.amount - amount >= 0:
                account.amount -= amount
                return True
            else:
                print("Withdrawal failed. Insufficient balance.")
        return False