
from ControlVista import *

from Model.Pawn import *
from Model.Rook import *
from Model.Knight import *
from Model.Bishop import *
from Model.Queen import *
from Model.King import *
from NoteHelper import *
from ctypes import *
from Model.Pieza import *
from Model.Square import *

import sys

from threading import *

from Queue import *

motor = cdll.LoadLibrary('Motor/genera.so')

motor.jugar.restype = POINTER(c_char)


class ControlPrincipal():

    
	
    LONG_CASTLE = 1000
    SHORT_CASTLE = 100
    PROMOTION = 10		
 

    NOTE_CASTLE = False
    NOTE_LONG_CASTLE = False	
#########################################################################################################
    def __init__(self):

	self.moveQueue = Queue()	
        self.controlView = ControlVista(self,self.moveQueue)
        self.iniciar_variables()
       # parser = XmlParser()
#########################################################################################################










#########################################################################################################
    def iniciar_variables(self):

	self.casillas=['a','b','c','d','e','f','g','h']
	self.tablero =[[Torre('B',(0,0),'T'),Caballo('B',(0,1),'C'),Alfil('B',(0,2),'A'),Dama('B',(0,3),'D'),Rey('B',(0,4),'R'),Alfil('B',(0,5),'A'),Caballo('B',(0,6),'C'),Torre('B',(0,7),'T')],
                   [Peon('B',(1,0),''),Peon('B',(1,1),''),Peon('B',(1,2),''),Peon('B',(1,3),''),Peon('B',(1,4),''),Peon('B',(1,5),''),Peon('B',(1,6),''),Peon('B',(1,7),'')],
                   [Square('',(2,0),'as'),Square('',(2,1),''),Square('',(2,2),''),Square('',(2,3),''),Square('',(2,4),''),Square('',(2,5),''),Square('',(2,6),''),Square('',(2,7),'')],
                   [Square('',(3,0),''),Square('',(3,1),''),Square('',(3,2),''),Square('',(3,3),''),Square('',(3,4),''),Square('',(3,5),''),Square('',(3,6),''),Square('',(3,7),'')],
                   [Square('',(4,0),''),Square('',(4,1),''),Square('',(4,2),''),Square('',(4,3),''),Square('',(4,4),''),Square('',(4,5),''),Square('',(4,6),''),Square('',(4,7),'')],
                   [Square('',(5,0),''),Square('',(5,1),''),Square('',(5,2),''),Square('',(5,3),''),Square('',(5,4),''),Square('',(5,5),''),Square('',(5,6),''),Square('',(5,7),'')],
                   [Peon('N',(6,0),''),Peon('N',(6,1),''),Peon('N',(6,2),''),Peon('N',(6,3),''),Peon('N',(6,4),''),Peon('N',(6,5),''),Peon('N',(6,6),''),Peon('N',(6,7),'')],
                   [Torre('N',(7,0),'T'),Caballo('N',(7,1),'C'),Alfil('N',(7,2),'A'),Dama('N',(7,3),'D'),Rey('N',(7,4),'R'),Alfil('N',(7,5),'A'),Caballo('N',(7,6),'C'),Torre('N',(7,7),'T')]]
  
	self.contador=0     
	self.controlView.dibujar(self.tablero) 
	self.turnoBlanco=True

	self.bl_en_jaque= False
	self.ng_en_jaque=False

	self.controlView.actual=self.controlView.actual +1
	self.controlView.actual_aux=self.controlView.actual_aux +1
	self.controlView.tablero_to_string(self.tablero)
	self.noterHelper = NoteHelper(self)
	

	self.mode = None
#########################################################################################################













