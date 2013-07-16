from Pieza import *
from Square import *

class Alfil(Pieza):




#####################################################################################################################

	def set_Imagen(self,casilla):
		
		if ((casilla[0]+casilla[1])%2) == 0 :
			self.imagen= 'Images/set1/Alfil'+self.color+'N'+'.jpg'
		else: 
			self.imagen= 'Images/set1/Alfil'+self.color+'B'+'.jpg'
#####################################################################################################################





#####################################################################################################################
	def legalMove(self, des,tablero):

		
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
			if not(isinstance(tablero[fila][col],Square)):
				break
		
		return jugada

#####################################################################################################################







##########################################################################################################################
	def verificar_descubierto(self,tablero):
		
		jugada_izq_ab=True
		jugada_izq_ar=True
		jugada_der_ab=True
		jugada_der_ar=True

		#Verifica hacia la izq
		#-------------------------------------------------------------------

		#Abajo
		fil=self.casilla[0]-1
		col=self.casilla[1]-1
		while(fil>=0 and col>=0):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jugada_izq_ab=False
				break
			fil=fil-1
			col=col-1
		
		#Arriba	
		fil=self.casilla[0]+1
		col=self.casilla[1]-1
		while(fil<=7 and col>=0):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jugada_izq_ar=False
				break
			fil=fil+1
			col=col-1	

		#Verifica hacia la der
		#-------------------------------------------------------------------

		#Abajo
		fil=self.casilla[0]-1
		col=self.casilla[1]+1
		while(fil>=0 and col<=7):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jugada_der_ab=False
				break
			fil=fil-1
			col=col+1
		
		#Arriba	
		fil=self.casilla[0]+1
		col=self.casilla[1]+1
		while(fil<=7 and col>=0):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jugada_der_ar=False
				break
			fil=fil+1
			col=col+1	

		jugada=(jugada_izq_ab and jugada_izq_ar) and (jugada_der_ab and jugada_der_ar)
		return jugada

##########################################################################################################################


##########################################################################################################################
	def verificar_jaque(self, tablero):
		
		jaque = False
		
		
		jaque_izq_ab=False
		jaque_izq_ar=False
		jaque_der_ab=False
		jaque_der_ar=False

		#Verifica hacia la izq
		#-------------------------------------------------------------------

		#Abajo
		fil=self.casilla[0]-1
		col=self.casilla[1]-1
		while(fil>=0 and col>=0):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				jaque_izq_ab=False	
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jaque_izq_ab=True
				break
			fil=fil-1
			col=col-1
		
		#Arriba	
		fil=self.casilla[0]+1
		col=self.casilla[1]-1
		while(fil<=7 and col>=0):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				jaque_izq_ar=False
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jaque_izq_ar=True
				break
			fil=fil+1
			col=col-1	
		
		#Verifica hacia la der
		#-------------------------------------------------------------------

		#Abajo
		fil=self.casilla[0]-1
		col=self.casilla[1]+1
		while(fil>=0 and col<=7):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				jaque_der_ab=False
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jaque_der_ab=True
				break
			fil=fil-1
			col=col+1
		
		#Arriba	
		fil=self.casilla[0]+1
		col=self.casilla[1]+1
		while(fil<=7 and col<=0):
			if(not(isinstance(tablero[fil][col],Square)) and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				jaque_der_ar=False
				break
			
			if(not(isinstance(tablero[fil][col],Square)) and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				jaque_der_ar=True
				break
			fil=fil+1
			col=col+1	
		
		jaque=(jaque_izq_ab or jaque_izq_ar) or (jaque_der_ab or jaque_der_ar)
		return jaque
##########################################################################################################################


