from Pieza import *


class Square(Pieza):




#####################################################################################################################

	def set_Imagen(self,casilla):
		if ((casilla[0]+casilla[1])%2) == 0 :
			self.imagen= 'Images/set1/Negro.jpg'
		else: 
			self.imagen= 'Images/set1/Blanco.jpg'
#####################################################################################################################


