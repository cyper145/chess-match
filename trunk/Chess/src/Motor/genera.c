/* MOTOR DE AJEDREZ
*
*Modulo generador de movimientos
*
*
*Autor:  Martin Alonso
*	enano.alonso@gmail.com
*/

/***********************************************************************************
* Dada una posicion inicial, se genera un arbol con todas las convinaciones de 
* movimientos posibles. El arbol tendra la profundidad definida en el fichero
* var_data.h, como constante 'DEEP'.
* Cada nodo en el arbol es una estructura definida en var_data.h y tiene los sig campos:
*
*	-jugada :	indica la casilla origen y destino del ultimo movimiento
*	-Tablero :	Contiene la posicion actual del juego
*	-notacion:	notacion algebraica de la ultima jugada
*	-value:		valoracion de la posicion
*	- *hijo:	punteros.
*	- *sig:
*	- *padre:
*	
************************************************************************************/




#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "poda.h"
#include "funcutilidad.h"
#include "var_data.h"
#include <time.h> 





unsigned long int contador =0;
int ultima=0;


const char cab[]="N";
const char tor[]="R";
const char alf[]="B";
const char dam[]="Q";
const char re[]="K";
const char come[]="x";

char *partido[2*DEEP];
int valores[3*DEEP];

    

void eliminar(nodo nod);
void mostrar_tablero(Tablero tab);
void gen(nodo inicial,Tablero tab,int turno);
void torre(nodo padre,Tablero tab,casilla cas);
void caballo(nodo padre,Tablero tab,casilla cas);
void alfil(nodo padre,Tablero tab,casilla cas);
void rey(nodo padre,Tablero tab,casilla cas);
void peon(nodo padre,Tablero tab,casilla cas);
void insertar_nodo(nodo padre,casilla from,casilla to);
void mostrar_arbol(int prof,nodo padre, char *z);
void generar(int prof,nodo nod,int turno);
void regenera(nodo nod);
void convert_to_char(nodo padre,casilla from,casilla to,char *s);
void set_jugada(int f_origen,int c_origen,int f_dest,int c_dest);
char* jugar(int t);
char* seleccionar(nodo nod,int color );





/*-------- Tablero con posicion inicial--------*/
Tablero posicion={{5,3,4,10,200,4,3,5},
		  {1,1,1,1,1,1,1,1},
		  {0,0,0,0,0,0,0,0},
		  {0,0,0,0,0,0,0,0},
		  {0,0,0,0,0,0,0,0},
		  {0,0,0,0,0,0,0,0},
		  {-1,-1,-1,-1,-1,-1,-1,-1},
		  {-5,-3,-4,-10,-200,-4,-3,-5}};
/*---------------------------------------------*/






char* generate(int t)
{
	int k, turno;
	char *a="", *jugada=NULL;;
	turno = t;
	
	clock_t start = clock();
	
	
	/*---Inicializa el primer nodo del arbol------*/
	nodo inicial;
	inicial=malloc(sizeof(struct Nodo));
	//struct Nodo inicial;
	memcpy(inicial->board,posicion,sizeof(Tablero));
	cont_free = 0;
	contador =0;
	cont_f=0;
  	inicial->hijo=NULL;
  	inicial->sig=NULL;
  	memcpy(inicial->notation,"",(5*sizeof(char)));
	inicial->turno=turno;
	inicial->value=0;
	inicial->shortCastle=1;
	inicial->longCastle=1;
	/*---------------------------------------------*/
	
	

	generar(0,inicial,turno);
	valuar_utilidad(inicial,0);
	poda(inicial);
	preseleccion(inicial);
	for(k=0;k<6;k++)	
	{	
		regenera(inicial);
		acomodar_minimax(inicial,0);
		preseleccion(inicial);
	}
	

	
	/*Selecciona la mejor jugada*/	
	jugada = seleccionar(inicial, turno);
	
	double finish = (((double)clock() - start) / CLOCKS_PER_SEC);
	printf ("Jugadas analizadas: %ld - timepo: %f  seg - Seleccionada: %s ",contador,finish,jugada );
	
	cont_f++;
	borrar_all_hijos(inicial);
	return (jugada);
}






