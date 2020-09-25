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
from primera_simulacion import *

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
		random_bits = np.random.randint(0, 2, size = (m, 1))
		random_index = np.random.randint(0, y, size = (m, 1))

		#se insertan los bits de error aleatoriamente:
		for i in range(m):
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


#==============================MAIN======================================
'''
1. Se inicializa la fuente de informaciom
y se llama al codificador de fuente
'''
fuente_info = image_source('./img_scr/dar.bmp')
x, y, z = fuente_info.shape
vT, bfT = source_encoder(fuente_info)

'''
2. Parametros dimensionales: m es el numero
de paquetes 1xk obtenidos del codificador
de fuente en bits; n > k
'''
m, k = bfT.shape
n = 16

'''
3. Se inicializa el objeto sistema, que cuenta
con codificador de canal, canal simetrico
y decodificador de canal con correccion de e.
'''
sistema = com_sys(m, k, n) #Se crea el objeto sistema
bcT = sistema.channel_encoder(bfT)
bcR = sistema.bin_symmetrical_channel(bcT)
#bfR = sistema.channel_decoder(bcR)
bfR = np.array([bcR[i][8:] for i in range(len(bcR))])
bfR = bfR.astype(str)

'''
4. Se llama al decodificador de fuente
y se simula el sumidero para recuperar
la imagen transmitida.
'''
vR = source_Decoder(bfR, x, y, z)
sumidero = Image.fromarray(vR)
sumidero.show()
sumidero.save('./salida.jpg')

