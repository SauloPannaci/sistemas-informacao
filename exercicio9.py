# solicite a entrada do preço da gasolina e do valor do pagamento
preço_gasolina = float(input("digite o preço da gasolina por litros:"))
valor_pagamneto =float(input("difgite o valor do pagamento:"))

# calcula quantos litros de gasolina podem ser comprados com o valor especificado
litros = valor_pagamneto / preço_gasolina

# Mostra o resultado na tela
print("com R$ {:.2f} é possivel comprar {:.2f} litros de gasolina.".format(valor_pagamneto, litros))