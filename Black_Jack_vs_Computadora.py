#Importar random para elegir al azar dos cartas
import random

#Crear jugador
def jugador():
    puntos_jugador = 1000
    nombre = input("Id del jugador: ")
    return puntos_jugador, nombre

#Crear funcion que cree el mazo
def crear_mazo():
# Crear matriz del mazo
   mazo = []
   for palo in ["Corazones", "Diamantes", "Treboles", "Pica"]: #Definir los palos
       for valor in range (2,11): #cartas del 2 al 10 con el valor de la misma carta
           mazo.append(str(valor) + " de " + palo)
           for comodines in ["J", "Q", "K", "A"]: #Cartas especiales
            mazo.append(comodines + " de "  + palo)
   random.shuffle(mazo)
   return mazo

def valor_mano(mano): #Función para definir el valor de la mano
    valor_mano = 0
    valor_ases = 0
    for carta in mano:
        valor_carta = carta.split(' ')[0]
        if valor_carta in ["J", "Q", "K"]: #Sumar el valor de los comodines con valor de 10 puntos
            valor_mano += 10
        elif valor_carta == "A": #Sumar para los ases con valor de 11 puntos
            valor_mano += 11
        else: #Sumar el valor de la carta comun
            valor_mano += int(valor_carta)
    
    while valor_mano > 21 and valor_ases > 0:
        valor_mano -= 10
        valor_ases -= 1
        
    return valor_mano

#Función para elegir cartas y decidir si se quiere seguir jugando o no
def partida(mazo):
    
    mano_jugador = [mazo.pop(), mazo.pop()] #Saca dos cartas del mazo
    mano_computadora = [mazo.pop(), mazo.pop()] #Saca dos cartas del mazo
    
    #Turno del jugador
    print(f"Tu mano es {mano_jugador} con valor {valor_mano(mano_jugador)}") #Mostrar mano
    
    
    while True:
        v = input("¿Quieres otra carta? si/no ").lower() #Turno del jugador
        if v == "si":
            mano_jugador.append(mazo.pop())
            print("Tu mano es:", mano_jugador, "con valor", valor_mano(mano_jugador))
            if valor_mano(mano_jugador) > 21:
                print("Te pasaste de 21. Perdiste")
                return -1
        elif v == "no":
            break
        else:
            print("Opción no válida.")
    
    #Turno de la computadora
    while valor_mano(mano_computadora) < 17:
        mano_computadora.append(mazo.pop())
        
    print(f"Mano de la computadora {mano_computadora} valor:  {valor_mano(mano_computadora)}")
        
    valor_jugador = valor_mano(mano_jugador)
    valor_computadora = valor_mano(mano_computadora)
    
    if valor_computadora > 21:
        print("La computadora tiene más de 21 puntos, tu ganas!!!")
        return 1
    elif valor_computadora < valor_jugador:
        print("Ganaste!!!!")
        return 1
    elif valor_jugador == valor_computadora:
        print("Empate")
        return 0
    else:
        print("Perdiste")
        return -1

def black_jack():
    puntos_jugador, nombre = jugador()
    print (f"{nombre} tienes {puntos_jugador} puntos")
    while puntos_jugador > 0 and puntos_jugador<10000:
        print(f"Puntos actuales: {puntos_jugador}")
        mazo = crear_mazo()
        while True:
            apuesta = int(input("¿Cuánto quieres apostar? "))
            if apuesta > puntos_jugador or apuesta <= 0:
                print("Apuesta no válida. Debes apostar una cantidad positiva que no exceda tus puntos.")
            else:
                break
        
        resultados_de_la_ronda = partida(mazo)
        
        if resultados_de_la_ronda == 1:
            puntos_jugador += apuesta
        elif resultados_de_la_ronda == -1:
            puntos_jugador = puntos_jugador - apuesta
        elif resultados_de_la_ronda == 0:
            puntos_jugador = puntos_jugador
            
    if puntos_jugador >= 10000:
        print(f"{nombre} le ganaste a la computadora :)")
    elif puntos_jugador <= 0:
        print(f"{nombre} perdiste :(")

def menu():
    print("1. Prueba información jugador")
    print("2. Prueba crear mazo")
    print("3. Jugar black jack")
    print("4. Salir")

def pruebas():
    while True:
        menu()
        v = int(input("¿Qué quieres hacer? "))
        if v==1:
            puntos_jugador, nombre = jugador()
            print (f"{nombre} tienes {puntos_jugador} puntos")
        elif v==2:
            mazo = crear_mazo()
            print(mazo)
        elif v==3:
            black_jack()
        elif v==4:
            print("Saliendo...")
            break
        else:
            print("Valor no valido")
            
pruebas() 