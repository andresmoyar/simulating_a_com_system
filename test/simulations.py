
#Paquetes
import numpy as np
from PIL import Image
from .context import source, channel, modulation, filepath

# Loads the image file to proccess
path = filepath('data/', 'dar.bmp')[0]

class sims():
    '''Una clase que contiene todas la simulaciones realizadas hasta ahora
    de forma progresiva con sus componentes'''
    #===============================================================================
    def simulation_1(self):
        # 1. Se llama la fuente de informacion:
        raw_image = source.image_source(path)
        y, x, z = raw_image.shape 

        # 2. Se codifican los canales r, g, b de cada pixel, en complemento a 1:
        vT, r, bfT = source.source_encoder(raw_image)

        #3. Se simula un canal con ruido 
        bfR  = source.noisy_channel(bfT, 5)

        # 4. Se decodifica la informacion entregada por el canal
        vR = source.source_decoder(bfR, y, x, z)

        # 5. Se reconstruye la imagen:
        img = Image.fromarray(vR)
        img.show()
    #===============================================================================
    def simulation_2(self):
        '''
        1. Se inicializa la fuente de informaciom
        y se llama al codificador de fuente
        '''
        fuente_info = source.image_source(path)
        x, y, z = fuente_info.shape
        vT, bfT, r = source.source_encoder(fuente_info)
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
        sistema = channel.com_sys(m, k, n) #Se crea el objeto sistema
        bcT = sistema.channel_encoder(bfT)
        bcR = sistema.bin_symmetrical_channel(bcT)
        bfR = np.array([bcR[i][8:] for i in range(len(bcR))])
        bfR = bfR.astype(str)
        '''
        4. Se llama al decodificador de fuente
        y se simula el sumidero para recuperar
        la imagen transmitida.
        '''
        vR = source.source_Decoder(bfR, x, y, z, 8)
        sumidero = Image.fromarray(vR)
        sumidero.show()
        #sumidero.save('./salida.jpg')
    #===============================================================================
    def simulation_3(self):
        '''
        1. Se inicializa la fuente de informaciom
        y se llama al codificador de fuente
        '''
        fuente_info = source.image_source(path)
        x, y, z = fuente_info.shape
        vT, bfT, r = source.source_encoder(fuente_info)
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
        sistema = channel.com_sys(m, k, n) #Se crea el objeto sistema
        bcT = sistema.channel_encoder(bfT)
        bcR = sistema.bin_symmetrical_channel(bcT)
        bfR = sistema.channel_decoder(bcR)
        '''
        4. Se llama al decodificador de fuente
        y se simula el sumidero para recuperar
        la imagen transmitida.
        '''
        vR = source.source_Decoder(bfR, x, y, True, 8)
        sumidero = Image.fromarray(vR)
        sumidero.show()
        #sumidero.save('./salida.jpg')
    #===============================================================================
    def simulation_4(self):
        '''
        1. Se inicializa la fuente de informacion
        y se llama al codificador de fuente
        '''
        fuente_info = source.image_source(path)
        x, y, z = fuente_info.shape
        vT, bfT, r = source.source_encoder(fuente_info)
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
        #Se crea el objeto sistema:
        sistema = channel.com_sys(m, k, n) 
        bcT = sistema.channel_encoder(bfT)
        '''
        4. Se inicializa el modulador, medio
        ideal y desmodulador
        '''
        modem = modulation.modulation(m, k, n)
        an = modem.symbol_modulator(bcT)
        modem.PAM(an)
        yn = modem.symbol_demodulator(an)
        '''
        5. Se inicializa decodificador de canal.
        '''
        bfR = sistema.channel_decoder(yn)
        '''
        6. Se llama al decodificador de fuente
        y se simula el sumidero para recuperar
        la imagen transmitida.
        '''
        vR = source.source_Decoder(bfR, x, y, True, 8)
        sumidero = Image.fromarray(vR)
        sumidero.show()
    #===============================================================================
    def simulation_5(self):
        '''
        1. Se inicializa la fuente de informaciom
        y se llama al codificador de fuente
        '''
        fuente_info = source.image_source(path)
        x, y, z = fuente_info.shape
        vT, bfT, r = source.source_encoder(fuente_info)
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
        sistema = channel.com_sys(m, k, n) #Se crea el objeto sistema
        bcT = sistema.channel_encoder(bfT)
        '''
        4. Se inicializa el modulador, medio
        de transmision con ruido al 20 % y 
        desmodulador
        '''
        modem = modulation.modulation(m, k, n)
        an = modem.symbol_modulator(bcT)
        modem.PAM(an)
        an = modem.noised_transmitter(an, 20)
        yn = modem.symbol_demodulator(an)
        '''
        5. Se inicializa decodificador de canal.
        '''
        bfR = sistema.channel_decoder(yn)
        '''
        6. Se llama al decodificador de fuente
        y se simula el sumidero para recuperar
        la imagen transmitida.
        '''
        vR = source.source_Decoder(bfR, x, y, True, 8)
        sumidero = Image.fromarray(vR)
        sumidero.show()
        #sumidero.save('./salida2.jpg')
    #===============================================================================
    def simulation_6(self):
        '''
        1. Se inicializa la fuente de informacion
        y se llama al codificador de fuente
        '''
        fuente_info = source.image_source(path)
        x, y, z = fuente_info.shape
        vT, bfT, r = source.source_encoder(fuente_info)
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
        #Se crea el objeto sistema:
        sistema = channel.com_sys(m, k, n) 
        bcT = sistema.channel_encoder(bfT)
        '''
        4. Se inicializa el modulador, medio
        ideal y desmodulador
        '''
        modem = modulation.modulation(m, k, n)
        an = modem.symbol_modulator(bcT)
        sT = modem.ask(an)
        yn = modem.ask_demodulator(sT)
        '''
        5. Se inicializa decodificador de canal.
        '''
        bfR = sistema.channel_decoder(yn)
        '''
        6. Se llama al decodificador de fuente
        y se simula el sumidero para recuperar
        la imagen transmitida.
        '''
        vR = source.source_Decoder(bfR, x, y, True, 8)
        sumidero = Image.fromarray(vR)
        sumidero.show()
        #sumidero.save('noised.jpg')
    #===============================================================================
    def simulation_7(self):
        '''
        1. Se inicializa la fuente de informacion
        y se llama al codificador de fuente
        '''
        fuente_info = source.image_source(path)
        x, y, z = fuente_info.shape
        vT, bfT, r = source.source_encoder(fuente_info)
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
        #Se crea el objeto sistema:
        sistema = channel.com_sys(m, k, n) 
        bcT = sistema.channel_encoder(bfT)
        '''
        4. Se inicializa el modulador, medio
        ideal y desmodulador
        '''
        modem = modulation.modulation(m, k, n)
        an = modem.symbol_modulator(bcT)
        sT = modem.ask(an)
        sN = modem.ask_noised_transmitter(sT, 50)
        yn = modem.ask_demodulator(sN)
        '''
        5. Se inicializa decodificador de canal.
        '''
        bfR = sistema.channel_decoder(yn)
        '''
        6. Se llama al decodificador de fuente
        y se simula el sumidero para recuperar
        la imagen transmitida.
        '''
        vR = source.source_Decoder(bfR, x, y, True, 8)
        sumidero = Image.fromarray(vR)
        sumidero.show()
        #sumidero.save('noised.jpg')
    #===============================================================================
    #===============================================================================