/*********************************************************************************************
*  Esta funcion es la que se llama para hacer jugar al motor.
*  Recibe el turno y retorna la jugada elegida por el motor.
*   
*  Para mantener la posicion del tablero, el motor guarda la posicion cada
*  vez que juega y cuando el oponente humano lo hace, se debe enviar la jugada
*  a traves de la funcion set_jugada asi el motor actualiza la posicion actual.
**********************************************************************************************/
char* jugar(int t)
{
  return(generate(t));		
}









/*********************************************************************************************
* Esta funcion se llama cuando un jugador humano realiza una jugada.
* Actualiza la posicion del tablero con la posicion actual.*
*********************************************************************************************/
void set_jugada(int f_origen,int c_origen,int f_dest,int c_dest)
{
	short aux,cero=0;
	aux = posicion[f_origen][c_origen];
	posicion[f_origen][c_origen] = cero;
	posicion[f_dest][c_dest] = aux;
	//printf("MOSTRAR TABLERO \n");	
	//mostrar_tablero(posicion);

}





void generar(int prof,nodo nod, int turno){
	
	gen(nod,nod->board,turno);
	nod->turno=turno;
	nod=nod->hijo;
	
	while(nod!=NULL){
		if(prof<DEEP){
			generar(prof+1,nod,(turno*-1));
			}
		nod=nod->sig;
	}
}








/***************************************************************************************
* Recorre todas las casillas del tablero. Por cada pieza del color del cual es
* el turno genera todas las posibles jugadas.
*
* @ inicial: nodo inicial del arbol
*
* @tab:	tablero con la posicion actual
*
* @turno: turno actual.  1 = blancas  -1 = negras
****************************************************************************************/
void gen(nodo inicial,Tablero tab,int turno)
{
  short f,c;

 for(f=0;f<8;f++){
	for(c=0;c<8;c++){
		if((tab[f][c]*turno)>0){
			casilla cas={f,c};
			switch (tab[f][c]*turno){
				case TORRE:
					torre(inicial,tab,cas);
					break;
				case CABALLO:
					caballo(inicial,tab,cas);
					break;
				case ALFIL:
					alfil(inicial,tab,cas);
					break;
				case DAMA:
					torre(inicial,tab,cas);
					alfil(inicial,tab,cas);
					break;
				case REY:
					rey(inicial,tab,cas);
					break;
				case PEON:
					peon(inicial,tab,cas);
					break;
			}
		}

	}
 }



}

void regenera(nodo nod)
{
	nodo aux;
	aux = nod->hijo;
	int turno = nod->turno;
	int a;
	while(aux!=NULL){
		if(aux->hijo != NULL){
			regenera(aux);
			}
		else {
			generar(DEEP-2,aux,turno);
			valuar_utilidad(aux,0);
			poda(aux);
			acomodar_minimax(aux,0);
			
			/*
			if(sem_wait(&semaforo) == 0){
				valuar_utilidad(aux,0);
				sem_post(&semaforo);
			}	
			if(sem_wait(&semaforo) == 0){
				poda(aux);
				sem_post(&semaforo);
			}
			if(sem_wait(&semaforo) == 0){
				acomodar_minimax(aux,0);
				sem_post(&semaforo);
			}
			*/
		}	
		aux=aux->sig;
	}
}






