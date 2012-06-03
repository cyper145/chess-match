
class Caballo():

#####################################################################################################################
	def __init__(self,color,casilla):

		self.color=color
		self.casilla=casilla
		self.name='C'
		self.set_Imagen(self.casilla)


#####################################################################################################################



#####################################################################################################################

	def set_Imagen(self,casilla):
		
		if ((casilla[0]+casilla[1])%2) == 0 :
			self.imagen= 'Images/set1/Caballo'+self.color+'N'+'.jpg'
		else: 
			self.imagen= 'Images/set1/Caballo'+self.color+'B'+'.jpg'
#####################################################################################################################



#####################################################################################################################
	def validar_Movimiento(self, des,tablero):

		
		jugada = False

		if (abs(self.casilla[0]-des[0]) == 2 and abs(self.casilla[1]-des[1])==1):
			jugada=True

		if (abs(self.casilla[1]-des[1]) == 2 and abs(self.casilla[0]-des[0])==1):
			jugada=True


		return jugada

#####################################################################################################################
