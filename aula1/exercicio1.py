#=====================================
#  OBJETIVO: Cálculo do IMC do usuário
#  DATA: 18/03/2025
#  AUTOR: DANIEL GOMES TORRES
#=====================================

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura (ex: 1.75): "))

imc = peso / (altura * altura)

print(f"O seu IMC é {imc:.2f}")