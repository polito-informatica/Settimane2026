# Informatica - 2026/2027 - Prova in Itinere di Programmaizone
# Prova 2 - Turno 2

# Esercizio 1: 

"""
Sia data una lista di numeri interi positivi e negativi di lunghezza qualsiasi.

Si divida la lista in due diverse liste: nella prima compaiano tutti i numeri negativi
(nello stesso ordine in cui comparivano nella lista di partenza), e nella seconda
tutti i numeri positivi (nello stesso ordine in cui comparivano nella lista di partenza).
Eventuali valori pari a zero vanno inseriti in entrambe le liste.

Esempio:
- lista di partenza:
[3, -9, -8, -3, -9, -4, -1, -9, 10, -10, 8, 0, 3, 7, -7]

- liste risultanti
[-9, -8, -3, -9, -4, -1, -9, -10, 0, -7]
[3, 10, 8, 0, 3, 7]
"""

numeri = [3, -9, -8, -3, -9, -4, -1, -9, 10, -10, 8, 0, 3, 7, -7]

negativi = []
positivi = []

for v in numeri:
    if v<0:
        negativi.append(v)
    elif v>0:
        positivi.append(v)
    else: # == 0
        negativi.append(v)
        positivi.append(v)

print(negativi)
print(positivi)