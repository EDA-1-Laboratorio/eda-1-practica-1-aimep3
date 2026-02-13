def crear_mensaje():
    print("\n--- CIFRADO ---")
    # Pedimos los datos y los convertimos a enteros (int)
    ren = int(input("Ingresar el tamaño de la escítala (Renglones): "))
    col = int(input("Ingresar el tamaño de la escítala (Columnas/Caras): "))
    
    # En Python no necesitamos declarar el tamaño del texto antes, pero
    # para seguir la lógica del ejercicio, pedimos el texto.
    texto = input("Escriba el texto a cifrar (sin espacios): ")

    # Creamos una matriz vacía llena de caracteres vacíos con 
    matriz = [['' for _ in range(col)] for _ in range(ren)]
    
    # --- PASO 1: Llenar la matriz (Escribir en la vara) ---
    # Llenamos fila por fila (orden normal de lectura/escritura)
    k = 0 # Índice para recorrer el texto lineal, es el contador para iniciar
    for i in range(ren):           # Para cada renglón
        for j in range(col):       # Para cada columna
            if k < len(texto):     # Si aún quedan letras en el texto (que tan largo es el mensaje)
                matriz[i][j] = texto[k] #Se va poniendo en la matriz
                k += 1             # Pasamos a la siguiente letra
            else:
                matriz[i][j] = ' ' # Rellenamos con espacio si sobra lugar

    print("El texto cifrado es:")
    
    # --- PASO 2: Leer para cifrar (Desenrollar la tira) ---
    # Leemos columna por columna (transposición)
    cifrado = ""
    for j in range(col):           # Primero se cuentan las columnas
        for i in range(ren):       # Aquí se van contando los renglones de cada columna
            cifrado += matriz[i][j] # Agregamos la letra al resultado
            
    print(cifrado)
    print("\n")

def descifrar_mensaje():
    print("\n--- DESCIFRADO ---")
    ren = int(input("Ingresar el tamaño de la escítala (Renglones original): "))
    col = int(input("Ingresar el tamaño de la escítala (Columnas original): "))
    
    texto_cifrado = input("Escriba el texto cifrado: ")

    # Creamos la matriz vacía nuevamente
    matriz = [['' for _ in range(col)] for _ in range(ren)]
    
    # Paso 1: Reconstruimos la matriz
    # El texto cifrado viene en orden vertical (columnas).
    # Así que llenamos la matriz columna por columna.
    k = 0
    for j in range(col):           # Como arriba, primero van las COLUMNAS
        for i in range(ren):       # Después los RENGLONES
            if k < len(texto_cifrado):
                matriz[i][j] = texto_cifrado[k]
                k += 1
            else:
                matriz[i][j] = ' '

    print("El texto descifrado es:")

    # Paso 2: Leer el mensaje original
    # Ahora leemos fila por fila (como leemos normalmente)
    mensaje_original = ""
    for i in range(ren):           # Primero van los RENGLONES
        for j in range(col):       # Después las COLUMNAS
            mensaje_original += matriz[i][j]

    print(mensaje_original)
    print("\n")

def main():
    while True: # Bucle infinito
        print("\n\t*** ESCÍTALA ESPARTANA ***")
        print("1) Crear mensaje cifrado (Cifrar).")
        print("2) Descifrar mensaje.")
        print("3) Salir.")
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            crear_mensaje()
        elif opcion == 2:
            descifrar_mensaje()
        elif opcion == 3:
            print("Saliendo del programa...")
            break # Rompe el ciclo while y termina el programa
        else:
            print("Opción no válida. Intente de nuevo.")
main()