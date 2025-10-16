# - leggere JSON in python
# - da Python a JSON
# - dati convertibili in JSON
        # dict
        # list
        # tuple
        # string
        # int
        # float
        # True
        # False
        # None
# - Formattare il JSON
# - ordinare il JSON

import json

# x = '{"nome" : "Luca", "cognome": "Rossi", "eta": 25}'
x = {
        "nome" : "Luca",
          "monetine" : 12.56,
        "fidanzata": None,
        "cognome": "Rossi",
        "eta": 25,
}

y = json.dumps(x, indent=4, separators=(", ", ": "), sort_keys=True)
# y = json.loads(x)

print(y)
print(type(y))
# print(y["nome"])