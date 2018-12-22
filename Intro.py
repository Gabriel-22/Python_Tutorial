print("Hello, World!")

#Comentário de uma linha

"""
Comentário de
múltiplas linhas
"""

# Declaração de variáveis
inteiro = 5 #tipo int
decimal = 4.0 #tipo float
string = "John" #tipo string

print("- ESCREVENDO VALORES:")
print(inteiro)
print(decimal)
print(string)
print(string + " and Mary")
print(inteiro + decimal)

print("- TIPOS DE OBJETOS:")
print(type(inteiro))
print(type(decimal))
print(type(string))

print("- CASTING DE OBJETOS:")
print(int(1.5))
print(float(2))
print(str(3))

print("- MANIPULAÇÃO DE STRINGS:")
s = "Hello, World!"
print(s.upper())
print(s[0:5])
print("Length : " + str(len(s)))
print(s.replace("!", "?"))
print(s.split(","))
print("Digite seu nome: ")
x = input()
print("Hello, " + x)