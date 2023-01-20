# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
# algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#     para homens: (72.7 * h) – 58
#     para mulheres: (62.1 * h) – 44.7

altura = float(input("Digite a sua altura: "))
sexo = input("Digite o seu sexo, homem ou mulher: ")

if sexo == 'homem' or sexo == 'Homem': 
  print("O peso ideal para você é de %.1f kg." %((72.7 * altura) - 58))
if sexo == 'mulher' or sexo == 'Mulher':
  print("O peso ideal para você é de %.1f kg." %((62.1 * altura) - 44.7))
