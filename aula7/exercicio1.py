#=======================================================================================================
#  OBJETIVO: # Sua missão: receber uma idade, um total de anos de contribuição, e o sexo, e responder se
#               a pessoa já pode pedir a aposentadoria. (retornando True ou False)
#               Consideraremos a regra para trabalhadores urbanos, descrita no link
#               Detalhes: o sexo será enviado como "homem" ou "mulher"

#  DATA: 15/04/2026
#  AUTOR: DANIEL GOMES TORRES
#=======================================================================================================


# def pode_aposentar(sexo, anoContribuicao, idade):
#     if sexo == "homem" and anoContribuicao >= 15 and idade >= 65:
#         print("Você pode se aposentar")
#           return False
#     if sexo == "mulher" and anoContribuicao >= 15 and idade >= 62:
#         print("Você pode se aposentar")
#           return False
#       return True

    
    
    
# assert (pode_aposentar("mulher", 10, 70) == False)
# assert (pode_aposentar("mulher", 20, 70) == True)
# assert (pode_aposentar("homem", 20, 50) == False)
# assert (pode_aposentar("homem", 12, 70) == False)
# assert (pode_aposentar("homem", 17, 70) == True)

###########################################################################################################

def pode_aposentar(sexo, anoContribuicao, idade):
    if sexo == "homem" and (anoContribuicao < 15 and idade < 65):
        print("Homem não pode se aposentar")
        return False
    if sexo == "mulher" and (anoContribuicao < 15 and idade < 62):
        print("Você pode se aposentar")
        return False

    
    
    
assert (pode_aposentar("mulher", 10, 70) == False)
assert (pode_aposentar("mulher", 20, 70) == True)
assert (pode_aposentar("homem", 20, 50) == False)
assert (pode_aposentar("homem", 12, 70) == False)
assert (pode_aposentar("homem", 17, 70) == True)