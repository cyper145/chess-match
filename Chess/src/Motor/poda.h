#ifndef _PODA_H
#define _PODA_H

#include "var_data.h"

long int cont_free;
long int cont_f;

void poda(nodo nod);
void acomodar_minimax(nodo nod, int prof);
void preseleccion(nodo nod);
void preselect(nodo nod,int max);
void borrar_all_hijos(nodo nod);

#endif