############################################################################################################################
   
    def newGame(self,blancas,negras,horas,minut,inc):	
	""" Maneja un juego entre dos oponentes. Cada jugador puede ser humano o el Motor de ajedrez  """

	self.blancas=blancas
	self.negras=negras

	self.game= Thread(target=self.Game)
    	self.game.daemon = True
    	self.game.start()
	#self.Game()
	
    def Game(self):
	
	self.contadpr = 0		
	while True:
		
		self.contador+=1
               
		#======================== JUEGAN BLANCAS ==========================================
		if self.blancas == 0:

			#.................... Humano ............................................
			valido = False
			while not valido:
				jugada = self.moveQueue.get()
				valido =self.validarMovimiento(jugada)
                        self.anotar(True,self.tablero[jugada[1][0]][jugada[1][1]],jugada[1])
			motor.set_jugada(jugada[0][0],jugada[0][1],jugada[1][0],jugada[1][1]);
			self.changeTurns()
			self.controlView.repaint(jugada[0],jugada[1],self.tablero)	
			#........................................................................


			#................... Computadora  .......................................
		else:
			jugada=self.jugarMotor(1);
			self.codificar_jugada(jugada)
			#self.changeTurns()
			self.controlView.set_text(str(self.contador)+"."+jugada)
			#........................................................................
		#====================================================================================
		

		#self.controlView.dibujar(self.tablero)
		#========================  JUEGAN NEGRAS ============================================
		if self.negras == 0:
			
			#................... Humano .................................................
			valido = False
			while not valido:	
				jugada = self.moveQueue.get()
				valido =self.validarMovimiento(jugada)
                        self.anotar(False,self.tablero[jugada[1][0]][jugada[1][1]],jugada[1])
			motor.set_jugada(jugada[0][0],jugada[0][1],jugada[1][0],jugada[1][1]);	
			self.changeTurns()
			self.controlView.repaint(jugada[0],jugada[1],self.tablero)
			#............................................................................


			#.................... Computadora ...........................................
		else:
			jugada=self.jugarMotor(-1);
			self.codificar_jugada(jugada)
			#self.changeTurns()
			self.controlView.set_text("  "+jugada+"\n")
			#............................................................................
       		#=====================================================================================
                #self.controlView.dibujar(self.tablero)
############################################################################################################################










############################################################################################################################
    def jugarMotor(self,turno):
	""" LLama la funcion del modulo c """
	i=0
	jugada=''
	a = motor.jugar(turno)
	while True:
		if (a[i] != '\x00'):
			jugada = jugada + a[i]
		else:
			break
		i=i+1
	print ""
	return jugada
############################################################################################################################











#########################################################################################################
    def validarMovimiento(self,mov): 
	"""Controla que el movimiento realizado por un humano sea valido, de acuerdo a las reglas del juego """

        self.origen = mov[0]
        self.dest = mov[1]
	self.fila1= mov[0][0]
	self.col1= mov[0][1]
	self.fila2= mov[1][0]
	self.col2= mov[1][1]
	self.controlView.set_mensaje("")	

        self.pieza=self.tablero[self.fila1][self.col1]
	self.destino = self.tablero[self.fila2][self.col2]
	

      	if(isinstance(self.pieza,Square)):
		return False
	if(self.isNotColorTurn()):
		return False
	if(self.takeSameColor()):
		return False
	if(not self.pieza.legalMove(mov[1],self.tablero)):
		return False
	if(self.isInCheck()):
		return False
	self.controlCheck()
        return True
#########################################################################################################












