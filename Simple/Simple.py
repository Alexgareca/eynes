__author__ = 'Alexander Gareca'

from random import randint as num


separador = '-' * 50
valido_ordenamiento = False


def lista_invalida(lista):
    if not isinstance(lista, list):
        mensaje = '{}'.format('\nEl elemento ingresado no pertenece a una lista\n')
        print(separador + mensaje + separador)
        return True

    elif len(lista) == 0:
        mensaje = '{}'.format('\nEl elemento ingresado es una lista vacia\n')
        print(separador + mensaje + separador)
        return True

    elif not isinstance(lista[0], dict):
        mensaje = '{}'.format('\nLa lista ingresada no contiene elementos de tipo diccionario\n')
        print(separador + mensaje + separador)
        return True

    return False


def generar_lista_clientes(n):
    """
    Crea una lista
    >>> clientes = generar_lista_clientes(10)

    Verifica que la lista fue creada con los n elementos
    >>> len(clientes)
    10

    """
    while n <= 0 or not isinstance(n, int):
        print('El numero ingresado no es valido')
        n = int(input('Ingresar un numero entero mayor a 0 (cero):'))

    global valido_ordenamiento
    valido_ordenamiento = False
    lista = []
    for i in range(1, n + 1):  # En esta caso use la variable "i" como el "id"
        edad = num(1, 100)
        datos_clientes = {'ID': i,
                          'Edad': edad}
        lista.append(datos_clientes)

    return lista


def mostrar_lista(lista):
    """
    Crea una lista y se muestra usando la funcion mostrar_lista
    >>> clientes = [{'ID': 1, 'Edad': 97}, {'ID': 2, 'Edad': 20}, {'ID': 3, 'Edad': 8}, {'ID': 4, 'Edad': 98}, {'ID': 5, 'Edad': 41}, {'ID': 6, 'Edad': 13}, {'ID': 7, 'Edad': 3}, {'ID': 8, 'Edad': 42}, {'ID': 9, 'Edad': 9}, {'ID': 10, 'Edad': 67}]
    >>> mostrar_lista(clientes)
    LISTA
    --------------------------------------------------
    ID:1     |    Edad:97
    ID:2     |    Edad:20
    ID:3     |    Edad:8
    ID:4     |    Edad:98
    ID:5     |    Edad:41
    ID:6     |    Edad:13
    ID:7     |    Edad:3
    ID:8     |    Edad:42
    ID:9     |    Edad:9
    ID:10    |    Edad:67

    Ingresa una lista vacia, es decir, un dato invalido
    >>> clientes = []
    >>> mostrar_lista(clientes)
    --------------------------------------------------
    El elemento ingresado es una lista vacia
    --------------------------------------------------

    Ingresa otro tipo de dato que no sea una lista, es decir, un dato invalido
    >>> mostrar_lista(5)
    --------------------------------------------------
    El elemento ingresado no pertenece a una lista
    --------------------------------------------------

    Ingresa una lista que no contiene elementos de tipo diccionario
    >>> clientes = [1,2,3,4]
    >>> mostrar_lista(clientes)
    --------------------------------------------------
    La lista ingresada no contiene elementos de tipo diccionario
    --------------------------------------------------

    """
    if lista_invalida(lista):
        return

    titulo = 'LISTA\n'
    print(titulo + separador)
    for cliente in lista:
        r = ''
        for key, value in cliente.items():
            if key == 'ID':
                r = '{}:{:<6}'.format(key, value) + '|'
            else:
                r += '{:>8}:{}'.format(key, value)
                print(r)
                r = ''


def ordenar_may_men(lista):
    """
    Crea una lista, invoca la funcion ordenar_may_men para retornar una lista ordenada de mayor edad
    a menor edad.
    >>> clientes = [{'ID': 1, 'Edad': 97}, {'ID': 2, 'Edad': 20}, {'ID': 3, 'Edad': 8}, {'ID': 4, 'Edad': 98}, {'ID': 5, 'Edad': 41}, {'ID': 6, 'Edad': 13}, {'ID': 7, 'Edad': 3}, {'ID': 8, 'Edad': 42}, {'ID': 9, 'Edad': 9}, {'ID': 10, 'Edad': 67}]
    >>> ordenar_may_men(clientes)
    [{'ID': 4, 'Edad': 98}, {'ID': 1, 'Edad': 97}, {'ID': 10, 'Edad': 67}, {'ID': 8, 'Edad': 42}, {'ID': 5, 'Edad': 41}, {'ID': 2, 'Edad': 20}, {'ID': 6, 'Edad': 13}, {'ID': 9, 'Edad': 9}, {'ID': 3, 'Edad': 8}, {'ID': 7, 'Edad': 3}]
    """
    if lista_invalida(lista):
        return
    lista_ordenada = lista
    n = len(lista)
    for i in range(n-1):
        ordenado = True
        for j in range(n-i-1):
            if lista_ordenada[j]['Edad'] < lista_ordenada[j+1]['Edad']:
                ordenado = False
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
        if ordenado:
            global valido_ordenamiento
            valido_ordenamiento = True
            break

    return lista_ordenada


def mostrar_may_men(lista):
    """
    Crea una lista, invoca la funcion ordenar_may_men para retornar la lista ordenada de mayor edad
    a menor edad y por ultimo se muestra el id con mayor edad y el id con menor edad.
    >>> clientes = [{'ID': 1, 'Edad': 97}, {'ID': 2, 'Edad': 20}, {'ID': 3, 'Edad': 8}, {'ID': 4, 'Edad': 98}, {'ID': 5, 'Edad': 41}, {'ID': 6, 'Edad': 13}, {'ID': 7, 'Edad': 3}, {'ID': 8, 'Edad': 42}, {'ID': 9, 'Edad': 9}, {'ID': 10, 'Edad': 67}]
    >>> lista_ordenada = ordenar_may_men(clientes)
    >>> mostrar_may_men(lista_ordenada)
    --------------------------------------------------
    ID de la persona más joven y más vieja
    --------------------------------------------------
    La persona mas joven: 7
    La persona mas vieja: 4

    Crea una lista, NO seinvoca la funcion ordenar_may_men, por lo tanto, es invalido
    >>> clientes = generar_lista_clientes(10)
    >>> mostrar_may_men(clientes)
    --------------------------------------------------
    El ordenamiento no fue generada, por favor genere el ordenamiento
    --------------------------------------------------
    """
    if lista_invalida(lista):
        return

    elif not valido_ordenamiento:
        mensaje = '\nEl ordenamiento no fue generada, por favor genere el ordenamiento\n'
        print(separador + mensaje + separador)
        return

    titulo = '{}'.format('\nID de la persona más joven y más vieja\n')
    r = '\n{:<22}'.format('La persona mas joven: ' + str(lista[-1]['ID'])) + '\n'
    r += '{}'.format('La persona mas vieja: ' + str(lista[0]['ID']))
    print(separador + titulo + separador + r)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
