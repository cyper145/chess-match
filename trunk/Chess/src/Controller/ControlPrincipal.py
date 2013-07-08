
from ControlVista import *
from XmlParser import *
from Model.Pawn import *
from Model.Rook import *
from Model.Knight import *
from Model.Bishop import *
from Model.Queen import *
from Model.King import *
from ctypes import *

import sys

from threading import *

from Queue import *

motor = cdll.LoadLibrary('Motor/genera.so')

motor.jugar.restype = POINTER(c_char)


class ControlPrincipal():

 
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
	self.tablero =[[Torre('B',(0,0)),Caballo('B',(0,1)),Alfil('B',(0,2)),Dama('B',(0,3)),Rey('B',(0,4)),Alfil('B',(0,5)),Caballo('B',(0,6)),Torre('B',(0,7))],
                   [Peon('B',(1,0)),Peon('B',(1,1)),Peon('B',(1,2)),Peon('B',(1,3)),Peon('B',(1,4)),Peon('B',(1,5)),Peon('B',(1,6)),Peon('B',(1,7))],
                   [None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None],
                   [Peon('N',(6,0)),Peon('N',(6,1)),Peon('N',(6,2)),Peon('N',(6,3)),Peon('N',(6,4)),Peon('N',(6,5)),Peon('N',(6,6)),Peon('N',(6,7))],
                   [Torre('N',((7,0))),Caballo('N',(7,1)),Alfil('N',(7,2)),Dama('N',(7,3)),Rey('N',(7,4)),Alfil('N',(7,5)),Caballo('N',(7,6)),Torre('N',(7,7))]]
  
	self.contador=0     
	self.controlView.dibujar(self.tablero) 
	self.turnoBlanco=True

	self.bl_en_jaque= False
	self.ng_en_jaque=False

	self.controlView.actual=self.controlView.actual +1
	self.controlView.actual_aux=self.controlView.actual_aux +1
	self.controlView.tablero_to_string(self.tablero)

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


    def Game(self):
	
	count = 0		
	while True:
		
		count+=1
                self.controlView.dibujar(self.tablero)
		#======================== JUEGAN BLANCAS ==========================================
		if self.blancas == 0:

			#.................... Humano ............................................
			valido = False
			while not valido:
				jugada = self.moveQueue.get()
				valido =self.validarMovimiento(jugada)
                        self.anotar(False,self.tablero[jugada[1][0]][jugada[1][1]],jugada[1])
			motor.set_jugada(jugada[0][0],jugada[0][1],jugada[1][0],jugada[1][1]);
			#........................................................................


			#................... Computadora  .......................................
		else:
			jugada=self.jugarMotor(1);
			self.codificar_jugada(jugada)
			self.controlView.set_text(str(count)+"."+jugada)
			#........................................................................
		#====================================================================================


		#========================  JUEGAN NEGRAS ============================================
		if self.negras == 0:
			
			#................... Humano .................................................
			valido = False
			while not valido:	
				jugada = self.moveQueue.get()
				valido =self.validarMovimiento(jugada)
                        self.anotar(False,self.tablero[jugada[1][0]][jugada[1][1]],jugada[1])
			motor.set_jugada(jugada[0][0],jugada[0][1],jugada[1][0],jugada[1][1]);	
			#............................................................................


			#.................... Computadora ...........................................
		else:
			jugada=self.jugarMotor(-1);
			self.codificar_jugada(jugada)
			self.controlView.set_text("  "+jugada+"\n")
			#............................................................................
       		#=====================================================================================
                self.changeTurns()
                
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
	print "Motor juega: ",jugada
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
	destino = self.tablero[self.fila2][self.col2]
       
	if(not pieza):
		return False
	if(self.isNotColorTurn()):
		return False
        if(self.takeSameColor()):
		return False
        if(not pieza.legalMove(mov[1],self.tablero)):
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
                        return True
	if (self.pieza.color=='B' and (not self.turnoBlanco)):
                       	return	True
        return False
    #------------------------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------------------------
    def takeSameColor(self):
		if (self.destino):
			if(self.destino.color== pieza.color):
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
       if(wTurn):
            texto= str(self.contador)+'. '+pieza.name+self.casillas[destino[1]]+str(destino[0]+1)
       else:
            texto='  '+pieza.name+self.casillas[destino[1]]+str(destino[0]+1)+'\n'
   
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
			 if (self.tablero[n][m]!= None):
			   if(self.tablero[n][m].color=='N'):
			     if(self.tablero[n][m].verificar_jaque(self.tablero)):
					  self.moveBack()
					  return True
		if ((not self.turnoBlanco) and self.ng_en_jaque):
		   for n in range(8):
		      for m in range(8):
			 if (self.tablero[n][m] != None):
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
        self.pieza.setCasilla(self.destino)
	self.pieza.set_Imagen(self.destino)
	pza=self.tablero[self.fila1].pop(self.col1)
	self.tablero[self.fila1].insert(self.col1,None)

	self.guardo=self.tablero[self.fila2].pop(self.col2)
	self.tablero[self.fila2].insert(self.col2,pza)
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
#########################################################################################################















