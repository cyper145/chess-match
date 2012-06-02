

class Dama():

#####################################################################################################################
	def __init__(self,color,casilla):

		self.color=color
		self.casilla=casilla
		self.name='D'

		self.set_Imagen(self.casilla)


#####################################################################################################################




#####################################################################################################################

	def set_Imagen(self,casilla):
		
		if ((casilla[0]+casilla[1])%2) == 0 :
			self.imagen= 'Images/set1/Dama'+self.color+'N'+'.jpg'
		else: 
			self.imagen= 'Images/set1/Dama'+self.color+'B'+'.jpg'
#####################################################################################################################



#####################################################################################################################
	def validar_Movimiento(self, des,tablero):
		print "Validar dama"
		if(self.validar_torre(des,tablero) or self.validar_alfil(des,tablero)):
			return True
		else:
			return False
		
#####################################################################################################################

#####################################################################################################################
	def validar_torre(self, des,tablero):
		jugada = False
		c=1
	
		#Mueve vertical
		if (self.casilla[1]==des[1]):
			jugada= True
	   		if (self.casilla[0]>des[0]):
				c = -1
	   		k= self.casilla[0]+ c
	   		while k != des[0]:	
				if (tablero[k][self.casilla[1]] != 'Blanco' and tablero[k][self.casilla[1]]!= 'Negro'):
					jugada= False
				k=k+c	

		#Mueve horizontal
		if (self.casilla[0]==des[0]):
			jugada=True
	 		if (self.casilla[1]>des[1]):
				c = -1
	   		k= self.casilla[1]+ c
	   		while k != des[1]:	
				if (tablero[self.casilla[0]][k] != 'Blanco' and tablero[self.casilla[0]][k]!= 'Negro'):
					jugada= False
				k=k+c	

	

		return jugada

#####################################################################################################################

#####################################################################################################################
	def validar_alfil(self, des,tablero):
		jugada=False
		d_c=1
		d_f=1
		fila=self.casilla[0]
		col=self.casilla[1]
		if(self.casilla[0]>des[0]):
			d_f=-1	
		if(self.casilla[1]>des[1]):
			d_c=-1
	
		for k in range (abs(self.casilla[1] - des[1])):
			fila=fila + d_f
			col= col + d_c
			if (des[0] == fila and des[1]==col):
				jugada = True
			if (tablero[fila][col] != 'Blanco' and tablero[fila][col] != 'Negro'):
				break
		return jugada

#####################################################################################################################
