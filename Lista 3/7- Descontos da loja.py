#  7. Uma loja está com uma promoção, os 20 primeiros clientes ganharão um desconto
#  em suas compras. Para os 10 primeiros clientes, em compras de até R$500, será
#  dado 10% de desconto, em compras maiores que esse valor será dado um
#  desconto de 25%. Já para os outros 10 clientes será dado um desconto de 5% em
#  compras de até R$600 e 15% para compras acima de R$ 600. Mostre o valor
#  original e o valor descontado de todos os 20 clientes.

valor = list(range(20))
 
for i in valor:
  valor[i] = float(input('Você é o %d cliente, digite o valor da sua compra: ' %(i+1)))

for i in range(20):
  if i < 10:
    if valor[i] > 500:
      print('O {0}° cliente pagará R$ {1:.2f} em vez de R$ {2:.2f} .'.format( (i+1), (valor[i]-(valor[i]*0.25)), valor[i] ))
    else:
      print('O {0}° cliente pagará R$ {1:.2f} em vez de R$ {2:.2f} .'.format( (i+1), (valor[i]-(valor[i]*0.1)), valor[i] ))
  else:
    if valor[i] > 600:
      print('O {0}° cliente pagará R$ {1:.2f} em vez de R$ {2:.2f} .'.format( (i+1), (valor[i]-(valor[i]*0.15)), valor[i] ))
    else:
      print('O {0}° cliente pagará R$ {1:.2f} em vez de R$ {2:.2f} .'.format( (i+1), (valor[i]-(valor[i]*0.05)), valor[i] ))
