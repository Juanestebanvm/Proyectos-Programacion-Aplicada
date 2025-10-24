#Este Ejercicio Vale una unidad y dos decimas en la Calificacion del Primer Corte
#Codigo Usando try except
#Juan Vargas 20232005027
import ClaseOperaciones
import ClaseAreas

try:
    obj = ClaseOperaciones.OperacionesBasicas()
    obj.ingresarValores()

    # --- Operaciones matemáticas ---
    obj.sumar(obj.getVal(), obj.getVal2())
    print("Suma:", obj.getR())

    obj.restar(obj.getVal(), obj.getVal2())
    print("Resta:", obj.getR())

    obj.dividir(obj.getVal(), obj.getVal2())
    print("División:", obj.getR())

    obj.multiplicar(obj.getVal(), obj.getVal2())
    print("Multiplicación:", obj.getR())

    obj.potenciar(obj.getVal(), obj.getVal2())
    print("Potenciación:", obj.getR())

    obj.raiz_cuadrada(obj.getVal())
    print("Raíz cuadrada del primer número:", obj.getR())

    if obj.getVal() >= 0 and obj.getVal() == int(obj.getVal()):
        obj.factorial(int(obj.getVal()))
        print("Factorial del primer número:", obj.getR())
    else:
        print("Factorial: Error, el número debe ser entero y no negativo")

    # --- Cálculo de áreas geométricas ---
    print("\n--- Cálculo de Áreas Geométricas ---")
    area = ClaseAreas.AreasGeometricas()

    # Cuadrado
    lado = float(input("Ingrese el lado del cuadrado: "))
    area.area_cuadrado(lado)
    print("Área del cuadrado:", area.getResultado())

    # Rectángulo
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area.area_rectangulo(base, altura)
    print("Área del rectángulo:", area.getResultado())

    # Circunferencia
    radio = float(input("Ingrese el radio de la circunferencia: "))
    area.area_circunferencia(radio)
    print("Área de la circunferencia:", area.getResultado())

    # Triángulo rectángulo
    base_t = float(input("Ingrese la base del triángulo rectángulo: "))
    altura_t = float(input("Ingrese la altura del triángulo rectángulo: "))
    area.area_triangulo_rectangulo(base_t, altura_t)
    print("Área del triángulo rectángulo:", area.getResultado())

except Exception as e:
    print("Ocurrió un error inesperado:", e)
