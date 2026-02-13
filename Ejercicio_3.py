import time
import os
import copy # Necesario para copiar matrices correctamente

FILAS = 10
COLS = 10

# Inicializamos el mundo vacío (lleno de ceros)
mundo = [[0 for _ in range(COLS)] for _ in range(FILAS)]

def inicializar_mundo():
    # Limpiamos todo a 0 (por si acaso se llama de nuevo)
    for i in range(FILAS):
        for j in range(COLS):
            mundo[i][j] = 0

    # Es donde van a estar los # en un inicio
    mundo[1][2] = 1
    mundo[2][3] = 1
    mundo[3][1] = 1
    mundo[3][2] = 1
    mundo[3][3] = 1

def imprimir_mundo():
    print("\nEstado Actual:")
    for i in range(FILAS):
        linea = ""
        for j in range(COLS):
            # Usamos '#' si es 1, '.' si es 0
            caracter = '#' if mundo[i][j] == 1 else '.' 
            linea += caracter + " " #Aqui se arman las filas 
        print(linea)
    print("-" * 20) #solo es una linea al final de guiones

def contar_vecinos(f, c):
    vecinos = 0
    
    # Recorremos un cuadro de 3x3 alrededor de la celda (f, c)
    # Desde f-1 hasta f+1 para que recorra todos
    for i in range(f - 1, f + 2):
        # Desde c-1 hasta c+1 para que recorra todos
        for j in range(c - 1, c + 2):
            
            # 1. Verificar que NO nos salgamos de los bordes del mapa
            if i >= 0 and i < FILAS and j >= 0 and j < COLS:
                
                # 2. Verificar que NO estemos contando a la propia celda central
                if not (i == f and j == c):
                    
                    # 3. Sumar si el vecino está vivo (vale 1)
                    if mundo[i][j] == 1:
                        vecinos += 1
    return vecinos

def siguiente_generacion():
    # Creamos una matriz vacía para el futuro 
    global mundo
    siguiente_mundo = [[0 for _ in range(COLS)] for _ in range(FILAS)]

    for i in range(FILAS):
        for j in range(COLS):
            # Paso crucial: Contar cuántos amigos tiene la celda actual
            vecinos = contar_vecinos(i, j)
            # Si la celda está VIVA actualmente
            if mundo[i][j] == 1:
                # REGLA 1 (Soledad): < 2 vecinos -> Muere
                # REGLA 2 (Sobrepoblación): > 3 vecinos -> Muere
                if vecinos < 2 or vecinos > 3:
                    siguiente_mundo[i][j] = 0
                else:
                    # REGLA 3 (Estabilidad): 2 o 3 vecinos -> Vive
                    siguiente_mundo[i][j] = 1
            
            # Si la celda está MUERTA actualmente
            else:
                # REGLA 4 (Reproducción): Exactamente 3 vecinos -> Nace
                if vecinos == 3:
                    siguiente_mundo[i][j] = 1
                else:
                    siguiente_mundo[i][j] = 0
    
    # Actualizamos el mundo real con el calculado
    # Usamos deepcopy para asegurarnos de pasar los valores al nuevo
    
    mundo = copy.deepcopy(siguiente_mundo)

def main():
    inicializar_mundo()
    iteraciones = 10

    for k in range(iteraciones):
        imprimir_mundo()
        siguiente_generacion()
        time.sleep(0.2) # Pausa de medio segundo para ver la animación
main()