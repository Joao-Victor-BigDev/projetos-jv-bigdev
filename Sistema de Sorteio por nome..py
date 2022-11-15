from random import choice
print('===== SISTEMA DE SORTEIO ===== #BIG')
print('Irei fazer um sorteio para um de voces apagar o quadro ')
nome1 = str(input('Nome do primeiro aluno '))
nome2 = str(input('Nome do segundo aluno '))
nome3 = str(input('Nome do terceiro aluno '))
nome4 = str(input('Nome do quarto aluno '))
lista = [nome1, nome2, nome3, nome4]
escolhido = (choice(lista))
print(f'{escolhido} foi o aluno sorteado, PARABENS! o/')
