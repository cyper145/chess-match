import gtk
import re
import pango
from View import *
from ControlTime import*
from Queue import *








class ControlVista():


#########################################################################################################
    def __init__(self, cp,queue):

	
	self.queue = queue	
	gtk.gdk.threads_init()
	self.lock = threading.Lock()
        self.builder= gtk.Builder()
        self.builder.add_from_file('View/board.glade' )
        self.ventanaprincipal = self.builder.get_object("window1" )
	self.windowsSet = self.builder.get_object("window2" )
	self.presentacion = self.builder.get_object("presentacion" )
	self.text = self.builder.get_object("textview1" )
        self.timeBlackLabel=self.builder.get_object("label1" )
        self.timeWhiteLabel=self.builder.get_object("label2" )
	self.mensaje=self.builder.get_object("label3" )
	self.label_negro=self.builder.get_object("label4" )
	self.label_blanco=self.builder.get_object("label5" )
	self.label=self.builder.get_object("label6" )
        self.choser=self.builder.get_object("filechooserdialog1" )
	self.boton_abrir=self.builder.get_object("button69" )
        self.winPGN=self.builder.get_object("winPGN" )
	self.treeview=self.builder.get_object("treeview1")

	
	fontdesc = pango.FontDescription("Serif Bold 10")
	self.timeBlackLabel.modify_font(fontdesc)
	self.timeWhiteLabel.modify_font(fontdesc)
	self.label.modify_font(fontdesc)
	self.mensaje.modify_font(fontdesc)

	self.controlP=cp


	#botones de windows set
	#--------------------------------------
	self.whiteHuman = self.builder.get_object("radiobutton3" )
	self.blackHuman = self.builder.get_object("radiobutton1" )
	self.spinHoras = self.builder.get_object("spinbutton1" )
	self.spinMinutos = self.builder.get_object("spinbutton2" )
	self.spinIncremento= self.builder.get_object("spinbutton3" )
	# ventana de presentacion
	#-----------------------------------------------------------------------------------------
	def draw_pixbuf(widget, event):
        	path = 'Images/backgrounds/back1.jpg'
        	pixbuf = gtk.gdk.pixbuf_new_from_file(path)
        	widget.window.draw_pixbuf(widget.style.bg_gc[gtk.STATE_NORMAL], pixbuf, 0, 0, 0,0)

	
	def on_button1_clicked(widget):
		print "Nueva Partida!"
		#self.controlP.newGame()
		self.builder.connect_signals(self)
		self.presentacion.hide()
		self.windowsSet.show()
        	#self.ventanaprincipal.show()
      		#self.ventanaprincipal.maximize()
		
		

	
	def on_button2_clicked(widget):
		print "Visor PGN"
		self.builder.connect_signals(self)
		self.presentacion.hide()
        	self.ventanaprincipal.show()
      		self.ventanaprincipal.maximize()


	#window = gtk.Window()
	#self.presentacion.set_title('Drawing Test')
	self.presentacion.set_size_request(600,265)
	#self.presentacion.connect('destroy',gtk.main_quit)
	hbbox = self.builder.get_object("hbuttonbox4" )
	#self.presentacion.add(hbbox)
	hbbox.connect('expose-event', draw_pixbuf)
	
	button1 = gtk.Button('Nueva Partida')
	hbbox.pack_start(button1, False, False, 0)
	button1.connect('clicked', on_button1_clicked)

	button2 = gtk.Button('Visor PGN')
	hbbox.pack_start(button2, True, False, 0)
	button2.connect('clicked', on_button2_clicked)
	
	
	self.presentacion.show_all()
	#-----------------------------------------------------------------------------------------



	#listore de la ventana WIN-PGN
	#---------------------------------------------------------------------------------------
	self.liststore = gtk.ListStore(str,str,str,str,str,str,str,str,str)

	self.treeview.columns = [None]*9
        self.treeview.columns[0] = gtk.TreeViewColumn('Blancas')
        self.treeview.columns[1] = gtk.TreeViewColumn('Elo')
        self.treeview.columns[2] = gtk.TreeViewColumn('Negras')
	self.treeview.columns[3] = gtk.TreeViewColumn('Elo')
	self.treeview.columns[4] = gtk.TreeViewColumn('Evento')
	self.treeview.columns[5] = gtk.TreeViewColumn('Lugar')
	self.treeview.columns[6] = gtk.TreeViewColumn('Fecha')
	self.treeview.columns[7] = gtk.TreeViewColumn('ECO')
	self.treeview.columns[8] = gtk.TreeViewColumn('Resultado')

	self.treeview.set_model(model = self.liststore)


	self.treeview.set_model(self.liststore)
	for n in range(9):
            	# add columns to treeview
            	self.treeview.append_column(self.treeview.columns[n])
            	# create a CellRenderers to render the data
            	self.treeview.columns[n].cell = gtk.CellRendererText()
            	# add the cells to the columns
            	self.treeview.columns[n].pack_start(self.treeview.columns[n].cell,True)
            	# set the cell attributes to the appropriate liststore column
            	self.treeview.columns[n].set_attributes(self.treeview.columns[n].cell, text=n)