#########################################################################################################

    def codificar_jugada(self,j):
	"""Transforma la jugada leida en notacion algebraica en un movimiento de pieza en el tablero"""
	d=-1
	#---------------------------------------------ENROQUE LARGO----------------------------------------------
	if(j[0:5]=='O-O-O'):

		if(self.turnoBlanco): fila=0
		else: fila=7
			
		#Muevo torre
		self.tablero[fila][0].casilla=(fila,3)
		self.tablero[fila][0].set_Imagen((fila,3))
			
		torre = self.tablero[fila].pop(0)
		self.tablero[fila].insert(0,None)
			
		self.tablero[fila].pop(3)
		self.tablero[fila].insert(3,torre)

		#Muevo rey
		self.tablero[fila][4].casilla=(fila,2)
		self.tablero[fila][4].set_Imagen((fila,2))
			
		rey = self.tablero[fila].pop(4)
		self.tablero[fila].insert(4,None)
			
		self.tablero[fila].pop(2)
		self.tablero[fila].insert(2,rey)

		self.turnoBlanco= not self.turnoBlanco
		self.controlView.change_turnos()
		self.controlView.dibujar(self.tablero)
		self.controlView.actual=self.controlView.actual +1
		self.controlView.actual_aux=self.controlView.actual_aux +1
		self.controlView.tablero_to_string(self.tablero)
		#self.controlView.partida.append(self.tablero)
		return
	#--------------------------------------------------------------------------------------------------------

	#---------------------------------------------ENROQUE CORTO----------------------------------------------
	if(j[0:3]=='O-O'):
		if(self.turnoBlanco): fila=0
		else: fila=7
		self.tablero[fila][7].casilla=(fila,5)
		self.tablero[fila][7].set_Imagen((fila,5))
		
		torre = self.tablero[fila].pop(7)
		self.tablero[fila].insert(7,None)
			
			
		self.tablero[fila].pop(5)
		self.tablero[fila].insert(5,torre)

			#Muevo rey
		self.tablero[fila][4].casilla=(fila,6)
		self.tablero[fila][4].set_Imagen((fila,6))
			
		rey = self.tablero[fila].pop(4)
		self.tablero[fila].insert(4,None)
			
		self.tablero[fila].pop(6)
		self.tablero[fila].insert(6,rey)

				
		self.turnoBlanco= not self.turnoBlanco
		self.controlView.change_turnos()
		self.controlView.dibujar(self.tablero)
		self.controlView.actual=self.controlView.actual +1
		self.controlView.actual_aux=self.controlView.actual_aux +1
		self.controlView.tablero_to_string(self.tablero)
		#self.controlView.partida.append(self.tablero)
		return

	#--------------------------------------------------------------------------------------------------------
	#Variables comunes a todas las piezas
	#Saca la fila destino- el except es por que puede haber un jaque '+'
	try:
		fila=int(j[-1])-1
	except:
		try:
			fila=int(j[-2])-1
		except: a=1

	try:
		columna=self.casillas.index(j[-2])
	except:
		try:
			columna=self.casillas.index(j[-3])
		except: a=1

	color='B'
	if(not self.turnoBlanco): color='N'

	if(j[-1]=='+' or j[-1]=='#' ): j=j[0:-1]
	#-------------------------PEON----------------------------------------------------------------------------
	if(j[0]=='a' or j[0]=='b' or j[0]=='c' or j[0]=='d' or j[0]=='e' or j[0]=='f' or j[0]=='g' or j[0]=='h'):

		#coronacion		
		if(re.match('.+=[NBRQ]',j)):
			
			fila=int(j[-3])-1
			columna=self.casillas.index(j[-4])
			if(fila==0): f=1
			else:	f=7
			c=self.casillas.index(j[0])
			self.tablero[f].pop(c)
			self.tablero[f].insert(c,None)
			
			if(j[-1]=='Q'):
				self.dibujar_reproducir(10,1,fila,columna)
				return	
			if(j[-1]=='R'):
				self.dibujar_reproducir(10,2,fila,columna)
				return
			if(j[-1]=='N'):
				self.dibujar_reproducir(10,3,fila,columna)
				return
			if(j[-1]=='B'):
				self.dibujar_reproducir(10,4,fila,columna)
				return
			
		if(j[1]!='x'):
			columna=self.casillas.index(j[0])
			col=columna
			
			if(not self.turnoBlanco):
				d=1
			if(self.tablero[fila+d][columna]!=None):
				ca=fila+d
			else:
				ca=fila+(2*d)
			
			self.dibujar_reproducir(ca,col,fila,columna)
			return
		else:
			col=self.casillas.index(j[0])
			#columna=self.casillas.index(j[2])
			try:
				fila=int(j[-1])-1
			except:
				fila=int(j[-2])-1
			if(not self.turnoBlanco): d=1
			ca=fila+d
			self.dibujar_reproducir(ca,col,fila,columna)
			return
	#--------------------------------------------------------------------------------------------------------		
	
	#-------------------------TORRE--------------------------------------------------------------------------	
	if(j[0]=='R'):
		
		if(len(j)==3 or j[1]=='x'):
					
			#izquierda
			c=columna-1
			while(c>=0):
				try:
					if(self.tablero[fila][c].name=='T' and self.tablero[fila][c].color==color):
						self.dibujar_reproducir(fila,c,fila,columna)
						return
					if(self.tablero[fila][c].name!=None):
						break
				except:
					a=1				
				c=c-1
	
			#derecha
			c=columna+1
			while(c<=7):
				try:	
					if(self.tablero[fila][c].name=='T' and self.tablero[fila][c].color==color):
						self.dibujar_reproducir(fila,c,fila,columna)
						return
					if(self.tablero[fila][c].name!=None):
						break
				except:
					a=1				
				c=c+1

			#abajo
			f=fila-1
			while(f>=0):
				try:
					if(self.tablero[f][columna].name=='T' and self.tablero[f][columna].color==color):
						self.dibujar_reproducir(f,columna,fila,columna)
						return
					if(self.tablero[fila][c].name!=None):
						break
				except:
					a=1
				f=f-1

			#arriba
			f=fila+1
			while(f<=7):
				try:
					if(self.tablero[f][columna].name=='T' and self.tablero[f][columna].color==color):
						self.dibujar_reproducir(f,columna,fila,columna)
						return
				except:
					a=1				
				f=f+1

		elif(re.match('.[a-h].+',j)):
			c=self.casillas.index(j[1])
			
			#abajo
			f=fila
			while(f>=0):
				try:
					if(self.tablero[f][c].name=='T' and self.tablero[f][c].color==color):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except:
					a=1
				f=f-1

			#arriba
			f=fila+1
			while(f<=7):
				try:
					if(self.tablero[f][c].name=='T' and self.tablero[f][c].color==color):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except:
					a=1				
				f=f+1
		elif(re.match('.[0-7].+',j)):
			f=int(j[1])-1
			c=columna-1
			while(c>=0):
				try:
					if(self.tablero[f][c].name=='T' and self.tablero[f][c].color==color):
						self.dibujar_reproducir(f,c,fila,columna)
						return
					if(self.tablero[f][c].name!=None):
						break
				except:
					a=1				
				c=c-1
	
			#derecha
			c=columna+1
			while(c<=7):
				try:	
					if(self.tablero[fila][c].name=='T' and self.tablero[fila][c].color==color):
						self.dibujar_reproducir(fila,c,fila,columna)
						return
					if(self.tablero[fila][c].name!=None):
						break
				except:
					a=1				
				c=c+1
	#--------------------------------------------------------------------------------------------------------


	#---------------------------------------------CABALLO----------------------------------------------------
	if(j[0]=='N'):
		
		if(len(j)==3 or j[1]=='x'):
						
			d_fila=2
			d_col=1
		
			for i in range(2):
				for p in range(2):
					for k in range(2):
				
						f=fila+ d_fila
						c=columna+d_col
						try:
							if (self.tablero[f][c].name=='C' and self.tablero[f][c].color == color):
								self.dibujar_reproducir(f,c,fila,columna)
								return
						except:
							a=1
					
						d_col=d_col*(-1)
					d_fila=d_fila*(-1)
				d_fila=1
				d_col=2
		elif(re.match('.[a-h].+',j)):
						
			c=self.casillas.index(j[1])
			d=1
			for k in range(2):
				
				f=fila+(d+k)
				try:					
					if (self.tablero[f][c].name=='C' and self.tablero[f][c].color == color):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except: a=1

				f=fila-(d+k)
				try:					
					if (self.tablero[f][c].name=='C' and self.tablero[f][c].color == color):
						self.dibujar_reproducir(f,c,fila,columna)
						return

				except: a=1
					

		elif(re.match('.[0-7].+',j)):
			
			f=int(j[1])-1
			d=1
			for k in range(2):
				
				try:
					c=columna+(d+k)					
					if (self.tablero[f][c].name=='C' and self.tablero[f][c].color == color):
						self.dibujar_reproducir(f,c,fila,columna)
						return
					c=columna-(d+k)					
					if (self.tablero[f][c].name=='C' and self.tablero[f][c].color == color):
						self.dibujar_reproducir(f,c,fila,columna)
						return

				except:
					a=1

	#--------------------------------------------------------------------------------------------------------



	#---------------------------------------------ALFIL------------------------------------------------------
	if(j[0]=='B'):
		
		if(len(j)==3 or j[1]=='x'):
						
			#Abajo-izq
			f=fila-1
			c=columna-1
			while(f>=0 and c>=0):
				try:
					if(self.tablero[f][c].name=='A' and self.tablero[f][c].color==color ):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except:
					a=1		
				f=f-1
				c=c-1
		
			#Arriba-izq
			f=fila+1
			c=columna-1
			while(f<=7 and c>=0):
				try:
					if(self.tablero[f][c].name=='A' and self.tablero[f][c].color==color ):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except:
					a=1		
				f=f+1
				c=c-1

			#Abajo-der
			f=fila-1
			c=columna + 1
			while(f>=0 and c<=7):
				try:
					if(self.tablero[f][c].name=='A' and self.tablero[f][c].color==color ):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except:
					a=1		
				f=f-1
				c=c+1

		
			#Arriba-der
			f=fila+1
			c=columna + 1
			while(f<=7 and c<=7):
				try:
					if(self.tablero[f][c].name=='A' and self.tablero[f][c].color==color ):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except:
					a=1		
				f=f+1
				c=c+1
		
	#--------------------------------------------------------------------------------------------------------

	#-------------------------------------------DAMA---------------------------------------------------------
	if(j[0]=='Q'):

		if(j[-1]=='+'): j=j[0:-1]
		
		if(len(j)==3 or j[1]=='x'):
			
			#############ALFIL##########################
			#Abajo-izq
			f=fila-1
			c=columna-1
			while(f>=0 and c>=0):
				try:
					if(self.tablero[f][c].name=='D' and self.tablero[f][c].color==color ):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except:
					a=1		
				f=f-1
				c=c-1
		
			#Arriba-izq
			f=fila+1
			c=columna-1
			while(f<=7 and c>=0):
				try:
					if(self.tablero[f][c].name=='D' and self.tablero[f][c].color==color ):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except:
					a=1		
				f=f+1
				c=c-1

			#Abajo-der
			f=fila-1
			c=columna + 1
			while(f>=0 and c<=7):
				try:
					if(self.tablero[f][c].name=='D' and self.tablero[f][c].color==color ):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except:
					a=1		
				f=f-1
				c=c+1

		
			#Arriba-der
			f=fila+1
			c=columna + 1
			while(f<=7 and c<=7):
				try:
					if(self.tablero[f][c].name=='D' and self.tablero[f][c].color==color ):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except:
					a=1		
				f=f+1
				c=c+1

			#######################TORRE#############################
			#izquierda
			c=columna-1
			while(c>=0):
				try:
					if(self.tablero[fila][c].name=='D' and self.tablero[fila][c].color==color):
						self.dibujar_reproducir(fila,c,fila,columna)
						return
				except:
					a=1				
				c=c-1
	
			#derecha
			c=columna+1
			while(c<=7):
				try:	
					if(self.tablero[fila][c].name=='D' and self.tablero[fila][c].color==color):
						self.dibujar_reproducir(fila,c,fila,columna)
						return
				except:
					a=1				
				c=c+1

			#abajo
			f=fila-1
			while(f>=0):
				try:
					if(self.tablero[f][columna].name=='D' and self.tablero[f][columna].color==color):
						self.dibujar_reproducir(f,columna,fila,columna)
						return
				except:
					a=1
				f=f-1

			#arriba
			f=fila+1
			while(f<=7):
				try:
					if(self.tablero[f][columna].name=='D' and self.tablero[f][columna].color==color):
						self.dibujar_reproducir(f,columna,fila,columna)
						return
				except:
					a=1				
				f=f+1

	#--------------------------------------------------------------------------------------------------------


	#-----------------------------------------REY-------------------------------------------------------------
	if(j[0]=='K'):
				
		f=fila
		try: 
			if(self.tablero[f][columna+1].name=='R' and self.tablero[f][columna+1].color==color):
				self.dibujar_reproducir(f,columna+1,fila,columna)
				return
		except: a=1
		try:
			if(self.tablero[f][columna-1].name=='R' and self.tablero[f][columna-1].color==color):
				self.dibujar_reproducir(f,columna-1,fila,columna)
				return
		except: a=1
		try:
			if(self.tablero[f+1][columna].name=='R' and self.tablero[f+1][columna].color==color):
				self.dibujar_reproducir(f+1,columna,fila,columna)
				return
		except: a=1
		try:
			if(self.tablero[f-1][columna].name=='R' and self.tablero[f-1][columna].color==color):
				self.dibujar_reproducir(f-1,columna,fila,columna)
				return
		except: a=1	
		df=1
		dc=1
		for p in range(2):
			for k in range(2):
				f=fila+df
				c=columna+dc
				try:
					if(self.tablero[f][c].name=='R' and self.tablero[f][c].color==color):
						self.dibujar_reproducir(f,c,fila,columna)
						return
				except: a=1
				dc=dc*-1
			df=df*-1
			

	#--------------------------------------------------------------------------------------------------------
	
	
	
