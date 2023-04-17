# lê a quantidade de camisetas pequenas vendidas
qtd_pequenas = int(input("digite a quabtidade de camisetas pequenas vendidas:" ))

# lê a quantidade de camisetas medias vendidas
qtd_media = int(input("digite a quantidade de camisetas medias vendidas:" ))

# lê a quantidade de camisetas grandes vendidas
qtd_grandes = int(input("digite a quantidade de camisetas grandes vendidas:" ))

# calcule o valor arrecadado
valor_arrecadado = qtd_pequenas * 10 + qtd_media * 12 + qtd_grandes * 15

# exibe o resultado
print(" o valor arrecadado foi de R${:.2f}".format(valor_arrecadado))
                    
 