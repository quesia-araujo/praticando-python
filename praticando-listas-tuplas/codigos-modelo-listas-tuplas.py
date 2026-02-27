# Listas
# Coleções de elementos mutáveis (adicionar, remover pu modificar elementos).
# Colchetes
lista = [1, 2, 3]

lista_mista = [1, "texto", 3.14, True, [1,2,3]]

# Tuplas coleções imutáveis
# parênteses
tupla = (1, 2, 3)
tupla_mista = (1, "texto", 3.14, False, [1,2,3])

# Operações comuns
# ---- Acesso por Índice ------
lista = [10, 20, 30]
print(lista[1])

tupla = (11, 42, 64)
print(tupla[1])

# ---- slicing ------
# extri partes da coleção, criando uma substrutura a partir de um intervalo de índices.
lista = [10, 20, 30, 40]
print(lista[1:3])

tupla = (10, 20, 30, 40)
print(tupla[1:3])

# ---- opeador in ----
lista = [10, 20, 30]
print(20 in lista)
print(40 in lista)

# Manipulação de listas
# append(), insert(), remove(), sort(), reverse()

# Concatenação de tuplas
tupla1 = (1,2)
tupla2 = (3,4)

nova_tupla = tupla1 + tupla2

# Iteração sobre elementos
lista = [1, 2, 3, 4]
for item in lista:
    print(item)

# Desempacotando
lista = [10, 20, 30]
x, y, z = lista
print(x, y, z)