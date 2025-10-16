# - cos'è un modulo: file contenente funzioni/variabili che vogliamo includere nel programma attuale
# - creare un modulo
# - funzioni e variabili in un modulo
# - creare un alias
# - moduli built in (platform, math)
# - funzione dir()
# - importare solo una parte del modulo

import math
import platform
import miomodulo as em
# from miomodulo import persona1

x = em.persona1["nome"]
y = platform.system
z = math.floor(2.90)

print(z)

print(y)
print(dir(math))

em.saluta(x)
