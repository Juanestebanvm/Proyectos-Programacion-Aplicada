#Este Ejercicio Vale una unidad en la Calificacion del Primer Corte
#Codigo Usando try except
#Juan Vargas 20232005027
import ClaseOperaciones

try:
    obj = ClaseOperaciones.OperacionesBasicas()
    obj.ingresarValores()

    # Suma
    obj.sumar(obj.getVal(), obj.getVal2())
    print("Suma: ", obj.getR())

    # Resta
    obj.restar(obj.getVal(), obj.getVal2())
    print("Resta: ", obj.getR())

    # División
    obj.dividir(obj.getVal(), obj.getVal2())
    print("División: ", obj.getR())

    # Multiplicación
    obj.multiplicar(obj.getVal(), obj.getVal2())
    print("Multiplicación: ", obj.getR())

except Exception as e:
    print("Ocurrió un error inesperado:", e)
