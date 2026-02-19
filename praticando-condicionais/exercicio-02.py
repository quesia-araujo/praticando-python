"""
Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto.
 Se algum valor for negativo, mostre uma mensagem informando o erro.
"""
atividade_a = int(input("Informe os dias para a atividade A: "))
atividade_b = int(input("Informe os dias para a atividade B: "))
atividade_c = int(input("Informe os dias para a atividade C: "))

if (atividade_a >= 0 and atividade_b >= 0 and atividade_c>= 0):
    tempo_total = atividade_a + atividade_b + atividade_c
    print(f"O tempo total do projeto é de {tempo_total} dias.")
else: 
    print("Erro: Os dias não podem ser negativos")