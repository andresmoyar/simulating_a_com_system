#!/usr/bin/python3
#---------------------------------------------------------------#
#		Jeaustin Sirias Chacon (jeaustin.sirias@ucr.ac.cr)		#
#		      			GitHub: JeaustinSirias					#
#---------------------------------------------------------------#

'''
Descripcion
'''

#Paquetes
import numpy as np
from PIL import Image
import sys
from simulacion_1 import *

#=================================Funciones====================================

class com_sys():

	def __init__(self, M, k, n):

		self.m = M
		self.k = k
		self.n = n
		self.P = np.random.randint(0, 2, size = (self.k, self.n - self.k))
		self.I = np.identity(self.k)

	#=====================================================================
	'''
	Un metodo que simula un codificador de canal
	solicitando el vector bfK que contiene un numero
	de arreglos 1xk. Se usa una matriz generadora
	para obter u = mG, con cada vector u de tamano
	1 x n. La salida es un vector bcT.
	'''
	def channel_encoder(self, bfT):
		G = [np.append(self.P[i], self.I[i]) for i in range(self.k)]
		G = np.array(G).astype(int)
		bcT = [np.dot(bfT[m], G) for m in range(self.m)]
		
		return np.array(bcT)

	#=====================================================================
	
	def channel_decoder(self, bcT):

		H = np.vstack((self.I, self.P)).astype(int) #matriz de verificacion
		return H

	def ideal_channel(self, params)
		pass

	def bin_symmetrical_channel(self, params)
		pass


#=====================================================================
imagen = image_source('./img_scr/teo.jpg')
vT, bft, bfT = source_encoder(imagen)

#parametros
M, k = bfT.shape
n = 16

sistema = com_sys(M, k, n)
bcT = sistema.channel_encoder(bfT)
decodificador = sistema.channel_decoder(bcT)
print(decodificador)