/***************************************************************************************
* Analiza y agrega al arbol cada jugada posible para una torre.
*
* @padre: nodo inicial del arbol
*
* @tab: tablero con la posicion actual
*
* @cas: casilla donde se encuentra la torre a analizar 
****************************************************************************************/
void torre(nodo padre,Tablero tab,casilla cas){

	short f,c,fil,col;

	fil=cas[0];
	col=cas[1];
	f=cas[0]-1;
	c=cas[1];

	/*abajo*/
	while(f>=0){

		if((tab[fil][col]*tab[f][c])==0){
			casilla to={f,c};
			insertar_nodo(padre,cas,to);
		}
		else if((tab[fil][col]*tab[f][c])<0){
			casilla to={f,c};
			insertar_nodo(padre,cas,to);
			break;
		}	
		else break;
		f--;
	}
	f=cas[0]+1;
	c=cas[1];

	/*arriba*/
	while(f<=7){
		if((tab[fil][col]*tab[f][c])==0){
			casilla to={f,c};
			insertar_nodo(padre,cas,to);
		}
		else if((tab[fil][col]*tab[f][c])<0){
			casilla to={f,c};
			insertar_nodo(padre,cas,to);
			break;
		}	
		else break;
		f++;
	}
	f=cas[0];
	c=cas[1]-1;

	/*izquierda*/
	while(c>=0){
		if((tab[fil][col]*tab[f][c])==0){
			casilla to={f,c};
			insertar_nodo(padre,cas,to);
		}
		else if((tab[fil][col]*tab[f][c])<0){
			casilla to={f,c};
			insertar_nodo(padre,cas,to);
			break;
		}	
		else break;
		c--;
	}
	f=cas[0];
	c=cas[1]+1;
	
	/*derecha*/
	while(c<=7){
		if((tab[fil][col]*tab[f][c])==0){
			casilla to={f,c};
			insertar_nodo(padre,cas,to);
		}
		else if((tab[fil][col]*tab[f][c])<0){
			casilla to={f,c};
			insertar_nodo(padre,cas,to);
			break;
		}	
		else break;
		c++;
	}
}






/***************************************************************************************
* Analiza y agrega al arbol cada jugada posible para un caballo.
*
* @padre: nodo inicial del arbol
*
* @tab: tablero con la posicion actual
*
* @cas: casilla donde se encuentra el caballo a analizar 
****************************************************************************************/
void caballo(nodo padre,Tablero tab,casilla cas){

  short  f,c,i,j,k,fil,col;
  short  d_f=2;
  short  d_c=1;
  fil=cas[0];
  col=cas[1];
  f=cas[0];
  c=cas[1];
  for(i=0;i<2;i++){
	for(j=0;j<2;j++){
		for(k=0;k<2;k++){
			f=cas[0]+d_f;
			c=cas[1]+d_c;
			if((0<=f)&&(f<=7)&&(0<=c)&&(c<=7)&&((tab[fil][col]*tab[f][c])<=0)){
				casilla to={f,c};
				insertar_nodo(padre,cas,to);
			}
			d_c=d_c*-1;
		}
	  	d_f=d_f*-1;
	}
	d_f=1;
	d_c=2;
   }

}











/***************************************************************************************
* Analiza y agrega al arbol cada jugada posible para un alfil.
*
* @padre: nodo inicial del arbol
*
* @tab: tablero con la posicion actual
*
* @cas: casilla donde se encuentra el alfil a analizar 
****************************************************************************************/
void alfil(nodo padre,Tablero tab,casilla cas){

  short  f,c,i,j,k,fil,col;
  short  d_f=1;
  short  d_c=-1;
  f=cas[0]+1;
  c=cas[1]-1;
  fil=cas[0];
  col=cas[1];
  /**Derecha**/
  /*abajo*/
  while((f<=7)&&(c>=0)){
	if((tab[fil][col]*tab[f][c])<=0){
		casilla to={f,c};
		insertar_nodo(padre,cas,to);
		if(tab[f][c]!=0) break;
	}
	else break;
	f++;
  	c--;
  }
  /*arriba*/
  f=cas[0]+1;
  c=cas[1]+1;
  while((f<=7)&&(c<=7)){
	if((tab[fil][col]*tab[f][c])<=0){
		casilla to={f,c};
		insertar_nodo(padre,cas,to);
		if(tab[f][c]!=0) break;
	}
	else break;
	f++;
  	c++;
  }
  /**izquierda**/
  /*arriba*/
  f=cas[0]-1;
  c=cas[1]+1;
  while((f>=0)&&(c<=7)){
	if((tab[fil][col]*tab[f][c])<=0){
		casilla to={f,c};
		insertar_nodo(padre,cas,to);
		if(tab[f][c]!=0) break;
	}
	else break;
	f--;
  	c++;
  }
   /*abajo*/
  f=cas[0]-1;
  c=cas[1]-1;
  while((f>=0)&&(c>=0)){
	if((tab[fil][col]*tab[f][c])<=0){
		casilla to={f,c};
		insertar_nodo(padre,cas,to);
		if(tab[f][c]!=0) break;
	}
	else break;
	f--;
  	c--;
  }
}









