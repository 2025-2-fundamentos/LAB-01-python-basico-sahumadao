"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
        letters = tuple(map(lambda x: x.split('\t')[0], lines))
        occurrencies = dict()
        for letter in letters:
            if letter in occurrencies:
                occurrencies[letter] += 1
            else:
                occurrencies[letter] = 1
        result = sorted(occurrencies.items(), key=lambda x: x)
        return result