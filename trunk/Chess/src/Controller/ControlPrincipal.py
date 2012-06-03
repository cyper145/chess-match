
from ControlVista import *
from Model.Pawn import *
from Model.Rook import *
from Model.Knight import *
from Model.Bishop import *
from Model.Queen import *
from Model.King import *


class ControlPrincipal():

 
#########################################################################################################
    def __init__(self):

	
        self.controlView = ControlVista(self)
	
        self.tablero =[[Torre('B',(0,0)),Caballo('B',(0,1)),Alfil('B',(0,2)),Dama('B',(0,3)),Rey('B',(0,4)),Alfil('B',(0,5)),Caballo('B',(0,6)),Torre('B',(0,7))],
                   [Peon('B',(1,0)),Peon('B',(1,1)),Peon('B',(1,2)),Peon('B',(1,3)),Peon('B',(1,4)),Peon('B',(1,5)),Peon('B',(1,6)),Peon('B',(1,7))],
                   [None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None],
                   [None,None,None,None,None,None,None,None],
                   [Peon('N',(6,0)),Peon('N',(6,1)),Peon('N',(6,2)),Peon('N',(6,3)),Peon('N',(6,4)),Peon('N',(6,5)),Peon('N',(6,6)),Peon('N',(6,7))],
                   [Torre('N',((7,0))),Caballo('N',(7,1)),Alfil('N',(7,2)),Dama('N',(7,3)),Rey('N',(7,4)),Alfil('N',(7,5)),Caballo('N',(7,6)),Torre('N',(7,7))]]

	self.casillas=['a','b','c','d','e','f','g','h']
	self.contador=0     
	self.controlView.dibujar(self.tablero) 
	self.turnoBlanco=True          
#########################################################################################################






