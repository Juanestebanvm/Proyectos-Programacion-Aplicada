while True:
    entrada = input("Ingresa un número para saber si es par o impar (o 'exit' para salir): ")
    if entrada.lower() == 'exit':
        print("Saliendo del programa...")
        break
    
    try:
        numero = int(float(entrada))  # Convertir a float y luego a int por si ingresan decimales
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")