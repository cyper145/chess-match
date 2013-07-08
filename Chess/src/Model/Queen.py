

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
        def setCasilla(self,pos):	
		self.casilla = pos
#####################################################################################################################





#####################################################################################################################
	def legalMove(self, des,tablero):
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
				if (tablero[k][self.casilla[1]] != None):
					jugada= False
				k=k+c	

		#Mueve horizontal
		if (self.casilla[0]==des[0]):
			jugada=True
	 		if (self.casilla[1]>des[1]):
				c = -1
	   		k= self.casilla[1]+ c
	   		while k != des[1]:	
				if (tablero[self.casilla[0]][k] != None):
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
			if (tablero[fila][col] != None):
				break
		return jugada

##########################################################################################################################



##########################################################################################################################
	def verificar_descubierto(self,tablero):
		

		t_jugada_ab=True
		t_jugada_ar=True
		t_jugada_izq=True
		t_jugada_der=True

		a_jugada_izq_ab=True
		a_jugada_izq_ar=True
		a_jugada_der_ab=True
		a_jugada_der_ar=True

		########################### Movimiento de torre################################
		#verifica horizontal
		#------------------------------------------------------------------------
		col=self.casilla[1]-1
		fil=self.casilla[0]
		while(col>=0):
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
		
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				t_jugada_ab=False
				break
			col=col-1
		col=self.casilla[1]+1
		while(col<=7):
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color))):
				break
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				t_jugada_ar=False
				break
			col=col+1


		#verifica vertical
		#------------------------------------------------------------------------
		col=self.casilla[1]
		fil=self.casilla[0]-1
		while(fil>=0):
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				
				break
			
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				t_jugada_izq=False
				break
			fil=fil-1
		fil=self.casilla[0]+1
		while(fil<=7):
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color))):
				
				break
			
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				t_jugada_der=False
				break
			fil=fil+1

		t_jugada= (t_jugada_ab and t_jugada_ar) and (t_jugada_izq and t_jugada_der)
		#####################################################################################################################



		################################### Movimiento de alfil ##############################################################

		#Verifica hacia la izq
		#-------------------------------------------------------------------

		#Abajo
		fil=self.casilla[0]-1
		col=self.casilla[1]-1
		while(fil>=0 and col>=0):
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
			
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				a_jugada_izq_ab=False
				break
			fil=fil-1
			col=col-1
		
		#Arriba	
		fil=self.casilla[0]+1
		col=self.casilla[1]-1
		while(fil<=7 and col>=0):
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
		
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				a_jugada_izq_ar=False
				break
			fil=fil+1
			col=col-1	

		#Verifica hacia la der
		#-------------------------------------------------------------------

		#Abajo
		fil=self.casilla[0]-1
		col=self.casilla[1]+1
		while(fil>=0 and col<=7):
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
			
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				a_jugada_der_ab=False
				break
			fil=fil-1
			col=col+1
		
		#Arriba	
		fil=self.casilla[0]+1
		col=self.casilla[1]+1
		while(fil<=7 and col<=0):
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				break
			
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				a_jugada_der_ar=False
				break
			fil=fil+1
			col=col+1	

		a_jugada=(a_jugada_izq_ab and a_jugada_izq_ar) and (a_jugada_der_ab and a_jugada_der_ar)
		jugada = t_jugada and a_jugada
		
		return jugada

##########################################################################################################################



##########################################################################################################################
	def verificar_jaque(self, tablero):

		t_jaque_ab=False
		t_jaque_ar=False
		t_jaque_izq=False
		t_jaque_der=False

		a_jaque_izq_ab=False
		a_jaque_izq_ar=False
		a_jaque_der_ab=False
		a_jaque_der_ar=False

		
		########################### Movimiento de torre################################
		#verifica horizontal
		#------------------------------------------------------------------------
		col=self.casilla[1]-1
		fil=self.casilla[0]
		while(col>=0):
			
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				t_jaque_ab=False				
				break
		
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				t_jaque_ab=True
				break
			col=col-1
		col=self.casilla[1]+1
		while(col<=7):
			
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color))):
				t_jaque_ar=False				
				break
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				t_jaque_ar=True
				break
			col=col+1


		#verifica vertical
		#------------------------------------------------------------------------
		col=self.casilla[1]
		fil=self.casilla[0]-1
		while(fil>=0):
			
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				t_jaque_izq=False
				break
			
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				t_jaque_izq=True
				break
			fil=fil-1
		fil=self.casilla[0]+1
		while(fil<=7):
			
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color))):
				t_jaque_der=False
				break
			
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				t_jaque_der=True
				break
			fil=fil+1

		t_jaque= (t_jaque_ab or t_jaque_ar) or (t_jaque_izq or t_jaque_der)
		#####################################################################################################################



		################################### Movimiento de alfil ##############################################################

		#Verifica hacia la izq
		#-------------------------------------------------------------------

		#Abajo
		fil=self.casilla[0]-1
		col=self.casilla[1]-1
		while(fil>=0 and col>=0):
			
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				a_jaque_izq_ab=False				
				break
			
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				a_jaque_izq_ab=True
				break
			fil=fil-1
			col=col-1
		
		#Arriba	
		fil=self.casilla[0]+1
		col=self.casilla[1]-1
		while(fil<=7 and col>=0):
			
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				a_jaque_izq_ar=False				
				break
		
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				a_jaque_izq_ar=True
				break
			fil=fil+1
			col=col-1	

		#Verifica hacia la der
		#-------------------------------------------------------------------

		#Abajo
		fil=self.casilla[0]-1
		col=self.casilla[1]+1
		while(fil>=0 and col<=7):
			
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				a_jaque_der_ab=False
				break
			
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				a_jaque_der_ab=True
				break
			fil=fil-1
			col=col+1
		
		#Arriba	
		fil=self.casilla[0]+1
		col=self.casilla[1]+1
		while(fil<=7 and col<=7):
			
			if(tablero[fil][col]!=None and (not(tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)) ):
				
				a_jaque_der_ar=False					
				break
			
			if(tablero[fil][col]!=None and (tablero[fil][col].name=='R' and tablero[fil][col].color!=self.color)):
				a_jaque_der_ar=True
				break
			fil=fil+1
			col=col+1	
			

		
		a_jaque=(a_jaque_izq_ab or a_jaque_izq_ar) or (a_jaque_der_ab or a_jaque_der_ar)
		jaque = t_jaque or a_jaque
		
		return jaque
#####################################################################################################################
