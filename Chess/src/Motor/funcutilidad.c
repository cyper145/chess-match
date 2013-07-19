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

#define MIN	-1
#define MAX	1




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


void valuar_utilidad(nodo inicial, int prof){
	nodo aux;
	int n;
	int m;
	aux =inicial->hijo;
	int min=10000;
	int max= -10000;
	int a;
	while(aux!=NULL){
		if(aux->hijo != NULL){
			valuar_utilidad(aux,prof+1);
			}
		else{
			m = valoracion(aux->board);
			memcpy(&aux->value,&m,sizeof(int));
			//aux->value=m;
		     }	
		if(aux->value > max) max=aux->value;
		if(aux->value < min) min=aux->value;
		aux=aux->sig;		
	}
	if(inicial->turno == blanco) memcpy(&inicial->value,&max,sizeof(int));//inicial->value = max;
	else	memcpy(&inicial->value,&min,sizeof(int));//inicial->value = min;
}





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

			//suma de material
			material=material + tab[i][j];
			if(tab[i][j] >= 3 ) fza_blanca = fza_blanca + tab[i][j];
			if(tab[i][j] <= -3 ) fza_negra = fza_negra + tab[i][j];

			if(i==0){
				if((tab[i][j] == 3) || (tab[i][j] == 4)) desarrollo_blanco = desarrollo_blanco - 2;  
			}

			if(i==7){
				if((tab[i][j] == -3) || (tab[i][j] == -4)) desarrollo_blanco = desarrollo_negro + 2;  
			}

			switch(tab[i][j]){
			
				case (PEON_N):
					/*PEON NEGRO*/
					posicion = posicion + valoracion_peon(tab,i,j,-1);
					if(i == F_5){
						
						if((j >= C_C )&& (j <= C_F)) centro=centro-1;
						if((j >= C_D) && (j <= C_E)) centro=centro-1;
					}
					if(i== F_6){
					//control del centro
						if((j >= C_D) && (j <= C_E)) centro=centro-1;
					}
					break;
				case (PEON_B):
					posicion = posicion + valoracion_peon(tab,i,j,1);
					if(i== F_4){
						//control del centro
						if((j >= C_C) && (j <= C_F)) centro=centro+1;
						if((j >= C_D) && (j <= C_E)) centro=centro+1;
					}
					if(i==2){
						//control del centro
						if((j >= C_D) && (j <= C_E)) centro=centro+1;
					}
					break;
				case (CABALLO_N):
					/*CABALLO NEGRO*/
					//control del centro
					/*
					if((i== F_6)&&(j==C_F)) centro=centro-4;
					if((i== F_7)&&(j==C_E)) centro=centro-1;
					if((i== F_6)&&(j==C_C)) centro=centro-4;
					if((i== F_7)&&(j==C_D)) centro=centro-2;


					//actividad de la pieza
					actividad=actividad+(actividad_caballo(tab,i,j,-1));
					*/
					//posicion
					posicion=posicion + (Tabla_posicion_caballo[i][j] * -10);
					break;
				case (CABALLO_B):
					/*CABALLO BLANCO*/
					//control del centro
					/*
					if((i== F_3)&&(j==C_F)) centro=centro+4;
					if((i== F_2)&&(j==C_E)) centro=centro+2;
					if((i== F_3)&&(j==C_C)) centro=centro+4;
					if((i== F_2)&&(j==C_D)) centro=centro+2;

					//actividad de la pieza
					actividad=actividad+(actividad_caballo(tab,i,j,1));
					*/
					//posicion
					posicion=posicion + (Tabla_posicion_caballo[i][j] * 10);
					break;
				case (ALFIL_N):
					//actividad de la pieza
					actividad=actividad+(actividad_alfil(tab,i,j,-1));
					break;
				case (ALFIL_B):
					//actividad de la pieza
					actividad=actividad+(actividad_alfil(tab,i,j,1));
					break;
				case (TORRE_B):
					/*TORRE BLANCA*/
					//control del centro
					if((i>2)&&(i<6)) centro=centro+2;

					//actividad de la pieza
					actividad=actividad+(actividad_torre(tab,i,j,1));

					//posicion
					posicion=posicion + (posicion_torre(tab,i,j,1));
					break;
				case (TORRE_N):
					/*TORRE NEGRA*/
					//control del centro
					if((i>2)&&(i<6)) centro=centro-2;

					//actividad de la pieza
					actividad=actividad+(actividad_torre(tab,i,j,-1));

					//posicion
					posicion=posicion + (posicion_torre(tab,i,j,1));
					break;
				case (DAMA_B):
					/*DAMA BLANCA*/
					actividad=actividad+(actividad_alfil(tab,i,j,1));
					actividad=actividad+(actividad_torre(tab,i,j,1));
					break;
				case (DAMA_N):
					/*DAMA NEGRA*/
					actividad=actividad+(actividad_alfil(tab,i,j,-1));
					actividad=actividad+(actividad_torre(tab,i,j,-1));
					break;

				case (REY_B):
					seguridad = seguridad + seguridad_rey(tab,i,j,1,fza_negra);
					break;

				case (REY_N):
					seguridad = seguridad + seguridad_rey(tab,i,j,1,fza_blanca);
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






int actividad_caballo(Tablero tab,int fila,int columna,int turno){
	int i,j,k,val=0,f,c,d_f=2,d_c=1;

	for(i=0;i<2;i++){
	for(j=0;j<2;j++){
		for(k=0;k<2;k++){
			f=fila+d_f;
			c=columna+d_c;
			if((0<=f)&&(f<=7)&&(0<=c)&&(c<=7)){
				val = val +turno;
			}
			d_c=d_c*-1;
		}
	  	d_f=d_f*-1;
	}
	d_f=1;
	d_c=2;
   }
   return (val);

}







int actividad_torre(Tablero tab,int fila,int columna,int turno){
	short int f,c,fil,col;
	int casillas=0;	
	fil=fila;
	col=columna;
	f=fila-1;
	c=columna;

	//abajo
	while(f>=0){
		if((turno*tab[f][c])<=0){
			casillas=casillas+turno;
		}
		else break;
		f--;
	}
	f=fila+1;
	c=columna;
	//arriba
	while(f<=7){
		if((turno*tab[f][c])<=0){
			casillas=casillas+turno;
		}
		else break;
		f++;
	}
	f=fila;
	c=columna-1;
	//izquierda
	while(c>=0){
		if((turno*tab[f][c])<=0){
			casillas=casillas+turno;
		}
		else break;
		c--;
	}
	f=fila;
	c=columna+1;
	//arriba
	while(c<=7){
		if((turno*tab[f][c])<=0){
			casillas=casillas+turno;
		}
		else break;
		c++;
	}
    return (casillas/5);
}






/************************************************************************** 
* Calcula cuantas casillas libres controla el alfil y si esta atacando
* alguna pieza enemiga
***************************************************************************/
int actividad_alfil(Tablero tab,int fila,int columna,int turno){
  short int f,c,i,j,k,fil,col;
  short int d_f=1;
  short int d_c=-1;
  int casillas=0;	
  f=fila+1;
  c=columna-1;
  fil=fila;
  col=columna;
  //Derecha
  //abajo
  while((f<=7)&&(c>=0)){
	if((turno*tab[f][c])<=0){
		casillas=casillas+turno;
		if((turno*tab[f][c])<0) {	
			casillas = casillas + (turno * tab[f][c]);
			break;
		}
	}
	else break;
	f++;
  	c--;
  }
  //arriba
  f=fila+1;
  c=columna+1;
  while((f<=7)&&(c<=7)){
	if((turno*tab[f][c])<=0){
		casillas=casillas+turno;
		if((turno*tab[f][c])<0) break;
	}
	else break;
	f++;
  	c++;
  }
  //izquierda
  //arriba
  f=fila-1;
  c=columna+1;
  while((f>=0)&&(c<=7)){
	if((turno*tab[f][c])<=0){
		casillas=casillas+1;
		if((turno*tab[f][c])<0) break;
	}
	else break;
	f--;
  	c++;
  }
   //abajo
  f=fila-1;
  c=columna-1;
  while((f>=0)&&(c>=0)){
	if((turno*tab[f][c])<=0){
		casillas=casillas+turno;
		if((turno*tab[f][c])<0) break;
	}
	else break;
	f--;
  	c--;
  }
  return (casillas);
}




/*******************************************************************************************
* La posicion de la torre mejora al estar en columnas abiertas o semi-abiertas
* y al estar apoyada por la otra torre 
*******************************************************************************************/
int posicion_torre(Tablero tab,int fila,int columna,int turno ){
	int valor=0;
	int j,v;
	
	return valor;
}





/******************************************************************************************
* 
******************************************************************************************/
int posicion_alfil(Tablero tab,int fila,int columna,int turno ){
	int valor=0;
	if(fila == (columna % 7)) valor = 3;
	return (valor);
}















/*************************************************************************************************************
* Si fza es mayor a 213, todavia hay piezas pesadas (torres y dama), por lo tanto el rey debe estar
* resguardado ya que existe la posibilidad de jaque mate. Cuando no hay piezas pesadas en el tablero
*el rey debe tomar un papael mas activo y ocupar el centro
**************************************************************************************************************/
int seguridad_rey(Tablero tab,int fila,int columna,int turno,int fza ){
	int valor = 0;

	
	//if( (fza* turno * -1) > 213){

		if((columna == 6) && (tab[fila][5] == (TORRE * turno))){
			valor = valor +1;
			if(tab[fila + turno][7] == turno) valor = valor +2;
			if(tab[fila + turno][6] == turno) valor = valor +2;
			if(tab[fila + turno][5] == turno) valor = valor +2;
 		}


		if((columna == 2) && (tab[fila][3] == (TORRE * turno))){
			valor = valor +1;
			if(tab[fila + turno][1] == turno) valor = valor +2;
			if(tab[fila + turno][2] == turno) valor = valor +2;
			if(tab[fila + turno][3] == turno) valor = valor +2;
			if(tab[fila + turno][4] == turno) valor = valor +2;
 		}

        //}
	return valor * turno;
}













/************************************************************************************************************
* La valoracion de un peon tiene en cuenta si este esta aislado, es un peon pasado o retrasado
**************************************************************************************************************/
int valoracion_peon(Tablero tab,int fila,int columna,int turno){
	int valor = 0;
	int inicio = (7 + turno) % 7;
	int izq = columna - 1;
	int der = columna + 1;
	int pasado = 1;
	
	while(inicio != 0){

		if(tab[inicio][columna] == -turno) pasado = 0;
		
		
		//-------------- Apoyado  (no aislado) ------------------
		if(izq>0){
			if (tab[inicio][izq] == turno){
				 valor++;
				 if(izq == (fila - turno)) valor++;	
			}	
			
			if (tab[inicio][izq] == -turno) pasado = 0;
		}


		if(der<7){
			if (tab[inicio][der] == turno){
				valor++;
				if(der == (fila - turno)) valor++;	
			}
			
			if (tab[inicio][der] == turno) pasado = 0;
		}
		//---------------------------------------------------------
		inicio = (inicio + turno) % 7;
	}

	if(pasado) valor = valor + 5;	
	return valor * turno;
}





	









