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

# n righe = len(luoghi)
# n colone = len(luoghi[0])

GIORNI=["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]

for giorno in range(len(luoghi[0])):
    # if giorno sono tutti nello stesso luogo:
    # if luoghi[0][giorno]==luoghi[1][giorno] and luoghi[0][giorno]==luoghi[2][giorno] and ... :
    # if tutti gli amici a>=1 hanno la proprietà che luoghi[a][giorno]==luoghi[0][giorno]:

    tutti_qui = True

    for a in range(1, len(luoghi)):
        if luoghi[a][giorno] != luoghi[0][giorno]:
            tutti_qui = False

    if tutti_qui:
        print("Nello stesso luogo: giorno", GIORNI[giorno])
