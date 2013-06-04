
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


#####################################################################################################################
	def verificar_jaque(self, tablero):


		#############################
		# Como maximo el caballo ataca
		# 8 casillas
		#############################
		jaque = False
		d_fila=2
		d_col=1
		
		
		for i in range(2):
			for j in range(2):
				for k in range(2):
				
					f=self.casilla[0]+ d_fila
					c=self.casilla[1]+d_col
					try:
						if (tablero[f][c].name=='R' and tablero[f][c].color != self.color):
							jaque = True
							break
					except:
						a=1
					
					d_col=d_col*(-1)
				d_fila=d_fila*(-1)
			d_fila=1
			d_col=2

				
		return jaque

#####################################################################################################################
