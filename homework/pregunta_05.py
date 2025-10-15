"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
        rows = tuple(map(lambda x: x.split('\t'), lines))
        occurrencies = dict()
        for row in rows:
            if row[0] in occurrencies:
                current_max, current_min = occurrencies[row[0]]
                occurrencies[row[0]] = max(current_max, int(row[1])), min(current_min, int(row[1]))
            else:
                occurrencies[row[0]] = int(row[1]), int(row[1])
        items = list(map(lambda x: (x[0], *x[1]), occurrencies.items()))
        result = sorted(items, key=lambda x: x[0])
        return result