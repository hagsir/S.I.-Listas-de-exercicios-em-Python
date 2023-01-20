#Uma empresa deseja contratar um encanador a R$ 20,00 por dia. Crie um algoritmo que solicite o
#número de dias trabalhados pelo encanador e imprima o valor líquido a ser pago, sabendo
#que são descontados 8% de imposto de renda.

dias = int(input('Digite o número de dias trabalhados pelo encanador: '))
print('O valor líquido a ser pago é de R$ {:.2f} com 8% de juros.'.format(((dias * 20) - ((dias * 20) * 0.08))))