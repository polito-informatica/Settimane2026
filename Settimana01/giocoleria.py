# Esercizio: giocoloeria
# il giocoliere vuole giocare lanciando tre palline ... ma ha solo due mani

# inizializzazione delle due variabili con una stringa
mano_destra = "nulla"
mano_sinistra = "nulla"

# stampa di testo e variabili insieme
print("il giocoliere ha", mano_destra, "nella mano destra e", mano_sinistra, "nella mano sinistra")

# le palline sono rispettivamente gialla, verde, rossa

# il giocoliere inizia a giocare e ne prende due in mano

# riassegnazione: i valori precedenti vengono sovrascritti
mano_destra = "pallina verde"
mano_sinistra = "pallina gialla"

print("il giocoliere ha", mano_destra, "nella mano destra e", mano_sinistra, "nella mano sinistra")

# manca una parte nel modo in cui abbiamo descritto il gioco:
# la collocazione della pallina che viene lanciata in aria

# variabile d'appoggio: salva il valore prima che venga sovrascritto
aria = mano_sinistra
# si copia il valore di una variabile in un'altra
mano_sinistra = mano_destra
# ora mano_destra può ricevere un nuovo valore senza perdere dati
mano_destra = "pallina rossa"

# stato finale: tre valori distribuiti su tre variabili
print("il giocoliere ha", mano_destra, "nella mano destra e", mano_sinistra, "nella mano sinistra e", aria, "in aria")