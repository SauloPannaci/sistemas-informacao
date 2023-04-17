custo_fabrica = float(input("Digite o custo de fabrica do carro:"))

# calcular a percentagem do distribuidor e dos impostos
percentagem_distribuidor = 0.28
percentagem_impostos = 0.45

#calcular o custo ao consumidor
custo_consumidor = custo_fabrica * (1+ percentagem_distribuidor + percentagem_impostos)

# imprimir o custo ao consumidor
print("o custo ao consumidordo carro é: R$",custo_consumidor)

