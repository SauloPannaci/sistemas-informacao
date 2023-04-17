# lê a quantidade de paes e bolos vendidos
quantidade_paes = int(input("digite a quantidade de paes:"))
quantidade_bolos = int(input("digite a quantidade de bolos:"))

# calcule o total com a arrecadaçao de paes e bolos 
valor_total = quantidade_paes *0.12 + quantidade_bolos *1.5

# calcular o valor a ser guardado na poupança (10% do valor arrecadado)
valor_poupança = valor_total *0.1

# exibe os resultados
print("o valor arrecadado foi R$ {:.2f}".format (valor_total))
print("o valor a ser guardado na poupança é R$ {:.2f}".format (valor_poupança))