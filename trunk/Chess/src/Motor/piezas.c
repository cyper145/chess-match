





#include <stdio.h>
#include <stdlib.h>
#include "piezas.h"



int peonAtacaCasilla(casilla peon, casilla cas, int color){

	if(color == BLANCO){
		if((cas[0] == peon[0]+1) && ((cas[1] == peon[1]+1) || (cas[1] == peon[1]+1)))
			return 1;
	}

	else{
		if((cas[0] == peon[0]-1) && ((cas[1] == peon[1]+1) || (cas[1] == peon[1]+1)))
			return 1;
	}

	return 0;
}






int torreAtacaCasilla(casilla torre, casilla cas, Tablero tab){
		
	int f,c;
	if(cas[0] == torre[0]){
		if(torre[1] < cas[1]){
			c = torre[1]+1;
			while(cas[1] > c){
				if(tab[cas[0]][c]!= 0) return 0;
				c++;
			}
		}
		else{
			c = torre[1]-1;
			while(cas[1] < c){
				if(tab[cas[0]][c]!= 0) return 0;
				c--;
			}
		}
		return 1;
	}
	else if(cas[1] == torre[1]){
		if(torre[0] < cas[0]){
			f= torre[0]+1;
			while(cas[0] > f){
				if(tab[f][torre[1]]!= 0) return 0;
				f++;
			}
		}
		else{
			f=torre[0]-1;
			while(cas[0] < f){
				if(tab[f][torre[1]]!= 0) return 0;
				f--;
			}
		}
		return 1;

	}
	return 0;
}






int caballoAtacaCasilla(casilla caballo, casilla cas){
	if ((abs(caballo[0]-cas[0]) == 1) &&  (abs(caballo[1]-cas[1]) == 2)) return 1;
	if ((abs(caballo[0]-cas[0]) == 2) &&  (abs(caballo[1]-cas[1]) == 1)) return 1;
	return 0;
}





int alfilAtacaCasilla(casilla alfil, casilla cas, Tablero tab){
	
	int i,j;
	int casAlfil = (8*alfil[0]) + alfil[1];
	int casCas = (8*cas[0]) + cas[1];
	int value = abs(casAlfil - casCas);

	int a1 = abs(alfil[0] - cas[0]);
	int a2 = abs(alfil[1] - cas[1]);	
	
	if(a1 == a2){
		i = alfil[0] +1;
		j = alfil[1]+1;
		while((i < cas[0]) && (j < cas[1])){
			if(tab[i][j] != 0) return 0;
			j++;
			i++;
		}

		i = alfil[0] +1;
		j = alfil[1]-1;
		while((i < cas[0]) && (j > cas[1])){
			if(tab[i][j] != 0) return 0;
			j--;
			i++;
		}


		i = alfil[0] -1;
		j = alfil[1]-1;
		while((i > cas[0]) && (j > cas[1])){
			if(tab[i][j] != 0) return 0;
			j--;
			i--;
		}

		i = alfil[0] -1;
		j = alfil[1]+1;
		while((i > cas[0]) && (j < cas[1])){
			if(tab[i][j] != 0) return 0;
			j++;
			i--;
		}
	
		return 1;
	}
	return 0;
}






int damaAtacaCasilla(casilla dama, casilla cas, Tablero tab){
	if((torreAtacaCasilla(dama,cas,tab)) || (alfilAtacaCasilla(dama,cas,tab)))
		return 1;
	return 0;
}
















