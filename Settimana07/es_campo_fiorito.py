from pprint import pprint
import random

# campo = [
#     [False, True, True, False],
#     [False, False, False, False],
#     [True, False, False, True],
#     [False, True, False, False],
# ]

# N = 4 

# M = 5

N = int(input("Lato del campo: "))
M = int(input("Numero di fiori: "))

# Creo un campo fatto solo di erba

campo = []
for riga in range(N):
    nuova = []
    for col in range(N):
        nuova.append(False)
    campo.append(nuova)

# pprint(campo)

# Posiziono M fiori nel campo

for fiore in range(M):
    riga_fiore = random.randint(0, N-1)
    col_fiore = random.randint(0, N-1) 

    while campo[riga_fiore][col_fiore]==True:
        riga_fiore = random.randint(0, N-1)
        col_fiore = random.randint(0, N-1) 

    campo[riga_fiore][col_fiore] = True

# pprint(campo)

# Stampa il campo

for riga in range(N):
    for col in range(N):
        if campo[riga][col]:
            print('🌸', end='')
        else:
            print('🟢', end='')
    print()

# Calcola gli adiacenti a ciascuna casella

vicini = [] 

for riga in range(N):
    nuova_riga = []
    for col in range(N):

        # calcolare fiori vicini (valori True) a campo[riga][col]
        n_vicini = 0 

        # visito tutte le celle vicine, ad ogni True incremento n_vicini
        for delta_riga in [-1, 0, 1]:
            for delta_col in [-1, 0, 1]:
                if ( 
                    (delta_riga!=0 or delta_col!=0) and
                    riga+delta_riga>=0 and
                    riga+delta_riga<N and
                    col+delta_col>=0 and
                    col+delta_col<N 
                ): 
                    if campo[riga+delta_riga][col+delta_col]==True:
                        n_vicini = n_vicini+1

        nuova_riga.append( n_vicini )
    vicini.append(nuova_riga)

pprint(vicini)