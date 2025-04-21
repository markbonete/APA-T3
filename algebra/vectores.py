"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Mark Bonete Ventura

    Tests unitarios

    >>> Vector([1, 2, 3]) * 2
    Vector([2, 4, 6])
    >>> Vector([1, 2, 3]) * Vector([2, 4, 6])
    Vector([2, 8, 18])
    >>> Vector([1, 2, 3]) @ Vector([2, 4, 6])
    28
    >>> Vector([2, 1, 2]) // Vector([0.5, 1, 0.5])
    Vector([1.0, 2.0, 1.0])
    >>> Vector([2, 1, 2]) % Vector([0.5, 1, 0.5])
    Vector([1.0, -1.0, 1.0])
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    
    def __mul__(self, other):
        """
        Multiplicación escalar o Hadamard.

        Argumentos:
            self (Vector): un vector
            other (Vector): otro vector
        Salida:
            Vector: producto de Hadamard
        """
        if isinstance(other, (int, float, complex)):
            return Vector(x * other for x in self)
        else:
            return Vector(x * y for x, y in zip(self, other))

    __rmul__ = __mul__


    def __matmul__(self, other):
        """
        Producto escalal de dos vectores de misma longitud

        Argumentos:
            self (Vector): un vector
            other (Vector): otro vector
        Salida:
            float: producto escalar
        """
        if not isinstance(other, Vector):
            raise TypeError('La función solo funciona para vectores')
        
        if len(self) != len(other):
            raise TypeError('Los vectores deben tener la misma longitud')
        
        return sum(self * other)
    
    __rmatmul__ = __matmul__ 


    def __floordiv__(self, other):
        """
        Componente tangencial de self respecto a other

        Argumentos:
            self (Vector): un vector
            other (Vector): otro vector
        Salida:
            Vector: Componente tangencial respecto a other
        """

        return (self @ other) / (other @ other) * other
    
    def __mod__(self, other):
        """
        Componente normal de self respecto a other

        Argumentos:
            self (Vector): un vector
            other (Vector): otro vector
        Salida:
            Vector: Componente normal respecto a other
        """

        return self - self // other
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)