# --- CREAZIONE DELLA GRIGLIA ---
N_RIGHE = 10
N_COLONNE = 10

griglia = []

for riga in range(N_RIGHE):
    griglia.append([0]*N_COLONNE)      # ogni riga è una NUOVA lista (no [[0]*C]*R!)


# --- SITUAZIONE DI PARTENZA ---
# scegli il pattern: "due_file", "lampeggiatore", "rospo", "aliante"
pattern = "aliante"

if pattern == "due_file":              # due file da 4: diventano due blocchi fermi
    for i in range(4,8):
        griglia[3][i]=1
        griglia[5][i]=1

elif pattern == "lampeggiatore":       # oscillatore di periodo 2
    griglia[4][3]=1
    griglia[4][4]=1
    griglia[4][5]=1

elif pattern == "rospo":               # oscillatore di periodo 2
    griglia[4][4]=1
    griglia[4][5]=1
    griglia[4][6]=1
    griglia[5][3]=1
    griglia[5][4]=1
    griglia[5][5]=1

elif pattern == "aliante":             # si sposta in diagonale verso il basso a destra
    griglia[1][2]=1
    griglia[2][3]=1
    griglia[3][1]=1
    griglia[3][2]=1
    griglia[3][3]=1

# stampa della situazione di partenza
for riga in range(N_RIGHE):
    for colonna in range(N_COLONNE):
        print(griglia[riga][colonna], end=" ")
    print()                            # a capo a fine riga

comando = input()                      # Invio = generazione successiva, altro = esci


# --- EVOLUZIONE ---
while comando == "":

    # nuova griglia vuota: si LEGGE da griglia, si SCRIVE in nuova_griglia
    nuova_griglia = []
    for riga in range(N_RIGHE):
        nuova_griglia.append([0]*N_COLONNE)

    # per ogni cella della griglia...
    for i_riga in range(N_RIGHE):
        for j_colonna in range(N_COLONNE):

            # ...conto i vicini vivi nel quadrato 3x3 attorno alla cella
            conta_vivi = 0
            for delta_i in range(-1,2): # -1, 0, 1
                for delta_j in range(-1,2):
                    # controllo di non uscire dalla griglia, su TUTTI e 4 i bordi
                    # (senza >= 0, l'indice -1 leggerebbe l'ultima riga/colonna!)
                    if i_riga+delta_i >= 0 and i_riga+delta_i < N_RIGHE and j_colonna+delta_j >= 0 and j_colonna+delta_j < N_COLONNE:
                        #print(griglia[i_elemento+delta_i][j_elemento+delta_j])
                        if griglia[i_riga+delta_i][j_colonna+delta_j] == 1:
                            if not (delta_i == 0 and delta_j == 0):   # escludo la cella stessa
                                conta_vivi+=1
            #print(conta_vivi)

            # ...e applico le regole
            if griglia[i_riga][j_colonna] == 1:
                #  SE è VIVO E HA 2 O 3 VICINI ALLORA RESTA VIVO
                if conta_vivi == 2 or conta_vivi == 3:
                    nuova_griglia[i_riga][j_colonna]=1
                else:
                    # ALTRIMENTI SI SPEGNE
                    nuova_griglia[i_riga][j_colonna]=0
            elif griglia[i_riga][j_colonna] == 0:
                # SE è SPENTO E HA ESATTAMENTE 3 VICINI ALLORA PRENDE VITA
                if conta_vivi == 3:
                    nuova_griglia[i_riga][j_colonna]=1
                # ALTRIMENTI RESTA SPENTO
                else:
                    nuova_griglia[i_riga][j_colonna]=0

    # solo ora, con la nuova griglia completa, passo alla generazione successiva
    griglia=nuova_griglia

    # stampa della nuova generazione
    for riga in range(N_RIGHE):
        for colonna in range(N_COLONNE):
            print(nuova_griglia[riga][colonna], end=" ")
        print()                        # a capo a fine riga

    comando = input()