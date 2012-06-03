import gtk
from View import *
from ControlTime import*



class ControlVista():


#########################################################################################################
    def __init__(self, cp):

	gtk.gdk.threads_init()
	self.lock = threading.Lock()
        self.builder= gtk.Builder()
        self.builder.add_from_file('View/board.glade' )
        self.ventanaprincipal = self.builder.get_object("window1" )
	self.text = self.builder.get_object("textview1" )
        timeBlackLabel=self.builder.get_object("label1" )
        timeWhiteLabel=self.builder.get_object("label2" )
	self.mensaje=self.builder.get_object("label3" )
	
	#variables de tiempo
	#------------------------------------------------------------------
	self.hb=0	
	self.mb=5
	self.sb=0
	self.hn=0	
	self.mn=5
	self.sn=0
	#------------------------------------------------------------------



	self.buff=gtk.TextBuffer()
	self.text.set_buffer(self.buff)
	self.controlP=cp
	
	self.tiempoBlanco=Timer(timeWhiteLabel,0,5,0)
	self.tiempoBlanco.turno=True
	self.tiempoNegro=Timer(timeBlackLabel,0,5,0)

	
        self.square=[]
        for k in range(8):
            self.square.append([0]*8)

	
            
        for a in range(8):
            for b in range(8):
		
                self.square[a][b]= self.builder.get_object("button"+ str((a*8)+(b+1)) )
		#print  self.square[a][b] 



     

        self.builder.connect_signals(self)
        self.ventanaprincipal.show()
        self.ventanaprincipal.maximize()

	#variables para indicar si es el primer o segundo click sobre el tablero
	self.primer_click= True
	self.jugada=[]
	
	#self.tiempoBlanco.start()
	#self.tiempoNegro.start()
		
#########################################################################################################




#########################################################################################################
    def on_window1_destroy(self, widget, data=None):
	 gtk.gdk.threads_leave()
	 self.tiempoBlanco.stop()
	 self.tiempoNegro.stop()
         gtk.main_quit()
#########################################################################################################





#########################################################################################################
    def dibujar(self,tabler):


       image = gtk.Image()	
       for a in range(8):
            for b in range(8):
		image = gtk.Image()
		if (tabler[a][b] != None):	
			image.set_from_file(tabler[a][b].imagen)
		else:
			if(a+b)%2==0:			
				image.set_from_file('Images/set1/'+'Negro'+'.jpg')
			else:		
				image.set_from_file('Images/set1/'+'Blanco'+'.jpg')
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


#########################################################################################################
    def set_text(self,jugada):
			
	self.buff.insert_at_cursor(jugada)
	self.text.set_buffer(self.buff)
	return
#########################################################################################################
 

#########################################################################################################
    def change_turnos(self):
	self.lock.acquire()
	self.tiempoBlanco.turno=not self.tiempoBlanco.turno
	self.tiempoNegro.turno=not self.tiempoNegro.turno
	self.lock.release()	
#########################################################################################################

#########################################################################################################
    def set_mensaje(self,texto):
	self.mensaje.set_text(texto)
#########################################################################################################
 
