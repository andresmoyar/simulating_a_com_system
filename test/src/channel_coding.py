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
from source_coding import *

#=================================Funciones====================================
class com_sys():

	def __init__(self, m, k, n):

		self.m = m #cantidad de paquetes 1xk
		self.k = k #dimension de cada paquete de bits
		self.n = n # n > k 
		self.P = np.random.randint(0, 2, size = (self.k, self.n - self.k))
		self.I = np.identity(self.k) #matriz identidad
		self.E = np.identity(self.n) #vector de error

	#=====================================================================
	'''
	Channel encoder:
	Un metodo que simula un codificador de canal
	solicitando el vector bfK que contiene un numero
	de arreglos 1xk. Se usa una matriz generadora
	para obter u = mG, con cada vector u de tamano
	1 x n. La salida es un array bcT con m paquetes 1xn.
	'''
	def channel_encoder(self, bfT):

		#se crea la matris generadora:
		G = [np.append(self.P[i], self.I[i]) for i in range(self.k)]
		G = np.array(G).astype(int)

		#Se codifican los paquetes 1xk en 1xn:
		bcT = np.dot(bfT, G)

		return bcT
	#=====================================================================
	'''
	Channel decoder:
	Un metodo que simula un decodificador de canal 
	solicitando el arreglo bcR proveniente del
	canal binario simetrico. Se evalua el Sindrome,
	se identifican los errores y se corrigen
	'''
	def channel_decoder(self, bcR):

		#Calculando el sindrome a partir de bcR:
		H = np.vstack((self.I, self.P)).astype(int) #matriz verificadora
		S1 = np.dot(bcR, H)
		S1 = self.set_bin_matrix(S1)

		#Calculado el sindrome a partir del error:
		S2 = np.dot(self.E, H)
		S2 = self.set_bin_matrix(S2)
		
		#Detectando y reparando errores segun sindromes S1 y S2:
		errores = 0
		for i in range(len(S1)):
			for j in range(len(S2)):
				if list(S1[i]) == list(S2[j]):

					bcR[i] = bcR[i] + self.E[j]
					errores += 1

		bfR = np.array([bcR[i][8:] for i in range(self.m)])
		bfR = self.set_bin_matrix(bfR)
		return bfR.astype(str)
	#=====================================================================
	'''
	bin_symmetrical_channel: 
	simula un canal binario simetrico introduciendo
	bits aleatorios en los paquetes 1 x n bajo una
	probabilidad p(e) ajustable. Retorna un arreglo
	de bits contaminados bcR
	'''
	def bin_symmetrical_channel(self, bcT):

		#Generando bits e indicies aleatorios:
		x, y = bcT.shape
		random_bits = np.random.randint(0, 2, size = (self.m, 1))
		random_index = np.random.randint(0, y, size = (self.m, 1))

		#se insertan los bits de error aleatoriamente:
		for i in range(self.m):
			idx = random_index[i]
			bcT[i][idx] = random_bits[i]
		
		return self.set_bin_matrix(bcT)
	#=====================================================================
	'''
	set_bin_matrix:
	una funcion auxiliar que reajusta una matriz 
	a su 'equivalente binario'. Si un elemento es 
	par, entonces coloca un cero. Caso contrario, un 1.
	'''
	def set_bin_matrix(self, array):
		x, y = array.shape
		for i in range(x):
			for j in range(y):

				bit = array[i][j]
				if bit % 2 == 1:
					array[i][j] = 1
				else:
					array[i][j] = 0

		return array.astype(int)
	#=====================================================================
