'''
Descripcion
'''

#Paquetes
import numpy as np
from PIL import Image
from bitstring import BitArray
import sys
from source_coding import *
from channel_coding import *
import matplotlib.pyplot as plt
"""                                                         Modulacion
Bits   ______________  simbolos  ______________   señal
      |              |          |              | 
------| bit-> simbolo|----------|    Pulso     |--------->
bcT   |______________|    an   	|______________|	x(t)
"""

#=================================Funciones====================================
class modulation():

	def init (self, m, k, n, mp):
		
		self.m = m
		self.k = k #dimension de cada paquete de bits
		self.n = n # n > k 
		self.mp = mp # 2^k

	#=====================================================================    

	'''
	Se crea una funcion que le asigna simbolos a 
	cada secuencia de bits que sale del canal bcT
	se sabe que M=2^k siendo k=16. M=65536.Aqui
	k es n, es la salida del codificador de canal
	'''

	def symbol_modulator(self, bcT):
		x,y = bcT.shape
		#se pasa el vector de bits obtenido en el canal a senal
		#codigo se pasan de bits a numeros del 0 al 256
		an = []
		for i in range(x):
			 decimal = BitArray(bcT[i])
			 an.append(decimal.uint)   

		return an
	#=====================================================================

	""" 
	Funcion para simular la senal PAM que va ser transmitida por el medio.
	Para simplificacion, solo se tomo los primeros 15 simbolos de an
	y se repiten 30 veces cada una para que se vea bien la grafica
	"""
	
	def PAM(self,an):
		dt = 0.1
		t = np.arange(0, 45, dt)   #hay que corregir esto,el tiempo es el T_simb que no se cual es
		p = []
		for i in range(15):
		    an[i] 
		    for j in range(30):
		        p.append(an[i])
		plt.plot(t,p)
		plt.xlabel('Timepo [s]')
		plt.ylabel('Amplitud')
		plt.title('Senal modulada PAM')
		plt.show()



	#=========DEMODULACION==========================================================


	"""                                      			Demodulacion
	simbolos   ______________  Bits
			  |              |          
	--------->| simbolo->bit |-------->bcT
	 an       |______________|    yn   	
	
	
	Se desmodula asumiendo que el medio es perfecto.
	La funcion pasa los simbolos a secuencia de bits, recibe
	el vector de simbolos (an)
	en este caso an = yn = an*
	"""
	
	def symbol_demodulator(self,an):
		x = []
		bits_sec = []
		for i in range(len(an)):                	#pasa de decimal a binario con 16 bits
			x.append(bin(an[i])[2:].zfill(16))
			
		for i in range(len(x)):						#Se pasan a vectores tipo enteros  
			bits_sec.append([int(i) for i in x[i]])
		yn = np.reshape(bits_sec,(len(x), 16)) 		#se acomoda en una matriz de tal forma que de igual a bcT
		return yn
	#=====================================================================




