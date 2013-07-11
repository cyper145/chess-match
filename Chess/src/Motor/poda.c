/* MOTOR DE AJEDREZ
*
* 	- Modulo de poda ALPHA-BETA con algoritmo MINIMAX
*
*
*   Autor:  Martin Alonso
*	enano.alonso@gmail.com
*/


/***********************************************************************************************
* Este modulo tiene como objetivo la reduccion del arbol de jugadas generado por el modulo de
* generacion. Para poder reducir los nodos del arbol se deben descartar las secuencia de jugadas 
* o lineas con menor valoracion. Para esto se utiliza el metodo de poda Alfa-Beta con el algoritmo
* MiniMax. Este consiste en valuar cada nodo con el menor valor de sus hijos (o el mayor en caso de
* turno negro) y elegir las mejores secuencias tomando el nodo con mayor valoracio para los turnos 
* blancos  y los con menor valoracion para los turnos negros. Asi, se va alternando en minimos y 
* maximos. De esta manera, es como ir elegiendo la mejor jugada propia y esperar la mejor jugada 
* del oponente.
*************************************************************************************************/


#define LEVEL_NODES	4

#include <stdio.h>
#include <stdlib.h>
#include "poda.h"






/***************************************************************************************************
* Por cada nodo en el arbol se eligen una cantidad (LEVEL_NODES) de hijos de acuerdo al algoritmo
* MiniMax. Los demas hijos son descartados.
* El algoritmo MiniMax basicamente espera o busca la mejores jugadas del oponente. Es decir, si el
* turno del nodo padre es blanco, se elegiran las [LEVEL_NODES] mejores jugadas negras.
* Luego de la poda, el ultimo nivel del arbol debe quedar con una cantidad de nodos igual a
* LEVEL_NODES elvado a DEEP. 
****************************************************************************************************/
void podar(nodo nod)
{
	nodo aux = nod->hijo,aux2;
	nodo ant;
	int val,i;
	int minimax[LEVEL_NODES];
	for(i=0;i < LEVEL_NODES-1;i++){
		minimax[i] = -10000;
	}	
	int t = nod->turno;
	while(aux != NULL)	
		{
			val=(aux->value * t);
			if(val > minimax[0]){
				minimax[0]=val;
				for(i=0;i<(LEVEL_NODES-1);i++){
					if(val >= minimax[i+1]){
						minimax[i]=minimax[i+1];
						minimax[i+1]=val;
						}
					else break;
				}
			}
		aux=aux->sig;
		}

	aux=nod->hijo;
	ant=NULL;
	int sem;
	while(aux != NULL)	
		{
			val=(aux->value * nod->turno);
			if(val < minimax[0]){
					
				if(ant==NULL) {
					nod->hijo=aux->sig;
					aux2 =aux->sig;
					borrar_all_hijos(aux);
					cont_f++;
					free(aux);
					aux = aux2;
					cont_free ++;
					
					
				}
				else	{
				ant->sig=aux->sig;
				aux2 =aux->sig;
				borrar_all_hijos(aux);
				cont_f++;
				free(aux);
				aux = aux2;
				cont_free ++;
				
				}
			}
			else{
			 ant=aux;
		         aux=aux->sig;
			}
		 }	
}










/***********************************************************************************************
* Borra y libera la memoria de todos los nodos hijos (y los hijos de los hijos....)
* para un nodo en particular
*************************************************************************************************/
void borrar_all_hijos(nodo nod){
	nodo aux = nod->hijo,aux2;
	int sem;
	while(aux != NULL)
	{
	 	if (aux->hijo != NULL){
			 aux2=aux->sig;
			 borrar_all_hijos(aux);
			 free(aux);
			 cont_free ++;
			 aux = aux2;
		}	
		else {
			aux2=aux->sig;
			free(aux);
			cont_free ++;
			aux = aux2;
			
		}		
	}
}





/**********************************************************************************************************
* Esta funcion es llamada para podar el arbol de jugadas. Recorre todos los nodos de manera decreciente,
* es dcir, comenzando por el padre hacia abajo y por cada uno llama a la funcion podar, la cual descartara
* los nodos con menor valoracion (peores jugadas).
***********************************************************************************************************/
int poda(nodo nod){
	podar(nod);
	nod=nod->hijo;
	int a;
	while(nod!=NULL){
		if(nod->hijo != NULL){
			a = poda(nod);
			}
		nod=nod->sig;
	}
	return 1;
}







int preseleccion(nodo nod)
{
	nodo aux = nod->hijo;
	int t = nod->turno;
	while(aux != NULL)	
		{
		   preselect(aux,aux->value);		
		   aux = aux->sig;	
		}
	return 1;		
}










void preselect(nodo nod,int max)
{
	nodo ax,ax2;
	nodo aux = nod->hijo;

	while(aux != NULL){
		if(aux->value != max) {
			ax = aux;
			aux = aux->sig;
			nod->hijo = aux;
			//free(ax);
			borrar_all_hijos(ax);
			cont_f++;
			free(ax);
			cont_free++;	
		}		
		else
		{
			nod->hijo = aux;
			//aca borrar todo lo q hay delante!!
			ax = aux->sig;
			while (ax != NULL){
				borrar_all_hijos(ax);
				ax2=ax->sig;
				free(ax);
				cont_free++;
				ax=ax2;	
			}
			aux->sig = NULL;
			preselect(aux,aux->value);
			break;
		}
	}
}







int acomodar_minimax(nodo nod, int prof){
	nodo aux;
	int m, n, min=10000, max= -10000;
	aux =nod->hijo;
	int a;

	while(aux!=NULL){
			if(aux->hijo != NULL){
				a = acomodar_minimax(aux,prof+1);
				}
			else{
				m = (aux->value);
			 }
			if(aux->value > max) max=aux->value;
			if(aux->value < min) min=aux->value;

			aux=aux->sig;
		}
	if(nod->turno != blanco) nod->value = max;
	else	nod->value = min;
	return 1;	
}

