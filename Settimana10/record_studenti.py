import csv  # modulo per i CSV: qui non lo usiamo ancora (leggiamo "a mano"),
            # servirà per la versione con csv.reader / csv.DictReader


def registra_studenti(filepath):
    """Legge un file CSV e restituisce una lista di record (dizionari),
    uno per ogni studente."""

    # "with" apre il file e lo chiude da solo alla fine del blocco
    with open(filepath, "r") as f:
        lista_record = []                 # qui accumuliamo i record letti

        # la prima riga contiene i nomi delle colonne: la leggiamo
        # per "consumarla", così il ciclo parte dai dati veri
        intestazione = f.readline()

        riga = f.readline()               # leggiamo la prima riga di dati

        # readline() restituisce "" (stringa vuota) quando il file è finito
        while riga != "":
            record = dict()               # nuovo dizionario per questo studente

            riga = riga.rstrip()          # togliamo il "\n" a fine riga
            valori = riga.split(",")      # spezziamo la riga sulle virgole:
                                          # "123,Rossi,Anna" -> ["123", "Rossi", "Anna"]

            # costruiamo il record: chiavi FISSE (i campi),
            # valori presi per posizione dalla lista
            record = {
                "matricola": valori[0],
                "cognome": valori[1],
                "nome": valori[2]
            }

            lista_record.append(record)   # aggiungiamo il record alla lista
                                          # (senza append, a ogni giro lo perderemmo)

            riga = f.readline()           # passiamo alla riga successiva:
                                          # senza questa istruzione, ciclo infinito!

    return lista_record                   # lista di dizionari: [{...}, {...}, ...]


def ordina_per_nome(lista_record):
    """Restituisce una NUOVA lista con i record ordinati per nome.
    La lista originale non viene modificata."""

    # sorted non sa confrontare due dizionari: con key gli diciamo
    # COSA confrontare. La lambda riceve un record e ne restituisce il nome.
    record_ordinati_per_nome = sorted(lista_record, key=lambda record: record["nome"])
    return record_ordinati_per_nome


def prendi_nome(record):
    """Fa la stessa cosa della lambda qui sopra, ma con un nome.
    Si può usare così: sorted(lista_record, key=prendi_nome)
    (senza parentesi: passiamo la funzione, non la chiamiamo)"""
    return record["nome"]


# ---------------- esecuzione ----------------

# 1. leggiamo il file e otteniamo la lista di record
studenti = registra_studenti("dati_studenti.csv")

# 2. ordiniamo per nome e stampiamo il risultato
print(ordina_per_nome(studenti))