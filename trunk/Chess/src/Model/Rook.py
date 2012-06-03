
class Torre():

#####################################################################################################################
	def __init__(self,color,casilla):

		self.color=color
		self.casilla=casilla
		self.name='T'
		self.enroque=True
		self.set_Imagen(self.casilla)


#####################################################################################################################



#####################################################################################################################

	def set_Imagen(self,casilla):
		
		if ((casilla[0]+casilla[1])%2) == 0 :
			self.imagen= 'Images/set1/Torre'+self.color+'N'+'.jpg'
		else: 
			self.imagen= 'Images/set1/Torre'+self.color+'B'+'.jpg'
#####################################################################################################################



#####################################################################################################################
	def validar_Movimiento(self, des,tablero):

		print "Validar torre"
		jugada = False
		c=1
		self.enroque=False
		#Mueve vertical
		if (self.casilla[1]==des[1]):
			jugada = True
	   		if (self.casilla[0]>des[0]):
				c = -1
	   		k= self.casilla[0]+ c
	   		while k != des[0]:	
				if (tablero[k][self.casilla[1]] != 'Blanco' and tablero[k][self.casilla[1]]!= 'Negro'):
					jugada= False
				k=k+c	

		#Mueve horizontal
		if (self.casilla[0]==des[0]):
			jugada= True
	 		if (self.casilla[1]>des[1]):
				c = -1
	   		k= self.casilla[1]+ c
	   		while k != des[1]:	
				if (tablero[self.casilla[0]][k] != 'Blanco' and tablero[self.casilla[0]][k]!= 'Negro'):
					jugada= False
				k=k+c	

	

		return jugada

#####################################################################################################################