#########################################################################################################

    #------------------------------------------------------------------------------------------------------
    def isNotColorTurn(self):
	if (self.pieza.color=='N' and self.turnoBlanco):
			print "Not your turn!"
                        return True
	if (self.pieza.color=='B' and (not self.turnoBlanco)):
			print "Not your turn!"
                       	return	True
        return False
    #------------------------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------------------------
    def takeSameColor(self):
		if (self.destino):
			if(self.destino.color== self.pieza.color):
				return True
		return False
    #------------------------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------------------------
    def controlCheck(self):
        if (self.pieza.verificar_jaque(self.tablero)):
            self.controlView.set_mensaje("Jaque")
            if self.turnoBlanco:
			self.ng_en_jaque= True
            else:
			self.bl_en_jaque= True
    #------------------------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------------------------
    def changeTurns(self):
        self.turnoBlanco= not self.turnoBlanco
	self.controlView.change_turnos()
	self.controlView.actual=self.controlView.actual +1
	self.controlView.actual_aux=self.controlView.actual_aux +1
	self.controlView.tablero_to_string(self.tablero)
    #------------------------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------------------------
    def anotar(self,wTurn,pieza, destino):

       	if(self.NOTE_CASTLE):
		play = 'O-O'
		self.NOTE_CASTLE = False
	elif(self.NOTE_LONG_CASTLE):
		play = 'O-O-O'	
		self.NOTE_LONG_CASTLE = False
	else:
       		play = pieza.name+self.casillas[destino[1]]+str(destino[0]+1)
       	if(wTurn):
       		texto= str(self.contador) + '. ' + play
       	else:
       		texto='  ' + play + '\n'
   
       	self.controlView.set_text(texto)
    #------------------------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------------------------
    def verificarDescubierto(self):
	""" El jaque descubierto sucede cuando una pieza se mueve y destapa el
         ataque de otra. Solo lo pueden hacer la torre, el alfil y la dama"""

	jugada=True
	if(self.turnoBlanco):
	   for filas in self.tablero:
		for casilla in filas:
		     try:
			if((casilla.name=='T'  or casilla.name=='A' or casilla.name =='D') and casilla.color=='N'):
				j=casilla.verificar_descubierto(self.tablero)
				jugada= jugada and j
		     except:
			 pass
	else:
	    for filas in self.tablero:
		for casilla in filas:
		     try:
			if((casilla.name=='T'  or casilla.name=='A' or casilla.name =='D') and casilla.color=='B'):
				j=casilla.verificar_descubierto(self.tablero)
				jugada= jugada and j
		     except:
			 pass

	return jugada
    #------------------------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------------------------
    def isInCheck(self):

                self.move()
 		#
		#-------------------verificar jaque descubierto (discovered Check)-----------
		if (not self.verificarDescubierto()):
			#volver pa atras
			self.moveBack()
			return True
		#----------------------------------------------------------------------------

		
		#-------------------verifica si esta en jaque--------------------------------
		if (self.turnoBlanco and self.bl_en_jaque):
		  for n in range(8):
		     for m in range(8):
			 if not(isinstance(self.tablero[n][m],Square)):
			   if(self.tablero[n][m].color=='N'):
			     if(self.tablero[n][m].verificar_jaque(self.tablero)):
					  self.moveBack()
					  return True
		if ((not self.turnoBlanco) and self.ng_en_jaque):
		   for n in range(8):
		      for m in range(8):
			 if not(isinstance(self.tablero[n][m],Square)):
			    if(self.tablero[n][m].color=='B'):
			       if(self.tablero[n][m].verificar_jaque(self.tablero)):
					  self.moveBack()
					  return True

		self.bl_en_jaque=False
		self.ng_en_jaque=False
		return False
    #------------------------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------------------------
    def move(self):
	if not(self.isCastle()):
		self.pieza.setCasilla(self.dest)
		self.pieza.set_Imagen(self.dest)
		pza=self.tablero[self.fila1].pop(self.col1)
		self.tablero[self.fila1].insert(self.col1,Square('',(self.fila1,self.col1),''))
		self.guardo=self.tablero[self.fila2].pop(self.col2)
		self.tablero[self.fila2].insert(self.col2,pza)
    #------------------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------------------
    def isCastle(self):
	if (isinstance(self.pieza,Rey) and self.pieza.casilla[1] == 4 and (self.dest[1] == 6 or self.dest[1] == 2)):
				
			fila = self.pieza.casilla[0]			
			self.pieza.setCasilla(self.dest)
			self.pieza.set_Imagen(self.dest)
			pza=self.tablero[self.fila1].pop(self.col1)
			self.tablero[self.fila1].insert(self.col1,Square('',(self.fila1,self.col1),''))
			self.tablero[self.fila2].pop(self.col2)
			self.tablero[self.fila2].insert(self.col2,pza)
	
			if self.dest[1] == 6: 
				f = 7
				c = 5
				self.NOTE_CASTLE = True
				
			else: 
				f = 0
				c = 3
				self.NOTE_LONG_CASTLE = True

			torre =	self.tablero[fila].pop(f)
			torre.setCasilla((fila,c))
			torre.set_Imagen((fila,c))

			self.tablero[fila].insert(f, Square('',(fila,f),''))
			self.tablero[fila].pop(c)
			self.tablero[fila].insert(c, torre)
			self.controlView.repaint((fila,f),(fila,c),self.tablero)
			motor.set_jugada(fila,f,fila,c);	
			return True
		
	else: return False

    #------------------------------------------------------------------------------------------------------	


    #------------------------------------------------------------------------------------------------------
    def moveBack(self):
        pza=self.tablero[self.fila2].pop(self.col2)
	self.pieza.setCasilla(self.origen)
	self.pieza.set_Imagen(self.origen)

	self.tablero[self.fila1].pop(self.col1)
	self.tablero[self.fila1].insert(self.col1,pza)
	self.tablero[self.fila2].insert(self.col2,self.guardo)
	self.controlView.set_mensaje("Movimiento ilegal")
    #------------------------------------------------------------------------------------------------------
 
    
    def getTurn(self):
	return self.turnoBlanco


    def setTurno(self,turn):
	self.turnoBlanco = turn	

    def	getTablero(self):
	return self.tablero 	
