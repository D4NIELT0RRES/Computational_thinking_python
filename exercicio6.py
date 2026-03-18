#====================================================================================================
#  OBJETIVO: Imprimir um valor guardado em KM para as medidas, m/h e m/s
#  DATA: 18/03/2025
#  AUTOR: DANIEL GOMES TORRES
#=====================================================================================================

velocidade = float(input("Digite o valor em KM/H: "))

kmh = velocidade
ms = kmh / 3.6

print(f"O valor em KM/H é {kmh:.2f}, em M/S é {ms:.2f}")

