"""Tupple e varie operazioni"""

citta = ("milano", "roma", "napoli", "venezia")

(x,y,*z) = citta

print(x) # milano
print(y) # roma
print(z) # ['napoli', 'venezia']


# Modificare una tupla -> escamotage
x = list(citta)
x[1] = "torino"
citta = tuple(x)
print(citta)
