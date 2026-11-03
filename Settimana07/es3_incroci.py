# Esercizio sulle tabelle: incroci settimanali

"""
Sia data una tabella contenente 7 colonne (corrispondenti ai giorni della settimana) e un numero variabile di righe
(corrispondenti a diversi amici). In ciascuna casella, compare una stringa che rappresenta il luogo in cui si trova
ciascuno degli amici in quella giornata.

Determinare in quali giorni della settimana tutti gli amici sono nello stesso luogo.
"""

luoghi = [
    ['Torino', 'Torino', 'Aosta', 'Aosta', 'Milano', 'Milano', 'Torino'],
    ['Milano', 'Torino', 'Milano', 'Aosta', 'Torino', 'Torino', 'Torino'],
    ['Milano', 'Torino', 'Aosta', 'Aosta', 'Genova', 'Genova', 'Torino'],
]

"""
Risultato atteso:
Nello stesso luogo: giorno 1
Nello stesso luogo: giorno 3
Nello stesso luogo: giorno 6
"""
