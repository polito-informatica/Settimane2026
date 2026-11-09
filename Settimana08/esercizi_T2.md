# Le formule che servono

#  sulla memoria
MEM (bit/byte) = N_Celle x Dimensione_cella (bit/byte)

Parallelismo memoria == Dimensione_cella == Dimensione DBUS == Dimensione Registri == Parallelismo ALU

N_celle <=  2 ^ (Dimensione ABUS)

MEM <= 2 ^ ABUS * DBUS

MEM = MEMORIA CENTRALE (RAM)

# sui tempi di esecuzione

Tempo di esecuzione = Numero di istruzioni (macchina) x Cicli di clock per Istruzione x Periodo di Clock

# 128

I registri rappresentano una piccola quantità di memoria interna alla CPU, direttamente
connessi alla ALU e alla FPU. Sono il tipo di memoria più veloce. Servono per memorizzare
i dati di lavoro del programma e gli operandi/risultati delle operazioni della ALU.

Il program counter invece non contiene dati di lavoro, bensì contiene l'indirizzo di memoria
della prossima istruzione che la CPU dovrà eseguire. Normalmente si incrementa da solo dopo
avere letto il codice dell'istruzione da eseguire.

# 127 

Unità di controllo
    Program Counter (PC) -> contiene indirizzo della prox istruzione da eseguire
    Instrunction Register (IR) -> contiene il codice binario della istruzione in corso di esecuzione
    Flag -> registro che memorizza una serie di bit che rappresentano l'esito dell'ultima operazione calcolata dalla ALU (positiva, negativa, overflow, carry, zero, ...)
    Logica di controllo -> legge il valore dell'IR e determinare quali operazioni devono essere eseguite e su quali dati

# 126

n_celle = dimensione_memoria / dimensione_cella = 8 kB / 2 B = 4 k celle 
quanti bit servono nell'ABUS per indirizzare 4k celle?
2 ^ ABUS = 4 k ?? ABUS = 12

# 125

ALU = Unità aritmetico-logica

Svolge le operazioni tra numeri interi (binario puro o complemento a due), sulla base dei
comandi che provengono dalla logica di controllo dell'unità di controllo
e dei dati presenti nei registri. Salva il risultato in un registro e aggiorna
il registro dei Flag.

# 124

ABUS = 10 bit (b)
Dimensione celle memoria = 2 Byte (B)

Max Memoria?
MEM = 2 ^ ABUS x dim_cella = 2 ^ 10 x 2 B = 2 kB

Se ABUS fosse di 11 b:
MEM = 2 ^ 11 x 2 B = 4 kB

# 123

Esecuzione di una istruzione - 3 fasi:
- Fetch (reperimento)
    IR = MEM(PC)
    La CPU chiede alla memoria di leggere il contenuto della cella il cui indirizzo
    è presente nel PC, e salva il risultato nell'IR
    PC = PC + 1
- Decode
    La logica di controllo nella CU legge contenuto di IR e definisce quale operazione
    la ALU/FPU debba eseguire, e su quali operandi.
    In pratica decide i comandi da dare alla ALU
- Execute
    La ALU/FPU esegue i comandi ricevuti e salva i risultati.

# 121

- Registri della CPU (T ~ ns, D ~ 100 B) Volatile
- Memoria cache (eventualmente 1o livello e 2o livello) (T ~ 100 ns, D ~ 1 MB ) Volatile
- Memoria centrale (RAM) (T ~ 1 ms, D ~ 10 GB) Volatile
- Memoria di massa: non volatile
    - Flash (SSD Solid State Disk) (T ~ 10-20 ms, D ~ 500 GB)
    - Hard Disk (T ~ 50-100 ms, D ~ 4-8 TB)

# 120

ABUS = 32 b = 4 B
Cella = 8 B

MEM = 2 ^ ABUS x Cella = 2 ^ 32 x 8 B = 2 ^ 35 B
1 M = 2 ^ 20
MEM = 2 ^ 35 = 2 ^ 15 MB = 32768 MB
= 2 ^ 5 GB = 32 GB

# 117

Esistono più memorie per permettere alla CPU di lavorare alla massima velocità con
le memorie più vicine a lei (Registri, Cache), ma allo stesso tempo non avere limitazioni
alla dimensione della memoria, che sarebbe troppo costoso ampliare a questi livelli.
Quindi aggiungiamo memoria meno costosa ma più capiente. Soprattutto la memoria centrale
(RAM) e solitamente memoria di massa.

#  116

Spiegare cosa sono i registri -> v. sopra

Nel ciclo di esecuzione intervengono PC e IR nella fase di fetch, ed i registri dati nella fase
di execution

# 114

La FPU (Floating point unit) svolge le operazioni tra numeri reali (floating point), solitamente
richiede un tempo di calcolo maggiore rispetto alla ALU.

# 113

Clock = un segnale periodico a frequenza fissa che definisce il cadenzamento di tutte
le operazioni interne alla CPU e corrisponde alla durata delle operazioni più semplici
(elementari) che la CPU può svolgere (leggi registro, scrivi registro, decodifica istruzione,
fai calcolo ALU...).

# 112

Unità Operativa =
    Registri
    ALU
    FPU

# 108

dimensione dei registri = 32 bit come il DBUS come la memoria
numero dei registri -> non possiamo dire niente

# 106

- Fetch
    ABUS = valore del PC
    CBUS = leggi
    DBUS = dato dalla memoria, che fisce in IR
- Decode
    i bus non fanno nulla
- Execute
    dipende, sono usati se l'istruzione corrente
    prevede lettura o scrittura dalla memoria

# 103

MEM = 4 GB
Cella = 32 b = DBUS
ABUS = ?

MEM = 2 ^ ABUS x DBUS

4 GB = 2 ^ ABUS x 32 b

4 2^30 B = 2 ^ ABUS x 4 B

2 ^ 30 = 2 ^ ABUS

ABUS = 30

# 84

f_CK = 2 GHz
    T_CK = 1 / f_CK = 0.5 ns
n_op = 10^7
CPI = 4 (cicli di clock per istruzione)
T = ?

T = n_op x CPI x T_CK = 10^7 x 4 x 0.5 ns = 2 x 10^7 ns = 20 ms