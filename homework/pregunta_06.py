"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open('files/input/data.csv', 'r') as f:
        lines = f.readlines()
        rows = tuple(map(lambda x: x.split('\t'), lines))
        occurrencies = dict()
        for row in rows:
            for item in row[4].split(','):
                key, value = item.split(':')
                if key in occurrencies:
                    current_min, current_max = occurrencies[key]
                    occurrencies[key] = min(current_min, int(value)), max(current_max, int(value))
                else:
                    occurrencies[key] = int(value), int(value)
        items = list(map(lambda x: (x[0], *x[1]), occurrencies.items()))
        result = sorted(items, key=lambda x: x[0])
        return result