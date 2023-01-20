#  Escreva um algoritmo para calcular a redução do tempo de vida de um fumante. Pergunte
#  a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um
#  fumante perde 7 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante
#  perderá. Exiba o total em dias.

cigarros = int(input('Digite a quantidade de cigarros fumados por dia: '))
anos = int(input("Digite quantos anos faz que o usuário fuma: "))
result = ((((anos * 365) * cigarros) * 7 ) / 1440)

print('Dias perdidos de vida: %d dias.' %result)