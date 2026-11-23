"""
Dato un file di testo contenente un romanzo,
identificare le 'parole uniche' presenti nel testo
e calcolare quante parole uniche diverse compaiono.

Nel definire le parole uniche, si devono ignorare
le differenze tra maiuscole e minuscole, e tutti
i segni di punteggiatura.
"""

"""
In seguito, leggere le parole presenti in un dizionario
italiano, e determinare quali parole del romanzo
siano errate (nel senso che non compaiono nel risultato).
"""

import string

def estrai_parole(riga):
    """
    Riceve un stringa che rappresenta un'intera riga del file
    e restituisce una lista di stringhe che corrispondono
    alle singole parole presenti (ripulite da
    maiuscole e punteggiatura)
    """
    riga = riga.lower()

    for ch in string.punctuation+'’':
        riga = riga.replace(ch, " ")
    
    parole = riga.split()

    # elimina punteggiatura in testa e in coda alla parola
    # for i in range(len(parole)):
    #     parole[i] = parole[i].strip(string.punctuation)

    return parole

def leggi_file(nome_file):
    """
    Legge un file di testo e restituisce la lista di tutte
    le parole presenti, minuscuole e senza punteggiatura, in 
    ordine di apparizione.
    """
    parole = []
    f = open(nome_file, "r", encoding='utf-8')
    for riga in f:
        parole_riga = estrai_parole(riga)
        parole.extend(parole_riga)
        # parole = parole + parole_riga
    f.close()
    return parole

def leggi_dizionario(nome_file):
    parole = []
    f = open(nome_file, "r", encoding="utf-8")
    for riga in f:
        parole.append(riga.rstrip())
    f.close()
    return parole
        

elenco_parole = leggi_file('collodi_pinocchio.txt')
parole_uniche = set(elenco_parole)

print('Parole totali:', len(elenco_parole))
print('Parole uniche:', len(parole_uniche))

dizionario = leggi_dizionario('60000_parole_italiane.txt')
print('Parole nel dizionario:', len(dizionario))

parole_errate = parole_uniche.difference( set(dizionario) )
print("Parole errate:")
print(parole_errate)