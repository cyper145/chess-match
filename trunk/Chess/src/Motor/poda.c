/* MOTOR DE AJEDREZ
*
* 	- Modulo de poda ALPHA-BETA del algoritmo MINIMAX
*
*
*   Autor:  Martin Alonso
*	enano.alonso@gmail.com
*/


/***********************************************************************************************
* 
*
*************************************************************************************************/


#define LEVEL_NODES	4

#include <stdio.h>
#include "poda.h"
#include "var_data.h"






void podar(nodo nod)
{
	nodo aux = nod->hijo,aux2;
	nodo ant;
	int val,i;
	//int minimax[LEVEL_NODES]={-100,-100,-100,-100,-100,-100,-100,-100};
	int minimax[LEVEL_NODES]={-100,-100,-100,-100};
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
	while(aux != NULL)	
		{
			val=(aux->value * nod->turno);
			if(val < minimax[0]){
					
				if(ant==NULL) {
					nod->hijo=aux->sig;
					aux2 =aux->sig;
					//aux=NULL;
					//free(aux);
					borrar_all_hijos(aux);
					cont_f++;
					free(aux);
					aux = aux2;
					cont_free ++;
					
				}
				else	{
				ant->sig=aux->sig;
				//printf("free %s\n",aux->notation);
				aux2 =aux->sig;
				//aux=NULL;
				//free(aux);
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


void borrar_all_hijos(nodo nod){

	
	nodo aux = nod->hijo,aux2;
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
			//aux = NULL;
			free(aux);
			aux = aux2;
			cont_free ++;
		}		



	}
	//printf("count_free %ld\n",cont_free);
	//free(nod);
	//cont_free++;
}


void poda(nodo nod){


	podar(nod);
	nod=nod->hijo;
	
	while(nod!=NULL){

		if(nod->hijo != NULL){

			poda(nod);

			}

		nod=nod->sig;

	}

}


void preseleccion(nodo nod)
{
	nodo aux = nod->hijo;
	int t = nod->turno;
	while(aux != NULL)	
		{
		   preselect(aux,aux->value);		
		   aux = aux->sig;	
		}		


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

void acomodar_minimax(nodo nod, int prof){

	nodo aux;
	int m,n;
	aux =nod->hijo;

	int min=10000;
	int max= -10000;

	while(aux!=NULL){

			if(aux->hijo != NULL){

				acomodar_minimax(aux,prof+1);

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

}

