#Joãozinho comprou um cofrinho e resolveu juntar moedas para economizar. Crie um
#algoritmo que calcule o valor, em reais, economizado. Considere a existência das
#seguintes moedas: 5, 10, 25, 50 centavos e 1 real.*/

m5 = int(input('Digite quantas moedas de 5 centavos há no cofre: '))
m10 = int(input('Digite quantas moedas de 10 centavos há no cofre: '))
m25 = int(input('Digite quantas moedas de 25 centavos há no cofre: '))
m50 = int(input('Digite quantas moedas de 50 centavos há no cofre: '))
m100 = int(input('Digite quantas moedas de 1 real há no cofre: '))

valor = (m5*0.05) + (m10*0.1) + (m25*0.25) + (m50*0.5) + m100

print('Há R$ %.2f reais no cofre.' %valor)