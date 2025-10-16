"""test classe"""
class Persona:
    """Classe blueprint persona"""
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    def saluta(self):
        """Print a schermo del nome"""
        print("Ciao sono", self.nome)
    
    
persona1 = Persona("Luca", "Rossi")
persona2 = Persona("Mario", "Verdi")

print(persona1.nome)
print(persona2.nome)
persona1.saluta()

persona2.nome = "Maria"
persona2.saluta()

del persona2.nome
print(persona2.cognome)
