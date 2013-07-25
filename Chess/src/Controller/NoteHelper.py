import re
from Model.Square import *

class NoteHelper():



	def __init__(self, control):
	
		self.control = control
		self.lCastle = "O-O-O"
		self.sCastle = "O-O"
		self.columnas = ['a','b','c','d','e','f','g','h']
		self.checkCharacters = ['+', '#','++']	
	





#########################################################################################################################################################################
    	def readMove(self,j):
		"""Transforma la jugada leida en notacion algebraica en un movimiento de pieza en el tablero"""
		self.tablero = self.control.getTablero()
		#---------------------------------------------ENROQUE LARGO----------------------------------------------
		if(self.lCastle in j):
			return self.longCastle()		
		#---------------------------------------------ENROQUE CORTO----------------------------------------------
		if(self.sCastle in j):
			return self.shortCastle()
	
		#--------------------------------------------------------------------------------------------------------
		#Variables comunes a todas las piezas Saca la fila destino- el except es por que puede haber un jaque '+'
		fila = self.readRow(j)
		columna = self.readCol(j)

		
		color='B'
		if(not self.control.getTurn()): color='N'

		if(j[-1] in self.checkCharacters): 
			j=j[0:-1]
		#-------------------------PEON----------------------------------------------------------------------------
		if(j[0] in self.columnas):
			return self.readPawn(j)
		#-------------------------TORRE---------------------------------------------------------------------------	
		if(j[0]=='R'):
			return self.readRook(j)
		#------------------------CABALLO--------------------------------------------------------------------------
		if(j[0]=='N'):
			return self.readKnight(j)
		#-------------------------ALFIL---------------------------------------------------------------------------
		if(j[0]=='B'):
			return self.readBishop(j)
		#--------------------------DAMA---------------------------------------------------------------------------
		if(j[0]=='Q'):
			return self.readQueen(j)
		#--------------------------REY----------------------------------------------------------------------------
		if(j[0]=='K'):
			return self.readKing(j)
				
		
################################################################################################################################################################











#............................................................................................................................................................
	def longCastle(self):

		if(self.control.getTurn()): 
			return [1000, 0],0
		else: 
			return [1000, 1],0
#............................................................................................................................................................






#............................................................................................................................................................
	def shortCastle(self):
	
		if(self.control.getTurn()): 
			return [100, 0],0
		else: 
			return [100, 1],0
#............................................................................................................................................................







	
#............................................................................................................................................................
	def readRow(self, j):
	
		fila = -1
		try:
			fila=int(j[-1])-1
		except:
			try:
				fila=int(j[-2])-1
			except: pass
		
		return fila
#............................................................................................................................................................






#............................................................................................................................................................
	def readCol(self, j):
	
		columna = -1
		try:
			columna=self.casillas.index(j[-2])
		except:
			try:
				columna=self.casillas.index(j[-3])
			except: pass
		return columna
#............................................................................................................................................................






#............................................................................................................................................................
	def readPawn(self,j):
		fila = self.readRow(j)
		#coronacion		
		if(re.match('.+=[NBRQ]',j)):
			fila=int(j[-3])-1
			columna=self.columnas.index(j[-4])
			if(fila==0): f=1
			else:	f=7
			c=self.columnas.index(j[0])
			
			
			if(j[-1]=='Q'):
				return	([10,1],[fila,columna,f,c])
			if(j[-1]=='R'):
				return ([10,2],[fila,columna,f,c])
			if(j[-1]=='N'):
				return ([10,3],[fila,columna,f,c])
			if(j[-1]=='B'):
				return ([10,4],[fila,columna,f,c])
		
		elif(j[1]!='x'):
			columna=self.columnas.index(j[0])
			col=columna
			
			if(self.control.getTurn()): d = -1
			else: d = 1 
			if not(isinstance(self.tablero[fila+d][columna],Square)):
				ca=fila+d
			else:
				ca=fila+(2*d)
			return ([ca,col], [fila,columna])

		else:
			col=self.columnas.index(j[0])
			columna=self.columnas.index(j[-2])
			
			if(self.control.getTurn()): d = -1
			else: d = 1 
			ca=fila+d
			return ((ca,col),(fila,columna))
			
#............................................................................................................................................................






