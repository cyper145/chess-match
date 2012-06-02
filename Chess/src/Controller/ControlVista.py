import gtk
from View import *

class ControlVista():


#########################################################################################################
    def __init__(self, cp):

        self.builder= gtk.Builder()
        self.builder.add_from_file('View/board.glade' )
        self.ventanaprincipal = self.builder.get_object("window1" )

	self.controlP=cp

        self.square=[]
        for k in range(8):
            self.square.append([0]*8)

	
            
        for a in range(8):
            for b in range(8):
		
                self.square[a][b]= self.builder.get_object("button"+ str((a*8)+(b+1)) )
		print  self.square[a][b] 

        self.timeBlackLabel=self.builder.get_object("label1" )
        self.timeWhiteLabel=self.builder.get_object("label2" )

        self.timeBlackLabel.set_text("0:00:00")
        self.timeWhiteLabel.set_text("0:00:00")

        self.builder.connect_signals(self)
        self.ventanaprincipal.show()
        self.ventanaprincipal.maximize()

	#variables para indicar si es el primer o segundo click sobre el tablero
	self.primer_click= True
	self.jugada=[]
#########################################################################################################




#########################################################################################################
    def on_window1_destroy(self, widget, data=None):
         gtk.main_quit()
#########################################################################################################





#########################################################################################################
    def dibujar(self,tabler):


       image = gtk.Image()	
       for a in range(8):
            for b in range(8):
		image = gtk.Image()	
		image.set_from_file('Images/set1/' + tabler[a][b]+'.jpg')
       		image.show()
		self.square[a][b].set_image(image)
     
#########################################################################################################                                
		
		
       



#########################################################################################################
    def pieza_clicked(self,widget, data=None):
      
      k=0
      #######################################  
      #Determina la primer y segunda casilla
      #	clickeada
      #######################################
      while k<8:	
	try:
	   columna = self.square[k].index(widget)
	  
	   if self.primer_click :
		self.jugada.append((k,columna))
		self.primer_click=False
		return	
	   else:
		self.jugada.append((k,columna))	
		self.controlP.validarMovimiento(self.jugada)		
		self.jugada=[]
		self.primer_click=True
		
		return		
	  
	except:
	   k = k+1	
	
     
#########################################################################################################

        
