# defina a quantidade de cada ingrediente por sanduiche
quant_queijo = 0.1 # 2 fatias de queijo = 100g
quant_presunto = 0.05 # 1 fatia de presunto = 50g
quant_carne =  0.1 # 1 rodela de hamburguer = 100g

# lê a quantidade de sanduiches a fazer
qtd_sanduiches = int(input("digite a quantidade de sanduiches a fazer:"))

# calcula a quantidade necessaria de cada ingrediente em quilos
qtd_queijo = quant_queijo * qtd_sanduiches
qtd_presunto = quant_presunto * qtd_sanduiches
qtd_carne = quant_carne * qtd_sanduiches

# exibe as quantidades necessarias de cada ingrediente em quilos
print("para fazer {} sanduiches, é necessario comprar:" .format(qtd_sanduiches))
print("{:.2f} kg de queijo".format(qtd_queijo))
print("{:.2f} kg de presunto".format(qtd_presunto))
print("{:.2f} kg de  carne".format(qtd_carne))
