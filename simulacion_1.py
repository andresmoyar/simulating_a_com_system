#!/usr/bin/python3
from PIL import Image
import numpy as np

#---------------------------------------------------------------#
#	Jeaustin Sirias Chacon (jeaustin.sirias@ucr.ac.cr)	#
#		      GitHub: JeaustinSirias			#
#---------------------------------------------------------------#


'''
Este es un script que simula un sistema de comunicacion, considerando 4 
etapas: fuente de informacion, un bloque de codificacion, un canal de
transmision con ruido, 
'''



#=================================Funciones====================================

'''
Una funcion que convierte base decimal
a base binaria en complemento a 1
'''
def DecToBin(num):
	bin_num = bin(num).replace('0b', '')
	if len(bin_num) < 8:
		
		missing_zeros = 8 - len(bin_num)
		for i in range(missing_zeros):
			bin_num = '0' + bin_num 
	return bin_num

'''
Una funcion que simula la fuente cruda
de informacion llamando una imagen de
un directorio del PC
'''
def image_source(img_dir):

	img = Image.open(img_dir)
	return np.array(img)

'''
Una funcion que simula un codificador
de pixeles. Opera conviertiendo los
canales RGB de cada pixel a base 2.
'''
def source_encoder(image_source):
	
	y, x, z = image_source.shape
	vT = []; bfT = ''

	for i in range(y):
		for j in range(x):
		
			r, g, b = image_source[i][j]
			vT.append(r); vT.append(g); vT.append(b)

	for i in range(len(vT)):

		bkT = DecToBin(vT[i])
		bfT += bkT

	#to get bfT 1xk arrays in one vector
	bfT2 = np.array(list(bfT)).astype(int)
	bfT2 = np.array(np.split(bfT2, len(bfT)/8)) #each channel has 8bit
	return vT, bfT, bfT2

'''
Una funcion que simula un canal de
transmision, con ruido. Toma la 
secuencia de bits el codificador
y altera aleatoreamente un porcen-
taje de bits al azar.
'''
def noisy_channel(bits_chain, noise_perc):
	
	#variables: 
	k = 0; bfR = ''
	transport = list(bits_chain)
	
	#porcentaje de ruido:
	noiseDeg = round(len(transport) * (noise_perc/100))

	#generacion de indices y bits aleatoreos:
	noise_size = np.random.random_integers(0, len(transport), (noiseDeg))
	noise = np.random.random_integers(0, 1, (noiseDeg))
	
	for i in noise_size:
		transport[i] = '{}'.format(noise[k]) 
		k += 1
		
	for i in range(len(transport)):
		
		bfR += transport[i]

	return bfR

'''
Una funcion que decodifica la senal de 
bits proporcionada por el canal de trans-
mision y reconstruye los pixeles.
'''
def source_decoder(noised_bits, y, x, z):
	
	bits_list = np.array(list(noised_bits)) #cadena de caracteres a lista
	dimGroups = int(len(bits_list)/8) #8-bits
	split_size = int(dimGroups/3) #3 canales (r, g, b)
	split = np.split(bits_list, dimGroups)
	
	vR = []
	for i in range(dimGroups):

		bkR = ''
		for j in range(8):
			bkR = bkR + split[i][j]
		
		vR.append(int(bkR, 2))
			
	bbk = np.array(np.split(np.array(vR), split_size))	
	vR = np.reshape(bbk, (y, x, z))

	return vR.astype(np.uint8), bbk

#=====================================main======================================

'''
# 1. Se llama la fuente de informacion:
raw_image = image_source('./img_scr/otro.jpeg')
y, x, z = raw_image.shape 

print(raw_image)

# 2. Se codifican los canales r, g, b de cada pixel, en complemento a 1:
vT, bfT = source_encoder(raw_image)

#3. Se simula un canal con ruido 
bfR  = noisy_channel(bfT, 5)

# 4. Se decodifica la informacion entregada por el canal
vR = source_decoder(bfR, y, x, z)

# 5. Se reconstruye la imagen:
img = Image.fromarray(vR)
img.save('output2.jpg')
'''
	