#---------------------------------------------------------------------------------------

	#inicialiso los labels
	self.label.set_text('')
	self.label_blanco.set_text('')
	self.label_negro.set_text('')	
	#---------------------------------------

	#Variables para el manejo del textView	
	self.buff=gtk.TextBuffer()
	self.marcas=[]	
 	self.h_tag = self.buff.create_tag( "h")
	self.c_tag = self.buff.create_tag( "colored", foreground="#FFFF00", background="#0000FF")

	self.text.set_buffer(self.buff)
	
	#self.ajuste=gtk.Adjustment()	
	#self.scroll=self.builder.get_object("scrolledwindow1")

	
	
	self.tiempoBlanco=Timer(self.timeWhiteLabel,0,5,0)
	self.tiempoBlanco.turno=True
	self.tiempoNegro=Timer(self.timeBlackLabel,0,5,0)

	
        self.square=[]
        for k in range(8):
            self.square.append([0]*8)

	
            
        for a in range(8):
            for b in range(8):
		
                self.square[a][b]= self.builder.get_object("button"+ str((a*8)+(b+1)) )
		#print  self.square[a][b] 



     

      #  self.builder.connect_signals(self)
	#self.presentacion.show()
      #  self.ventanaprincipal.show()
      #  self.ventanaprincipal.maximize()

	#variables para indicar si es el primer o segundo click sobre el tablero
	self.primer_click= True
	self.jugada=[]
	self.partida=[]      
	self.actual=-1 
	self.actual_aux=-1   
	
	#self.tiempoBlanco.start()
	#self.tiempoNegro.start()
		
#########################################################################################################




#########################################################################################################
    def on_window1_destroy(self, widget, data=None):
	 gtk.gdk.threads_leave()
	 self.tiempoBlanco.stop()
	 self.tiempoNegro.stop()
	 try:	
		print "stop"
		self.controlP.game.stop()
		self.controlP.game.join()
	 except:
		print "no stop"
		#pass
         gtk.main_quit()
#########################################################################################################

    def  QUIT(self):	
	 gtk.gdk.threads_leave()
	 self.tiempoBlanco.stop()
	 self.tiempoNegro.stop()
	 try:	
		print "stop"
		self.controlP.game.stop()
		self.controlP.game.join()
	 except:
		print "no stop"
		pass
         gtk.main_quit()


#########################################################################################################
    def dibujar(self,tabler):
	
       self.lock.acquire() 		
       self.image=[]
       
       for a in range(64):
            self.image.append(gtk.Image())
		
      
       		
       for a in range(8):
            for b in range(8):
		if (tabler[a][b] != None):	
			self.image[(8*a)+b].set_from_file(tabler[a][b].imagen)
	
       		self.image[(8*a)+b].show()
		self.square[a][b].set_image(self.image[(8*a)+b])
       
       self.lock.release()      
       

#########################################################################################################                                
		
    def repaint(self,cas1,cas2, tablero):		
        self.lock.acquire() 		

	self.image[(8* cas1[0])+cas1[1]].set_from_file(tablero[cas1[0]][cas1[1]].imagen)
	self.image[(8* cas2[0])+cas2[1]].set_from_file(tablero[cas2[0]][cas2[1]].imagen)
	self.image[(8* cas1[0])+cas1[1]].show()
	self.image[(8* cas2[0])+cas2[1]].show()
	self.square[cas1[0]][cas1[1]].set_image(self.image[(8* cas1[0])+ cas1[1]])
	self.square[cas2[0]][cas2[1]].set_image(self.image[(8* cas2[0])+ cas2[1]])


	self.lock.release()      