/***************************************************************************************
* Analiza y agrega al arbol cada jugada posible para un rey. (falta implementar los enroques!!)
*
* @padre: nodo inicial del arbol
*
* @tab: tablero con la posicion actual
*
* @cas: casilla donde se encuentra el rey a analizar 
****************************************************************************************/
void rey(nodo padre,Tablero tab,casilla cas){

 short  f,c,i,j,k,fil,col;
 short  d_f=1;
 short  d_c=0;

 fil=cas[0];
 col=cas[1];

 for(i=0;i<2;i++){
	for(j=0;j<2;j++){
		f=cas[0]+d_f;
		c=cas[1]+d_c;
		if((0<=f)&&(f<=7)&&(0<=c)&&(c<=7)&&((tab[fil][col]*tab[f][c])<=0)){
			casilla to={f,c};
			insertar_nodo(padre,cas,to);
		}
		d_f=d_f*-1;
		d_c=d_c*-1;
	}
	d_f=0;
	d_c=1;
  }

 d_f=1;
 d_c=1;
 for(i=0;i<2;i++){
	for(j=0;j<2;j++){
		f=cas[0]+d_f;
		c=cas[1]+d_c;
		if((0<=f)&&(f<=7)&&(0<=c)&&(c<=7)&&((tab[fil][col]*tab[f][c])<=0)){
			casilla to={f,c};
			insertar_nodo(padre,cas,to);
			
		}
		d_c=d_c*-1;
	}
	d_f=d_f*-1;
  }

  /*------------ enroque ---------------------------------------*/
  if((padre->shortCastle) && (tab[cas[0]][6] == 0) && (tab[cas[0]][5] == 0) ){
	casilla from={ENROQUE_CORTO,0};
	casilla to={cas[0],6};
	insertar_nodo(padre,from,to);
  }	
  if((padre->longCastle) && (tab[cas[0]][1] == 0) && (tab[cas[0]][2] == 0) && (tab[cas[0]][3] == 0) ){

	casilla from = {ENROQUE_LARGO,0};
	casilla to = {cas[0],2};
	insertar_nodo(padre,from,to);
  }	
}











/***************************************************************************************
* Analiza y agrega al arbol cada jugada posible para un peon.
*
* @padre: nodo inicial del arbol
*
* @tab: tablero con la posicion actual
*
* @cas: casilla donde se encuentra el peon a analizar 
****************************************************************************************/
void peon(nodo padre,Tablero tab,casilla cas){

   short  paso,f,c,j,d_c,fil,col, destino;
   fil=cas[0];
   col=cas[1];

   paso=tab[fil][col];
   

   /*una casilla adelante*/
   f=cas[0]+paso;
   c=cas[1];
   destino = tab[f][c];
   if((0<=f)&&(f>=7))	
   if((tab[f][c]) == 0){
	casilla to={f,c};
	insertar_nodo(padre,cas,to);
	}


   /*dos casillas adelante*/
   if (((cas[0]==((paso+7)%7))&& (tab[f][cas[1]]==0)) && (tab[f+paso][c]==0)){
	casilla to={(f+paso),c};
	insertar_nodo(padre,cas,to);
 	}

   /*come*/
   d_c=1;
   for(j=0;j<2;j++){
	c=cas[1]+d_c;
	if(((tab[f][c]*tab[fil][col])<0)&&((c<=7)&&(0<=c))) {
		casilla to={f,c};
		insertar_nodo(padre,cas,to);
	}
	d_c=d_c*-1;
    }
}















