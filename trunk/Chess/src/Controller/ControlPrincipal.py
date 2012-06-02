
from ControlVista import *

class ControlPrincipal():

 
#########################################################################################################
    def __init__(self):

        self.controlView = ControlVista(self)

        self.tablero =[['TorreBN','CaballoBB','AlfilBN','DamaBB','ReyBN','AlfilBB','CaballoBN','TorreBB'],
                   ['PeonBB','PeonBN','PeonBB','PeonBN','PeonBB','PeonBN','PeonBB','PeonBN'],
                   ['Negro','Blanco','Negro','Blanco','Negro','Blanco','Negro','Blanco'],
                   ['Blanco','Negro','Blanco','Negro','Blanco','Negro','Blanco','Negro',],
                   ['Negro','Blanco','Negro','Blanco','Negro','Blanco','Negro','Blanco'],
                   ['Blanco','Negro','Blanco','Negro','Blanco','Negro','Blanco','Negro',],
                   ['PeonNN','PeonNB','PeonNN','PeonNB','PeonNN','PeonNB','PeonNN','PeonNB'],
                   ['TorreNB','CaballoNN','AlfilNB','DamaNN','ReyNB','AlfilNN','CaballoNB','TorreNN']]

        self.controlView.dibujar(self.tablero)           
#########################################################################################################






#########################################################################################################
    def validarMovimiento(self,mov): 

	fila1= mov[0][0]
	col1= mov[0][1]	
	fila2= mov[1][0]
	col2= mov[1][1]	
	

	
	if pieza == 'T':
		self.validarTorre(mov)
	if pieza == 'C':
		self.validarCaballo(mov)
	if pieza == 'A':
		self.validarAlfil(mov)
	if pieza == 'D':
		self.validarDama(mov)
	if pieza == 'R':
		self.validarRey(mov)
	if pieza == 'P':
		self.validarPeon(mov)
	
	if (self.tablero[fila2][col2] == 'Negro' or self.tablero[fila2][col2] == 'Blanco'):

			
			if (self.tablero[fila1][col1][-1] == 'B'):
				print "3"
				if (self.tablero[fila2][col2]=='Negro' or self.tablero[fila2][col2][-1]=='N'):  
					im= self.tablero[fila1][col1][:-1]+ 'N'
					print "IM "+im
					self.tablero[fila2].pop(col2)
					self.tablero[fila2].insert(col2,im)
				else:
					self.tablero[fila2].pop(col2)		
					self.tablero[fila2].insert(col2,self.tablero[fila1][col1])
	
				self.tablero[fila1].pop(col1)
				self.tablero[fila1].insert(col1,'Blanco')
				
			
			else:	
				print "4"
				if (self.tablero[fila2][col2]=='Blanco' or self.tablero[fila2][col2][-1]=='B'):  
					im= self.tablero[fila1][col1][:-1]+ 'B'
					self.tablero[fila2].pop(col2)
					self.tablero[fila2].insert(col2,im)
				else:
					self.tablero[fila2].pop(col2)		
					self.tablero[fila2].insert(col2,self.tablero[fila1][col1])

				self.tablero[fila1].pop(col1)			
				self.tablero[fila1].insert(col1,'Negro')

			print self.tablero

			self.controlView.dibujar(self.tablero) 
        return
#########################################################################################################




#########################################################################################################
    def validarTorre(self,mov):
	print "Validar torre"

#########################################################################################################


#########################################################################################################
    def validarCaballo(self,mov):
	print "Validar caballo"

#########################################################################################################


#########################################################################################################
    def validarAlfil(self,mov):
	print "Validar alfil"

#########################################################################################################



#########################################################################################################
    def validarDama(self,mov):
	print "Validar dama"

#########################################################################################################


#########################################################################################################
    def validarRey(self,mov):
	print "Validar rey"

#########################################################################################################


#########################################################################################################
    def validarPeon(self,mov):
	print "Validar peon"
	jugada = False
	if(mov[0][1]+1)==mov[1][1] and (self.tablero[mov[1][0]][mov[1][1]]=='Blanco' or self.tablero[mov[1][0]][mov[1][1]]=='Negro'):
		jugada=True
	if (mov[0][1] == 1 and mov[1][1]==3) and (self.tablero[mov[1][0]][mov[1][1]]=='Blanco' or self.tablero[mov[1][0]][mov[1][1]]=='Negro'):
		jugaa=True
	
#########################################################################################################
