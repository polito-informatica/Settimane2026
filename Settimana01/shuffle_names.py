# Rimescola nomi, cognomi, matricole dell'elenco degli studenti per motivi di privacy

import csv
import operator
import random


ELENCO_ORIGINALE = "14BHDWZ_2027.csv"  # questo file è riservato
ELENCO_MESCOLATO = "14BHDWZ_2027_shuffled.csv"  # file di uscita con i nomi rimescolati


def main():
    with open(ELENCO_ORIGINALE, "r", encoding="latin-1", newline="") as f_in:
        reader = csv.reader(f_in)
        header = next(reader)
        studenti = list(reader)

    transposed = transpose(studenti)

    for column in transposed:
        random.shuffle(column)

    shuffled = transpose(transposed)

    shuffled.sort(key=operator.itemgetter(1, 2))

    with open(ELENCO_MESCOLATO, "w", encoding="utf-8", newline="") as f_out:
        writer = csv.writer(f_out)
        writer.writerow(header)
        writer.writerows(shuffled)


def transpose(array: list[list[any]]) -> list[list[any]]:
    """Computes and returns the transposed of an array (list of lists).

    Credits: https://stackoverflow.com/a/6473742/986709

    Args:
        array (list[list[any]]): The original array

    Returns:
        list[list[any]]: The transposed array
    """
    return [list(i) for i in zip(*array)]


main()