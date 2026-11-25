# Un dizionario associa CHIAVI a VALORI: chiave -> valore
# Si scrive tra graffe, con coppie chiave: valore separate da virgole
colori_preferiti = {
    "Romeo": "verde",
    "Adam": "viola",
    "Juliet": "blu",
    "Eve": "blu"        # i VALORI possono ripetersi ("blu" due volte),
}                       # le CHIAVI no: ogni chiave è unica

print(colori_preferiti)

# Quattro modi di creare contenitori vuoti
una_lista_vuota = []
un_dizionario_vuoto = {}             # attenzione: {} è un dizionario, NON un set!
un_altra_lista_vuota = list()
un_altro_dizionario_vuoto = dict()   # un set vuoto si crea solo con set()

# Assegnare a una chiave NUOVA la crea
un_dizionario_vuoto["Adam"] = "viola"
un_dizionario_vuoto["Eve"] = "viola"

# Assegnare a una chiave ESISTENTE sovrascrive il valore precedente
# (la sintassi è identica: dipende solo dal fatto che la chiave ci sia già)
un_dizionario_vuoto["Eve"] = "blu"
print(un_dizionario_vuoto["Eve"])    # blu

# Il valore può essere di qualsiasi tipo.
# Ogni assegnazione su "Adam" sovrascrive la precedente:
un_dizionario_vuoto["Adam"] = ["verde", "viola"]                        # una lista
un_dizionario_vuoto["Adam"] = {"verde", "viola"}                        # un set
un_dizionario_vuoto["Adam"] = {"Giovedì": "verde", "Venerdì": "viola"}  # un altro dizionario!
print(un_dizionario_vuoto)
# {'Adam': {'Giovedì': 'verde', 'Venerdì': 'viola'}, 'Eve': 'blu'}
# Ad "Adam" resta solo l'ultimo valore assegnato

# Anche le CHIAVI non devono per forza essere stringhe: qui un intero.
# Non è un indice di posizione, è solo un'etichetta che vale 0
un_dizionario_vuoto[0] = "bianco"

# Leggere: dizionario[chiave]
valore = un_dizionario_vuoto[0]
print(valore)       # bianco

# Chiavi numeriche che NON sono posizioni:
# numeri[0] non è "il primo elemento", è "il valore con chiave 0"
numeri = {
    3: "primo",
    2: "secondo",
    1: "terzo"
}

# Leggere una chiave che non esiste dà KeyError,
# quindi prima controlliamo con "in"
if 0 in numeri.keys():        # basterebbe anche: if 0 in numeri
    print(numeri[0])
else:
    print("chiave non presente")

# Alternativa compatta: get(chiave, valore_di_default)
# restituisce il valore se la chiave c'è, altrimenti il default (senza errori)
print(numeri.get(0, "chiave mancante"))

print()

# Scorrere una LISTA: enumerate dà coppie (indice, valore)
# l'indice è la POSIZIONE: 0, 1, 2, ...
lista_nomi = ["Anna", "Mario", "Marta", "Andrea"]
for indice, valore in enumerate(lista_nomi):
    print(indice, valore)

# Scorrere un DIZIONARIO: items() dà coppie (chiave, valore)
# la chiave è un'ETICHETTA, non una posizione
for chiave, valore in numeri.items():
    print(chiave, valore)