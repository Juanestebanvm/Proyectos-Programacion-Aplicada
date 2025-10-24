class OperacionesBasicas:
    def __init__(self):
        self.val = 0
        self.val2 = 0
        self.r = 0
    
    # Métodos getter y setter
    def getVal(self):
        return self.val
    
    def setVal(self, valor):
        self.val = valor

    def getVal2(self):
        return self.val2
    
    def setVal2(self, valor):
        self.val2 = valor

    def getR(self):
        return self.r
    
    def setR(self, valor):
        self.r = valor
    
    # Operaciones básicas
    def sumar(self, a, b):
        self.r = a + b
    
    def restar(self, a, b):
        self.r = a - b

    def dividir(self, a, b):
        try:
            self.r = a / b
        except ZeroDivisionError:
            self.r = "Error: División por 0"

    def multiplicar(self, a, b):
        self.r = a * b

    def potenciar(self, base, exponente):
     resultado = 1
     if exponente == 0:
        resultado = 1
     elif exponente > 0:
        for _ in range(int(exponente)):
            resultado *= base
     else:
        for _ in range(abs(int(exponente))):
            resultado *= base
        resultado = 1 / resultado
     self.r = resultado

    def raiz_cuadrada(self, numero):
     if numero < 0:
        self.r = "Error: No se puede calcular la raíz de un número negativo"
     else:
        aproximacion = numero / 2
        for _ in range(20):
            aproximacion = (aproximacion + numero / aproximacion) / 2
        self.r = aproximacion

    def factorial(self, numero):
     if numero < 0:
        self.r = "Error: No existe factorial de números negativos"
     elif numero == 0 or numero == 1:
        self.r = 1
     else:
        resultado = 1
        for i in range(2, int(numero) + 1):
            resultado *= i
        self.r = resultado

    # Entrada de valores
    def ingresarValores(self):
        while True:
            try:
                v1 = float(input("Ingrese el primer número: "))
                self.setVal(v1)
                break
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        
        while True:
            try:
                v2 = float(input("Ingrese el segundo número (diferente de 0): "))
                if v2 == 0:
                    print("Error: No se puede dividir entre 0. Intente de nuevo.")
                else:
                    self.setVal2(v2)
                    break
            except ValueError:
                print("Error: Debe ingresar un número válido.")
