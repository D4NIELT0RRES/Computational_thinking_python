#=====================================================================================================
#  OBJETIVO: Recebe um nome e uma idade, retorna uma string falando se aquela pessoa pode ou não votar
#  DATA: 08/04/2026
#  AUTOR: DANIEL GOMES TORRES
#=====================================================================================================

def posicao(velocidade, kmAtual):
    psc1 = velocidade + kmAtual
    psc2 = psc1 + kmAtual
    print(f'A posição do seu carro daqui 2 horas será {psc2}')
    return psc2

a = posicao (100, 1)
# assert a == 140
# b = posicao (200, 5)
# assert b == 250
