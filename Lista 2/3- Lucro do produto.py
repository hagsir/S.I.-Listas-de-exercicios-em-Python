#Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da
#compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. Elabore um
#algoritmo que leia o valor do produto e imprima o valor de venda para o produto.

valor = float(input('Digite o valor do produto: '))

if valor>20:
  valor += valor*0.45
else:
  valor += valor*0.45

print('O valor de venda do produto deverá ser de R$ %.2f .' %valor)