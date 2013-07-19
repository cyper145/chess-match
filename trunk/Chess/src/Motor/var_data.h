
#ifndef _VAR_DATA_H
#define _VAR_DATA_H



#define DEEP	3


//--------CASILLAS---------------------------
#define F_1	0
#define F_2	1
#define F_3	2
#define F_4	3
#define F_5	4
#define F_6	5
#define F_7	6
#define F_8	7

#define C_A	0
#define C_B	1
#define C_C	2
#define C_D	3
#define C_E	4
#define C_F	5
#define C_G	6
#define C_H	7
//------------------------------------------


//--------PIEZAS----------------------------
#define	PEON_N		-1
#define	CABALLO_N	-3
#define	ALFIL_N		-4
#define	TORRE_N		-5
#define	DAMA_N		-10
#define	REY_N		-200

#define	PEON_B	 	1
#define	CABALLO_B	3
#define	ALFIL_B		4
#define	TORRE_B		5
#define	DAMA_B		10
#define	REY_B		200

#define	PEON	 	1
#define	CABALLO		3
#define	ALFIL		4
#define	TORRE		5
#define	DAMA		9
#define	REY		200
//------------------------------------------



//-------PONDERACIONES-----------------------
#define P_MATERIAL	10
#define P_CENTRO	2
#define P_ACTIVIDAD	4
#define P_POSICION	4
#define P_SEGURIDAD	100
#define P_DESARROLLO	10
//-------------------------------------------


//-----------ENROQUES------------------------
#define ENROQUE_CORTO		10
#define ENROQUE_LARGO   	100
//-------------------------------------------




#define blanco 		1
#define negro		-1






typedef short  casilla [2];
typedef short  Tablero [8][8];





struct Jugada{
	casilla from;
	casilla to;
};
typedef struct Jugada jugada;



struct Nodo {
	jugada j;
	Tablero board;
	char notation[5];
	int value;
	short  turno;
	short shortCastle;
	short longCastle;
	struct Nodo  *hijo;
	struct Nodo  *sig;
	struct Nodo  *padre;
};
typedef struct Nodo* nodo;



#endif
