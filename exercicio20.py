# lê a quantidade de cada tipo de moeda
moeda_1 = int(input("digite a quantidade de moeda de 1 centavo:  "))
moeda_5 = int(input("digite a quantidade de moeda de 5 centavos:  "))
moeda_10 = int(input("digite a quantidade de moeda de 10 centavos: "))
moeda_25 = int(input("digite a quantidade de moeda de 25 centavos: "))
moeda_50 = int(input("digite a quantidade de moeda de 50 centavos: " ))
moeda_1_real = int(input("digite a quantidade de moeda de 1 real: "))

# calcule o valor total economizado em reais
total = moeda_1 * 0.01 + moeda_5 * 0.05 + moeda_10 * 0.1 + moeda_25 *0.25 + moeda_50 *0.5 + moeda_1_real * 1

# imprime o resultado
print(" o total economizado é de R$ {:.2f}" .format(total))