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
from src.source_coding import *

#==============================MAIN======================================


# 1. Se llama la fuente de informacion:
raw_image = image_source('/home/jussc_/Desktop/Comunicaciones/Proyecto_simulado/src/teo.jpg')
y, x, z = raw_image.shape 

# 2. Se codifican los canales r, g, b de cada pixel, en complemento a 1:
vT, r, bfT = source_encoder(raw_image)

#3. Se simula un canal con ruido 
bfR  = noisy_channel(bfT, 5)



# 4. Se decodifica la informacion entregada por el canal
vR = source_decoder(bfR, y, x, z)

# 5. Se reconstruye la imagen:
img = Image.fromarray(vR)
img.show()

	
