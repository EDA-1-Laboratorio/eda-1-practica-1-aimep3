def generar_espiral():
    print("--- GENERADOR DE MATRIZ ESPIRAL ---")
    try:
        n = int(input("Ingrese el tamaño N de la matriz: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    # Creamos una matriz de N x N llena de ceros
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    valor = 1  # El número con el que vamos a empezar
    
    # Definimos los 4 límites de nuestra matriz
    top = 0             # Límite superior (fila 0)
    bottom = n - 1      # Límite inferior (fila N-1)
    left = 0            # Límite izquierdo (columna 0)
    right = n - 1       # Límite derecho (columna N-1)

    # El bucle principal: seguimos mientras no llenemos todas las casillas
    while valor <= n * n:
        
        # Recorrer de IZQUIERDA a DERECHA (llenando la fila superior actual)
        # El rango en python va hasta limite - 1, por eso ponemos right + 1
        for i in range(left, right + 1): #Vamos a recorrer todos los espacios de derecha a izquierda uno por uno, sumando uno, y el +1 para que si llegue al numero que queremos
            matriz[top][i] = valor #top es la fila, esta fija, mientras que por el for, i si se mueve hasta llenar la fila
            valor += 1
        top += 1  # La primera fila ya está llena asi que bajamos el techo

        # Recorrer de ARRIBA a ABAJO (llenando la columna derecha actual)
        for i in range(top, bottom + 1):
            matriz[i][right] = valor
            valor += 1
        right -= 1 # La columna derecha ya está llena, movemos la pared derecha

        # Recorrer de DERECHA a IZQUIERDA (llenando la fila inferior actual)
        if top <= bottom: # Verificamos si aún hay filas válidas
            # range(inicio, fin, paso). -1 significa ir hacia atrás.
            for i in range(right, left - 1, -1):
                matriz[bottom][i] = valor
                valor += 1
            bottom -= 1 # La fila inferior está llena, subimos el piso

        # 4. Recorrer de ABAJO a ARRIBA (llenando la columna izquierda actual)
        if left <= right: # Verificamos si aún hay columnas válidas
            for i in range(bottom, top - 1, -1):
                matriz[i][left] = valor
                valor += 1
            left += 1 # La columna izquierda está llena, movemos la pared izquierda hacia adentro

    imprimir_matriz(n, matriz)

def imprimir_matriz(n, matriz):
    print(f"\n--- Matriz Espiral de {n}x{n} ---")
    for i in range(n):
        for j in range(n):
            # Usamos :4d para que cada número ocupe 4 espacios y se vea alineado
            print(f"{matriz[i][j]:4d}", end=" ") #El end es para que se vea cuadrado y no como lista
        print() # Salto de línea al terminar cada fila
generar_espiral()