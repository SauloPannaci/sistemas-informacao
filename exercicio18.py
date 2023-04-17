# le o salario do funcionario
salario = float(input("digite o salario do funcionario:"))

# calcula o novo salario com aumento de 15%
novo_salario = salario * 1.15

# calcule o salario final apos descontar 8% de impostos
salario_final = novo_salario * 0.92

# exibe os resultados
print("salario inicial: R$ {:.2f}".format(salario))
print("salario com aumento: R$ {:.2f}".format(novo_salario))
print("salario final apos descontar impostos: R$ {:.2f}".format(salario_final))