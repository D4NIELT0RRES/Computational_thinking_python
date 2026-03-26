#=========================================================================================
#  OBJETIVO: 
# 
        # Faça um programa que retorne verdadeiro ou falso sobre sua aprovação na disciplina, 
        # considerando a presença (um numero de 0 a 100, indicando a porcentagem de presença) e 
        # a nota (de 0 a 10)

#  DATA: 25/03/2025
#  AUTOR: DANIEL GOMES TORRES
#=========================================================================================

presenca = int(input('Digite a sua porcentagem de presença no semestre: '))
nota = int(input('Digite qual foi a sua nota nesta disciplina: '))


# #Esse if, vai desenvolver a lógica e saber se a presença é maior ou igual a 75 e a nota é maior ou igual a 6
# if (presenca >= 75) and (nota >= 6):
#     print('\n Você foi aprovado nesta matéria')

# #Esse elif, vai desenvolver a lógica e saber se a presença é menor ou igual a 75 e a nota maior ou igual que 6
# elif (presenca <= 75) and (nota >= 4  and nota <= 6):
#     print('\n Você está em recuperação')

# #Esse if, vai desenvolver a lógica e saber se a presença é maior que 75 e a nota menor que 6
# elif (presenca >= 75) and (nota <= 6):
#     print('\n Você está em recuperação')
# else:
#     print('\n Você ficou detido nesta disciplina')

def aprovado(nota, presenca):

    if (presenca >= 75) and (nota >= 6):
        print('\n Você foi aprovado nesta matéria')

    elif (presenca <= 75) and (nota >= 4  and nota <= 6):
        print('\n Você está em recuperação')

    elif (presenca >= 75) and (nota <= 6):
        print('\n Você está em recuperação')
    else:
        print('\n Você ficou detido nesta disciplina')




