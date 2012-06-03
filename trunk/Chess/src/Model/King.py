

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
	def validar_Movimiento(self, des,tablero):

		print "Validar rey"
		jugada=False
		
		if((abs(self.casilla[0]-des[0])<=1) and (abs(self.casilla[1]-des[1])<=1)):
			jugada=True
			self.enroque=False
			return jugada
		
		#Enroque corto
		#-------------------------------------------------------------------------
		if((des[1]==6 and self.enroque) and (des[0]==self.casilla[0])):
			if(tablero[des[0]][5][-1]=='o' and tablero[des[0]][6][-1]=='o'):
				try:
					if(tablero[des[0]][7].enroque):				
						jugada=True
						self.enroque=False
						self.aviso=True
				except:
					print"No hay torre!!"
					
		return jugada

#####################################################################################################################
