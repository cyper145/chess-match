



#ifndef _FUNCUTILIDAD_H
#define _FUNCUTILIDAD_H

#include "var_data.h"


void valuar_utilidad(nodo inicial, int prof);
int valoracion(Tablero tab);
int actividad_caballo(Tablero tab,int fila,int columna,int turno);
int actividad_torre(Tablero tab,int fila,int columna,int turno);
int actividad_alfil(Tablero tab,int fila,int columna,int turno);
int posicion_torre(Tablero tab,int fila,int columna,int turno );
int posicion_caballo(Tablero tab,int fila,int columna,int turno );
int posicion_alfil(Tablero tab,int fila,int columna,int turno );

#endif
