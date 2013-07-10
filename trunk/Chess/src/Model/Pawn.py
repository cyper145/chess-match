
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
        def setCasilla(self,pos):
	       print "Peon set Casilla"	
	       print pos	
               self.casilla = pos
#####################################################################################################################




#####################################################################################################################
	def legalMove(self, des,tablero):

		jugada = False
                print "PEON----->" + self.color
                if self.color=='B':
	  	#--------PEON BLANCO--------------------	

	  		#Misma columna- se mueve para adelante	
	  		if(self.casilla[1]==des[1] and (tablero[des[0]][des[1]]==None)):	
	    
	    			#Una casilla para adelante - tiene q estar desocupada			
	    			if (self.casilla[0]+1)==des[0]:
					jugada=True
	    			#Dos casillas adelante - tiene q estar vacia y ser entre las filas 1 y 3
	    			if (self.casilla[0] == 1 and des[0]==3 and (tablero[2][des[1]]==None)):
					jugada=True

	  		#Distinta columna - come pieza
	  		elif (self.casilla[1]==des[1]+1 or self.casilla[1]==des[1]-1)  and (tablero[des[0]][des[1]].color=='N'):
                                
				if (self.casilla[0]==des[0]-1 ):
                                       
					jugada=True


		else:
		#--------PEON NEGRO--------------------	

	  		#Misma columna- se mueve para adelante	
	  		if(self.casilla[1]==des[1] and (tablero[des[0]][des[1]]==None)):	
	   
		    		#Una casilla para adelante - tiene q estar desocupada			
		    		if (self.casilla[0]-1)==des[0]:
					jugada=True
	  
		    		#Dos casillas adelante - tiene q estar vacia y ser entre las filas 1 y 3
	    	    		if (self.casilla[0] == 6 and des[0]==4 and (tablero[5][self.casilla[1]]==None)):
					jugada=True
	
	  		#Distinta columna - come pieza
	  		elif (self.casilla[1]==des[1]+1 or self.casilla[1]==des[1]-1)  and (tablero[des[0]][des[1]].color=='B'):
                                print "peon------"
                                print self.casilla[0]
                                print des[0]+1
				if (self.casilla[0]==des[0]+1 ):
                                        print "peon2"
					jugada=True
	
		return jugada


#####################################################################################################################






#####################################################################################################################
	def verificar_jaque(self, tablero):
	
		##################################
		#El peon ataca solo dos casillas
	        # Se comprueba q el rey enemigo
		# no este en ninguna de las dos
		######################################
		d_f=1
		color_enemigo='N'
		jaque = False
	
		if self.color == 'N':
			d_f= -1
			color_enemigo='B'
		fila = self.casilla[0] + d_f
		try:
			if (tablero[fila][self.casilla[1]+1].name=='R' and tablero[fila][self.casilla[1]+1].color== color_enemigo ):
				jaque = True
			if (tablero[fila][self.casilla[1]-1].name=='R' and tablero[fila][self.casilla[1]-1].color== color_enemigo ):
				jaque= True

		except:
			a=1
		return jaque

#####################################################################################################################




