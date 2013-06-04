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
#include "var_data.h"



void valuar_utilidad(nodo inicial, int prof){
	nodo aux;
	int m,n;
	aux =inicial->hijo;
	int min=10000;
	int max= -10000;

	while(aux!=NULL){
		if(aux->hijo != NULL){
			valuar_utilidad(aux,prof+1);
			}
		else{
			m = valoracion(aux->board);
			aux->value=m;
		     }	
		if(aux->value > max) max=aux->value;
		if(aux->value < min) min=aux->value;
		aux=aux->sig;		
	}
	if(inicial->turno != blanco) inicial->value = max;
	else	inicial->value = min;
		
}





int valoracion(Tablero tab){
		
	int i,j;
	int centro=0;		//valua el control de las casillas centrales
	int material=0;		//valua la cantidad de material
	int actividad=0;	//mide la cantidad de casillas que controla la pieza
	int posicion=0;		//mide la ubicacion de las piezas

	for(i=0;i<8;i++){
		for(j=0;j<8;j++){

			//suma de material
			material=material + tab[i][j];

			switch(tab[i][j]){
			
				case (PEON_N):
					/*PEON NEGRO*/
					//control del centro
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
					/*PEON BLANCO*/
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
					if((i== F_6)&&(j==C_F)) centro=centro-4;
					if((i== F_7)&&(j==C_E)) centro=centro-1;
					if((i== F_6)&&(j==C_C)) centro=centro-4;
					if((i== F_7)&&(j==C_D)) centro=centro-2;


					//actividad de la pieza
					actividad=actividad+(actividad_caballo(tab,i,j,-1));

					//posicion
					posicion=posicion + (posicion_caballo(tab,i,j,-1));
					break;
				case (CABALLO_B):
					/*CABALLO BLANCO*/
					//control del centro
					if((i== F_3)&&(j==C_F)) centro=centro+4;
					if((i== F_2)&&(j==C_E)) centro=centro+2;
					if((i== F_3)&&(j==C_C)) centro=centro+4;
					if((i== F_2)&&(j==C_D)) centro=centro+2;

					//actividad de la pieza
					actividad=actividad+(actividad_caballo(tab,i,j,1));

					//posicion
					posicion=posicion + (posicion_caballo(tab,i,j,1));
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
					posicion=posicion + (posicion_caballo(tab,i,j,1));
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
				default:
					break;
				
			}
		}
	}
	

	centro = centro * P_CENTRO;
	material = material * P_MATERIAL;
	actividad = actividad * P_ACTIVIDAD;	
	posicion = posicion * P_POSICION;

	return (centro + material + actividad + posicion);
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
		if(tab[f][c]<0) break;
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
		if(tab[f][c]<0) break;
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
		if(tab[f][c]<0) break;
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
		if(tab[f][c]<0) break;
	}
	else break;
	f--;
  	c--;
  }
  return (casillas/3);
}






int posicion_torre(Tablero tab,int fila,int columna,int turno ){

	int valor=0;
	int j,v;
	if(columna == C_E || columna == C_D) valor +=2;
	if(columna == C_C || columna == C_F) valor +=1;
	for(j=0;j<8;j++){
			if((tab[j][columna]*turno)==1) {
				v=0;
				break;
			}
			v=3;
	}
	return (valor + v);
}






int posicion_caballo(Tablero tab,int fila,int columna,int turno ){
	int valor=0;
	if(fila>F_3 && fila<F_6 && columna>C_C && columna < C_F){
		valor=3;
	}
	return (valor);
}







int posicion_alfil(Tablero tab,int fila,int columna,int turno ){
	int valor=0;
	if(fila == (columna % 7)) valor = 3;
	return (valor);
}
