# Informatica - 2026/2027 - Prova in Itinere di Programmaizone
# Prova 2 - Turno 1

# Esercizio 2: 

"""
Sia data una tabella contenente 7 colonne (corrispondenti ai giorni della settimana) e un numero variabile di righe
(corrispondenti a diversi lavoratori). In ciascuna casella, compare una stringa (di 1 o 2 caratteri) che rappresenta 
il ruolo del lavoratore nel giorno specificato.

Calcolare e stampare una lista di 7 stringhe, in cui ciascun elemento sia una stringa ottenuta concatenendo i 
ruoli dei diversi lavoratori nel giorno corrispondente.

Esempio:

Data la tabella
ruoli = [
    ['AB', 'K', 'K', 'K', 'AB', 'ZZ', 'ZZ'],
    ['K', 'AB', 'AB', 'ZZ', 'Y', 'AB', 'AB'],
    ['Y', 'ZZ', 'Y', 'AB', 'AB', 'K', 'K'],
]
si dovrà stampare il risultato pari a:
['ABKY', 'KABZZ', 'KABY', 'KZZAB', 'ABYAB', 'ZZABK', 'ZZABK']
"""

ruoli = [
    ['AB', 'K', 'K', 'K', 'AB', 'ZZ', 'ZZ'],
    ['K', 'AB', 'AB', 'ZZ', 'Y', 'AB', 'AB'],
    ['Y', 'ZZ', 'Y', 'AB', 'AB', 'K', 'K'],
]

risultato = []

for giorno in range(7):
    stringa = ""
    for riga in range(len(ruoli)):
        stringa = stringa + ruoli[riga][giorno]
    risultato.append(stringa)

print(risultato)