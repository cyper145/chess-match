#ifndef _PODA_H
#define _PODA_H

#include "var_data.h"


int peonAtacaCasilla(casilla peon,casilla cas,int color);
int torreAtacaCasilla(casilla torre,casilla cas,Tablero tab);
int alfilAtacaCasilla(casilla alfil, casilla cas, Tablero tab);
int damaAtacaCasillla(casilla dama, casilla cas, Tablero tab);
int caballoAtacaCasilla(casilla caballo,casilla cas);

#endif
