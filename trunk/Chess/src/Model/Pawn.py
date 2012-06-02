
class Peon():

#####################################################################################################################
	def __init__(self,color,casilla):

		self.color=color
		self.casilla=casilla
		self.name=""
		
		self.set_Imagen(self.casilla)
		
#####################################################################################################################


#####################################################################################################################

	def set_Imagen(self,casilla):
		
		if ((casilla[0]+casilla[1])%2) == 0 :
			self.imagen= 'Images/set1/Peon'+self.color+'N'+'.jpg'
		else: 
			self.imagen= 'Images/set1/Peon'+self.color+'B'+'.jpg'
#####################################################################################################################



#####################################################################################################################
	def validar_Movimiento(self, des,tablero):

		print "VALIDAR PEON"
		jugada = False
		
	

		if self.color=='B':
	  	#--------PEON BLANCO--------------------	

	  		#Misma columna- se mueve para adelante	
	  		if(self.casilla[1]==des[1] and (tablero[des[0]][des[1]]=='Blanco' or tablero[des[0]][des[1]]=='Negro')):	
	    
	    			#Una casilla para adelante - tiene q estar desocupada			
	    			if (self.casilla[0]+1)==des[0]:
					jugada=True
	    			#Dos casillas adelante - tiene q estar vacia y ser entre las filas 1 y 3
	    			if (self.casilla[0] == 1 and des[0]==3 and (tablero[2][des[1]]=='Blanco' or tablero[2][des[1]]=='Negro')):
					jugada=True

	  		#Distinta columna - come pieza
	  		elif (self.casilla[1]==des[1]+1 or self.casilla[1]==des[1]-1)  and (tablero[des[0]][des[1]].color=='N'):
				if (self.casilla[0]==des[0]-1 ):
					jugada=True


		else:
		#--------PEON NEGRO--------------------	

	  		#Misma columna- se mueve para adelante	
	  		if(self.casilla[1]==des[1] and (tablero[des[0]][des[1]]=='Blanco' or tablero[des[0]][des[1]]=='Negro')):	
	   
		    		#Una casilla para adelante - tiene q estar desocupada			
		    		if (self.casilla[0]-1)==des[0]:
					jugada=True
	  
		    		#Dos casillas adelante - tiene q estar vacia y ser entre las filas 1 y 3
	    	    		if (self.casilla[0] == 6 and des[0]==4 and (tablero[5][self.casilla[1]]=='Blanco' or tablero[5][self.casilla[1]]=='Negro')):
					jugada=True
	
	  		#Distinta columna - come pieza
	  		elif (self.casilla[1]==des[1]+1 or self.casilla[1]==des[1]-1)  and (tablero[des[0]][des[1]].color=='B'):
				if (self.casilla[0]==des[0]+1 ):
					jugada=True
	
		return jugada


#####################################################################################################################


#####################################################################################################################
	def set_Casilla(self,casilla):
		self.casilla=casilla
#####################################################################################################################
