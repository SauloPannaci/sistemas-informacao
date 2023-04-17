# digite os dados

valor_depositado = float(input("digite o valor que foi depositado:"))

juros = 0.0070  # 0,70% ao mês
rendimentos = valor_depositado * juros

valor_total = valor_depositado + rendimentos

print(" o valor com rendimentos apos um mes é: R$ {:.2f}".format(valor_total))