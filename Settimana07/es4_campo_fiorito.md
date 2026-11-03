
# Esercizio "Campo Fiorito"

*Argomenti richiesti: tabelle, random*


Consideriamo il gioco del **Campo Fiorito**,
in cui in una griglia quadrata di `N`x`N` caselle di prato sono presenti `M` fiori.

🐝 Chi gioca deve scoprire tutte le caselle che contengono fiori,
evitando di perdere tempo esplorando quelle che invece contengono solo una zolla d'erba.

## Fase 1: creazione del campo

Il programma deve innanzitutto creare una matrice `N`x`N` e posizionare
gli `M` fiori in posizioni casuali (distinte tra loro).
I fiori possono essere rappresentati da un valore Booleano `True`/`False`.

In seguito, il programma calcoli una matrice `N`x`N` di numeri interi,
in cui ciascuna cella contenga il numero di fiori presenti
nelle `8` celle adiacenti (se esistono).
Si stampi il contenuto di queste due matrici,
per verificare la correttezza dei calcoli.

## Fase 2: interazione utente

Si permetta poi all'utente di selezionare una casella
(inserendone le coordinate di riga e colonna).

In funzione del contenuto di tale casella, sono possibili i 
seguenti tre casi:
- casella *già selezionata* in precedenza: si stampi un messaggio di errore
- casella contenente una *zolla d'erba*: si stampi un messaggio di sconfitta,
    e il numero di fiori nelle caselle adiacenti
- casella contenente *un fiore*: si stampi il numero di fiori trovati fino a quel momento

### Esempio:
```
🟢🟢🟢🟢  1110
🟢🌸🟢🟢  2121
🌸🟢🟢🌸  1331
🟢🟢🌸🟢  1212
```