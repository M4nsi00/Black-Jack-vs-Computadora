"Contexto"


El proyecto será el juego "BlackJack", un juego de cartas en el que se tiene el objetivo de ganarle a la casa (Computadora"). Para ganarle a la computadora el jugador debe de tener o estar cerca a 21 puntos sumados en sus cartas, si el jugador tiene más puntos pierde automaticamente, si la computadora esta más cerca de los 21 puntos está gana. 
A diferencia de la versión clásica aquí el jugador va a tener una cantidad inicial de puntos, en este caso 1000 puntos, y tiene el objetivo de conseguir 10,000 puntos, cada ronda puede decidir apostar cierta cantidad de puntos y si gana duplica el valor apostado; Si pierde e jugador perdera los puntos apostados. El juego termina cuado el jugador consigue 10,000 puntos o pierde todos sus puntos.

Álgoritmo:

Entrada: Cantidad de puntos para apostar, Semilla aleatoria para barajar las cartas

Proceso: Pedir cantidad de puntos a apostar

Crear una baraja de 52 cartas y crear mazoz para el jugador y la computadora

Repartir dos cartas al jugador

Preguntar si el jugador quiere otra carta o deja ahí su mazo

Si el jugador elige otra carta y la suma de los puntos de las cartas es mayor a 21 imprimr "La casa gana"

Si el juagodr elige otra carta y la suma de puntos es menor a 21 cartas preguntar si quiere otra carta, en el caso que quiera otra carta verificar el paso anterior y este

Si el jugador decide quedarse con solo dos cartas, empezar a repartir cartas a la computadora

Si la computadora esta más cerca a los 21 puntos o tiene 21 puntos imprimir "La casa gana"

Si el jugador esta más cerca a los 21 puntos o tiene 21 puntos imprimir "El jugador gana"

Si tanto el jugador como la computadora obtuvieron el mismo resultado imprimr "Es un empate"

Si el jugador gano duplicar los puntos apostados, si perdio quitarle los puntos apostados, si fue un empate devolver los puntos apostados

Se repite este proceso hasta que el jugador pierda todos sus puntos o llegue a los 10,000 puntos, si pierde imprimir "Perdio la partida", si el jugador gana poner "Felicidades ganaste"


Salida: Mensaje, suma o perdida de puntos
