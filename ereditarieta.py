"""Ereditarietà"""
class Persona:
    """Classe blueprint persona"""
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    def saluta(self):
        """Print a schermo del nome"""
        print("Ciao sono", self.nome)
        
        
class Insegnante(Persona):
    """Insegnante che estende persona"""
    def __init__(self, nome, cognome, materia="italiano"):
        super().__init__(nome, cognome)
        self.materia = materia
    def spiega_materia(self):
        """Print a schermo della materia insegnata"""
        print("Io insegno", self.materia)
    # Override
    def saluta(self):
        print("Buongiorno, sono", self.nome, self.cognome)
    def dai_voto(self):
        print("Bravo, un bel 8")

persona1 = Persona("Luca", "Rossi")
insegnante1 = Insegnante("Anna", "Neri")


insegnante1.saluta()

insegnante1.spiega_materia()
insegnante1.dai_voto()
