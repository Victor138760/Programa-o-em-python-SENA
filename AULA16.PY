

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

def verificar_positivo_negativo_zero(numero):
    if numero > 0:
        print(f"O número {numero} é positivo.")
    elif numero < 0:
        print(f"O número {numero} é negativo.")
    else:
        print(f"O número é zero.")

def verificar_string_vazia(string):
    if string == "":
        print("A string está vazia.")
    else:
        print("A string não está vazia.")

def verificar_maior_menor_igual_a_10(numero):
    if numero > 10:
        print(f"O número {numero} é maior que 10.")
    elif numero < 10:
        print(f"O número {numero} é menor que 10.")
    else:
        print(f"O número {numero} é igual a 10.")

def classificar_idade(idade):
    if idade <= 12:
        print("Você é uma criança.")
    elif 13 <= idade <= 17:
        print("Você é um jovem.")
    elif 18 <= idade <= 59:
        print("Você é um adulto.")
    else:
        print("Você é um idoso.")

# Exemplo de uso das funções
numero = int(input("Digite um número: "))
verificar_par_ou_impar(numero)
verificar_positivo_negativo_zero(numero)
verificar_maior_menor_igual_a_10(numero)

string = input("Digite uma string: ")
verificar_string_vazia(string)

idade = int(input("Digite a sua idade: "))
classificar_idade(idade)
