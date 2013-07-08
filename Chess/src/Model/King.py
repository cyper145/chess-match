

class Rey():

#####################################################################################################################
	def __init__(self,color,casilla):

		self.color=color
		self.casilla=casilla
		self.name='R'
		self.set_Imagen(self.casilla)
		self.enroque=True
		self.aviso=False

#####################################################################################################################




#####################################################################################################################

	def set_Imagen(self,casilla):
		
		if ((casilla[0]+casilla[1])%2) == 0 :
			self.imagen= 'Images/set1/Rey'+self.color+'N'+'.jpg'
		else: 
			self.imagen= 'Images/set1/Rey'+self.color+'B'+'.jpg'
#####################################################################################################################




#####################################################################################################################
        def setCasilla(self,pos):	
		self.casilla = pos
#####################################################################################################################




#####################################################################################################################
	def legalMove(self, des,tablero):

		jugada=False
		
		if((abs(self.casilla[0]-des[0])<=1) and (abs(self.casilla[1]-des[1])<=1)):
			jugada=True
			self.enroque=False
			return jugada
		
		#Enroque corto
		#-------------------------------------------------------------------------
		if((des[1]==6 and self.enroque) and (des[0]==self.casilla[0])):
			if(tablero[des[0]][5]==None and tablero[des[0]][6]==None):
				try:
					if(tablero[des[0]][7].enroque):				
						jugada=True
						self.enroque=False
						self.aviso=True
						return jugada
				except:
					print"No hay torre!!"
		#-------------------------------------------------------------------------

			
		#Enroque largo
		#-------------------------------------------------------------------------
		if((des[1]==2 and self.enroque) and (des[0]==self.casilla[0])):
			if((tablero[des[0]][3]==None and tablero[des[0]][2]==None)and tablero[des[0]][1]==None):
				try:
					if(tablero[des[0]][0].enroque):				
						jugada=True
						self.enroque=False
						self.aviso=True
						return jugada
				except:
					print"No hay torre!!"
		#-------------------------------------------------------------------------

		return jugada

#####################################################################################################################

                """ debe realizarse en la clase Rey
		#Enroque corto 
		#------------------------------------------------------------------------------------------------------
		if(pieza.name=='R' and pieza.aviso) and col2==6:
			pieza.aviso=False
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
			self.controlView.actual=self.controlView.actual +1
			self.controlView.actual_aux=self.controlView.actual_aux +1
			self.controlView.tablero_to_string(self.tablero)
			#self.controlView.partida.append(self.tablero)
			return True
		#------------------------------------------------------------------------------------------------------
		
		#Enroque largo
		#------------------------------------------------------------------------------------------------------
		if(pieza.name=='R' and pieza.aviso) and mov[1][1]==2:
			pieza.aviso=False
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
			self.controlView.actual=self.controlView.actual +1
			self.controlView.actual_aux=self.controlView.actual_aux +1
			self.controlView.tablero_to_string(self.tablero)
			#self.controlView.partida.append(self.tablero)
			return True
		#------------------------------------------------------------------------------------------------------
		"""

#####################################################################################################################
	def verificar_jaque(self,tablero):
		return False
#####################################################################################################################
