# esempi di lettura e analisi di file di testo in Python
outfile=open("output.txt",'w',encoding='utf-8')
outfile.write("Ciao Mondo!! Adesso so scrivere i txt da python!\n")
# lettura di base di un file di testo
infile=open("output.txt",'r',encoding='utf-8')
# print(infile) 
contenuto=infile.read()
print(contenuto)
infile.close()
'''
#oppure
primariga=infile.readline()
print(primariga)
secondariga=infile.readline()
print(secondariga)
#oppure
for riga in infile: 
    print(riga)
#oppure
listarighe=infile.readlines()
print(listarighe)
'''


#  contare i caratteri di ogni riga in un file di testo
n_ch=[]
infile=open("diario.txt",'r',encoding='utf-8')
for riga in infile:
    n_ch.append(len(riga))
    print(riga + ' ha ' + str(len(riga)) + ' caratteri')

infile.close()

# programma che legga il file allenamenti.txt
# che contiene gli allenamenti della settimana
# come tipo allnamneto, durata in minuti, velocità media
#  e mi comunichi le statistiche della settimana
# in particolare il totale di ore di allenamento
# e la velocità media ponderata
durate=[]
velocita=[]
infile= open('allenamenti.txt','r',encoding='utf-8')
for riga in infile:
    riga_s=riga.split()
    print(riga_s)
    durate.append(float(riga_s[1]))
    velocita.append(float(riga_s[2]))
infile.close()

print(durate)
print(velocita)
numeratore=0
print('In totale questa settimana ti sei allenato ' + str(sum(durate))+' minuti')
for i in range( len(durate)):
    numeratore= numeratore + durate[i] * velocita[i]

mediap=numeratore/sum(durate)
print(mediap)
