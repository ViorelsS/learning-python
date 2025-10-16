# List comprehension

lista_citta = ["udine", "roma", "bari","napoli", "venezia"]

y = [print(citta) for citta in lista_citta if citta!="roma"]

x = ["Milano" for citta in lista_citta if citta!="roma"]
print(x)


lista_citta.sort() # Ordinare alfabeticamente la lsita
print("Lista ordinata", lista_citta)
lista_citta.sort(reverse=True)
print("Lista ordinata inversa", lista_citta)

y = list(lista_citta)
print(y)

for citta in y:
    x.append(citta)
    
print(x)

lista_citta.append(x)
print(lista_citta)

