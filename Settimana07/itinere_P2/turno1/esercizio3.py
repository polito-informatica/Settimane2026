# Informatica - 2026/2027 - Prova in Itinere di Programmaizone
# Prova 2 - Turno 1

# Esercizio 3: 

"""
Una lista di numeri reali contiene gli zeri di una funzione (cioè le ascisse x in cui
la funzione vale zero). I valori sono ordinati in ordine strettamente crescente.

Si scriva un programma per cui un utente inserisca un numero reale, ed il programma stampi
i due zeri adiacenti (uno a sinistra ed uno a destra) al numero dato. Si considerino anche i 
casi particolari in cui vi sia un solo adiacente.

Esempio:

Zeri della funzione
[-3.40, -1.91, 1.36, 2.60, 11.35, 12.24, 13.68, 17.41]

Numero inserito:
3.00
Zeri adiacenti:
2.60 e 11.35

Numero inserito:
100.00
Zeri adiacenti:
17.41
"""

zeri = [-3.40, -1.91, 1.36, 2.60, 11.35, 12.24, 13.68, 17.41]

x = float(input("Numero: "))
