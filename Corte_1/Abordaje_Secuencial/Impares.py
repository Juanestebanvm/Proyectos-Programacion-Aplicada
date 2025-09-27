#Este Ejercicio Vale una Decima en la Calificacion del Primer Corte
#Juan Vargas 20232005027
while True:
    try:
        entrada = input("Introduce un número entero (o deja vacío para salir): ")
        if not entrada:
            break
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} es PAR")
        else:
            print(f"{numero} es IMPAR")

    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. ¡Adiós!")
        break
