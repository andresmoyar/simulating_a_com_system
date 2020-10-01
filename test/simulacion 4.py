'''
SIMULACION DE UN SISTEMA DE COMUNICACIONES CON CODIFICADOR
DE CANAL, CANAL BINARIO SIMETRICO + MODULACION + 
DEMODULACION + DECODIFICADOR DE CANALCON CORRECCION DE ERRORES
'''

#Paquetes
import numpy as np
from PIL import Image
import sys
from modulationcoding import *
from channel_coding import *
from source_coding import *

#==============================MAIN======================================
'''
1. Se inicializa la fuente de informaciom
y se llama al codificador de fuente
'''
fuente_info = image_source('dar.bmp')
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
'''
sistema = com_sys(m, k, n) #Se crea el objeto sistema
bcT = sistema.channel_encoder(bfT)
bcB = sistema.set_bin_matrix(bcT)
#bcR = sistema.bin_symmetrical_channel(bcT)


'''
4. Se inicializa el modulador, medio de transmision
y desmodulador
'''

modem = modulation()
an = modem.symbol_modulator(bcT)

pam =modem.PAM(an)

yn = modem.symbol_demodulator(an)



'''
5. Se inicializa decodificador de canal con correccion de e.
'''
bfR = sistema.channel_decoder(yn)# -----> meter aca yn
#Ruido
#bfR = np.array([bcR[i][8:] for i in range(len(bcR))])
#bfR = bfR.astype(str)

'''
6. Se llama al decodificador de fuente
y se simula el sumidero para recuperar
la imagen transmitida.
'''
vR = source_Decoder(bfR, x, y, z)
sumidero = Image.fromarray(vR)
sumidero.show()
#sumidero.save('./salida.jpg')