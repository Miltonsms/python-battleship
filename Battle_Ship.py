#coding: utf-8
import time
import os
import sys
import random

def jugador1():
	print """
.______    __          ___   ____    ____  _______ .______          __  
|   _  \  |  |        /   \  \   \  /   / |   ____||   _  \        /_ | 
|  |_)  | |  |       /  ^  \  \   \/   /  |  |__   |  |_)  |        | | 
|   ___/  |  |      /  /_\  \  \_    _/   |   __|  |      /         | | 
|  |      |  `----./  _____  \   |  |     |  |____ |  |\  \----.    | | 
| _|      |_______/__/     \__\  |__|     |_______|| _| `._____|    |_| 
"""
def jugador2():
	print"""
.______    __          ___   ____    ____  _______ .______          ___   
|   _  \  |  |        /   \  \   \  /   / |   ____||   _  \        |__ \  
|  |_)  | |  |       /  ^  \  \   \/   /  |  |__   |  |_)  |          ) | 
|   ___/  |  |      /  /_\  \  \_    _/   |   __|  |      /          / /  
|  |      |  `----./  _____  \   |  |     |  |____ |  |\  \----.    / /_  
| _|      |_______/__/     \__\  |__|     |_______|| _| `._____|   |____| 
"""
def frente():

	print"""
                 ()
                   ||q',,'
                   ||d,~
        (,---------------------,)
         ',    COGNITS 2014   ,'
           \       986       /
            \  8p, d8b ,q8  /
             ) 888a888a888 (
            /  8b` q8p `d8  \              O
           /       689       \             |','
          /       d888b       \      (,---------,)
        ,'_____________________',     \   ,8,   /
        (`__________L|_________`)      ) a888a (    _,_
        [___________|___________]     /___`8`___\   }*{
          }:::|:::::}::|::::::{      (,=========,)  -=-
           '|::::}::|:::::{:|'  .,.    \:::|:::/    ~`~=
             '|}:::::|::{:::|'          ~".,."~`~
              '|:}::|::::|'~`~".,."
          ~`~".,."~`~".,                 "~`~".,."~
                         ".,."~`~
"""
def muerte():
	print"""
				██│░░░░░░░░░░░░░░░░░░░│██
				█▌│░░░░░░░░░░░░░░░░░░░│▐█
				█░└┐░░░░░░░░░░░░░░░░░┌┘░█
				█░░└┐░░░░░░░░░░░░░░░┌┘░░█
				█░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░█
				█▌░│██████▌░░░▐██████│░▐█
				██░│▐███▀▀░░▄░░▀▀███▌│░██
				█▀─┘░░░░░░░▐█▌░░░░░░░└─▀█
				█▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄█
				███▄─┘██▌░░░░░░░▐██└─▄███
				████░░▐█─┬┬┬┬┬┬┬─█▌░░████
				███▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐███
				████▄░░░└┴┴┴┴┴┴┴┘░░░▄████
				██████▄░░░░░░░░░░░▄██████
"""









