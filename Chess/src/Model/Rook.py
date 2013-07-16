from Pieza import *
from Square import *

class Torre(Pieza):



#####################################################################################################################
	def set_Imagen(self,casilla):
		if ((casilla[0]+casilla[1])%2) == 0 :
			self.imagen= 'Images/set1/Torre'+self.color+'N'+'.jpg'
		else: 
			self.imagen= 'Images/set1/Torre'+self.color+'B'+'.jpg'
#####################################################################################################################






#####################################################################################################################
        def setCasilla(self,pos):	
		self.casilla = pos
#####################################################################################################################






#####################################################################################################################
	def legalMove(self, des,tablero):

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
				if not(isinstance(tablero[k][self.casilla[1]],Square)):
					jugada= False
				k=k+c	

		#Mueve horizontal
		if (self.casilla[0]==des[0]):
			jugada= True
	 		if (self.casilla[1]>des[1]):
				c = -1
	   		k= self.casilla[1]+ c
	   		while k != des[1]:	
				if not(isinstance(tablero[self.casilla[0]][k],Square)):
					jugada= False
				k=k+c	

	
		return jugada

#####################################################################################################################



#####################################################################################################################
	def verificar_descubierto(self,tablero):

		
		
		jugada = False		
		jugada_abajo=True
		jugada_arriba=True
		jugada_izq=True
		jugada_der=True

		#verifica horizontal
		#------------------------------------------------------------------------
		col=self.casilla[1]-1
		fil=self.casilla[0]
		while(col>=0):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jugada_abajo=False
				break
			col=col-1
		col=self.casilla[1]+1
		while(col<=7):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color))):
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jugada_arriba=False
				break
			col=col+1


		#verifica vertical
		#------------------------------------------------------------------------
		col=self.casilla[1]
		fil=self.casilla[0]-1
		while(fil>=0):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jugada_izq=False
				break
			fil=fil-1
		fil=self.casilla[0]+1
		while(fil<=7):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color))):
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jugada_der=False
				break
			fil=fil+1
		
		jugada= (jugada_abajo and jugada_arriba) and (jugada_izq and jugada_der)
		
		return jugada
#####################################################################################################################




#####################################################################################################################
	def verificar_jaque(self, tablero):

		
		jaque = False		
		jaque_abajo=False
		jaque_arriba=False
		jaque_izq=False
		jaque_der=False

		#verifica horizontal
		#------------------------------------------------------------------------
		col=self.casilla[1]-1
		fil=self.casilla[0]
		while(col>=0):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				jaque_abajo=False				
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jaque_abajo=True
				break
			col=col-1
		col=self.casilla[1]+1
		while(col<=7):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color))):
				jaque_arriba=False				
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jaque_arriba=True
				break
			col=col+1


		#verifica vertical
		#------------------------------------------------------------------------
		col=self.casilla[1]
		fil=self.casilla[0]-1
		while(fil>=0):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				jaque_izq=False				
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jaque_izq=True
				break
			fil=fil-1
		fil=self.casilla[0]+1
		while(fil<=7):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color))):
				jaque_der=False				
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jaque_der=True
				break
			fil=fil+1
		
		jaque= (jaque_abajo or jaque_arriba) or (jaque_izq or jaque_der)
		
		return jaque


#####################################################################################################################
