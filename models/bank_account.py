
class BankAccount:

    def __init__ (self, client, balance, iban):
        self.client=client
        self.balance=balance
        self.iban=iban

    def __str__(self):
        return f"Titular: {self.client}, Cantidad: {self.balance}, iban: {self.iban}"