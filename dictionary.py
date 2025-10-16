"""Dictionary -> collezioni di dati ordinate, modificabili ma non permette duplicati"""

# I dict sono coppie di chiave-valore
x = {
    "nome": "Luca",
    "cognome":"Rossi",
    "eta":25
}

x["nome"] = "mario"
x["colore"] = "rosso"

print(x.get("nome"))
print(x.keys())
print(x.values())
print(x.items())

x.pop("nome")
print(x.items())


x.popitem()
print(x.items())

print(x.items())

print("\n\n\n")
for prop in x.values():
    print(prop)
   