#==========================================================================================
#  OBJETIVO: Calculando 
#  DATA: 18/03/2025
#  AUTOR: DANIEL GOMES TORRES
#========================================================================================== 

# Dada uma quantidade de minutos e um aumento em minutos, dizer qual o próximo valor dos minutos (depois a gente pensa na hora!)
# minutos 
# Agora acrescente a(s) horas!

minutos = int(input("Digite a quantidade de minutos: "))
aumento = int(input("Digite o aumento em minutos: "))

proxMinuto = minutos + aumento

if proxMinuto >= 60:
    hora = proxMinuto // 60
    minutos = proxMinuto % 60
    print(f"{hora}h e {minutos}min ")
else:
    print(f"A quantidade de minutos total é de {proxMinuto} min ")
