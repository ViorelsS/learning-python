# Exception


print("Ciao")
# x = 5
try:
    print(x)
    # print(x + "ciao")
except NameError:
    print("x non definita")
except:
    print("Non è nameError")
else:
    print("Tutto ok")
finally:
    print("In ogni caso vado qui")   