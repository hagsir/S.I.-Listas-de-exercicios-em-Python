#  Desenvolver um algoritmo que leia a altura de 10 pessoas. Este programa deverá
#  calcular e mostrar :
#  a. A menor altura do grupo;
#  b. A maior altura do grupo;

maiorAltura = 0
menorAltura = 0

for i in range(10):
  altura = float(input('Digite a altura da %dª pessoa: ' %(i+1)))
  if i == 0:
    maiorAltura = altura
    menorAltura = altura
  if maiorAltura < altura:
    maiorAltura = altura
  if menorAltura > altura:
    menorAltura = altura

print('A maior altura é: {:.2f}\nA menor altura é: {:.2f}'.format(maiorAltura, menorAltura))
        