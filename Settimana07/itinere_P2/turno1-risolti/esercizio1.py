# Informatica - 2026/2027 - Prova in Itinere di Programmaizone
# Prova 2 - Turno 1

# Esercizio 1: 

"""
Sia data una lista di numeri interi positivi e negativi di lunghezza qualsiasi.

Si calcoli e si stampi una nuova lista nella quale compaiano per primi tutti i numeri negativi
(nello stesso ordine in cui comparivano nella lista di partenza), seguita da tutti i numeri positivi
(nello stesso ordine in cui comparivano nella lista di partenza). Eventuali valori pari a zero
vanno ignorati e non riportati nella lista finale.

Esempio:
- lista di partenza:
[3, -9, -8, -3, -9, -4, -1, -9, 10, -10, 8, 0, 3, 7, -7]

- lista risultante
[-9, -8, -3, -9, -4, -1, -9, -10, -7, 3, 10, 8, 3, 7]
"""

numeri = [3, -9, -8, -3, -9, -4, -1, -9, 10, -10, 8, 0, 3, 7, -7]


nuova = []

for v in numeri:
    if v<0:
        nuova.append(v)
        
for v in numeri:
    if v>0:
        nuova.append(v)

print(nuova)