
def statistica_esame(nome_file):
    totale = 0
    superamenti = 0
    try:
        with open(nome_file, encoding = "utf-8") as f:
            for line in f:
                voto = int(line)

                totale= totale + 1
                if voto >= 18:
                    superamenti = superamenti + 1
        statistica = superamenti/totale
        print ("statistica di superamento: ", statistica)
    except FileNotFoundError:
        print("il file non è stato trovato")
    except ZeroDivisionError:
        print("qualcosa è andato storto")

    return statistica


#nome_file = "esame_analisi1.txt"

#nome_file = input("Inserire nome file: ")

flag = True

while flag:
    nome_file = input("Inserire nome file: ")
    mia_statistica = statistica_esame(nome_file)
    if nome_file == '':
        flag = False