#########################################################################################################
    def pieza_clicked(self,widget, data=None):

      
      #if (self.controlP.turno == 'computer'):
      #		return	  

      
      k=0
      #######################################  
      #Determina la primer y segunda casilla
      #	clickeada
      #######################################
      self.lock.acquire()	
      while k<8:	
	try:
	   columna = self.square[k].index(widget)
	  
	   if self.primer_click :
		self.jugada.append((k,columna))
		self.primer_click=False
		self.lock.release()
		return	
	   else:
		self.jugada.append((k,columna))	
		#self.controlP.validarMovimiento(self.jugada)
		self.queue.put(self.jugada)
		
		self.jugada=[]
		self.primer_click=True
		
		#self.controlP.turno = 'computer'
		self.lock.release()
		return		
	  
	except:
	   k = k+1	
      self.lock.release()
#########################################################################################################


#########################################################################################################
    def set_text(self,jugada):
	

	self.lock.acquire()		
	it= self.buff.get_end_iter()
	self.marcas.append(self.buff.get_char_count())
	#mark = self.buff.create_mark('m', self.buff.get_end_iter(), left_gravity=False)
	#self.marcas.append(it)	
	self.buff.remove_tag(self.c_tag, self.buff.get_start_iter(), it)
	
	self.buff.insert_with_tags(it,jugada,self.c_tag)
	
	self.text.set_buffer(self.buff)
	#self.text.scroll_to_iter(it,0.0,False,0,0)
	#self.text.scroll_to_iter(it,0.4)
	self.text.scroll_to_mark(self.buff.get_insert(), 0)
	#self.ajuste.set_upper(upper)

	self.lock.release()
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
	self.lock.acquire()
	self.mensaje.set_text(texto)
	self.lock.release()
#########################################################################################################



#########################################################################################################
    def tablero_to_string(self, tablero):
	self.lock.acquire()
	posicion=[] 
	for a in range(8):
            for b in range(8):
		if (tablero[a][b] != None):	
			posicion.append(tablero[a][b].imagen)
		else:
			if(a+b)%2==0:			
				posicion.append('Images/set1/'+'Negro'+'.jpg')
			else:		
				posicion.append('Images/set1/'+'Blanco'+'.jpg')

	#print posicion
	self.partida.append(posicion)
	self.lock.release()
#########################################################################################################




#########################################################################################################
    def reproducir_posicion(self,posicion):	
	

	#self.lock.acquire()
	for a in range(8):
            for b in range(8):

		p= (8 * a)+ b
		image = gtk.Image()
			
		image.set_from_file(posicion[p])
		
       		image.show()
		self.square[a][b].set_image(image)
	
	#self.lock.release()
#########################################################################################################





