#====================================================================================================
#  OBJETIVO: Calcular o PIB do pais de acordo com o aumento que o usuário digital
#  DATA: 18/03/2025
#  AUTOR: DANIEL GOMES TORRES
#=====================================================================================================

# nomePais = input("Digite o nome de um país: ")
# pibAtual = float(input("Digite o PIB atual deste país: ").replace(".", "").replace(",", "."))

# pibFormatado = f"{pibAtual:,.0f}".replace(",", ".")

# print(f"No ano de 2024 o PIB do país {nomePais} era de {pibFormatado}")



nomePais = input("Digite o nome do país: ")
pib = float(input("Digite o PIB atual: ").replace(".", "").replace(",", "."))

# ANO 1
p = float(input("Digite o percentual do próximo ano: "))
pib = pib + (pib * p / 100)
print(f"Novo PIB: {pib:.2f}")

