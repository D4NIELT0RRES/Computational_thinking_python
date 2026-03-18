#==========================================================================================
#  OBJETIVO: Calculando quanto a pessoa vai estar devendo em 1, 2, 3 meses (DÍVIDA E JUROS)
#  DATA: 18/03/2025
#  AUTOR: DANIEL GOMES TORRES
#========================================================================================== 

divida = float(input("Digite o valor da sua divida: ").replace(".", "").replace(",", "."))

juros = 10

aumento = divida * (juros/100)
divida = divida + aumento

aumento = divida * (juros/100)
divida = divida + aumento

aumento = divida * (juros/100)
divida = divida + aumento

print(f"O valor da sua dívida é de R${divida:.2f}")