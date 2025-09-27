import time

while True:
    entrada = input("Introduce un número para verificar si es primo (o 'exit' para salir): ")
    if entrada.lower() == 'exit':
        print("Saliendo del programa...")
        break

    try:
        num = int(entrada)
        if num < 1:
            print("Por favor, ingresa un número entero positivo.")
            continue
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número entero.")
        continue

    inicio = time.time()

    conta = 0
    for n in range(1, num + 1):
        if num % n == 0:
            conta += 1

    fin = time.time()

    if conta == 2:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} NO es un número primo.")

    print(f"Tiempo de cálculo: {(fin - inicio)*1000:.2f} ms\n")
