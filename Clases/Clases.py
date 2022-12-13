__author__ = 'Alexander Gareca'

from math import pi

separador = '-' * 60


class Circulo:
    """
    Crea el objeto con un valor aceptado
    >>> circulo_1 = Circulo(10)

    No crea el objeto porque el valor ded radio es invalido
    >>> circulo_2 = Circulo(-1)
    Traceback (most recent call last):
        ...
    Exception: El numero del radio ingresado es menor a 0 (cero)
    """

    def __init__(self, radio):
        if radio <= 0:
            raise Exception('El numero del radio ingresado es menor a 0 (cero)')
        else:
            self.__radio = radio

    def __mul__(self, n):
        """
        Crea un objeto
        >>> circulo_1 = Circulo(10)

        Crea el segundo objeto con un valor de radio de n * Circulo, el valor de n es valido
        >>> circulo_2 = circulo_1 * 10

        Crea el tercer objeto con un valor de radio de n * Circulo, el valor de n NO es valido
        >>> circulo_3 = circulo_1 * -1
        ------------------------------------------------------------
        El valor númerico n ingresado no es valido
        Por favor ingresar un valor que sea mayor a 0 (cero)
        ------------------------------------------------------------
        Ingresar valor de n valido:
        """
        while n <= 0:
            mensaje = 'El valor númerico n ingresado no es valido\n'
            mensaje += 'Por favor ingresar un valor que sea mayor a 0 (cero)'
            print(separador + '\n' + mensaje + '\n' + separador)
            n = float(input("Ingresar valor de n valido:"))

        radio_2 = self.__radio * n
        return Circulo(radio_2)

    def set_radio(self, radio):
        """
        Crea un objeto
        >>> circulo_1 = Circulo(10)

        Modifica el valor del radio por un numero ingresado valido, retorna True
        >>> circulo_1.set_radio(20)
        True

        Modifica el valor del radio por un numero invalido, retorna False
        >>> circulo_1.set_radio(-1)
        ------------------------------------------------------------
        Error
        El número de radio ingresado es menor o igual a 0 (cero)
        ------------------------------------------------------------
        False
        """
        if radio <= 0:
            mensaje = '\nError\n'
            mensaje += 'El número de radio ingresado es menor o igual a 0 (cero)\n'
            print(separador + mensaje + separador)
            return False

        self.__radio = radio
        return True

    def get_radio(self):
        """
        Crea el objeto
        >>> circulo_1 = Circulo(20)

        Retorna el valor del radio
        >>> circulo_1.get_radio()
        20
        """
        return self.__radio

    def perimetro(self):
        """
        Crea el objeto
        >>> circulo_1 = Circulo(10)

        Retorna el perimetro
        >>> circulo_1.perimetro()
        62.83
        """
        p = round(((self.__radio * 2) * pi), 2)
        return p

    def area(self):
        """
        Crea el objeto
        >>> circulo_1 = Circulo(10)

        Retorna el area
        >>> circulo_1.area()
        314.16
        """
        a = round(((self.__radio ** 2) * pi), 2)
        return a


    def to_string(self):
        """
        Crea el objeto
        >>> circulo_1 = Circulo(10)

        Imprime por pantalla el valor del radio, perimetro y area
        >>> circulo_1.to_string()
        'Radio: 10 cm        |    Perimetro: 62.83 cm      |    Area: 314.16 cm²'
        """

        r = '{:<20}{:<5}'.format('Radio: ' + str(self.__radio) + ' cm',  '|')
        r += '{:<25}{:<5}'.format('Perimetro: ' + str(self.perimetro()) + ' cm', '|')
        r += '{}'.format('Area: ' + str(self.area()) + ' cm²')
        return r

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
