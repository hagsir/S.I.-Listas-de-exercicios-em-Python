# Faça um algoritmo para ler a temperatura atual e conforme leitura, imprimir o resultado de
# acordo com a tabela
#  até 15°         Muito frio
#  de 16° a 23°    Frio
#  de 23° a 26°    Agradável
#  de 26° a 30°    Calor
#  acima de 31°    Muito quente

temperatura = float(input('Digite a temperatura atual: '))

if temperatura>31:
  print('Muito quente.')
elif temperatura>=26:
  print("Calor")
elif temperatura>=23:
  print("Agradável")
elif temperatura>=16:
  print("Frio")
else:
  print("Muito frio.")