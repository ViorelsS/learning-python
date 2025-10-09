"""Stringhe:
    - Stringhe multiriga
    - Trattare le stringhe come array (prendere carattere, lenght, loop)
    - Prendere parte di stringa str[:5], str[2:], str[-5:-2]
    - Modificare stringa con upper(), lower(), strip(), split() e replace()
    - Concatenare stringhe
    - Usare format() per combinare stringhe e numeri
    - Escape dei caratteri
"""

VAR = "prova "
print(VAR)
print(VAR[0])
print(VAR[5]) # Anche lo spazio viene considerato carattere
print(len(VAR))

for carattere in VAR:
    print(carattere)

VAR = 'singoli-apici'
print(VAR)
print(VAR[0])

# Stringhe multi-linea
VAR = """
Stringa,
multi 
linea
"""
print(VAR)

print(VAR[0])

print(VAR[-5:-2],"\n\n")
print(VAR[1:12])


print("\nUPPER-------------------:\n",VAR.upper())
print("\nLOWER-------------------:\n",VAR.lower())
# Togliamo gli spazi bianchi davanti e dopo la stringa
print("\nSTRIP-------------------:\n",VAR.strip()) 

print("\nVAR+VAR-------------------:\n",VAR + VAR)

x = 43
eta = "Ciao sono Mario Rossi, ho {2} anni, peso {0}kg e sono alto {1}m."
print(eta.format(65, 1.70, 43))
