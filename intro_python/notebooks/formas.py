import math

class Circulo():
    """
    Círculo para analítica avanzada
    """
    def __init__(self, radio: float):
        self.radio = radio
        self.unidad_longitud = 'm'
        self.unidad_area = 'm^2'
        
    def area(self):
        """
        Calcula el área de un círculo
        
        returns: área, unidad
        """
        return math.pi * self.radio**2, self.unidad_area

    def perimetro(self):
        """
        Calcula el perímetro
        
        returns: perímetro, unidad
        """
        return 2 * math.pi * self.radio, self.unidad_longitud

    
class Cuadrado():
    """
    Cuadrado para analítica avanzada
    """
    def __init__(self, lado):
        self.lado = lado
        self.unidad_longitud = 'm'
        self.unidad_area = 'm^2'
        
    def area(self):
        """
        Calcula el área
        
        returns: área, unidad
        """
        return self.lado**2, self.unidad_area

    def perimetro(self):
        """
        Calcula el perímetro
        
        returns: perímetro, unidad
        """
        return 4 * self.lado, self.unidad_longitud

