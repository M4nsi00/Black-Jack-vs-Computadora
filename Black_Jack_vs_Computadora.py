#Importar random para elegir al azar dos cartas
import random

#Crear jugador
def jugador():
    puntos_jugador = 1000
    nombre = input("Id del jugador: ")
    print (nombre, "tienes", puntos_jugador, "puntos")
'''
Caso de prueba nombre
Id del jugador: Mansi
Mansi tienes  1000 puntos
'''
#Crear funcion que cree las cartas
def cartas():
    # Usar random para elegir un número de carta, asignar los valores de J, Q, K, A
    carta = random.randint(1, 13)
    if carta == 11:
        carta = "J"
    elif carta == 12:
        carta = "Q"
    elif carta == 13:
        carta = "K"
    elif carta == 1:
        carta = "A"
    
    # Usar random para elegir uno de los 4 palos de cartas
    palo = random.randint(1, 4)
    if palo == 1:
        palo = "Treboles"
    elif palo == 2:
        palo = "Picas"
    elif palo == 3:
        palo = "Corazones"
    elif palo == 4:
        palo = "Diamantes"
    
    # Imprimir carta
    print(carta, "de", palo)
    
    # Definir el valor de cada carta
    valor_carta = 0
    if carta == "J" or carta == "Q" or carta == "K":
        valor_carta = 10
    elif carta == "A":
        valor_carta = 11
    else:
        valor_carta = carta
    # Aquí carta ya es un número
    # Retornar el valor de la carta
    return valor_carta
'''
Caso de prueba carta
8 de diamantes
K de Picas
'''

#Función para elegir cartas y decidir si se quiere seguir jugando o no
def partida():
    jugador()
    carta1 = cartas()
    carta2 = cartas()
    suma_cartas = carta1 + carta2
    print("Suma ", suma_cartas)
   #Ciclo para terminar una partida si el jugador tiene más de 21 puntos o en el caso que tenga menos de 21 preguntar si quiere otra carta 
    while True:
        if suma_cartas >= 21:
            print("Fin de la partida")
            break

        respuesta = input("¿Quieres otra carta? (si/no) ")
        if respuesta.lower() == "si":
            carta3 = cartas()
            suma_cartas += carta3
            print("Suma ", suma_cartas)
        elif respuesta.lower() == "no":
            print("Fin de la partida")
            break
        else:
            print("Respuesta no válida. Por favor, responde con 'si' o 'no'")
'''
Caso de prueba partida
Id del jugador: Mansi
Mansi tienes 1000 puntos
8 de Picas
J de Treboles
Suma 18
¿Quieres otra carta? (si/no) si
5 de Corazones
Suma 23
Fin de la partida
'''

def menu():
    print("1. Prueba función jugador")
    print("2. Prueba función crear una carta")
    print("3. Prueba función jugar una partida (Probar todas las funciones)")
    print("4. Salir")
def prueba():
    while True:
        menu()
        respuesta = int(input("¿Qué quieres hacer? "))
        if respuesta == 1:
            jugador()
        elif respuesta == 2:
            cartas()
        elif respuesta == 3:
            partida()
        elif respuesta == 4:
            print("Saliendo")
            break
        else:
            print("Valor no valido")
prueba()