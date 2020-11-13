# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Jeaustin Sirias
#
import numpy as np
from numpy.random import randint
from PIL import Image
from bitstring import BitArray
import matplotlib.pyplot as plt
import tikzplotlib as tk

class modulation():

	'''
	Esta es una clase que contiene los
	metodos necesarios para implementar
	un modulador PAM y AKS, con medio ideal y
	ruidoso, asi como un demodulador. 
	Debe usarse junto a las clases
	source() y sys_com() de las sim-
	mulaciones anteriores para ensamblar
	el sistema de comunicaciones completo
	'''
	
    #El constructor:
	def __init__(self, m, k, n):
		
		#numero de paquetes 1 x k:
		self.m = m
		
		#dimension de cada paquete de bits:
		self.k = k 
		
		#dimension de paquetes 1 x n:
		self.n = n # n > k 
		
	#================METODOS==================  

	'''
	Se crea una funcion que le asigna simbolos a 
	cada secuencia de bits que sale del canal bcT
	se sabe que M=2^k siendo k=16. M=65536. Aqui
	k es n, es la salida del codificador de canal
	'''
	def symbol_modulator(self, bcT):
		x, y = bcT.shape
		'''
		se pasa el vector de bits obtenido en el 
		canal a senal codigo se pasan de bits a
		números del 0 a 2^16.
		'''
		an = []
		for i in range(x):
			 decimal = BitArray(bcT[i])
			 an.append(decimal.uint)   

		return an
	#==========================================

	''' 
	Funcion para simular la senal PAM que va ser 
	transmitida por el medio. Para simplificacion, 
	solo se toman los primeros 15 simbolos de an 
	y se repiten 30 veces cada una para que se 
	vea bien la grafica
	'''
	def PAM(self,an):
		dt = 0.1
		t = np.arange(0, 45, dt)  
		p = []
		for i in range(15):
		    an[i] 
		    for j in range(30):
		        p.append(an[i])
		plt.plot(t,p)
		plt.xlabel('Tiempo [s]')
		plt.ylabel('Amplitud')
		plt.title('Señal modulada PAM')
		plt.show()

	#===========================================
	'''
	Una funcion que muestra visualmente los 
	primeros 45 s de la senal modulada por ASK
	No influye en el sistema de comunicaciones
	'''
	def ask_plot(self, an):
		dt = 0.1
		t = np.arange(0, 45, dt)  
		p = []
		An = []
		for i in range(15):
		    for j in range(30):
		        p.append(an[i])

		c = np.sin(2 * np.pi * 0.75 * t)
		plt.plot(t,p)
		plt.plot(t, p*c)
		plt.plot(t, -1*np.array(p))
		plt.xlabel('Tiempo [s]')
		plt.ylabel('Amplitud')
		plt.title('Señal modulada ASK')
		tk.save('ask.tikz')
		plt.show()

	#===========================================
	'''
	Esquema de modulacion ASK para una secuencia
	de simbolos an. Retorna un arreglo sT con 
	dimensiones m x Ns
	'''
	def ask(self, an):

		M = len(an)
		Ns = 10
		xK = []
		t = np.arange(0, M, 0.1)
		cK = np.sqrt(2/1.809) * np.sin(2 * np.pi * t)

		for i in range(M):
		    for j in range(Ns):
		        xK.append(an[i])

		sT = xK * cK
		sT = np.split(sT, M)
		return sT

	#===========================================
	'''
	Esquema de demodulacion para el arreglo sT
	modulado por ASK. No compatible con el 
	metodo PAM de esta misma clase. Retorna
	la secuencia de bits yn recuperada 
	'''
	def ask_demodulator(self, sT):
		#detectando envolvente en k = Ns/2 - 1
		env_arr = []
		for i in range(len(sT)):
			env = round(sT[i][3])
			env_arr.append(env)

		#decodificando simbolos recuperados
		env_arr = np.array(env_arr).astype(int)
		yn = self.symbol_demodulator(env_arr)

		return yn

		

	#===========================================
	'''
	Un metodo que simula un medio de 
	transmision ruidoso para PAM. Pide por 
	parametro an, que corresponde a 
	la secuencia de simbolos y N, 
	el porcentaje de ruido deseado 
	entre [0 - 100]
	'''
	def noised_transmitter(self, an, N):
		#cantidad de ruido
		noise = round(len(an) * (N / 100))

		#simbolos aleatorios
		a = randint(0, 2**16, size = (noise, 1))
		symbs = a.transpose()[0]

		#indices aleatorios
		b = randint(0, self.m, size = (noise, 1))
		index = b.transpose()[0]

		#insertando errores en an:
		k = 0
		for i in index:
			an[i] = symbs[k]
			k += 1
		
		return an

	#===========================================
	'''
	Un metodo que simula un medio de transmision 
	ruidoso para mod ASK. Pide por parametro el 
	vector de muestras S(k) con dimensiones, 
	m x Ns. El parametro N es el porcentaje de 
	ruido deseado entre [0 - 100]
	'''
	def ask_noised_transmitter(self, an, N):
		#cantidad de ruido
		noise = round(len(an) * (N / 100))

		#simbolos aleatorios
		a = randint(0, 2**16, size = (noise, 1))
		symbs = a.transpose()[0]

		#indices aleatorios en la dimension M
		b = randint(0, len(an), size = (noise, 1))
		index = b.transpose()[0]

		#insertando errores en an:
		k = 0
		for i in index:
			an[i][3] = symbs[k]
			k += 1
		
		return an

	#=============================================
	'''
	Un metodo que interpreta simbolos para obtener
	su equivalente binario (decodificacion)
	'''
	def symbol_demodulator(self, an):
		x = []; bits_sec = []
		#pasa de decimal a binario con 16 bits:
		for i in range(len(an)):                	
			x.append(bin(an[i])[2:].zfill(16))

		#Se pasan a vectores tipo enteros:
		for i in range(len(x)):						  
			bits_sec.append([int(i) for i in x[i]])
		'''
		se ordena en una matriz de tal forma 
		que de igual a bcT:
		'''
		yn = np.reshape(bits_sec,(len(x), 16)) 		

		return yn
	#==============================================



