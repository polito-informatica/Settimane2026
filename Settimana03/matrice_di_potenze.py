# Stampiamo una tabella di potenze in cui 
# ogni riga i è la base e ogni colonna j è l'esponente, 
# quindi la cella (i, j) contiene i**j

# Arriviamo ai cicli annidati partendo da cicli singoli ripetuti

# Ciclo singolo: le potenze di 1 (base fissa, esponente che varia)
# range(1, 5) produce 1, 2, 3, 4: l'estremo destro è ESCLUSO
for i in range(1, 5):
    print(1**i, end=" ")   # end=" " stampa uno spazio invece di andare a capo
print()                    # print() vuoto: va a capo

# Stesso ciclo, cambia solo la base: le potenze di 2
for i in range(1, 5):
    print(2**i, end=" ")
print()

# Invece di copiare il ciclo per ogni base,
# facciamo variare ANCHE la base con un secondo ciclo: cicli annidati
n_righe = 5      # numero di basi (righe della tabella)
n_colonne = 5    # numero di esponenti (colonne della tabella)

for i in range(1, n_righe + 1):          # ciclo esterno: una riga per ogni base i
    for j in range(1, n_colonne + 1):    # ciclo interno: scorre tutti gli esponenti j
        print(i**j, end="\t")            # \t (tabulazione) allinea le colonne
    print()                              # fine riga: si va a capo PRIMA della base successiva