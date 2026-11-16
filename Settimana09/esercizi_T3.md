# Esercizi di Teoria
# Domanda 3 (Python)

Domande tratte da: https://github.com/polito-informatica/Esempi-esame/blob/master/teoria/python.md

# 123

Un ciclo for è utilizzato quanto si conosce a priori il numero di iterazioni
da eseguire, e/o si deve iterare sui valori presenti un contenitore o in un range di valori.

    for elemento in lista:
        print(elemento)

Un ciclo while invece è il caso generale, valido anche quando non conosco in anticipo
il numero di iterazioni.

    x = 1000
    while x>1:
        print(x)
        x = x / 2

# 122 

Liste vs Tuple

Una tupla è un contenitore sequenziale (come una lista), con la differenza che la
tupla è **immutabile**: non è possibile aggiungere, rimuovere o sostituire elementi una volta
creata. È invece possibile modificare il valore dei singoli elementi (se questi sono
mutabili).

Mentre una lista si costruisce con [ 1,2,3 ], la tupla usa le parentesi tonde (1,2,3)

# 111

i numeri in entrambi i casi vengono ordinati in modo crescente.

elenco.sort() la lista 'elenco' viene modificata ed i suoi elementi compariranno 
nel nuovo ordine crescente

sorted(elenco) la lista 'elenco' NON viene modificata, rimane uguale. Gli elementi
ordinati saranno inseriti in una nuova lista che viene restituita dalla funzione
sorted. Quindi è necessario assegnare il risultato di tale funzione ad una variabile.
    elenco_ordinato = sorted(elenco)

Nota: se provassi a fare
    elenco_ordinato = elenco.sort()  non va perché elenco_ordinato = None

# 109

La lista stampata NON è ordinata perché la funzione non modifica la lista
passata come argomento (sorted() non modifica la lista).

La funzione calcola dentro new_lista una versione ordinata degli stessi numeri,
ma questo valore non viene utilizzato in nessun punto.

Correzione: 
def ordina (myLista):
    myLista.sort()

lista = [4, 3, 1, 2]
ordina(lista)
print(lista)

Oppure:
def ordina (myLista):
    newlista = sorted(myLista)
    return newlista

lista = [4, 3, 1, 2]
lista = ordina(lista)
print(lista)

# 108

Il problema è che si cancellano elementi da una lista su cui si sta iterando.

Quindi: 
- l'indice 'i' arriverà a valori che sono maggior degli indici validi della lista
in cui stiano stati cancellati degli elementi
- poiche il ciclo for incrementa 'i' in ogni caso, quando ci siano dei <0 consecutivi,
il secondo viene "saltato" perché nel frattempo gli elementi successivi sono stati
anticipati di una posizione.

Soluzioni possibili:
- iterare la lista partendo dal fondo: range(len(int_list)-1, -1, -1)
- costruire una nuova lista inserendo solo gli elementi >=0 (con append)

# 106

Parametro formale:
    **Nome** di una variabile di comodo utilizzata all'interno della funzione per 
    rappresentare i valori ricevuti.
        def ipotenusa(a, b):

Parametro attuale:
    Il **valore** che viene attribuito ai parametri formali nel momento in cui chiamo
    la funzione.
        c = ipotenusa( 3, 7 )
        z = ipotenusa( x, y )

# 102

Argomenti : valori in ingresso (che saranno assegnati ai parametri formali)

Il Valore restituito da una funzione è indicato dall'istruzione 'return' e permettere 
di fornire un valore "risultato" al chiamante della funzione

    def ipotenusa(a, b):
        c = math.sqrt(a*a+b*b)
        return c

I valori restituiti (quando sono più di uno) solitamente vengono impacchettati in una tupla
che viene restituita come unico valore.

    return (x, y)

    return x, y

# 101

L'operatore di slice si può utilizzare su tutte le sequenze (sequenza = contenitore ordinato, indicizzabile, accessibile via indice): stringhe, liste, tuple.

Estrae una sotto-sequenza delimitata dall'indice del primo elemento (compreso) fino all'indice
dell'ultimo elemento (eslcuso).
    lista[3:7]
    stringa[0:4]

Esiste anche il terzo parametro opzionale che indica il "passo" di estrazione.

# 98

Stringhe e liste sono entrambi contenitori sequenziali.
Stringa può contenere solo caratteri. Sono IMmutabili. Si indicano con " ", ' ', ''' ''', """ """ 
Lista può contenere qualsiasi tipo di elementi. Sono MUTabili. Si indica con [ ]

# 97

x è una lista di 2 elementi
Gli elementi sono entrambi tuple, entrambe di 2 elementi, i quali sono numeri interi

# 96

Non bisogna usare remove() ma pop() perché altrimenti si cancella il primo "1" trovato
anziché quello nella posizione in cui è doppio.

Non bisgona incrementare "i" quanto si è rimosso l'elemento, altrimenti si rischia
di saltare il successivo.

# 89

Enumerate riceve come argomento una sequenza, e restituisce una lista di coppie,
ciascuna composta da un indice e da un elemento della sequenza iniziale.
Esempio:
    a = [ 6, 12, 18 ]
    enumerate(a) = [ (0, 6), (1, 12), (2, 18) ]

Utilizzato soprattutto per iterare contemporeaneamente sugli indici
e sui valori di una sequenza:
    for i, x in enumerate(a):

# 79

Indentazione del codice consiste in un numero di spazi inziali
nelle righe di codice.

Serve per delimitare i BLOCCHI di istruzioni che ricadono sotto
uno dei costrutti di controllo del flusso (che tipicamente 
terminano con un : per aprire un nuovo blocco.).

Si apre un nuovo livello di indentazione ogni volta che abbiamo
una istruzione: if, else, elif, while, for, with, def.
e l'indentazione viene ridotta alla fine del blocco di istruzioni
interessato

# 78

La funzione non restituisce nulla e non modifica il contenuto
del suo parametro formale 'lista', in quanto la riga
    lista = intList
modifica il valore della variablie 'lista' rendendola non più
collegata al parametro attuale che si vorrebbe modificare.

Per non perdere l'alias occorre fare solo operazioni che 
modifichino il VALORE ma non la VARIABILE.

    lista[:] = intList

    oppure uso direttamente 
    lista.append()
    invece di intList.append()

Scriendo invece 
    return lista
il chiamenta poteva avere i valori, ma NON nel parametro attuale fornito.

    valori = []
    valori2 = read(valori)

# 65

Per modificare il primo elemento di a posso:
    a[0] = 'Z'

Essendo b una stringa (immutabile)
    b[0] = 'Z' è vietato
non si può modificare il primo elemento

b = 'Z' + b[1:]
non modifica effettivamente 