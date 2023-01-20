#Faça um algoritmo que calcule o volume de um cilindro.

raio = float(input('Digite o raio do cilíndro: '))
altura = float(input('Digite a altura do cilíndo: '))
volume = raio**2 * 3.14 * altura
print('O volume do cilíndro é de %.1f .' %volume)