#====================================================================================================
#  OBJETIVO: Calcular a tarifa do taxi dado o número de KMs rodados e o número de horas paradas
#  DATA: 18/03/2025
#  AUTOR: DANIEL GOMES TORRES
#===================================================================================================== 

tarifa_base = 4.5
preco_km = 8
preco_hora_parada = 44

km_rodado = int(input("Digite a quantidade de KMs rodados: "))
horas_esperadas = int(input("Digite a quantidade de horas paradas: "))

preco_corrida = tarifa_base
preco_corrida = preco_corrida + (preco_km * km_rodado)
preco_corrida = preco_corrida + (preco_hora_parada * tarifa_base)

print("O valor da corrida é de R$",preco_corrida)