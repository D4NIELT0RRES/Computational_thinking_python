from datetime import date

#=======================================================================================================================================================
#  OBJETIVO: Ler o ano de nascimento de uma pessoa (assumindo que ela já fez aniversário esse ano) criar uma variável que indica se ela é maior de idade
#  DATA: 22/03/2025
#  AUTOR: DANIEL GOMES TORRES
#=======================================================================================================================================================


ano_nasc = int(input('Digite o ano em que você nasceu: '))

ano_atual = date.today().year

idade = ano_atual - ano_nasc

if ano_nasc >= ano_atual:
    print(f'Você é menor de idade, porque você tem {idade} anos de idade')
else:
    print(f'Você é maior de idade, porque você tem {idade} anos de idade')