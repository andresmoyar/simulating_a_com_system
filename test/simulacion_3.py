#!/usr/bin/python3
#---------------------------------------------------------------#
#		Jeaustin Sirias Chacon (jeaustin.sirias@ucr.ac.cr)		#
#		      			GitHub: JeaustinSirias					#
#---------------------------------------------------------------#

'''
SIMULACION DE UN SISTEMA DE COMUNICACIONES CON CODIFICADOR
DE CANAL, CANAL BINARIO SIMETRICO + DECODIFICADOR DE CANAL
CON CORRECCION DE ERRORES
'''

#Paquetes
import numpy as np
from PIL import Image
from src.channel import *
from src.source import *

#==============================MAIN======================================
'''
1. Se inicializa la fuente de informaciom
y se llama al codificador de fuente
'''
fuente_info = image_source('/home/jussc_/Desktop/Comunicaciones/Proyecto_simulado/src/dar.bmp')
x, y, z = fuente_info.shape
vT, bfT, r = source_encoder(fuente_info)

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
bfR = sistema.channel_decoder(bcR)


'''
4. Se llama al decodificador de fuente
y se simula el sumidero para recuperar
la imagen transmitida.
'''
vR = source_Decoder(bfR, x, y, True, 8)
sumidero = Image.fromarray(vR)
sumidero.show()
#sumidero.save('./salida.jpg')

