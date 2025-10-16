"""Set --> collezione non ordinata"""

x = {"milano", "roma", "napoli"}
y = {"torino", 5, "2412421"}

print(x)
print(y)

for citta in x:
    print("Milano corrisponde all'elemento corrente? ","milano" in citta)
        
x.add("udine")

print("Lista completa città:")
for citta in x:
    print("\t", citta)
  
# set.union() e set.update() eliminano i duplicati
# set.insersection -> ci da solo il valore in comune
# set.symmetric_intersection -> ci da solo i valori non in comune

