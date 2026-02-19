"""
Crie um programa que receba o número de vendas dos dois produtos
e exiba uma mensagem indicando qual deles vendeu mais. 
Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
"""
produto_1 = int(input("Digite a quantidade de maçãs vendidas: "))
produto_2 = int(input("Digite a quantidade de bananas vendidas: "))

if produto_1 > produto_2:
    print("As maças tiveram mais vendas")
elif produto_2 > produto_1:
    print("As bananas tiveram mais vendas")
else:
    print("As vendas foram iguais")