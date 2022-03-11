from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        print(f'Carro: {piloto}, Trajeto: {trajeto}\n')

t_carro1 = Thread(target=carro, args=[10, 'Python'])
t_carro2 = Thread(target=carro, args=[20, 'Java'])

t_carro1.start()
t_carro2.start()