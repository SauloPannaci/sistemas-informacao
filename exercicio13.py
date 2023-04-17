preço_custo = float(input("digite o preço de custo do produto:" ))
percentual_acrescimo = float(input(" digite o percentual de acrescimo: "))

preço_venda = preço_custo * (1 + percentual_acrescimo/100)

print(" o preço de venda é: R$ {:.2f}".format(preço_venda))