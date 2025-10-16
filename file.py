# r - read -> errore se non esiste
# a - append -> errore se non esiste
# w - write -> errore se non esiste
# x - create -> errore se non esiste

f = open("testo.txt", "r")

print(f.read()) # lettura file

f.close()

print(f.readline())



