# data una situazione dei parcheggi
# trova e stampa l'elenco di tutte 
# le file di posti liberi

# park = [ '_', '_', 'X', '_', '_', 'X', '_', '_', '_', '_' ]

park = ['_'] * 20

# pos=0, lun=2
# pos=3, lun=2
# pos=6, lun=4

while '_' in park:

    lun_max = 0

    for i in range(len(park)):
        lun = 0

        while i+lun<len(park) and park[i+lun]=='_':
            # print(i, lun)
            lun=lun+1

        # print(i, lun)
        # sì, ma tu sei la più lunga?
        if lun>lun_max:
            lun_max = lun
            pos_max = i

    # print("sequenza max", pos_max, lun_max)

    nuova_pos = pos_max + lun_max//2

    # print("parcheggia in posizione", nuova_pos)
    park[nuova_pos] = 'X'
    print(park)