#............................................................................................................................................................
	def readRook(self, j):
		fila = int(j[-1]) - 1
		columna = self.columnas.index(j[-2])
		

		if(self.control.getTurn()): color='B'
		else:color = 'N'

		if(len(j)==3 or j[1]=='x'):
			c = columna	
			f = fila
		elif(re.match('.[a-h].+',j)):
			c=self.columnas.index(j[1])
			f = -1		
		elif(re.match('.[0-7].+',j)):
			f=int(j[1])-1
			c = -1
			
		for row in self.tablero:
			for pieza in row:
				try:
					if pieza.name == 'T' and pieza.color == color:
						if (pieza.casilla[0] == f  or pieza.casilla[1] == c) and pieza.legalMove((fila,columna),self.tablero) : 
					    		return((pieza.casilla[0],pieza.casilla[1]),(fila,columna))
				except: pass
#............................................................................................................................................................








#............................................................................................................................................................
	def readKnight(self,j):
	
		fila = int(j[-1]) - 1
		columna = self.columnas.index(j[-2])

		if(self.control.getTurn()): color='B'
		else:color = 'N'

		if(len(j)==3 or j[1]=='x'):
			c = columna	
			f = fila	
			for row in self.tablero:
				for pieza in row:
					try:
						if pieza.name == 'C' and pieza.color == color:
							if (pieza.legalMove((fila,columna),self.tablero)): 
								return((pieza.casilla[0],pieza.casilla[1]),(fila,columna))
					except: pass	
		
			
			
		elif(re.match('.[a-h].+',j)):
			c=self.columnas.index(j[1])
			f = -1
		elif(re.match('.[0-7].+',j)):
			f = int(j[1])-1
			c = -1
		for row in self.tablero:
			for pieza in row:
				try:
					if pieza.name == 'C' and pieza.color == color:
						if (pieza.casilla[0] == f  or pieza.casilla[1] == c) and pieza.legalMove((fila,columna),self.tablero) : 
					    		return((pieza.casilla[0],pieza.casilla[1]),(fila,columna))
				except: pass	
#............................................................................................................................................................








#............................................................................................................................................................
	def readBishop(self,j):

		fila = int(j[-1]) - 1
		columna = self.columnas.index(j[-2])

		if(self.control.getTurn()): color='B'
		else:color = 'N'

		for row in self.tablero:
			for pieza in row:
				try:
					if pieza.name == 'A' and pieza.color == color:
						if pieza.legalMove((fila,columna),self.tablero):
							return((pieza.casilla[0],pieza.casilla[1]),(fila,columna))
				except: pass
#............................................................................................................................................................








#............................................................................................................................................................
	def readQueen(self,j):
		fila = int(j[-1]) - 1
		columna = self.columnas.index(j[-2])

		if(self.control.getTurn()): color='B'
		else:color = 'N'
		if(len(j)==3 or j[1]=='x'):
			for row in self.tablero:
				for pieza in row:
					try:
						if pieza.name == 'D' and pieza.color == color:
							if pieza.legalMove((fila,columna),self.tablero):
								return((pieza.casilla[0],pieza.casilla[1]),(fila,columna))
					except: pass	
				
		else:
			if(re.match('.[a-h].+',j)):
				c=self.casillas.index(j[1])
				f = -1
			elif(re.match('.[0-7].+',j)):
				f = int(j[1])-1
				c = -1
		
		for row in self.tablero:
			for pieza in row:
				try:
					if pieza.name == 'D' and pieza.color == color:
						if (pieza.casilla[0] == f  or pieza.casilla[1] == c) and pieza.legalMove((fila,columna),self.tablero) : 
					    		return((pieza.casilla[0],pieza.casilla[1]),(fila,columna))
				except: pass	
#............................................................................................................................................................








#............................................................................................................................................................
	def readKing(self,j):
		fila = int(j[-1]) - 1
		columna = self.columnas.index(j[-2])

		if(self.control.getTurn()): color='B'
		else:color = 'N'

		for row in self.tablero:
			for pieza in row:
				try:
					if pieza.name == 'R' and pieza.color == color:
						return((pieza.casilla[0],pieza.casilla[1]),(fila,columna))
				except: pass	
#............................................................................................................................................................			
		