class juego1(object):

	os.system("clear")
	def jueg1(self):
		tablero = []
		for x in range(0,5):
		  tablero.append(["O"] * 5)

		def print_tablero(tablero):
		  for fila in tablero:
			print "                          " ,"  ".join(fila)
			
		print """
             ====================================
	       Al ataque a comenzado  la batalla 
	     ===================================="""
		print 
		print
		

		def fila_aleatoria(tablero):
		  return random.randint(0,len(tablero)-1)

		def columna_aleatoria(tablero):
		  return random.randint(0,len(tablero[0])-1)
		barco_fila = fila_aleatoria(tablero)
		barco_col = columna_aleatoria(tablero)
		print barco_fila
		print barco_col
		for turno in range(4):
			while True:
				
				try: 
					print_tablero(tablero)
					print"  "
					self.adivina_fila = input("                     Adivina fila:")
					self.adivina_columna = input("                  Adivina columna:")
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					time.sleep(2)
					os.system("clear")
			if self.adivina_fila == barco_fila and self.adivina_columna == barco_col:
				print "				NO!!!!!!!!!!! as undido mi barco"
				muerte()
				time.sleep(4)
				os.system("clear")
				print "cargando segundo nivel......"
				time.sleep(2)
				os.system("clear")
				juu=juegoo1()
				juu.juego1()
				break
			else:
				if (self.adivina_fila < 0 or self.adivina_fila > 4) or (self.adivina_columna < 0  or self.adivina_columna > 4):
					print "Vaya, esto ni siquiera esta en el océano."
					time.sleep(2)
					os.system("clear")
				elif(tablero[self.adivina_fila][self.adivina_columna] == "X"):
					print "Ya dijiste esa."
					time.sleep(2)				    
					print 
					os.system("clear")
				else:
				  	print "No impactaste mi barco"
				  	tablero[self.adivina_fila][self.adivina_columna] = "X"
				  	time.sleep(2)
				  	os.system("clear")
				if turno == 3:
				    print "Termino el juego la respuesta es ","fila" ,barco_fila,"columna", barco_col
				print turno + 1
		time.sleep(4)
		os.system("clear")
		respuesta = 0
		while (respuesta == 0):
			print """ que desea hacer regresar al 
								1.menu 
							2.Reiniciar juego """
			menu2 = raw_input("Opcion 1 o 2 ? ")
			if menu2 == "1":
				time.sleep(0.4)
				os.system("clear")
				for x in range(0,3):
					print "cargado menù."
					time.sleep(0.4)
					os.system("clear")
					print "cargado menù.."
					time.sleep(0.4)
					os.system("clear")
					print "cargado menù..."
					time.sleep(0.4)
					os.system("clear")
				break
			elif menu2 == "2":
				for x in range(0,3):
					print "cargado juego."
					time.sleep(0.4)
					os.system("clear")
					print "cargado juego.."
					time.sleep(0.4)
					os.system("clear")
					print "cargado juego..."
					time.sleep(0.4)
					os.system("clear")
				MenU = juego1()
				MenU.jueg1()
			else:
				print"opcion no valida "
				respuesta = 0
			
			
		
		
class juegoo1(object):
	def juego1(self):
		tablero = []
		cont = 0
		for x in range(0,10):
		  tablero.append(["O"] * 10)

		def print_tablero(tablero):
		  for fila in tablero:
			print '                        '," ".join(fila)

		print "Juguemos batalla naval"

		def fila_aleatoria(tablero):
		  return random.randint(0,len(tablero)-1)

		def columna_aleatoria(tablero):
		  return random.randint(0,len(tablero[0])-1)

		barco_fila = fila_aleatoria(tablero)
		barco_col = columna_aleatoria(tablero)
		barco_fil = fila_aleatoria(tablero)
		barco_co = columna_aleatoria(tablero)
		barco_fi = fila_aleatoria(tablero)
		barco_c = columna_aleatoria(tablero)
		barco_ = fila_aleatoria(tablero)
		barco = columna_aleatoria(tablero)

		for turno in range(8):
			
			while True:
				try:
					print_tablero(tablero)
					self.adivina_fila = input("                   Adivina fila:")
					self.adivina_columna = input("                Adivina columna:")
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					time.sleep(2)
					os.system("clear")
			if self.adivina_fila == barco_fila and self.adivina_columna == barco_col:
				tablero[self.adivina_fila][self.adivina_columna] = "*"
				cont += 1				
				print "Felicitaciones Hundiste mi barco"
				muerte()
				time.sleep(3)
				os.system("clear")
			elif self.adivina_fila == barco_fil and self.adivina_columna == barco_co:
				tablero[self.adivina_fila][self.adivina_columna] = "*"
				cont += 1
				print "Felicitaciones Hundiste mi barco"
				muerte()
				time.sleep(2)
				os.system("clear")
			elif self.adivina_fila == barco_fi and self.adivina_columna == barco_c:
				tablero[self.adivina_fila][self.adivina_columna] = "*"
				cont += 1
				print "Felicitaciones Hundiste mi barco"
				muerte()
				time.sleep(2)
				os.system("clear")
			elif self.adivina_fila == barco_ and self.adivina_columna == barco:
				tablero[self.adivina_fila][self.adivina_columna] = "*"
				cont += 1				
				print "Felicitaciones Hundiste mi barco"
				muerte()
				time.sleep(2)
				os.system("clear")
				
			else:
				if (self.adivina_fila < 0 or self.adivina_fila > 10) or (self.adivina_columna < 0  or self.adivina_columna > 10):
					print "Vaya, esto ni siquiera esta en el océano."
					time.sleep(2)
				    
					os.system("clear")
				elif(tablero[self.adivina_fila][self.adivina_columna] == "X"):
					print "Ya dijiste esa."
					time.sleep(2)				    
					print 
					os.system("clear")
				else:
				  	print "No impactaste mi barco"
				  	tablero[self.adivina_fila][self.adivina_columna] = "X"
				  	time.sleep(2)
				  	os.system("clear")
				if turno == 7:
				    print "Termino el juego la respusta es ","fila" ,barco_fila,"columna", barco_col
				print turno + 1
			print "logros conseguidos",cont
			time.sleep(4)
			os.system("clear")
		
		
		



