# Crie um programa que calcula o IMC de uma pessoa e que informe
# a situação dela segundo a tabela:
# Menor do que 18,5 - Abaixo do peso normal
# 18,5 ; 24,9 - Peso normal
# 25,0 ; 29,9 - Excesso de peso
# Maior do que 30  - Obesidade

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura**2;

if imc >= 30: print('Obesidade.')

elif imc >= 25: print('Excesso de peso.')

elif imc >= 18.5: print('Peso normal.')
  
else: print('Abaixo do peso normal.')

