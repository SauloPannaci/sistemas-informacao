# solicita a entrada do nome do vendedor, salário fixo e total de vendas
nome_vendedor = input("digite o nome do vendedor: ")
salari0_fixo = float(input("digite o salario fixo do vendedor: "))
total_vendas = float(input("digite o total de vendas do vendedor no mes: "))

# calcula a comissao do vendedor e o salario final
comissao = total_vendas * 0.15
salario_final = salari0_fixo + comissao

# mostra o resultado na tela
print("nome do vendedor:", nome_vendedor)
print("salario fixo: R$ {:.2f}".format(salari0_fixo))
print("comissao: R$ {:.2F}".format(comissao))
print("salario final: R$ {:.2f}".format(salario_final))