#########################################################################################################
# 		BOTONES << Y >>
#########################################################################################################
    

    #----------------------------------------------------------------------------------------------------
    def on_button65_clicked(self,widget, data=None):
	self.lock.acquire()
	if(self.actual_aux >=1):
		
        	self.actual_aux=self.actual_aux-1
				
		#Obtengo los iteradores q marcan la jugada actual y aplico el tag
		itera=self.buff.get_iter_at_offset(self.marcas[self.actual_aux-1])
		itera1=self.buff.get_iter_at_offset(self.marcas[self.actual_aux])
	
		#Obtengo el iterador q apunta al ultimo y remuevo todos los tags
		it= self.buff.get_end_iter()
		self.buff.remove_tag(self.c_tag, self.buff.get_start_iter(), it)
		
		if(self.actual_aux>0):	self.buff.apply_tag(self.c_tag, itera,itera1)
		#self.lock.acquire()
		self.text.scroll_to_iter(itera,0)
		#self.lock.release()
		self.reproducir_posicion(self.partida[self.actual_aux])
	self.lock.release()	
    #----------------------------------------------------------------------------------------------------


    #----------------------------------------------------------------------------------------------------
    def on_button66_clicked(self,widget, data=None):
	self.lock.acquire()
	if(self.actual_aux <self.actual):
        	self.actual_aux=self.actual_aux+1
		

		#Obtengo el iterador q apunta al ultimo y remuevo todos los tags
		it= self.buff.get_end_iter()
		self.buff.remove_tag(self.c_tag, self.buff.get_start_iter(), it)
	
		#Obtengo los iteradores q marcan la jugada actual y aplico el tag
		itera=self.buff.get_iter_at_offset(self.marcas[self.actual_aux-1])
		if(self.actual==self.actual_aux): itera1=self.buff.get_end_iter()
		else:	itera1=self.buff.get_iter_at_offset(self.marcas[self.actual_aux])
		if(self.actual_aux>0):	self.buff.apply_tag(self.c_tag, itera,itera1)

		
		#self.lock.acquire()
		self.text.scroll_to_iter(itera,0.0)
		#self.lock.release()
		self.reproducir_posicion(self.partida[self.actual_aux])
	self.lock.release()
    #----------------------------------------------------------------------------------------------------
    def on_button73_clicked(self,widget, data=None):

	self.actual_aux=0
	it= self.buff.get_end_iter()
	self.buff.remove_tag(self.c_tag, self.buff.get_start_iter(), it)

	self.lock.acquire()
	self.text.scroll_to_iter(self.buff.get_start_iter(),0.0)
	self.lock.release()

	self.reproducir_posicion(self.partida[self.actual_aux])
    #----------------------------------------------------------------------------------------------------    

    #----------------------------------------------------------------------------------------------------
    def on_button74_clicked(self,widget, data=None):

	self.actual_aux=self.actual
	it= self.buff.get_end_iter()
	
	self.buff.remove_tag(self.c_tag, self.buff.get_start_iter(), it)

	#Obtengo los iteradores q marcan la jugada actual y aplico el tag
	itera=self.buff.get_iter_at_offset(self.marcas[self.actual_aux-1])
	itera1=self.buff.get_end_iter()
	self.buff.apply_tag(self.c_tag, itera,itera1)

	self.lock.acquire()
	self.text.scroll_to_iter(itera,0.0)
	self.lock.release()

	self.reproducir_posicion(self.partida[self.actual_aux])

    #----------------------------------------------------------------------------------------------------  

	
#########################################################################################################





