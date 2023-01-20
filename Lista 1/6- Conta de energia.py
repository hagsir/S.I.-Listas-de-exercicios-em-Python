#Um cliente gostaria de saber o quanto de seu salário é destinado ao pagamento da conta de
#energia elétrica. Sabendo que a tarifa é R$ 0,78 por kWh, faça um algoritmo que receba o
#salário do cliente e seu consumo (em kWh), e imprima qual a porcentagem do salário do
#cliente deve ser destinado para pagamento da conta de energia elétrica.

salario = float(input('Digite o seu salário: '))
kwh = float(input('Digite o seu consumo de energia em kWh: '))
porcentagem =  (100 * (kwh * 0.78)) / salario
print('A porcentagem do seu salário destinado a conta de energia é de %.1f%%' %porcentagem)