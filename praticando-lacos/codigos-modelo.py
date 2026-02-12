# for elemento in iterável:
#    bloco de código
nomes = ["Carlos", "Ana", "Pedro", "Maria"]

for nome in nomes:
    print(nome)

print("\n")
# ------------------------------------------
# while condicao:
#    bloco de código
contador = 0

while contador < 5:
    print(f"Contador atual: {contador}")
    contador += 1

print("\n")
#------------------------------------------
# Loop Infinito
# contador = 0
# while contador < 5:
#     print("Contador:", contador)

print("\n")
#-----------------------------------------
# Uso do break
nomes = ["PM3", "Alura", "Latam", "Outros"]

for nome in nomes:
    if nome == "Alura":
        print("Nome encontrado! Saindo do laço.")
        break
    print(nome)

print("\n")
#-----------------------------------------
# Uso do continue
nomes = ["PM3", "Alura", "Latam", "Outros"]

for nome in nomes:
    if nome == "Alura":
        print("Ignorando Alura.")
        continue
    print(f"Nome: {nome}")

# Funções úteis em laços

# len() é utilizada para obter o comprimento de uma lista, string ou outro tipo de coleção.
#  Ela nos permite saber quantas iterções precisamos realizar em um laço.

# range(), gera uma sequência de números, que é frequentemente utilizada para controlar a iteração em laços for.
#  Com ela podemos especifivar um intervalo de númeors para iterar, podemos também definir um passo. 
# Por exemplo, range(6) gera os númeos de 0 a 5.