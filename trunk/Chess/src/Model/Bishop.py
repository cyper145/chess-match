

class Alfil():

#####################################################################################################################
	def __init__(self,color,casilla):

		self.color=color
		self.casilla=casilla
		self.name='A'

		self.set_Imagen(self.casilla)


#####################################################################################################################




#####################################################################################################################

	def set_Imagen(self,casilla):
		
		if ((casilla[0]+casilla[1])%2) == 0 :
			self.imagen= 'Images/set1/Alfil'+self.color+'N'+'.jpg'
		else: 
			self.imagen= 'Images/set1/Alfil'+self.color+'B'+'.jpg'
#####################################################################################################################


#####################################################################################################################
	def validar_Movimiento(self, des,tablero):

		print "Validar alfil"
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

