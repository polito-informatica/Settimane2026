# Sviluppo di primi esempi su tipi di dato in Python
# seconda riga di commento 

"""
commenti su 
più righe
....
"""

# stampa di una stringa
print("Hello world!")
# print senza argomenti: stampa una riga vuota
print()
# stampa di un numero intero
print(4)

# valutazione espressioni
# somma tra interi: stampa 8
print(4+4)

# più valori separati da virgola: stampati con uno spazio in mezzo
print("Hello, world", 4, 4+4)

# tra virgolette è una stringa: non viene calcolata
print("4 + 4")

# + tra stringhe le concatena: stampa 44
print("4" + "4")

# str() converte l'intero in stringa per concatenarlo: stampa 44
print("4" + str(4))

# la virgola separa due valori: stampa 2 5
print(2 , 5)
# numero decimale (float): si usa il punto
print(2.5)

# la divisione / restituisce sempre un float
print(1 / 3)

# errore (TypeError): non si possono sommare una stringa e un intero
# print("4" + 4)

# Le variabili

# assegnazione di un valore intero alla variabile a
a = 3

# stampa il contenuto della variabile
print(a)

# riassegnazione: il nuovo valore sostituisce il precedente
a = 5
print(a)

# La stessa variabile, che prima conteneva un numero, ora contiene una stringa:
# la stessa variabile può ricevere assegnazioni di valori di tipo diverso
a = "Nel mezzo del cammin di nostra vita..."
print(a)