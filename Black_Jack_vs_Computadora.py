#importamos el valor random para usar al repartir cartas
import random

#puntos iniciales del jugador
puntos_jugador = 1000
#Checamos si el valor esta ajustado
print (puntos_jugador)

#Cree una dunción para el maso, pero necesita el uso de matrices para un mejor funcionamiento
#Función para crear un maso de cartas
def crear_maso():
    # Cantidad de cartas sin contar los comodines (JOKER)
    maso = ""
    #Valor de los 4 palos
    for palo in ("Corazones", "Diamantes", "Tréboles", "Picas"):
        #Valores del 2 al 10, se termina en 11 para contar el valor 10
        for valor in range (2,11):
            print(str(valor) + " de " + palo)
        #Valores de A,J,Q,K
        for caras in ("J", "Q", "K", "A"):
            print(str(caras) + " de " + palo)

#Crear función para obtener el valor de la mano
def valor_mano(carta1, carta2, carta3=None):
    valor = 0
    aces = 0
    for carta in (carta1, carta2, carta3):
        if valor_mano in ("J", "Q", "K"):
            valor +=10
        elif valor_mano == "A":
            valor +=11
            ases +=1
        else:
            valor += int(carta1) + int(carta2)
        
        #Ajustar cuando el valor de supera 21 puntos y si hay ases
        while valor > 21 and aces:
            valor -= 10
            ases -= 1
    print("El valor de la mano es: ", valor)

#Turno del jugador
def turno_jugador(carta1, carta2):
    #Primer turno con dos cartas
    print("Tus cartas son ", carta1, carta2)
    valor_mano = 0
    
    #Calcular valor inicial de la mano
    if carta1 == "A" or carta2 == "A":
        valor_mano += 11
    elif carta1 in ("J", "Q", "K") or carta2 in ("J", "Q", "K"):
        valor_mano += 10
    else:
        valor_mano += int(carta1) + int(carta2)
    print ("Valor mano", valor_mano)
    
    #Preguntar si el jugador quiere otra carta
    while valor_mano < 21:
        mensaje = input("¿Quiéres otra carta? (si/no)")
        if mensaje == "si" or mensaje == "Si":
            nueva_carta = input("Nueva carta: ")

crear_maso()
valor_mano(2,9)