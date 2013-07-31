/* MOTOR DE AJEDREZ
*
*Modulo de calculo de funcion de utilidad
*
*
*Autor:  Martin Alonso
*	enano.alonso@gmail.com
*/


/***********************************************************************************************
* Se calcula una valoracion de la posicion para cada nodo terminal en el arbol
* de jugadas.
* Un valor positivo indica ventaja de las blancas y un valor negativo ventaja de las
* negras.
* Los criterios que se tienen en cuenta para la valoracion son:
* 	- Material de cada bando
* 	- Control de las casillas centrales
* 	- Cantidad de casillas que controlan las piezas
* 	- posicion de las piezas
*
*************************************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "var_data.h"








int Tabla_posicion_caballo[8][8]={{-10,-5,-5,-5,-5,-5,-5,-10},
				{-5,0,0,3,3,0,0,-5},
				{-4,0,5,5,5,5,0,-4},
				{-4,0,5,10,10,5,0,-4},
				{-4,0,5,10,10,5,0,-4},
				{-4,0,5,5,5,5,0,-4},
				{-5,0,0,3,3,0,0,-5},
				{-10,-5,-5,-5,-5,-5,-5,-10}};
















/*************************************************************************************
* Recorre el arbol hasta el ultimo nivel y valua estos nodos. Los nodos superiores
* se acomodan de acuerdo al algoritmo minimax
**************************************************************************************/
void valuar_utilidad(nodo inicial, int prof){
	nodo aux;
	aux =inicial->hijo;
	int m,min=10000,max= -10000;

	while(aux!=NULL){
		if(aux->hijo != NULL){
			valuar_utilidad(aux,prof+1);
			}
		else{
			m = valoracion(aux->board);
			memcpy(&aux->value,&m,sizeof(int));
		 }	
		if(aux->value > max) max=aux->value;
		if(aux->value < min) min=aux->value;
		aux=aux->sig;		
	}
	if(inicial->turno == BLANCO) memcpy(&inicial->value,&max,sizeof(int));
	else	memcpy(&inicial->value,&min,sizeof(int));
}
/******************************************************************************************/


















/********************************************************************************************
* Recibe un Tablero con una posicion. Calcula y devuelve una valoracion para tal posicion.
* Se tienen en cuenta varios aspectos como: Material, Posicion, Actividad de las piezas,
* Seguridad del rey, desarrollo, control del centro, etc.
* Un valor positivo representa una posicion ventajosa para el blanco, mientras que un valor 
* negativo lo hace para el negro.
*********************************************************************************************/
int valoracion(Tablero tab){
		
	int i,j;
	int fza_blanca = 0;
	int fza_negra = 0;
	int centro = 0;			//valua el control de las casillas centrales
	int material = 0;		//valua la cantidad de material
	int actividad = 0;		//mide la cantidad de casillas que controla la pieza
	int posicion = 0;		//mide la ubicacion de las piezas
	int seguridad = 0;		//seguridad del rey
	int desarrollo_negro = 0;
	int desarrollo_blanco = 0;

	for(i=0;i<8;i++){
		for(j=0;j<8;j++){
			material=material + tab[i][j];
			switch(tab[i][j]){
				case (PEON_N):
					posicion = posicion + valoracion_peon(tab,i,j,-1);
					break;
				case (PEON_B):
					posicion = posicion + valoracion_peon(tab,i,j,1);
					break;
				case (CABALLO_N):
					posicion=posicion + (Tabla_posicion_caballo[i][j] * -2);
					break;
				case (CABALLO_B):
					posicion=posicion + (Tabla_posicion_caballo[i][j] * 2);
					break;
				case (ALFIL_N):
					actividad=actividad+(actividad_alfil(tab,i,j,-1));
					break;
				case (ALFIL_B):
					actividad=actividad+(actividad_alfil(tab,i,j,1));
					break;
				case (TORRE_B):
					actividad=actividad+(actividad_torre(tab,i,j,1));
					posicion=posicion + (posicion_torre(tab,i,j,1));
					break;
				case (TORRE_N):
					actividad=actividad+(actividad_torre(tab,i,j,-1));
					posicion=posicion + (posicion_torre(tab,i,j,-1));
					break;
				case (DAMA_B):
					actividad=actividad+(actividad_alfil(tab,i,j,1));
					actividad=actividad+(actividad_torre(tab,i,j,1));
					break;
				case (DAMA_N):
					actividad=actividad+(actividad_alfil(tab,i,j,-1));
					actividad=actividad+(actividad_torre(tab,i,j,-1));
					break;
				case (REY_B):
					seguridad = seguridad + seguridad_rey(tab,i,j,1,fza_negra);
					break;
				case (REY_N):
					seguridad = seguridad + seguridad_rey(tab,i,j,-1,fza_blanca);
					break;
				default:
					break;
				
			}
		}
	}
	centro = centro * P_CENTRO;
	material = material * P_MATERIAL;
	actividad = actividad * P_ACTIVIDAD;	
	posicion = posicion * P_POSICION;
	seguridad = seguridad * P_SEGURIDAD;
	desarrollo_blanco = desarrollo_blanco + P_DESARROLLO;
	desarrollo_negro = desarrollo_negro + P_DESARROLLO;
	return (centro + material + actividad + posicion + seguridad + desarrollo_blanco + desarrollo_negro);
}
/***************************************************************************************************************************/













