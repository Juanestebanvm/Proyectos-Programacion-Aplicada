class AreasGeometricas:
    def __init__(self):
        self.resultado = 0

    def getResultado(self):
        return self.resultado

    def setResultado(self, valor):
        self.resultado = valor

    # a. Área del cuadrado
    def area_cuadrado(self, lado):
        if lado < 0:
            self.resultado = "Error: El lado no puede ser negativo."
        else:
            self.resultado = lado * lado

    # b. Área del rectángulo
    def area_rectangulo(self, base, altura):
        if base < 0 or altura < 0:
            self.resultado = "Error: Las dimensiones no pueden ser negativas."
        else:
            self.resultado = base * altura

    # c. Área de la circunferencia (π ≈ 3.1416 sin librerías)
    def area_circunferencia(self, radio):
        if radio < 0:
            self.resultado = "Error: El radio no puede ser negativo."
        else:
            pi = 3.1416
            self.resultado = pi * (radio * radio)

    # d. Área del triángulo rectángulo
    def area_triangulo_rectangulo(self, base, altura):
        if base < 0 or altura < 0:
            self.resultado = "Error: Las dimensiones no pueden ser negativas."
        else:
            self.resultado = (base * altura) / 2
