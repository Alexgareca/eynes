__author__ = 'Alexander Gareca'

from random import randint as num

separador = '-' * 40


def crear_matriz(f, c):
    """
    Creamos una matriz de 5 filas y 5 columnas
    >>> matriz = crear_matriz(5,5)

    Verifica que se haya creado la matriz correctamente, mediante el calculo de filas*columnas
    >>> len(matriz) * len(matriz[0])
    25

    Crea una matriz con un valor numerico de filas invalido
    >>> matriz = crear_matriz(-1, 5)
    El numero de filas es invalido
    Ingresar un numero entero mayor a 0 (cero):

    Crea una matriz con un valor numerico de columnas invalido
    >>> matriz = crear_matriz(5, 1.5)
    El numero de columnas es invalido
    Ingresar un numero entero mayor a 0 (cero):
    """
    while f <= 0 or isinstance(f, float):
        print('El numero de filas es invalido')
        f = int(input('Ingresar un numero entero mayor a 0 (cero):'))

    while c <= 0 or isinstance(c, float):
        print('El numero de columnas es invalido')
        c = int(input('Ingresar un numero entero mayor a 0 (cero):'))

    m = [[0] * c for i in range(f)]  # genera una matriz m*n
    for i in range(f):
        for j in range(c):
            m[i][j] = num(1, 100)

    return m


def mostrar_matriz(m):
    """
    Crea una matriz
    >>> matriz = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 8, 7], [4, 5, 12, 9, 10], [11, 34, 21, 34, 12]]

    Muestra la matriz
    >>> mostrar_matriz(matriz)
    ----------------------------------------
    Matriz
    ----------------------------------------
        1    2    3    4    5
        2    3    4    5    6
        3    4    5    8    7
        4    5   12    9   10
       11   34   21   34   12
    """
    titulo = '\nMatriz\n'
    r = ''
    for i in range(len(m)):
        r += '\n'
        for j in range(len(m[i])):
            r += '{:>5}'.format(str(m[i][j]))
    print(separador + titulo + separador + r)


def string_num_consecutivo(orientacion, fila_i, col_i, fila_f, col_f):
    r = '\n{:<20}'.format(orientacion)
    r += '{:<15}{:<15}'.format('|| fila: ' + str(fila_i), '| columna: ' + str(col_i))
    r += '{:<15}{}'.format('|| fila: ' + str(fila_f), '| columna: ' + str(col_f))
    return r


def num_consecutivos(m):
    """
    Crea una matriz
    >>> matriz = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 8, 7], [4, 5, 12, 9, 8], [11, 34, 21, 34, 12]]

    Encuentra los numeros consecutivos y los muestra
    >>> num_consecutivos(matriz)
    ----------------------------------------
    Numeros consecutivos
    Orientacion         || Posicion Inicial           || Posicion Final
    Horizontal          || fila: 0     | columna: 0   || fila: 0     | columna: 3
    Vertical            || fila: 0     | columna: 0   || fila: 3     | columna: 0
    Horizontal          || fila: 0     | columna: 1   || fila: 0     | columna: 4
    Horizontal          || fila: 1     | columna: 0   || fila: 1     | columna: 3
    Vertical            || fila: 0     | columna: 1   || fila: 3     | columna: 1
    Horizontal          || fila: 1     | columna: 1   || fila: 1     | columna: 4
    Vertical            || fila: 0     | columna: 4   || fila: 3     | columna: 4
    """
    pos_ini_h = None  # posicion inicial horizontal
    pos_ini_v = None  # posicion inicial vertical
    titulo = '\nNumeros consecutivos\n'
    titulo += '{:<20}'.format('Orientacion')
    titulo += '{:<30}'.format('|| Posicion Inicial')
    titulo += '{}'.format('|| Posicion Final')
    r = ''
    for i in range(len(m)):
        cont_h = 0  # contador horizontal
        cont_v = 0  # contador vertical
        for j in range(len(m[i]) - 1):
            if m[i][j] + 1 == m[i][j+1]:
                cont_h += 1
                if cont_h == 1:
                    pos_ini_h = j

                elif cont_h == 3:
                    r += string_num_consecutivo('Horizontal', i, pos_ini_h, i, j+1)

                elif cont_h > 3:
                    pos_ini_h += 1
                    r += string_num_consecutivo('Horizontal', i, pos_ini_h, i, j+1)

            else:
                cont_h = 0

            if m[j][i] + 1 == m[j+1][i]:
                cont_v += 1
                if cont_v == 1:
                    pos_ini_v = j

                elif cont_v == 3:
                    r += string_num_consecutivo('Vertical', pos_ini_v, i, j+1, i)

                elif cont_v > 3:
                    pos_ini_v += 1
                    r += string_num_consecutivo('Vertical', pos_ini_v, i, j+1, i)

            else:
                cont_v = 0

    print(separador + titulo + r)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