/*********************************************************************************************
* Inserta una nueva jugada en el arbol de jugadas.
*
* @padre: nodo inicial del arbol.
*
* @from: casilla origen de la pieza a mover.
*
* @to: casilla final de la pieza a mover.
**********************************************************************************************/
void insertar_nodo(nodo padre,casilla from,casilla to){

	nodo nuevo,aux;
	short  auxiliar,j,i;
	char *nota;
	short fila;

	

	auxiliar=padre->board[from[0]][from[1]];

	contador++;

	nuevo=malloc(sizeof(struct Nodo));
	//nuevo=(nodo)malloc(sizeof(struct Nodo));
	if(nuevo!=NULL){

		nuevo->j.from[0]=from[0];
		nuevo->j.from[1]=from[1];
		nuevo->j.to[0]=to[0];
		nuevo->j.to[1]=to[1];
		
		memcpy(nuevo->board,padre->board,sizeof(Tablero));
		
		short  ax = 0;

		nuevo->hijo=NULL;
		nuevo->sig=NULL;
		nuevo->value=0;

		if(from[0] == ENROQUE_CORTO){
			
			if(from[1] == blanco)	fila = 0;
			else	fila = 7;
			nuevo->board[fila][5] = nuevo->board[fila][7];
			nuevo->board[fila][7] = 0 ;
			nuevo->board[fila][6] = nuevo->board[fila][4];
			nuevo->board[fila][4] = 0;
			nuevo->longCastle = 0;
			nuevo->shortCastle = 0;
			memcpy(nuevo->notation,"O-O", 5*sizeof(char));

		}

		else if(from[0] == ENROQUE_LARGO){

			if(from[1] == blanco)	fila = 0;
			else	fila = 7;

			nuevo->board[fila][3] = nuevo->board[fila][0];
			nuevo->board[fila][0] = 0 ;
			nuevo->board[fila][2] = nuevo->board[fila][4];
			nuevo->board[fila][4] = 0;
			nuevo->longCastle = 0;
			nuevo->shortCastle = 0;
			memcpy(nuevo->notation,"O-O-O", 5*sizeof(char));

		}

		else{
			

			nuevo->board[to[0]][to[1]]=nuevo->board[from[0]][from[1]];
			nuevo->board[from[0]][from[1]]=0;
		

			
			convert_to_char(padre,from,to,nuevo->notation);
		}

		if(padre->hijo==NULL){
			padre->hijo=nuevo;
			nuevo->padre=padre;
			}
		else{
			//aux=(nodo)malloc(sizeof(struct Nodo));
			aux=padre->hijo;
			while(aux->sig!=NULL){
				aux=aux->sig;
				}
			aux->sig=nuevo;
			nuevo->padre=aux->padre;
			aux->padre=NULL;
			//free(aux);
			}

	}
	else printf("no hay memoria\n");
}



int cont=0;




