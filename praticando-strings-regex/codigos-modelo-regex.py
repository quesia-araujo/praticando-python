# Expressões regulares (Regex)
# busca, manipulação e validação de padrão de string
# email, telefone, validação de entrada e etc.
import re
texto = "Entre em contato pelo email support@example.com"
padrao_email = r'[a-z-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

resultado = re.search(padrao_email, texto)

if resultado:
    print("Email encontrado:", resultado.group())
else:
    print("Nenhum email encontrado.")

#-------------------------------------------------------
# Ferramentas
# Testar expressões regulares em ferramentas como o regex101