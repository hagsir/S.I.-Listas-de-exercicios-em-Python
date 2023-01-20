# Faça um programa que calcule o fatorial de um número

num = int(input('Digite um número inteiro qualquer: '))
valor = 1

for i in range(num):
  valor*=num
  num = num - 1
  print(valor)