void mostrar_arbol(int prof,nodo padre, char *z){

	int k;
	
	partido[prof]=padre->notation;
	valores[prof]=padre->value;
	//partido[prof]=padre->hijo->notation;
	nodo aux =padre->hijo;
	//partido[prof]=aux->notation;
	//printf("padre v:%s  %d\n",padre->notation,padre->value);
	while(aux!=NULL){
		//printf("%s ",&aux->notation);
		//if(prof<DEEP){
		if(aux->hijo != NULL){
			mostrar_arbol(prof+1,aux,z);

			}

		//if(prof==DEEP){
		else{
			partido[prof+1]=aux->notation;
			//valores[prof+1]=aux->value;

			for(k=1;k<= prof+1;k++){
				printf("%s ",partido[k]);
			}
			printf("valor: %d\n",aux->value);
			cont=cont+1;
		}
		aux=aux->sig;
	}
	
}



/*******************************************************************************************
* Convierte una jugada en notacion algebraica para poder realizar la anotacion.
* 
* @from: casilla inicial de la pieza a mover.
*
* @to:	casilla final de la pieza a mover.
********************************************************************************************/
void convert_to_char(nodo padre,casilla from,casilla to,char *s){

	char not[5]="",cc[2]="";

	int pza,pza2;
	char casillas[8]={'a','b','c','d','e','f','g','h'};

	pza=padre->board[from[0]][from[1]];
	pza2=padre->board[to[0]][to[1]];

	if(pza==5 || pza==-5) 	strcat(not,tor);

	if(pza==4 || pza==-4)	strcat(not,alf);

	if(pza==3 || pza==-3)	strcat(not,cab);

	if(pza==10 || pza==-10)	strcat(not,dam);

	if(pza==100 || pza==-100)   strcat(not,re);

	if(pza==1 || pza==-1)  {

		cc[0]=casillas[from[1]];
		strcat(not,cc);
		if(pza2!=0) {
			strcat(not,come);
			cc[0]=casillas[to[1]];
			strcat(not,cc);
			sprintf(cc,"%hd",(to[0]+1));
			strcat(not,cc);
			//printf("%s \n",not);
			//return(not);
			memcpy(s,not,sizeof(not));
			return;
			//s=not;
		}
		else{
			sprintf(cc,"%hd",(to[0]+1));
			strcat(not,cc);
			//printf("%s \n",not);
			//return(not);
			memcpy(s,not,sizeof(not));
			return;
			//s=not;
		}

	}

	if(pza2!=0) strcat(not,come);



	//strcat(cc,casillas[to[1]]);
	cc[0]=casillas[to[1]];
	strcat(not,cc);
	sprintf(cc,"%hd",(to[0]+1));
	strcat(not,cc);

	//printf("%s \n",not);
	//return (not);
	memcpy(s,not,sizeof(not));
	return;
	//s=not;

}


void mostrar_tablero(Tablero tab)
{
 int j,k;
	for(j=0;j<8;j++){
		for(k=0;k<8;k++){
			printf("%i",tab[j][k]);
		}
		printf("\n");
	}
	return;
}





/*****************************************************************************************************
* Selecciona la mejor jugada del arbol ya evaluado y podado.
* Si es el turno blanco elije el nodo con mayor valoracion,o la de menor valoracion
* para el turno negro.
*
* @nodo: arbol de jugadas evaluado y podado
*
* @color: indica de quien es el turno:
*         1 = blanco   -1 = negro
******************************************************************************************************/
char* seleccionar(nodo nod, int color)
{
	nodo aux;
	aux = nod->hijo;
	int max = -1000;
	short auxiliar,f_origen,c_origen,f_dest,c_dest;
	char * j;
	jugada move;
	int flag = 0;
	while(aux != NULL)
	{

		if((aux->value* color) > max)
		{
			max = (aux->value * color);
			j = aux->notation;
			f_origen=aux->j.from[0];
			c_origen=aux->j.from[1];
			f_dest=aux->j.to[0];
			c_dest=aux->j.to[1];	
			flag=1;
		
		}
		
		aux = aux->sig;
	}	

	auxiliar = posicion[f_origen][c_origen];
	if(flag){
		posicion[f_origen][c_origen] = 0;
		posicion[f_dest][c_dest] = auxiliar;
	}
	return (j);
}