#lo siguiente es los ingresos ya esta para que no ingreses dataso mayores y uno sobres otro y ya esta par aque se bore cada ves que eligis algo 
#----------------------jugador 1----ingresos de datos -------------------*


class juego2(object):
	def jueg1(self):
		tablero = [] #jagador 1
		tabler2 = []
		tablero2 = []  #juagador1
		tabler22 = []
		puntaje = 0 
		puntaj = 0 
		fallos = 0
		fallo = 0 
		respuesta = 0
		
#tablero jugador 1 ingresos		
		for x in range(0,10):
		  tabler2.append(["O"] * 10)
		  

		def print_tabler2(tabler2):
		  for fila in tabler2:
			print " ".join(fila)
					
#tablero jugador 1 ingresos
		for x in range(0,10):
		  tabler22.append(["O"] * 10)			
			
		def print_tabler22(tabler22):
		  for fila in tabler22:
			print " ".join(fila)
		
		
		
		
		while (respuesta==0):
			while True:
				try:
	
					jugador1()
					self.a = int(input("ingrese fila pirmer barco1: "))
					break
				except (ValueError, NameError ,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					print "cargando....."
					time.sleep(2)
					os.system("clear")
			if (self.a >=10):	
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
				print "cargando....."
				time.sleep(2)
				os.system("clear")
			else:
				break
		while (respuesta==0):
			while True:
				try:
					self.b = int(input("ingrese columna primer barco1: "))
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					print "cargando....."
					time.sleep(2)
					os.system("clear")
			if (self.b >10):	
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
				print "cargando....."
				time.sleep(2)
				os.system("clear")
			else:
				break
			
		while (respuesta==0):	
			while True:
				try:
					self.c = int(input("ingrese fila segundo barco1: "))
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					print "cargando....."
					time.sleep(2)
					os.system("clear")
			if (self.c >=10 or self.c==self.a or self.c==self.b):	
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
				time.sleep(2)
				os.system("clear")
			else:
				break
		while (respuesta==0):
			while True:
				try:	
					self.d = int(input("ingrese posición1"))
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					print "cargando....."
					time.sleep(2)
					os.system("clear")
			if (self.d > 10 or self.d==self.b or self.d==self.a):	
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			else:
				break
		while (respuesta==0):
			print "ingrese la posición que desea para su buque."
			# parte de ingresos para barco principal
			d222 = input("ingrese fila: ")
			dg22 = input("ingrese columna : ")
			d2 = dg22+1 # PARTE DE DOS DEL BARCO
			ddd2 = d2+1 # PARTE DE DOS DEL tRES
			dd2	=ddd2+1 	  # PARTE DE DOS DEL CUARTA
			
			if	(d222 >=10  or d222 == self.a or d222 == self.b or d222 == self.c or d222 == self.d ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			elif(dg22 >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0	
			elif(d2 >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			elif(ddd2 >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			elif(dd2 >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			else:
				break
			#buque de defenza 
		while (respuesta==0):
			print "ingrese la pocición que desea para su buque de defenza"
			bd = input("ingrese fila: ")
			bd1 = input("ingrese columna : ")
			bd2 = bd+1 # PARTE DE DOS DEL BARCO
			bd3 = bd2+1 # PARTE DE DOS DEL tRES

			
			if	(bd >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			elif(bd1 >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0	
			elif(bd2 >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			elif(bd3 >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			else:
				break
		#---------------------jugador 1 ingresos de datos al tablero -----------------*
		for x in range(0,10):
		  tablero.append(["O"] * 10)
		  

		def print_tablero(tablero):
		  for fila in tablero:
			print " ".join(fila)
				#barco principal

		def fila_aleato2(tablero):
			return d222

		def columna_aleato2(tablero):
			return dg22

		def part_ba2(tablero): #part_ba =  es una parte del varco principal
			return d2

		def part_b2(tablero): #part_b =  es una parte del varco principal
			return ddd2
		
		def part_bar2(tablero): #part_b =  es una parte del varco principal
			return dd2
		#buque de defenza 
		def bdf(tablero):
			return bd

		def bd1f(tablero):
			return bd1

		def bd2f(tablero): #part_ba =  es una parte del varco principal
			return bd2

		def bd3f(tablero): #part_b =  es una parte del varco principal
			return bd3
		

		def fila_aleatoria(tablero):
		  return self.a

		def columna_aleatoria(tablero):
		  return self.b

		def fila_aleatori(tablero):
		  return self.c

		def columna_aleatori(tablero):
		  return self.d

		#----------------------------------------------
		barco_fila = fila_aleatoria(tablero)
		barco_col = columna_aleatoria(tablero)
		barco_fil = fila_aleatori(tablero)
		barco_co = columna_aleatori(tablero) 
		barco2 =  fila_aleato2(tablero)
		barc2 = columna_aleato2(tablero)
		bar2 = part_ba2(tablero)
		ba2 = part_b2(tablero)
		#
		b2 = part_bar2(tablero)
		tabler2[self.a][self.b]="b"
		tabler2[self.c][self.d]="b"
		tabler2[dg22][d222]="B"
		tabler2[d2][d222]="B"
		tabler2[ddd2][d222]="B"
		tabler2[dd2][d222]="B"
		#
		tabler2[bd1][bd]="D"
		tabler2[bd1][bd2]="D"
		tabler2[bd1][bd3]="D"
		#
		print "juego de batalla nabal sus barcos fuerno ingresados y escondidos "
		print_tabler2(tabler2)
		print "cargando....."
		time.sleep(2)
		os.system("clear")
		#------------------------------------------------
		#--------------------jugador 2----ingesos de dhttps://github.com/Miltonsms/Battle_Ship.gitatos--------------*

		while (respuesta==0):
			print "*********************hora de ingreso del segudno jugador  *********"
			print "cargado configuración......"
			time.sleep(5)
			os.system("clear")
			print "*********************puede ingresar sus barcos ************"
			while True:
				try:
					jugador2()
					self.aa = int(input("ingrese fila pirmer barco2: "))
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					print "cargando....."
					time.sleep(2)
					os.system("clear")
			if (self.aa >=10):	
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
				print "cargando....."
				time.sleep(2)
				os.system("clear")
			else:
				break
		while (respuesta==0):
			while True:
				try:
					self.bb = int(input("ingrese colucna primer barco2: "))
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					print "cargando....."
					time.sleep(2)
					os.system("clear")
			if (self.bb >=10):	
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
				print "cargando....."
				time.sleep(2)
				os.system("clear")
			else:
				break
		while (respuesta==0):
			while True:
				try:
					self.cc = int(input("ingrese fila segundo barco2: "))
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					print "cargando....."
					time.sleep(2)
					os.system("clear")
			if (self.cc >=10 or self.cc==self.aa or self.cc==self.bb):	
				print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
				print "cargando....."
				time.sleep(2)
				os.system("clear")
			else:
				break
		while (respuesta==0):
			while True:
				try:
					self.dd = int(input("ingrese posición2: "))
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					print "cargando....."
					time.sleep(2)
					os.system("clear")
			if (self.dd >=10 or self.dd==self.bb or self.dd==self.aa):	
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			else:
				break
		while (respuesta==0):
			print "ingrese la pocición que desea para su buque."
			# parte de ingresos para barco principal
			d22 = input("ingrese fila: ")
			dg2 = input("ingrese columna : ")
			d = dg2+1 # PARTE DE DOS DEL BARCO
			ddd = d+1 # PARTE DE DOS DEL tRES
			dd	=ddd+1 	  # PARTE DE DOS DEL CUARTA
			
			if	(d22 >=10   or d22 == self.aa or d22 == self.bb or d22 == self.cc or d222 == self.dd ):
				print "Opcioón no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			elif(dg2 >=10  ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0	
			elif(d >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			elif(ddd >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			elif(dd >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			else:
				break
		while (respuesta==0):
			print "ingrese su buque de defenza"
			bd2 = input("ingrese fila: ")
			bd21 = input("ingrese columna : ")
			bd22 = bd2+1 # PARTE DE DOS DEL BARCO
			bd23 = bd22+1 # PARTE DE DOS DEL tRES
			
			if	(bd2 >=10 ):
				print "Opcioón no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			elif(bd21 >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0	
			elif(bd22 >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			elif(bd23 >=10 ):
				print "Opción no valida elija nuevamente, recuerda que es del 0 al 10"
				respuesta = 0
			else:
				break
				
		#---------------------jugador 2 ingresos de datos al tablero -----------------*
		for x in range(0,10):
		  tablero2.append(["O"] * 10)

		def print_tabler(tablero2):
		  for fil in tablero2:
			 print " ".join(fil)

		
		#barco principal 

		def fila_aleato(tablero2):
			return d22

		def columna_aleato(tablero2):
			return dg2

		def part_ba(tablero2): #part_ba =  es una parte del varco principal
			return d

		def part_b(tablero2): #part_b =  es una parte del varco principal
			return ddd
		
		def part_bar(tablero2): #part_b =  es una parte del varco principal
			return dd
			
		#barco de defenza
		def db2f(tablero2):
			return bd2

		def db21f(tablero2):
			return bd21

		def db22f(tablero2): #part_ba =  es una parte del varco principal
			return bd22

		def db23f(tablero2): #part_b =  es una parte del varco principal
			return bd23
	#barcos menores 
		def fila_aleatori(tablero2):
			return self.aa

		def columna_aleatori(tablero2):
			return self.bb

		def fila_aleator(tablero2):
			return self.cc

		def columna_aleator(tablero2):
			return self.dd
		#----------------------------------------------
		barco_fi = fila_aleatori(tablero2)
		barco_c = columna_aleatori(tablero2)
		barco_f = fila_aleator(tablero2)
		barco_cc = columna_aleator(tablero2)
		barco =  fila_aleato(tablero2)
		barc = columna_aleato(tablero2)
		bar = part_ba(tablero2)
		ba = part_b(tablero2)
		b = part_bar(tablero2)
		tabler22[self.aa][self.bb]="b"
		tabler22[self.cc][self.dd]="b"
		tabler22[dg2][d22]="B"
		tabler22[d][d22]="B"
		tabler22[ddd][d22]="B"
		tabler22[dd][d22]="B"
		#
		tabler22[bd21][bd2]="D"
		tabler22[bd21][bd22]="D"
		tabler22[bd21][bd23]="D"
		
		#
		print "juego de batalla nabal sus barcos fuerno ingresados y escondidos "
		print_tabler22(tabler22)
		print "Cargando juego.........."
		time.sleep(3)
		os.system("clear")
		#--------------------operacion del juego   ----------------------------
		print "bueno es hora del ataque Hunde todo los barcos posibles escondidos"
		for turno in range(5):
			print "impactos realizados en el ataque......."
			print_tablero(tablero)
			time.sleep(2)
			os.system("clear")
			jugador1()
			print "tablero jugador 2"
			print_tabler(tablero2) 
			print "tablero jugador 1"
			print_tabler2(tabler2)
			while True:
				try:
					adivina_fil = input("Adivina fila:")
					adivina_column = input("Adivina columna:")
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar numeros enteros!  !"
					print "cargando....."
					time.sleep(2)
					os.system("clear")
			if adivina_fil == barco_fi and adivina_column == barco_c:
				tablero2[adivina_fil][adivina_column] = "*"
				tabler22[self.aa][self.bb]="*"
				print "Felicitaciones Hundiste mi barco" 
				muerte()
				puntaje += 1 
				print "cargando....."
				time.sleep(2)
				os.system("clear")
				print_tabler(tablero2)
			elif adivina_fil == barco_f and adivina_column == barco_cc:
				tablero2[adivina_fil][adivina_column] = "*"
				tabler22[self.cc][self.dd]="*"
				muerte()
				puntaje += 1 
				print "cargando....."
				time.sleep(2)
				os.system("clear")
				print_tabler(tablero2)
			elif adivina_fil == barco and adivina_column == barc:
				tablero2[adivina_fil][adivina_column] = "*"
				tabler22[dg2][d22]="*"
				print "Felicitaciones Hundiste mi barco principal"
				muerte()
				puntaje += 10 
				print "as ganado ;)"
				time.sleep(2)
				os.system("clear")
				break
			elif adivina_fil == ba and adivina_column == barco:
				tablero2[adivina_fil][adivina_column] = "*"
				tabler22[d][d22]="*"
				
				print "capitan impactaron a nuestro buque"
				puntaje += 3 
				print "cargando...."
				time.sleep(2)
				os.system("clear")
			elif adivina_fil == bar and adivina_column == barco:
				tablero2[adivina_fil][adivina_column] = "*"
				tabler22[ddd][d22]="*"
				print "capitan impactaron a nuestro buque"
				puntaje += 2 
				print "cargando...."
				time.sleep(2)
				os.system("clear")
			elif adivina_fil == b and adivina_column == barco:
				tablero2[adivina_fil][adivina_column] = "*"
				tabler22[dd][d22]="*"
				print "capitan impactaron a nuestro buque"
				puntaje += 2 
				print "cargando...."
				time.sleep(2)
				os.system("clear")
				#BARCO DE DEFENZA
			elif adivina_fil == db21f(tablero2) and adivina_column == db2f(tablero2):
				tablero2[adivina_fil][adivina_column] = "*"
				tabler22[bd21][bd2]="*"
				print "capitan impactaron a nuestro buque de defenza"
				puntaje += 2 
				print "cargado.........."
				time.sleep(2)
				os.system("clear")
			elif adivina_fil == db21f(tablero2) and adivina_column == db22f(tablero2):
				tablero2[adivina_fil][adivina_column] = "*"
				tabler22[bd21][bd22]="*"
				print "capitan impactaron a nuestro buque de defenza"
				puntaje += 2 
				print "cargando...."
				time.sleep(2)
				os.system("clear")
			elif adivina_fil == db21f(tablero2) and adivina_column == db23f(tablero2):
				tablero2[adivina_fil][adivina_column] = "*"
				tabler22[bd21][bd23]="*"
				print "capitan impactaron a nuestro buque de defenza"
				puntaje += 2 
				print "cargando...."
				time.sleep(2)
				os.system("clear")
				#
			else:
				if (adivina_fil < 0 or adivina_fil > 9) or (adivina_column < 0 or adivina_column > 9):
					print "Vaya, esto ni siquiera esta en el océano."
					fallos +=1
					os.system("clear")
				elif (tablero2[adivina_fil][adivina_column] == "X"):
					print "Ya dijiste esa."
					fallos +=1
					print "cargando....."
					time.sleep(2)
					os.system("clear")
				else:
					print "No impactaste mi barco"
					print "cargando....."
					fallos +=1
					time.sleep(2)
					os.system("clear")
					tablero2[adivina_fil][adivina_column] = "X"
					time.sleep(1)
					os.system("clear")

		#---------------------jugador 2 ingresos de datos al tablero -----------------*
			print "impactos realizados en el ataque......."
			print_tabler(tablero2)
			time.sleep(2)
			os.system("clear")
			print "Es momento del Contra taque"
			jugador2()
			print "tablero jugador #1"
			print_tablero(tablero)
			print "tablero jugador #2"
			print_tabler22(tabler22)
			while True:
				try:
					adivina_fila = input("Adivina fila:")
					adivina_columna = input("Adivina columna:")
					break
				except (ValueError, NameError,SyntaxError):
					print "Solo puede ingresar números enteros!!"
					print "cargando....."
					time.sleep(2)
					os.system("clear")
			if adivina_fila == barco_fila and adivina_columna == barco_col:
				tablero[adivina_fila][adivina_columna] = "*"
				tabler2[self.a][self.b]="*"
				print "Felicitaciones Hundiste mi barco" 
				muerte()
				puntaj += 1 
				print "cargando....."
				time.sleep(2)
				os.system("clear")				
			elif adivina_fila == barco_fil and adivina_columna == barco_co:
				tablero[adivina_fila][adivina_columna] = "*"
				tabler2[self.c][self.d]="*"
				print "Felicitaciones Hundiste mi barco"
				muerte()
				puntaj += 1 
				print "cargando....."
				time.sleep(2)
				os.system("clear")
			elif adivina_fila == barco2 and adivina_columna == barc2:
				tablero[adivina_fila][adivina_columna] = "*"
				tabler2[dg22][d222]="*"
				print "Felicitaciones Hundiste mi barco principal"
				muerte()
				puntaj += 10 
				print "as ganado ;)"
				time.sleep(2)
				os.system("clear")
				break
			elif adivina_fila == ba2 and adivina_column == barco2:
				tablero[adivina_fila][adivina_columna] = "*"
				tabler2[d2][d222]="*"
				print "capitan impactaron a nuestro buque"
				puntaj += 3 
				print "cargando...."
				time.sleep(2)
				os.system("clear")
			elif adivina_fila == bar2 and adivina_columna == barco2:
				tablero[adivina_fila][adivina_columna] = "*"
				tabler2[ddd2][d222]="*"
				print "capitan impactaron a nuestro buque"
				puntaj += 2 
				print "cargando...."
				time.sleep(2)
				os.system("clear")
			elif adivina_fila == b2 and adivina_column == barco2:
				tablero[adivina_fila][adivina_columna] = "*"
				tabler2[dd2][d222]="*"
				print "capitan impactaron a nuestro buque"
				puntaj += 2 
				print "cargando...."
				time.sleep(2)
				os.system("clear")
				#BARCO DE DEFENZA 
			elif adivina_fila == bd1f(tablero2) and adivina_columna == bdf(tablero2):
				tablero[adivina_fila][adivina_columna] = "*"
				tabler2[bd1][bd]="*"
				print "capitan impactaron a nuestro buque de defenza"
				puntaj += 2
				print "cargado....."
				time.sleep(2)
				os.system("clear")
			elif adivina_fila == bd1f(tablero2) and adivina_column == bd2f(tablero2):
				tablero[adivina_fila][adivina_columna] = "*"
				tabler2[bd1][bd2]="*"
				print "capitan impactaron a nuestro buque de defenza"
				puntaj += 2 
				print "cargando...."
				time.sleep(2)
				os.system("clear")
			elif adivina_fila == bd1f(tablero2) and adivina_columna == bd3f(tablero2):
				tablero[adivina_fila][adivina_columna] = "*"
				tabler2[bd1][bd3]="*"
				print "capitan impactaron a nuestro buque de defenza"
				puntaj += 2 
				print "cargando...."
				time.sleep(2)
				os.system("clear")
				#
			else:
				if (adivina_fila < 0 or adivina_fila > 9) or (adivina_columna < 0 or adivina_columna > 9):
					print "Vaya, esto ni siquiera esta en el océano."
					fallo +=1
					print "cargando....."
					time.sleep(2)
					os.system("clear")
				elif(tablero[adivina_fila][adivina_columna] == "X"):
					print "Ya dijiste esa."
					fallo +=1
					print "cargando....."
					time.sleep(2)
					os.system("clear")
				else:
					print "No impactaste mi barco"
					fallo +=1
					print "cargando....."
					time.sleep(2)
					os.system("clear")
					tablero[adivina_fila][adivina_columna] = "X"
		os.system("clear")
		print "tablero jugador 1 impactos resividos"
		print ""
		print_tablero(tablero)
		print "tiros fallidos: ",fallo,"inpactos realizados",puntaje
		print "***********************************************************"
		print "talbero jugador 1 inpactos realisados"
		print_tabler(tablero2)
		print "tiros fallidos: ",fallos,"inpactos ",puntaj
		if puntaje > puntaj:
			print "Fue una gran batalla pero gano el jugador 1 con: ", puntaje,"impactos"
		elif puntaje == puntaj:
			print "ambos lados tuvieron una batalla que los dejo en las mismas condiciones"
		else:
			print "Fue una gran batalla pero gano el juador 2 con: ", puntaj,"inpactos"
		respuesta = 0
		while (respuesta == 0):
			print """ que desea hacer regresar al 
								1.menu 
							2.Reiniciar juego """
			menu2 = raw_input("Opcion 1 o 2 ? ")
			if menu2 == "1":
				time.sleep(0.4)
				os.system("clear")
				for x in range(0,3):
					print "cargado menù."
					time.sleep(0.4)
					os.system("clear")
					print "cargado menù.."
					time.sleep(0.4)
					os.system("clear")
					print "cargado menù..."
					time.sleep(0.4)
					os.system("clear")
				break
				break
			elif menu2 == "2":
				for x in range(0,3):
					print "cargado juego."
					time.sleep(0.4)
					os.system("clear")
					print "cargado juego.."
					time.sleep(0.4)
					os.system("clear")
					print "cargado juego..."
					time.sleep(0.4)
					os.system("clear")
				MeNU = juego2()
				MeNU.jueg2()
			else:
				print"opcion no valida "
				respuesta = 0	
			time.sleep(8)
			os.system("clear")
		for x in range(0,3):
				print "cargado ."
				time.sleep(0.4)
				os.system("clear")
				print "cargado .."
				time.sleep(0.4)
				os.system("clear")
				print "cargado ..."
				time.sleep(0.4)
				os.system("clear")

		
	
class salir():
	def jueg1(self):
		sys.exit(1)
		

		
		


def menu():
	print u"""

			 ====================================
			 Bienvenido al Juego de batalla naval
			 ====================================
	***********************************************************************
	*           Instrucciones del juego de un jugador                      *
	*       1. tendrás 4 vidas para acertar un barco.                      *
	*	2. si aciertas pasaras de nivel  y tenderas 8 vidas.           *
	*	3. solo puedes usar número enteros y no podrás ingresar letras.*
	*                                                                      *
	*           Instrucciones de Multi jugador                             *
	*       1. tendrán un tiempo cada jugador para esconder sus barcos.    *
	*	2. tendrán cuatro intentos para logra hundir los barcos.       *
	*	3. solo puedes usar número enteros y no podrás ingresar letras.*
	**********************************************************************"""
	
	menu = {'1':juego1,"2":juego2,'3':salir}  #de llave poner la variable que queremos, de valor el nombre de la clase
	respuesta = 0
	while (respuesta==0):
		frente()
		print """
			        1.play
			        2.multiplayer
				3.salir """
		opcion = raw_input("Ingrese opción: ")
		if opcion == "1" or opcion == "2" or opcion == "3":
	
			variable = menu[opcion]() # nombre_de_su_diccionario[lo_que_ingreso_el_usuario]() << parentesis al final
			time.sleep(0.4)
			os.system("clear")
			for x in range(0,3):
					print "cargado ."
					time.sleep(0.4)
					os.system("clear")
					print "cargado .."
					time.sleep(0.4)
					os.system("clear")
					print "cargado ..."
					time.sleep(0.4)
					os.system("clear")
			print variable.jueg1() # instanciar la mera funcion

		else:
			print "opción no reconocida"
			time.sleep(2)
			os.system("clear")
			respuesta = 0
			
menu()	
	
	

