import string   # ci serve string.punctuation: tutti i segni di punteggiatura ASCII


def conta_occorrenze(filepath):
    """Legge un file di testo e restituisce un dizionario
    parola -> numero di volte in cui compare (array associativo)."""

    with open(filepath, "r", encoding="utf-8") as f:
        conta_parole = dict()     # chiavi: parole (non note in anticipo!)
                                  # valori: quante volte le abbiamo viste

        # parole troppo comuni che non ci interessano.
        # È un SET: il controllo "in" è velocissimo e non ci sono duplicati
        stopword = {"the", "and", "to", "a", "of", "it", "she", "i", "you", "in", "said", "was"}

        riga = f.readline()       # leggiamo la prima riga
        while riga != "":         # "" = fine del file (NON -1!)

            # puliamo la riga PRIMA di spezzarla in parole
            riga = riga.replace("--", " ")   # "wonderland--said" -> due parole
            riga = riga.replace("-", " ")    # anche i trattini singoli
                                             # (la riga sopra a questo punto è ridondante)
            riga = riga.lower()              # "Alice" e "alice" sono la stessa parola
            riga = riga.rstrip()             # togliamo "\n" (split lo farebbe comunque)

            parole_riga = riga.split()       # lista delle parole della riga

            for parola in parole_riga:
                # strip toglie la punteggiatura SOLO agli estremi: "(alice)," -> "alice"
                parola = parola.strip(string.punctuation)

                # CORRETTO: se la "parola" era solo punteggiatura ora è "": la saltiamo
                if parola == "":
                    continue

                if parola not in stopword:
                    # schema classico del contatore:
                    # prima volta -> 1, volte successive -> +1
                    if parola not in conta_parole.keys():
                        conta_parole[parola] = 1
                    else:
                        conta_parole[parola] += 1

            riga = f.readline()       # riga successiva (senza: ciclo infinito)

        print(conta_parole)           # stampa di controllo (molto lunga!)
        return conta_parole


def ordina_alfabeticamente(dizionario_conte):
    """Lista di coppie (parola, conteggio) in ordine alfabetico."""
    # items() dà le coppie (chiave, valore). Senza key, sorted confronta
    # le tuple dal primo elemento, cioè la parola -> ordine alfabetico
    elementi_ordinati = sorted(dizionario_conte.items())
    return elementi_ordinati


def ordina_per_conta(dizionario_conte):
    """Lista di coppie (parola, conteggio) dalla più frequente alla meno."""
    # key: per ogni coppia guardiamo elemento[1], cioè il conteggio.
    # reverse=True: dal più grande al più piccolo
    elementi_ordinati = sorted(dizionario_conte.items(), key=lambda elemento: elemento[1], reverse=True)
    return elementi_ordinati


def top5(elementi_ordinati):
    """Stampa un istogramma testuale delle prime 5 parole.
    Si aspetta una lista GIÀ ordinata per conteggio."""

    top5 = elementi_ordinati[:5]      # slicing: i primi 5 elementi
    massimo = top5[0][1]              # conteggio della parola più frequente

    for chiave, valore in top5:
        # scaliamo: la più frequente avrà 40 "#", le altre in proporzione
        # CORRETTO: la moltiplicazione per 40 va DENTRO round
        print(chiave, "#" * round(valore / massimo * 40))
    return top5


# ---------------- esecuzione ----------------

conta_parole = conta_occorrenze("alice_in_wonderland.txt")   # 1. contiamo
print(ordina_alfabeticamente(conta_parole))                  # 2. ordine alfabetico
elementi_ordinati = ordina_per_conta(conta_parole)           # 3. ordine per frequenza
top5(elementi_ordinati)                                      # 4. istogramma