#########################################################################################################
#########################################################################################################
#													#
#----------------  VENTANA ABRIR PGN -------------------------------------------------------------------#
#													#
#########################################################################################################
#########################################################################################################   

    def on_imagemenuitem11_activate(self,widget, data=None):
	#self.lock.acquire()
	self.choser.show()
	#self.lock.release()

    def on_button70_clicked(self,widget, data=None):
	#self.lock.acquire() 	
	self.choser.hide()
	#self.lock.release()
    def on_button69_clicked(self,widget, data=None): 
       
	#self.lock.acquire()
	filename=self.choser.get_filename()	
	self.open_pgn(filename)	
	self.choser.hide()
	self.winPGN.show()
	#self.liststore.append(["Martin Alonso","1976","Gonzalo Jaimez","2013","Torneo por equipos","Cordoba","25/07/2000","A06","1-0"])
	#self.lock.release()
    def on_file_activated(self,widget, data=None): 

	filename=self.choser.get_filename()
	if(filename[-4:] ==".pgn"):
		filename=self.choser.get_filename()	
		self.open_pgn(filename)	
		self.choser.hide()
		self.winPGN.show()
	
    def on_selection_changed(self,widget, data=None): 
	
	filename=self.choser.get_filename()
	if(filename != None):
		if(filename[-4:] ==".pgn"):
			self.boton_abrir.set_sensitive(True)
       		else:
			self.boton_abrir.set_sensitive(False)
	

   #------------------------------------------------------------------------------------
    def open_pgn(self,filename):
	
	partido=True
	self.f = open(filename, 'r')
	linea = self.f.readline()
	self.lista=[]
	while linea:
	 		
	 	wte=""
	 	wtee=""
	 	blk=""
	 	blke=""
	 	event=""
	 	site=""
	 	date=""
	 	eco=""
	 	rst=""
	 		
     		while(linea[0]=='['):
	
			mo = re.match('\[Event.*"(.+)"',linea )
			if(mo):		 
				event=mo.group(1)
			mo = re.match('\[Site.*"(.+)"',linea )
			if(mo):		 
				site=mo.group(1)
			mo = re.match('\[Date.*(".+")',linea )
			if(mo):		 
				date=mo.group(1)
			mo = re.match('\[Round.*"(.+)"',linea )
			if(mo):		 
				rnd=mo.group(1)
			mo = re.match('\[White .*"(.+)"',linea )
			if(mo):		 
				wte=mo.group(1)
			mo = re.match('\[Black .*"(.+)"',linea )
			if(mo):		 
				blk=mo.group(1)
			mo = re.match('\[Result.+"(.+)"',linea )
			if(mo):		 
				rst=mo.group(1)
			mo = re.match('\[WhiteElo.*"(.+)"',linea )
			if(mo):		 
				wtee=mo.group(1)
			mo = re.match('\[BlackElo.*"(.+)"',linea )
			if(mo):		 
				blke=mo.group(1)
			mo = re.match('\[ECO.*"(.+)"',linea )
			if(mo):		 
				eco=mo.group(1)
		

	
			linea = self.f.readline()
		if(wte!="" and blk!=""):
			self.lista.append(self.f.tell())
			self.liststore.append([wte,wtee,blk,blke,event,site,date,eco,rst]) 
		linea = self.f.readline()
    #------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------ 	
    def on_button71_clicked(self,widget, data=None): 	
	"""BOTON CANCELAR"""
	self.liststore.clear()
	self.winPGN.hide()
	self.f.close()
    #------------------------------------------------------------------------------------
    
    #------------------------------------------------------------------------------------
    def on_button72_clicked(self,widget, data=None): 	
	"""BOTON ABRIR"""
	partida=""
	cursor=self.treeview.get_cursor()[0][0]
	sel1,sel2= self.treeview.get_selection().get_selected()
	
	#obtengo los datos de la seleccion
	blanco=sel1.get_value(sel2,0)
	blancoElo=sel1.get_value(sel2,1)	
	negro=sel1.get_value(sel2,2)
	negroElo=sel1.get_value(sel2,3)
	evento=sel1.get_value(sel2,4)
	lugar=sel1.get_value(sel2,5)
	fecha=sel1.get_value(sel2,6)
	eco=sel1.get_value(sel2,7)
	resul=sel1.get_value(sel2,8)

	#cargo los labels con los datos
	self.label_negro.set_text(negro+'   ['+negroElo+']')	
	self.label_blanco.set_text(blanco+'   ['+blancoElo+']')

	

	self.timeBlackLabel.set_text('Evento: '+evento)
	self.timeWhiteLabel.set_text('Lugar: '+lugar)
	self.label.set_text('Fecha: '+fecha)
	self.mensaje.set_text(resul)


	self.f.seek(self.lista[cursor])
	linea=self.f.readline()
	partida=partida+linea
	while(not re.match('.*(1-0|1/2-1/2|0-1)',linea)):
		linea =self.f.readline()
		partida=partida+linea
	self.f.close()	
	
	self.winPGN.hide()

	par=partida.split()
	par.pop(-1)
	
	while(par):
		jb= par.pop(0)
		
		mo=re.match('.+\.(.+)',jb)
		if(mo): 
			j=mo.group(1)
			self.set_text(jb+'  ')
		else: 
			cuenta=jb
			j=par.pop(0)
			self.set_text(jb+j+'  ')	
		self.controlP.codificar_jugada(j)
		try:
			jn= par.pop(0)
			self.set_text(jn+'\n' )	
			self.controlP.codificar_jugada(jn)
		except:
			break	
		#print j,jn

    #------------------------------------------------------------------------------------

#########################################################################################################



    


##################################### WINDOW SET #########################################################

    def on_winset_Aceptar_clicked(self,widget):

	#self.lock.acquire()
	self.windowsSet.hide()
	self.ventanaprincipal.show()
      	self.ventanaprincipal.maximize()
	#self.lock.release()	

	HUMAN = 0
        COMPUTER = 1

	if self.whiteHuman.get_active():
		blancas = HUMAN 
	else:
		blancas = COMPUTER
		

	if self.blackHuman.get_active():
		negras = HUMAN
	else:
		negras = COMPUTER

	horas = self.spinHoras.get_value_as_int()
	minutos = self.spinMinutos.get_value_as_int()
	incremento = self.spinIncremento.get_value_as_int()
	
 	

	
	
	#self.lock.acquire()
	self.controlP.newGame(blancas,negras,horas,minutos,incremento)	
	#self.lock.release()	


    def on_winset_Cancelar_clicked(self,widget):	
	self.windowsSet.hide()
	self.presentacion.show()

#########################################################################################################




    def setActual(self):
	self.lock.acquire()
	self.actual +=1
	self.actual_aux +=1
	self.lock.release()	
 