/************************************************************************** 
* Calcula cuantas casillas libres controla la torre 
***************************************************************************/
int actividad_torre(Tablero tab,int fila,int columna,int turno){
	short i,j,casillas=0;	
	casilla torre = {fila,columna};
	
	for(i=0;i<8;i++){ 
		casilla c1 = {i,columna};
		casilla c2 = {fila,i};	
		casillas = casillas + torreAtacaCasilla(torre,c1,tab); 
		casillas = casillas + torreAtacaCasilla(torre,c2,tab); 
  	}
    return (casillas * turno);
}
/*************************************************************************************************************/














/************************************************************************** 
* Calcula cuantas casillas libres controla el alfil 
***************************************************************************/
int actividad_alfil(Tablero tab,int fila,int columna,int turno){
  short i,j;
  int casillas=0;	
  casilla alfil={fila,columna}; 	  
  
  for(i=0;i<8;i++){
	for(j=0;j<8;j++){
		if( abs(i-fila) && abs(j - columna)){
			casilla cas={i,j};
			casillas = casillas + alfilAtacaCasilla(alfil,cas,tab); 	
		}
	} 	
  }	
  return (casillas * turno);
}
/*****************************************************************************************************/















/*******************************************************************************************
* La posicion de la torre mejora al estar en columnas abiertas o semi-abiertas
* y al estar apoyada por la otra torre 
*******************************************************************************************/
int posicion_torre(Tablero tab,int fila,int columna,int turno ){
	int i,torre = TORRE * turno;
	int abierta =1, semi_abierta = 1,apoyada=0;
	
	for(i=0;i<8;i++){
		if(tab[i][columna] == turno) abierta = 0;
		if(tab[i][columna] == -turno) semi_abierta = 0;
		if( ((tab[i][columna] == torre) || (tab[fila][i] == torre)) && (i!=fila || i!=columna)) apoyada = 1;
	}
	return ((abierta* 10) + (semi_abierta*5) + (apoyada*10) * turno);
}
/*******************************************************************************************/













/******************************************************************************************
* La posicion del alfil mejora cuando esta apoyado por un peon ya que ambos se protegen
******************************************************************************************/
int posicion_alfil(Tablero tab,int fila,int columna,int turno ){
	int valor=0, f,c1,c2;
	f = fila - turno;
	c1 = columna + 1;
	c2 = columna -1;

	if((f > 0) && (f <7))
		if(c1 <7)	
			if(tab[f][c1] == turno)	valor = 25;
		if(c2 >0)	
			if(tab[f][c2] == turno)	valor = 25;

	return (valor * turno);
}
/***********************************************************************************************/














/*************************************************************************************************************
* Si fza es mayor a 213, todavia hay piezas pesadas (torres y dama), por lo tanto el rey debe estar
* resguardado ya que existe la posibilidad de jaque mate. Cuando no hay piezas pesadas en el tablero
*el rey debe tomar un papael mas activo y ocupar el centro
**************************************************************************************************************/
int seguridad_rey(Tablero tab,int fila,int columna,int turno,int fza ){
	int valor = 0;
	int f1 = fila + turno;
	
	if((columna%4) == 2){	
		valor = valor +10;
		if(tab[f1][columna +1] == turno) valor = valor +2;
		if(tab[f1][columna -1] == turno) valor = valor +2;
		if(tab[f1][columna] == turno) valor = valor +2;
 	}
	/*Habria q tener en cuenta los rayos-x de las piezas enemigas*/
	return (valor * turno);
}
/*****************************************************************************************************************/












/************************************************************************************************************
* La valoracion de un peon tiene en cuenta si este esta aislado, es un peon pasado o retrasado
**************************************************************************************************************/
int valoracion_peon(Tablero tab,int fila,int columna,int turno){
	int i,aislado = 1,pasado=1;
	int inicio = (7 + turno) % 7;
	int izq = columna - 1;
	int der = columna + 1;
	
	for(i=0;i<6;i++){
		if(tab[inicio][columna] == -turno) pasado = 0;
		if(izq>0) {
			if (tab[inicio][izq] == -turno) pasado = 0;
			if (tab[inicio][izq] == turno)  aislado = 0;
		}
		if(der<7){
			if (tab[inicio][der] == -turno) pasado = 0;
			if (tab[inicio][der] == turno)  aislado = 0;
		}
		inicio = (inicio + turno) % 7;
	}
	return (((pasado * 10)-(aislado*5)) * turno);
}
/*****************************************************************************************************/




	









