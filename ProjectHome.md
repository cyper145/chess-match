This project involves the implementation of a chess engine, along with a graphical interface and visualization capabilities and creating PGN files (standard format for reading chess games.). The game engine is written in C and is designed based on three modules or stages:
> -Moves Generator: The first stage that the engine performs. Given a position of the board, generates all possible combinations of spins with a defined depth.

> -Evaluation function: It is the most complex stage and the most important. Evaluate each of the previously generated plays and assesses them based on certain criteria such as: material, king safety, activity room, control center, etc.

> - Pruning Alpha/Beta  algorithm: Once you have valued all generated moves, discard all those with lower valuation. That is all inferior moves are discarded and allowed a small number of branches to analyze in more depth.

Once the engine has completed these three steps, and obtained a small number of sequences of the best moves are repeated several times again the three stages until finally the move for which the valuation is higher is chosen.

The GUI is developed in python + gtk (possibly switching to python + pygame) and has a basic funcionalides chess as:
- Board with pieces
- Annotate moves in algebraic form
- Buttons for forward / back a play
- Buttons to jump to the end / beginning of the game
- Watch for each player

//

Este proyecto consiste en la implementación de un motor de ajedrez, junto con una interfaz grafica y funcionalidades de visualización y creación de archivos PGN (formato standar para lectura de partidas de ajedrez.).
El motor de juego esta escrito en el lenguaje C y esta diseñado en base a tres módulos o etapas que son las siguientes:
-Generador de jugadas: Es la primera de las etpas que realiza el motor. Dada una posición de una partida, genera todas las posibles combinaciones de jugadas con una profundidad definida.
- Función de evaluación: Es la mas compleja de las etapas y la más importante. Evalúa cada una de las jugadas anteriormente generadas y las valora en base a ciertos criterios de juego como ser: material, seguridad del rey, actividad de las piezas, control del centro, etc.
- Algoritmo de poda Alfa/Beta: Una vez que se han valuado todas las jugadas generadas, se descartan todas aquellas con menor valoración. Es decir se descartan todas las jugadas inferiores y se dejan un número pequeño de ramas para analizar con mas profundidad.

Una vez que el motor ha realizado estas tres etapas, y ha obtenido un numero pequeño de secuencias de las mejores jugadas, se repiten varias veces de nuevo las tres etapas hasta que finalmente se elije la jugada para la cual la valoración es mayor.

La interfaz gráfica está desarrollada en python + gtk (posiblemente se cambie a python + pygame) y cuenta con las funcionalides básicas de un juego de ajedrez como ser:
- Tablero con piezas
- Anotación de jugadas en formato algebraico
- Botones para avanzar/volver una jugada
- Botones para ir al final/principio del partido
- Reloj para cada jugador