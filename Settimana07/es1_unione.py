"""
Sono date due liste di stringhe: la prima contiene i nomi di persone,
mentre la seconda contiene, in posizione corrispondente, il cognome delle
stesse persone.

Si calcoli e si stampi una terza lista di stringhe, che contenga
il nome completo delle persone, rappresentando il nome ed il cognome
separati da uno spazio.

Esempio:

Lista dei nomi:
['Peter', 'Clark', 'Bruce', 'Tony', 'Steve', 'Diana', 'Barry', 'Arthur']

Lista dei cognomi:
['Parker', 'Kent', 'Wayne', 'Stark', 'Rogers', 'Prince', 'Allen', 'Curry']

Risultato:
['Peter Parker', 'Clark Kent', 'Bruce Wayne', 'Tony Stark', 'Steve Rogers', 'Diana Prince', 'Barry Allen', 'Arthur Curry']

"""

nomi = ['Peter', 'Clark', 'Bruce', 'Tony', 'Steve', 'Diana', 'Barry', 'Arthur']
cognomi = ['Parker', 'Kent', 'Wayne', 'Stark', 'Rogers', 'Prince', 'Allen', 'Curry']

nuova = []
for i in range(len(nomi)):
    completo = nomi[i] + " " + cognomi[i]
    nuova.append(completo)

print(nuova)
