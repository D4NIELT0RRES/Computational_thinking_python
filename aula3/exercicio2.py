#=========================================================================================
#  OBJETIVO: 
# 
#           Exercício: Escreva um programa para determinar se uma pessoa deve ou não pagar imposto, 
#           considerando seu salário mensal – procure no google o salário anual mínimo que exige o 
#           pagamento de imposto
#
#  DATA: 25/03/2026
#  AUTOR: DANIEL GOMES TORRES
#=========================================================================================

salario = float(input('Digite o valor do seu salário mensal: '))

if salario <= 5000:
    print('Você não precisa pagar imposto sobre o seu salário!!')
else:
    print('Você precisa pagar imposto sobre o seu salário')


######################################################################

salarioAtual = float(input('Digite o valor do seu salário: '))

salarioAtual = salarioAtual * 12

if salarioAtual <= 60000:
    print('Você não paga imposto pelo seu anual')

else: 
    print('Voê deve pagar imposto pelo seu salário anual')
