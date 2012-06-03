import time
import threading



class Timer(threading.Thread):

################################################################################################################
 	def __init__(self,view,h,m,s):
 		print "timer"
		self.horas=h
		self.min=m
		self.sec=s
		self.view=view
		threading.Thread.__init__(self)
		self.turno=False
		self.seguir=True
		horas=str(self.horas)
		if(self.min<10):		
			minutos='0'+str(self.min)
		else:
			minutos=str(self.min)
		if(self.sec<10):		
			segundos='0'+str(self.sec)
		else:
			segundos=str(self.sec)
		
		self.view.set_text(horas+':'+minutos+':'+segundos)
		self.lock = threading.Lock()

################################################################################################################




################################################################################################################
 	def run(self):
		print "timer run"
		while True:
		  self.lock.acquire()
		  if(not self.seguir):
			break		
 		  if self.turno:
			self.lock.release()	
			if(self.sec ==0):
				if(self.min==0):
					if(self.horas==0):
						#self.horas=15
						break	
					else:
						self.horas=self.horas-1
						self.min=59
						self.sec=59
				else:
					self.min=self.min-1
					self.sec=59
			else:
				self.sec=self.sec-1
 			horas=str(self.horas)
			if(self.min<10):		
				minutos='0'+str(self.min)
			else:
				minutos=str(self.min)
			if(self.sec<10):		
				segundos='0'+str(self.sec)
			else:
				segundos=str(self.sec)
			#print horas+':'+minutos+':'+segundos
			self.lock.acquire()
			self.view.set_text(horas+':'+minutos+':'+segundos)
			self.lock.release()

			time.sleep(1)
		  else:
			self.lock.release()				
################################################################################################################ 

################################################################################################################ 
	def stop(self):
		self.seguir=False
################################################################################################################ 
		
