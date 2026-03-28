#=========================================================================================
#  OBJETIVO: 
# 
        #Escreva um código que define as seguintes variáveis: velocidade do carro e velocidade máxima permitida. Se a velocidade for maior que a máxima permitida, imprima “você tomou multa”

#  DATA: 27/03/2025
#  AUTOR: DANIEL GOMES TORRES
#=========================================================================================

# velocidade_maxima_permitida = 100
# velocidade_carro = 120

# percentual = (velocidade_carro - velocidade_maxima_permitida) / velocidade_maxima_permitida * 100

# if velocidade_carro <= velocidade_maxima_permitida:
#     print("Você não tomou multa")
# elif(percentual <= 20):
#     print("Você levou uma multa de R$ 130,16 e 4 pontos na CNH")
# elif(percentual <= 50):
#     print("Você levou uma multa R$ 195,23 e 5 pontos na CNH")
# else:
#     print("VocÊ levou uma multa de R$ 880,41 e Suspensão da CNH")

#=========================================================================================

v_medida = 160
v_maxima = 80	
limite1  = v_maxima
limite2  = v_maxima + v_maxima*0.2
limite3  = v_maxima + v_maxima*0.5
	
if v_medida > limite1 and v_medida < limite2 :
	print("voce tomou uma multa de", 130.16)
	    
if v_medida >= limite2 and v_medida < limite3 :
	print("voce tomou uma multa de", 195.23)
	
if v_medida >= limite3 :
	print("voce tomou uma multa de", 880.41)