#########################################################################################################
    def validarMovimiento(self,mov): 

	fila1= mov[0][0]
	col1= mov[0][1]	
	fila2= mov[1][0]
	col2= mov[1][1]	
	elf.controlView.set_mensaje("")	
	pieza=self.tablero[fila1][col1]
	

	if(pieza!=None):
			
		if (pieza.color=='N' and self.turnoBlanco):
			print "no es el turno Negro"
			return
		if (pieza.color=='B' and (not self.turnoBlanco)):
			print "No es el turno blanco"
			return	
	
			
		jugada=pieza.validar_Movimiento(mov[1],self.tablero)
		
	
	
		#No come pieza del mismo color
		#------------------------------------------------------------------------------------------------------
		if (self.tablero[mov[1][0]][mov[1][1]]!= None ):
			if (self.tablero[mov[1][0]][mov[1][1]].color== self.tablero[mov[0][0]][mov[0][1]].color):
				jugada = False
		#------------------------------------------------------------------------------------------------------
		


		#Enroque corto
		#------------------------------------------------------------------------------------------------------
		if(self.tablero[fila1][col1].name=='R' and self.tablero[fila1][col1].aviso) and mov[1][1]==6:
			self.tablero[fila1][col1].aviso=False
			#Muevo torre
			self.tablero[fila1][7].casilla=(fila1,5)
			self.tablero[fila1][7].set_Imagen((fila1,5))
			
			torre = self.tablero[fila1].pop(7)
			self.tablero[fila1].insert(7,None)
			
			
			self.tablero[fila1].pop(5)
			self.tablero[fila1].insert(5,torre)

			#Muevo rey
			self.tablero[fila1][4].casilla=(fila1,6)
			self.tablero[fila1][4].set_Imagen((fila1,6))
			
			rey = self.tablero[fila1].pop(4)
			self.tablero[fila1].insert(4,None)
			
			self.tablero[fila1].pop(6)
			self.tablero[fila1].insert(6,rey)

			#anoto
			if(self.turnoBlanco):
				self.contador=self.contador+1
				texto= str(self.contador)+'. '+'0-0' 
			else:
				texto='  '+'0-0'+'\n' 
			self.controlView.set_text(texto)
			texto=''
			self.turnoBlanco= not self.turnoBlanco
			self.controlView.change_turnos()
			self.controlView.dibujar(self.tablero)
			return
		#------------------------------------------------------------------------------------------------------

		#Enroque largo
		#------------------------------------------------------------------------------------------------------
		if(self.tablero[fila1][col1].name=='R' and self.tablero[fila1][col1].aviso) and mov[1][1]==2:
			self.tablero[fila1][col1].aviso=False
			#Muevo torre
			self.tablero[fila1][0].casilla=(fila1,3)
			self.tablero[fila1][0].set_Imagen((fila1,3))
			
			torre = self.tablero[fila1].pop(0)
			self.tablero[fila1].insert(0,None)
			
			self.tablero[fila1].pop(3)
			self.tablero[fila1].insert(3,torre)

			#Muevo rey
			self.tablero[fila1][4].casilla=(fila1,2)
			self.tablero[fila1][4].set_Imagen((fila1,2))
			
			rey = self.tablero[fila1].pop(4)
			self.tablero[fila1].insert(4,None)
			
			self.tablero[fila1].pop(2)
			self.tablero[fila1].insert(2,rey)

			#anoto
			if(self.turnoBlanco):
				self.contador=self.contador+1
				texto= str(self.contador)+'. '+'0-0-0' 
			else:
				texto='  '+'0-0-0'+'\n' 
			self.controlView.set_text(texto)
			texto=''
			self.turnoBlanco= not self.turnoBlanco
			self.controlView.change_turnos()
			self.controlView.dibujar(self.tablero)
			return
		#------------------------------------------------------------------------------------------------------


		
		if jugada:
	 
			if(self.turnoBlanco):			
				self.contador=self.contador+1
			pieza.casilla=mov[1]
			pieza.set_Imagen(mov[1])
			
			
			
				
				
			pza=self.tablero[fila1].pop(col1)
			self.tablero[fila1].insert(col1,None)
			
			guardo=self.tablero[fila2].pop(col2)
			self.tablero[fila2].insert(col2,pza)

			#verificar jaque descubierto
			#-----------------------------------------
			if (not self.verificarDescubierto()):
				#volver pa atras
				
			
				pza=self.tablero[fila2].pop(col2)

				pieza.casilla=mov[0]
				pieza.set_Imagen(mov[0])
			
				self.tablero[fila1].pop(col1)
				self.tablero[fila1].insert(col1,pza)

				self.tablero[fila2].insert(col2,guardo)
				self.controlView.set_mensaje("Movimiento ilegal")	
				
				return
			#-----------------------------------------

			self.controlView.dibujar(self.tablero)
			
			if(self.turnoBlanco):
				texto= str(self.contador)+'. '+pieza.name+self.casillas[col2]+str(fila2+1) 
			else:
				texto='  '+pieza.name+self.casillas[col2]+str(fila2+1)+'\n' 
			self.controlView.set_text(texto)
			texto=''
			self.turnoBlanco= not self.turnoBlanco
			self.controlView.change_turnos()
	
	
        return
#########################################################################################################







#########################################################################################################
    def verificarDescubierto(self):
		
		
		########################################
		#El jaque por descubierto solo lo pueden
		# hacer la torre, el alfil y la dama
		########################################
		jugada=True
		
		if(self.turnoBlanco):
		   for filas in self.tablero:
			for casilla in filas:
			     try:
				
				if((casilla.name=='T'  or casilla.name=='A' or casilla.name =='D') and casilla.color=='N'):
					j=casilla.verificar_descubierto(self.tablero)
					jugada= jugada and j
			     except:	
				 a=1		
		else:
		    for filas in self.tablero:
			for casilla in filas:
			     try:
				
				if((casilla.name=='T'  or casilla.name=='A' or casilla.name =='D') and casilla.color=='B'):
					j=casilla.verificar_descubierto(self.tablero)
					jugada= jugada and j
			     except:	
				 a=1	
		 		
		print "JAQUE DESCUBIERTO: ",jugada
		return jugada
#########################################################################################################



