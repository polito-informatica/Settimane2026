# Vogliamo contare quante volte ciascun nome compare
# e associare la conta di ciascun nome al nome stesso
nomi = ["Anna", "mario", "Marta", "Andrea", "Anna", "Mario", "Gino", "andrea"]

# TENTATIVO 1: un contatore per ogni nome
#   conta_anna = 0
#   if nome == "Anna":       # HARD CODED: funziona solo per "Anna"!
#       conta_anna += 1
# Problema: dovremmo sapere in anticipo quali nomi ci sono
# e creare una variabile per ciascuno -> impossibile in generale.

# TENTATIVO 2: un insieme
#   insieme_nomi = set()
#   insieme_nomi.add(nome)
# Ci dice QUALI nomi ci sono (senza duplicati),
# ma non QUANTE VOLTE compare ciascuno.

# SOLUZIONE: un dizionario (array associativo)
#   chiave  -> il nome
#   valore  -> quante volte l'abbiamo visto
# Le chiavi vengono create man mano che i nomi compaiono:
# non serve conoscerle in anticipo.
conte_nomi = dict()

for nome in nomi:
    nome = nome.lower()            # "Mario" e "mario" devono contare come lo stesso nome

    if nome in conte_nomi.keys():  # l'abbiamo già visto?
        conte_nomi[nome] = conte_nomi[nome] + 1   # sì: aumentiamo di 1
    else:
        conte_nomi[nome] = 1       # no: prima volta, creiamo la chiave con valore 1

print(conte_nomi)
# {'anna': 2, 'mario': 2, 'marta': 1, 'andrea': 2, 'gino': 1}