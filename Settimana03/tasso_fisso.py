# PROBLEMA: calcolare il saldo di un conto che parte da saldo_iniziale,
# con un tasso di interesse composto annuo del TASSO%.
# Ci fermiamo al primo anno in cui il saldo supera SOGLIA euro.
# Output: anno di stop, saldo finale, differenza tra saldo finale e iniziale.

# Costanti: per convenzione si scrivono in MAIUSCOLO
TASSO = 5          # tasso di interesse annuo in percentuale
SOGLIA = 20000     # obiettivo da superare

saldo_iniziale = 1000
saldo = saldo_iniziale   # variabile "accumulatore": cambia a ogni giro
anno = 0                 # variabile "contatore": conta i giri del ciclo

# while: ripetiamo finché la condizione è vera,
# NON sappiamo in anticipo quante volte (a differenza di un for)
while saldo < SOGLIA:
    anno += 1                        # passa un anno
    saldo += saldo * TASSO / 100     # interesse composto: si calcola sul saldo AGGIORNATO

# Usciti dal ciclo, saldo ha appena superato la soglia
differenza = saldo - saldo_iniziale

# str() converte i numeri in stringhe per poterli concatenare con +
# round(..., 2) arrotonda ai centesimi
print("Anno: " + str(anno) +
      "\nSaldo: " + str(round(saldo, 2)) +
      "\nDifferenza: " + str(round(differenza, 2)))