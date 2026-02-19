"""
Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC 
usando a fórmula: IMC = peso / (altura ** 2)
 Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), 
 peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
"""
peso = int(input("Diite seu peso (kg): "))
altura = int(input("Digite sua altura (m): "))

imc = peso/(altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com peso normal")
else:
    print("Você está acima do peso.")