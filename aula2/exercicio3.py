#=========================================================================================
#  OBJETIVO: Ler um ano, e criar 3 variáveis: passado, presente e futuro
#  DATA: 22/03/2025
#  AUTOR: DANIEL GOMES TORRES
#=========================================================================================

numero = int(input('Digite um número: '))

if numero <= -1:
    print('Esse número não é válido porque é um número negativo')
elif numero >= 1:
    print('Esse número é válido pois é um número positivo')