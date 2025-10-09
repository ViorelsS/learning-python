""" 04 Tipi di dati
   - ottenere il tipo di dato
   - come viene assegnato il tipo
   - tipi dati (str, int, float, bool, list, tuple, range, dict, set)"""

X = 5.5
print(type(X))

X = "ciao"
print(type(X))

X = False
print(type(X))

# collezione -> list (non è un array -> l'array è nella libreria numpy)
X= ["roma", "milano", "torino"]
print(type(X))
X.append("padova")
print(X)

X =range(7)
print(X)
print(type(X))
