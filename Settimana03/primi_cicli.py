# ============================================================
# CICLI: WHILE E FOR
# ============================================================

# --- Perché servono i cicli ---

# Stampa i numeri da 0 a 3: senza ciclo dobbiamo scrivere ogni istruzione
print(0)
print(1)
print(2)
print(3)

# Stampa i numeri da 0 a N: con un ciclo basta cambiare N
N = 100
n = 0                  # inizializzazione
while n <= N:          # condizione
    print(n)
    n += 1             # aggiornamento: senza questo il ciclo non finisce mai

print()
print()


# --- Quante volte viene eseguito il ciclo? ---

# Condizione falsa fin dall'inizio (100 < 10): il corpo non viene MAI eseguito
i = 0
totale = 100
while totale < 10:
    i += 1
    totale += 1
    print(i, totale)

# Anche qui zero esecuzioni: 0 < 0 è falso (disuguaglianza stretta)
i = 0
totale = 0
while totale < 0:
    i += 1
    totale += 1
    print(i, totale)

# Incremento di 2: il ciclo gira 5 volte e totale arriva esattamente a 10
i = 0
totale = 0
while totale < 10:
    i += 1
    totale += 2
    print(i, totale)

# Il valore iniziale conta: partendo da 10, 10 < 10 è falso, zero esecuzioni
i = 5
totale = 10
while totale < 10:
    i += 1
    totale += 2
    print(i, totale)

# Condizione con ==: 0 == 10 è falso, il ciclo non parte
i = 0
totale = 0
while totale == 10:
    i += 1
    totale += 1
    print(i, totale)

# ATTENZIONE: CICLO INFINITO (disattivato)
# totale diminuisce, quindi resta sempre < 10 e il ciclo non termina mai
"""
i = 0
totale = 0
while totale < 10:
    i += 1
    totale -= 1
    print(i, totale)
"""


# --- Scorrere una stringa lettera per lettera ---

nome = "Virginia"

# Con while: usiamo un indice i e accediamo alla lettera con nome[i]
# len(nome) è la lunghezza, gli indici vanno da 0 a len(nome) - 1
i = 0
while i < len(nome):
    lettera = nome[i]
    print(lettera)
    i += 1

print()

# Con for: Python scorre la stringa da solo, niente indice da gestire
for lettera in nome:
    print(lettera)

# range(3, 5) produce 3 e 4: l'estremo destro è ESCLUSO
for i in range(3, 5):
    print(i)

# enumerate: ci dà insieme l'indice e la lettera
for i, lettera in enumerate(nome):
    print(i, lettera)