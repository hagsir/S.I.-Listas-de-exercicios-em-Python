#Escreva um algoritmo que pergunte a quantidade de km percorridos por um carro alugado
#pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o
#preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.

km = int(input('Digite a quantidade de quilômetros percorrido pelo o carro alugado: '))
dias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))
valor = (60*dias) + (km*0.15)
print('O preço a pagar pelo carro alugado é de R$ %.2f .' %valor)