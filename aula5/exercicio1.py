from datetime import datetime
#=====================================================================================================
#  OBJETIVO: Recebe um nome e uma idade, retorna uma string falando se aquela pessoa pode ou não votar
#  DATA: 08/04/2025
#  AUTOR: DANIEL GOMES TORRES
#=====================================================================================================


def calculoIdade(nome, ano_nascimento):
    agora = datetime.now()
    anoAtual = agora.year
    idade = anoAtual - ano_nascimento
    print(f"{nome} você tem {idade} anos de idade")
    return idade

a = calculoIdade("Daniel", 2007)