"Contexto"

El proyecto será el juego "BlackJack", un juego de cartas en el que se tiene el objetivo de ganarle a la casa (Computadora"). Para ganarle a la computadora el jugador debe de tener o estar cerca de 21 puntos sumados en sus cartas, si el jugador tiene más puntos pierde automáticamente, si la computadora está más cerca de los 21 puntos está gana. A diferencia de la versión clásica aquí el jugador va a tener una cantidad inicial de puntos, en este caso 1000 puntos, y tiene el objetivo de conseguir 10,000 puntos, cada ronda puede decidir apostar cierta cantidad de puntos y si gana duplica el valor apostado; Si pierde el jugador perderá los puntos apostados. El juego termina cuando el jugador consigue 10,000 puntos o pierde todos sus puntos.

Álgoritmo:

Entrada: 

1.	Pedir cantidad de puntos a apostar.
   
2.	Usar el mazo para repartir dos cartas al jugador y a la computadora.
   
3.	Preguntar si el jugador quiere otra carta o se queda con el valor de las primeras dos cartas.
   
4.	Si el jugador elige otra carta y la suma de puntos es mayor a 21 se imprime el mensaje “La casa gana” y se restan los puntos apostados por el jugador de sus puntos totales.
   
5.	Si la suma de puntos no es mayor a 21 se pregunta al jugador si quiere otra carta y se repite el paso anterior.

6.	Si el jugador decidió no agarrar una tercera carta es turno de la computadora.

7.	Si la computadora tiene 21 puntos o está más cerca que el jugador de los 21 puntos se imprime el mensaje “La casa gana” y se le restan los puntos apostados al jugador.

8.	Si el jugador esta más cerca de los 21 puntos o si tiene 21 puntos se imprime el mensaje “El jugador gana” y se le suma el doble de los puntos apostados.

9.	Si tanto el jugador como la computadora obtuvieron 21 puntos o la misma cantidad de puntos se imprime el mensaje “Fue un empate” y se devuelven los puntos apostados por el jugador.

10.	Se repite este proceso hasta que el jugador se quede sin puntos, en ese caso se imprime el mensaje “Fin del juego”, si el jugador obtiene la meta de los 10,000 puntos se imprime el mensaje “Felicidades has ganado”

Salida: Mensaje, suma o perdida de puntos

¿Cómo usar?

1. Antes que nada recomiendo instalar python para poder correr el programa, puedes usar el siguiente link para eso: https://www.youtube.com/watch?v=yXoiFeK4_Sk

2. Descargar la carpeta Black-Jack-vs-Computador.zip

Nota (Si descargas solo el archivo de Blacj-Jack-vs-Computadora.py no va a funcionar el juego

4. Ejecutar el archivo, se debería de poder abrir en python

5. Usar el archivo es sencillo, puedes elegir entre empezar a jugar o hacer alguna prueba del código.

6. Dsifruta del juego :)



Veni Vidi Vici
