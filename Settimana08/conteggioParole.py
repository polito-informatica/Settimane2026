# conteggiare il numero di parole presenti nel file intervistaLinus.txt
# printare le domande fatte nell'intervista (non svolto, solo contate)

infile=open('intervistaLinus.txt','r',encoding='utf-8')
tot_parole=0
for riga in infile:
    parole=riga.split()
    tot_parole=tot_parole+len(parole)
infile.close()


infile=open('intervistaLinus.txt','r',encoding='utf-8')
testo=infile.read()
infile.close()
tot_domande=0
pos=0
while pos != -1:
    pos=testo.find('?')
    tot_domande+=1
    testo=testo[pos+1:] 
print('il testo ha ' + str(tot_domande)+' domande')
'''
# oppure
infile=open('intervistaLinus.txt','r',encoding='utf-8')
for riga in infile:
    tot_domande+=riga.count('?')
infile.close()
print('il testo ha ' + str(tot_domande)+' domande')

#oppure
infile=open('intervistaLinus.txt','r',encoding='utf-8')
tot_domande=sum(riga.count('?') for riga in infile)
infile.close()
print('il testo ha ' + str(tot_domande)+' domande')

# oppure
infile=open('intervistaLinus.txt','r',encoding='utf-8')
testo=infile.read()
infile.close()
tot_domande=testo.count('?')
print('il testo ha ' + str(tot_domande)+' domande')
'''
# stampare le domande fatte nell'intervista
# le domande possono stare ovunque nella riga, quindi si lavora sull'intero testo:
# si scorre il testo carattere per carattere, accumulando la frase corrente
# quando si incontra '.', '!', '?' o '\n' la frase e' finita:
# se termina con '?' è una domanda e la si stampa
infile=open('intervistaLinus.txt','r',encoding='utf-8')
testo=infile.read()
infile.close()

frase=''
for carattere in testo:
    if carattere == '?':
        frase=frase+carattere
        frase=frase.strip()
        if frase != '?':
            print(frase)
        frase=''
    elif carattere == '.' or carattere == '!' or carattere == '\n':
        # fine di una frase che non e' una domanda: la si scarta
        frase=''
    else:
        frase=frase+carattere
