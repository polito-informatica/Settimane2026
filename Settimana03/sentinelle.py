# Una sentinella è un valore speciale che l'utente inserisce
# per dire "ho finito". Non sappiamo in anticipo quanti dati
# arriveranno, quindi usiamo un while controllato da quel valore.

"""
# Due modi di controllare un while (codice disattivato)

totale = 1000    # ATTENZIONE: con totale = 0 il ciclo sotto è infinito,
                 # perché 0 * 5/100 = 0 e totale non cresce mai
contatore = 0

# Ciclo controllato da una CONDIZIONE sul valore
while totale < 2000:
    totale += totale * 5 / 100
    contatore += 1

# Ciclo controllato da un CONTATORE (numero di ripetizioni fisso)
contatore = 0
while contatore < 10:
    totale += totale * 5 / 100
    contatore += 1
"""


# ESEMPIO 1: la sentinella è la stringa vuota (l'utente preme solo Invio)
# più un limite massimo di 5 inserimenti: il ciclo si ferma
# alla PRIMA delle due condizioni che diventa falsa (ciclo misto)
contatore = 0
numero = input("Inserisci un numero: ")   # lettura PRIMA del ciclo
while numero != "" and contatore < 5:
    print(numero)
    contatore += 1
    numero = input("Inserisci un numero: ")   # nuova lettura ALLA FINE del corpo


# ESEMPIO 2: la sentinella è un numero negativo
# sommiamo i numeri finché l'utente non ne inserisce uno negativo
# (il negativo NON viene sommato: serve solo a fermare il ciclo)
totale = 0
contatore = 0
numero = float(input("Dammi un numero: "))   # lettura iniziale
while numero >= 0:
    contatore += 1
    totale += numero
    numero = float(input("Dammi un numero: "))   # lettura successiva

print("Hai inserito", contatore, "numeri, totale:", totale)


# ESEMPIO 3: stesso problema, ma con una variabile FLAG (booleana)
# la condizione del while non controlla il numero direttamente,
# ma una variabile che dice se abbiamo finito
totale = 0
contatore = 0
finito = False                         # all'inizio non abbiamo finito

numero = float(input("Dammi un numero: "))
if numero < 0:                         # se il primo numero è già la sentinella
    finito = True                      # non entriamo proprio nel ciclo

while not finito:                      # "finché NON abbiamo finito"
    contatore += 1
    totale += numero
    numero = float(input("Dammi un numero: "))
    if numero < 0:
        finito = True                  # alziamo la bandiera: il ciclo si ferma

print("Hai inserito", contatore, "numeri, totale:", totale)