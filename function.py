"""Costruzione funzioni"""

def somma_due_numeri():
    num1 = input("inserisci primo numero: ")
    num2 = input("inserisci il secondo numero: ")
    
    print("\nRES:", int(num1)+int (num2))

somma_due_numeri()

def somma_numeri(*numeri):
    numeri_list = list(numeri)

    
    for num in numeri_list[1:]:
        numeri_list[0] += num
    
    print("SOMMA NUMERI", numeri_list[0])
        
somma_numeri(1,1,1,1,1,1)
