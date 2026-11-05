# Informatica - 2026/2027 - Prova in Itinere di Programmaizone
# Prova 2 - Turno 2

# Esercizio 3: 

"""
Una lista di numeri reali contiene gli zeri di una funzione (cioè le ascisse x in cui
la funzione vale zero). I valori sono ordinati in ordine strettamente crescente.

Si scriva un programma per cui un utente inserisca un numero reale, ed il programma stampi
lo zero più vicino al numero dato (nel senso di distanza minima lungo l'asse x).

Esempio:

Zeri della funzione
[-3.40, -1.91, 1.36, 2.60, 11.35, 12.24, 13.68, 17.41]

Numero inserito:
3.00
Zero più vicino:
2.60

Numero inserito:
100.00
Zero più vicino:
17.41
"""

zeri = [-3.40, -1.91, 1.36, 2.60, 11.35, 12.24, 13.68, 17.41]

x = float(input("Numero: "))
