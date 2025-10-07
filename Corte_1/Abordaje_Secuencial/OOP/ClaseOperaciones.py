class OperacionesBasicas:
    def __init__(self):
        self.val = 0
        self.val2 = 0
        self.r = 0
    
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
