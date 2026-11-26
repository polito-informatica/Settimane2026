


try:
    with open("nazioni.txt", encoding = "utf-8") as f:
        print(f.readline())

    n = int(input("inserisci un nunmero: "))

except FileNotFoundError as error:
    print("Il file non è stato trovato")

except ValueError as ve:
    print("Non hai inserito un numero")
    