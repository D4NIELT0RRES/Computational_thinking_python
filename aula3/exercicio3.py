#=========================================================================================
#  OBJETIVO: 
# 
#           Dada uma idade de uma pessoa, crie os seguintes booleanos: 
#           Pessoa pode entrar na cabine e votar (direito_voto)
#           Pessoa tem a obrigação de votar (obrigacao_voto)
#           Pessoa tem o voto, mas opcional (voto_opcional)
#
#  DATA: 25/03/2026
#  AUTOR: DANIEL GOMES TORRES
#=========================================================================================

idade = int(input('Digite a sua idade: '))

if (idade >= 16 and idade <18 ) or (idade <=70):
    print('O seu voto é opcional!!')

elif (idade >18) and (idade <70):
    print('O seu voto é obrigatório!!')

else:
    print('Você ainda não pode votar')


######################################################################


idade = 16

voto_opcional = idade >= 16 or idade < 18
voto_obrigatorio = idade >= 18 or idade <= 70
direito_voto = voto_opcional or voto_obrigatorio