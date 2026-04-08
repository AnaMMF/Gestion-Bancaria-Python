
class person:

    def __init__ (self, name, lastname, id):
        self.name=name
        self.lastname=lastname
        self.id=id

    def __str__(self):
        return f"Nombre: {self.name}, Apellidos: {self.lastname}, DNI: {self.id}"