############################################################################################################################
    def dibujar_reproducir(self,ca,col,fila,columna):
	
	#Coronocaion de peon
	if(ca==10):
		if(self.turnoBlanco): color='B'
		else: color='N'
		if(col==1):	#Dama
			dama = Dama(color,(fila,columna))
			self.tablero[fila].insert(columna,dama)
		if(col==2):	#torre
			torre = Torre(color,(fila,columna))
			self.tablero[fila].insert(columna,torre)
		if(col==3):	#Caballo
			caballo = Caballo(color,(fila,columna))
			self.tablero[fila].insert(columna,caballo)
		if(col==4):	#Alfil
			alfil = Alfil(color,(fila,columna))
			self.tablero[fila].insert(columna,alfil)

	else:
		pza=self.tablero[ca].pop(col)
		self.tablero[ca].insert(col,None)
		self.tablero[fila].pop(columna)
		self.tablero[fila].insert(columna,pza)


	self.tablero[fila][columna].set_Imagen((fila,columna))
		
	self.controlView.dibujar(self.tablero)
	self.turnoBlanco= not self.turnoBlanco
	self.controlView.change_turnos()

		
	self.controlView.actual=self.controlView.actual +1
	self.controlView.actual_aux=self.controlView.actual_aux +1
	self.controlView.tablero_to_string(self.tablero)
############################################################################################################################




