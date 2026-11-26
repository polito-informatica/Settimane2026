# Sistemi di Numerazione

## Turno 1/A

Si considerino i seguenti numeri, codificati in complemento a 2 su 8 bit, e per comodità rappresentati in base 16.

Si esegua l'operazione X+Y, fornendo il risultato in base 2 ed in base 16, e si dica se si verifica una condizione di overflow e perché.

X = 6B
Y = 5A


## Turno 1/B

Si considerino i seguenti numeri, codificati in complemento a 2 su 8 bit, e per comodità rappresentati in base 16.

Si esegua l'operazione X+Y, fornendo il risultato in base 2 ed in base 16, e si dica se si verifica una condizione di overflow e perché.

X = CA
Y = 5F

## Turno 2/A e 3/A

Si considerino i seguenti numeri, codificati in complemento a 2 su 8 bit, e per comodità rappresentati in base 16.

Si esegua l'operazione X-Y, fornendo il risultato in base 2 ed in base 16, e si dica se si verifica una condizione di overflow e perché.

X = 6B
Y = 5A

## Turno 2/B e 3/B

Si considerino i seguenti numeri, codificati in complemento a 2 su 8 bit, e per comodità rappresentati in base 16.

Si esegua l'operazione X-Y, fornendo il risultato in base 2 ed in base 16, e si dica se si verifica una condizione di overflow e perché.

X = CA
Y = 5F



# Architettura degli elaboratori


## Turno 1/A

Sia dato un sistema di elaborazione con CPU a 64 bit dotata di 16 registri, connessa a 16 GB di memoria RAM ed una memoria cache di 256 kB, con accesso a 512 GB di memoria di massa. Il clock della CPU è pari a 2 GHz e la CPU impiega in media 1.5 cicli di clock per istruzione. L'unità operativa contiene due ALU e una FPU.

Si determini il tempo necessario per eseguire 500 milioni di istruzioni.

## Turno 1/B

Sia dato un sistema di elaborazione con CPU a 64 bit dotata di 16 registri, connessa a 16 GB di memoria RAM ed una memoria cache di 256 kB, con accesso a 512 GB di memoria di massa. Il clock della CPU è pari a 2 GHz e la CPU impiega in media 1.5 cicli di clock per istruzione. L'unità operativa contiene due ALU e una FPU.

Si determini la quantità massima di memoria RAM installabile se l'ABUS avesse 32 bit

## Turno 2/A e 3/A

Sia dato un sistema di elaborazione con CPU a 64 bit dotata di 16 registri, connessa a 16 GB di memoria RAM ed una memoria cache di 256 kB, con accesso a 512 GB di memoria di massa. Il clock della CPU è pari a 2 GHz e la CPU impiega in media 1.5 cicli di clock per istruzione. L'unità operativa contiene due ALU e una FPU.

Si determini il numero di istruzioni che il sistema è in grado di eseguire in 100 ms.


## Turno 2/B e 3/B

Sia dato un sistema di elaborazione con CPU a 64 bit dotata di 16 registri, connessa a 16 GB di memoria RAM ed una memoria cache di 256 kB, con accesso a 512 GB di memoria di massa. Il clock della CPU è pari a 2 GHz e la CPU impiega in media 1.5 cicli di clock per istruzione. L'unità operativa contiene due ALU e una FPU.

Si determini la dimensione minima dei bus di sistema (DBUS e ABUS).



# Programmazione Python

## Turno 1/A

Date le seguenti istruzioni:

```python
a = [1, 2]
b = list(a)
b.pop(0)
```
determinare il contenuto di `a` e `b` e giustificarne il motivo.


## Turno 1/B

Date le seguenti istruzioni:

```python
a = [1, 2]
b = a
a.append(3)
```

determinare il contenuto di `a` e `b` e giustificarne il motivo.

## Turno 2/A e 3/A

Date le seguenti istruzioni:

```python
a = [1, 2]
b = list(a)
b.append(3)
```
determinare il contenuto di `a` e `b` e giustificarne il motivo.

## Turno 2/B e 3/B

Date le seguenti istruzioni:

```python
a = [1, 2]
b = a
a = a + [3]
```
determinare il contenuto di `a` e `b` e giustificarne il motivo.
