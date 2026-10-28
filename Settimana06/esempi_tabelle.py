# --- UNA TABELLA È UNA LISTA DI LISTE ---

lista_medaglie = [1, "Oro", "Argento", "Bronzo"]   # lista semplice (tipi misti: da evitare!)

# ogni riga è una lista: una per paese
tabella_medaglie_italia = [0, 3, 0]   # oro, argento, bronzo
tabella_medaglie_canada = [3, 0, 1]

# la tabella mette le righe una sotto l'altra (8 paesi x 3 medaglie)
tabella_medaglie = [
    [ 0, 3, 0 ],
    [ 0, 0, 1 ],
    [ 0, 0, 1 ],
    [ 1, 0, 0 ],
    [ 0, 0, 1 ],
    [ 3, 1, 1 ],
    [ 0, 1, 0 ],
    [ 1, 0, 1 ]
    ]

#print(lista_medaglie[0][0])   # ERRORE: lista_medaglie[0] è l'intero 1, non una lista

print(tabella_medaglie[0][0])   # due indici: prima la riga, poi la colonna


# --- CREAZIONE INCREMENTALE DI UNA TABELLA ---
NUMERO_RIGHE = 5
NUMERO_COLONNE = 5
tabella_zeri = []

for riga in range(NUMERO_RIGHE):
    tabella_zeri.append([0]*NUMERO_COLONNE)   # una NUOVA lista per ogni riga

for riga in tabella_zeri:   # stampa riga per riga
    print(riga)


# --- SOMMA PER RIGA (riga i fissa, scorro le colonne j) ---
totale_riga = 0
i = 2
for j in range(len(tabella_medaglie[0])):   # len(tabella[0]) = numero di colonne
    totale_riga = totale_riga + tabella_medaglie[i][j]
print("Totale riga", i, ":", totale_riga)

# --- SOMMA PER COLONNA (colonna j fissa, scorro le righe i) ---
totale_colonna = 0
j = 1
for i in range(len(tabella_medaglie)):      # len(tabella) = numero di righe
    totale_colonna = totale_colonna + tabella_medaglie[i][j]
print("Totale colonna", j, ":", totale_colonna)


# --- ORDINAMENTO E ALIAS ---
lista_paesi = ["Canada", "Marocco", "Serbia", "Italia", "USA"]

print("Prima del sorting")
print(lista_paesi)
print("Dopo il sorting")
lista_ordinata = lista_paesi        # ALIAS: due nomi per la STESSA lista
lista_ordinata.sort()               # sort() modifica la lista sul posto...
#lista_ordinata = sorted(lista_paesi)   # ...sorted() invece crea una lista nuova
print(lista_paesi)                  # ...quindi anche lista_paesi risulta ordinata!
print(lista_ordinata)


# --- ORDINAMENTO DI UNA TABELLA ---
for riga in tabella_medaglie:
    print(riga)

tabella_medaglie.sort()             # ordina le RIGHE intere, confrontandole come liste
print()                             # (elemento per elemento: prima gli ori, poi gli argenti...)

for riga in tabella_medaglie:
    print(riga)


# --- COPIA SUPERFICIALE (SHALLOW) ---
nuova_tabella = list(tabella_zeri)  # nuova lista esterna, ma le RIGHE sono condivise

# CASO 1: sostituisco una riga intera
# nuova_tabella[2] ora punta a una lista NUOVA -> l'originale NON cambia
nuova_tabella[2] = [3, 3, 3, 3, 3]

# CASO 2: modifico un elemento DENTRO una riga
# nuova_tabella[0] e tabella_zeri[0] sono la STESSA lista -> cambia anche l'originale!
nuova_tabella[0][0] = 9

for riga in tabella_zeri:
    print(riga)                     # riga 0 inizia con 9 (caso 2), riga 2 è ancora di zeri (caso 1)