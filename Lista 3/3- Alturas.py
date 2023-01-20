#   3. Marcos tem 1,50 metro e cresce 2 centímetros por ano, enquanto Lucas tem 1,10
#   metro e cresce 3 centímetros por ano. Construa um algoritmo que calcule e imprima
#   quantos anos serão necessários para que Lucas seja maior que Marcos.

marcos = 1.50
lucas = 1.10
anos = 0

while lucas < marcos:
  marcos += 0.02
  lucas += 0.03
  anos+=1

print(anos)