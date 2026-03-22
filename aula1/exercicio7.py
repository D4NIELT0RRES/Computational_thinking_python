#====================================================================================================
#  OBJETIVO: Calcular o PIB do pais de acordo com o aumento que o usuário digital
#  DATA: 18/03/2025
#  AUTOR: DANIEL GOMES TORRES
#=====================================================================================================


nomePais = input("Digite o nome do país: ")
pib = float(input("Digite o PIB atual: ").replace(".", "").replace(",", "."))

# ANO 1
p = float(input("Digite o percentual do próximo ano: "))
pib = pib + (pib * p / 100)
print(f"Novo PIB: {pib:.2f}")