#########################################################################################################















#########################################################################################################

    def codificar_jugada(self,j):
	"""Transforma la jugada leida en notacion algebraica en un movimiento de pieza en el tablero"""
	(origen,destino) = self.noterHelper.readMove(j)	
	self.reproducir(origen,destino)



	
	
############################################################################################################################
    def reproducir(self,origen,destino):
	
	#............. movimientos especiales ................................................
	if(origen[0] == self.PROMOTION):
		if(self.turnoBlanco): color='B'
		else: color='N'
			
		self.tablero[detino[2]].pop(detino[3])
		self.tablero[detino[2]].insert(detino[3],Square('',(destini[2],destino[3]),''))
		if(origen[1] == 1):	#Dama
			dama = Dama(color,(fila,columna))
			self.tablero[fila].insert(columna,dama)
		if(origen[1] == 2):	#torre
			torre = Torre(color,(fila,columna))
			self.tablero[fila].insert(columna,torre)
		if(origen[1] == 3):	#Caballo
			caballo = Caballo(color,(fila,columna))
			self.tablero[fila].insert(columna,caballo)
		if(origen[1] == 4):	#Alfil
			alfil = Alfil(color,(fila,columna))
			self.tablero[fila].insert(columna,alfil)

	elif(origen[0] == self.LONG_CASTLE):
		if(self.turnoBlanco): fila=0
		else: fila=7
		#Muevo torre
		self.tablero[fila][0].casilla=(fila,3)
		self.tablero[fila][0].set_Imagen((fila,3))
		torre = self.tablero[fila].pop(0)
		self.tablero[fila].insert(0,Square('',(fila,0),''))
		self.tablero[fila].pop(3)
		self.tablero[fila].insert(3,torre)
 
		#Muevo rey
		self.tablero[fila][4].casilla=(fila,2)
		self.tablero[fila][4].set_Imagen((fila,2))
		rey = self.tablero[fila].pop(4)
		self.tablero[fila].insert(4,Square('',(fila,4),''))
		self.tablero[fila].pop(2)
		self.tablero[fila].insert(2,rey)

		self.controlView.repaint((fila,0),(fila,3),self.tablero)
		origen = (fila,4)
		destino = (fila,2)		

	elif(origen[0] == self.SHORT_CASTLE):	
		if(self.turnoBlanco): fila=0
		else: fila=7
		#Muevo torre
		self.tablero[fila][7].casilla=(fila,5)
		self.tablero[fila][7].set_Imagen((fila,5))
		torre = self.tablero[fila].pop(7)
		self.tablero[fila].insert(7,Square('',(fila,7),''))
		self.tablero[fila].pop(5)
		self.tablero[fila].insert(5,torre)

		#Muevo rey
		self.tablero[fila][4].casilla=(fila,6)
		self.tablero[fila][4].set_Imagen((fila,6))
		rey = self.tablero[fila].pop(4)
		self.tablero[fila].insert(4,Square('',(fila,4),''))
		self.tablero[fila].pop(6)
		self.tablero[fila].insert(6,rey)

		self.controlView.repaint((fila,7),(fila,5),self.tablero)
		origen = (fila,6)
		destino = (fila,4)		
	#......................................................................................

	else:
		ca = origen[0]
		col = origen[1]
		fila = destino[0]
		columna = destino[1]
		pza=self.tablero[ca].pop(col)
		self.tablero[ca].insert(col,Square('',(ca,col),''))
		pza.setCasilla(destino)	
		self.tablero[fila].pop(columna)
		self.tablero[fila].insert(columna,pza)
		pza.set_Imagen((fila,columna))

	
	self.controlView.repaint(origen,destino,self.tablero)
	#self.controlView.dibujar(self.tablero)
	self.turnoBlanco= not self.turnoBlanco
	self.controlView.change_turnos()
	self.controlView.setActual()
	self.controlView.tablero_to_string(self.tablero)
############################################################################################################################




