mensagem = 'Olá mundo'
mensagem = "Python é incrível"
texto = """Essa é uma string que pode ter múltiplas linhas"""

#------------------------------
# f-strings
# Elas usam a sintaxe f"{variável}"
estudante = "Pedro"
nota = 10
mensagem = f"{estudante} tirou a nota {nota}!"

print(mensagem)

#-------------------------------
# Indexação de strings
texto = "python"

print(texto[5])
print(texto[-1])

#-------------------------------
# Slicing: extrair parte da string
# string[inicio:fim:passo]
texto = "Python"
print(texto[1:4])
print(texto[:3])
print(texto[::2])

#--------------------------------
# Operador in
# Verifica se uma substring está presente m uma strinh
texto = "Python"
print("Py" in texto)
print("Java" in texto)

#--------------------------------
# Método startswith()
# Método endswith()
print(texto.startswith("Py"))
print(texto.startswith("py"))

print(texto.endswith("on"))
print(texto.endswith("ton"))
