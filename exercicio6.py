# solicite a entrada do nome do aluno e suas notas
nome_aluno = input("digite o nome do aluno:")
nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("digite a tereira nota:"))

#clacula a media aritmética das notas
media = (nota1 + nota2 +nota3) / 3

# mostra o resultado na tela
print("o aluno",nome_aluno,"obteve média",media)