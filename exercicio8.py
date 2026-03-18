#====================================================================================================
#  OBJETIVO: Fazer um programa que recebe um nome, uma quantidade de vezes, 
#            produz e imprime uma nova string, que repe o nome pelo numero de vezes pedido.
#
#  DATA: 18/03/2025
#  AUTOR: DANIEL GOMES TORRES
#=====================================================================================================

nome = input("Digite um nome: ")
repeticao = int(input("Digite o número de vezes que aquele nome deve se repetir: "))

resultado = (nome + " ") * repeticao

print( resultado )