#Nome: Thalisson Diogo Fernandes Lima
#Data: 05/08/26
#Curso: Desenvolvimento de Jogos Digitais

# 1. Trabalhando com Números (Int e Float)

Idade = int(input("Digite sua idade:"))
Altura = float(input("Digite sua altura(Ex: 1,70):"))

# 2. Manipulação de Textos (Strings)

frase = input("Digite uma frase que você goste:")
print("\n------Analisando seus Dados----")

#Fazendo cálculos simples

print("Sua idade daqui 5 anos será:", Idade+5)
print("Sua altura em centímetros:", Altura*100, "cm")

# 3. Usando Métodos de String
# Explicar o que .upper(), .lower() e o len() fazem

print("Sua frase toda em MAIÚSCULAS:", frase.upper())
print("Sua frase toda em minúsculas:", frase.lower())

print("A sua frase digitada tem", len(frase), "caracteres")
print("--------------------------------------------------------------------------")
