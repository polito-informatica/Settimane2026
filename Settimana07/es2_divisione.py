"""
È data una lista di nomi di persone, ciascuno rappresentato da una stringa con nome e cognome separati da uno spazio.
Si assuma che non vi siano nomi doppi o cognomi doppi.

Costruire e stampare due liste di stringhe, in cui la prima contenga
i nomi propri delle persone, e la seconda contenga i cognomi delle stesse
persone, in ordine corrispondente

Esempio:

Lista di nomi iniziale:
supereroi = [
    "Peter Parker",
    "Clark Kent",
    "Bruce Wayne",
    "Tony Stark",
    "Steve Rogers",
    "Diana Prince",
    "Barry Allen",
    "Arthur Curry"
]

Risultato:
Lista nomi:
['Peter', 'Clark', 'Bruce', 'Tony', 'Steve', 'Diana', 'Barry', 'Arthur']
Lista cognomi:
['Parker', 'Kent', 'Wayne', 'Stark', 'Rogers', 'Prince', 'Allen', 'Curry']
"""

supereroi = [
    "Peter Parker",
    "Clark Kent",
    "Bruce Wayne",
    "Tony Stark",
    "Steve Rogers",
    "Diana Prince",
    "Barry Allen",
    "Arthur Curry"
]

nomi=[]
cognomi=[]

for sup in supereroi:
    # pos_spazio = sup.find(" ")
    # nomi.append( sup[:pos_spazio] )
    # cognomi.append( sup[pos_spazio+1:])
    separati = sup.split(' ')  # separati = [ 'Peter', 'Parker' ]
    nomi.append(separati[0])
    cognomi.append(separati[1])

print(nomi)
print(cognomi)