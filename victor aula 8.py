# 1* Verifique se um número é positivo, negativo ou zero.
numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# 2* Verifique se a pessoa pode votar com base na idade.
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você pode votar.")
else:
    print("Você não pode votar.")

# 3* Verifique se um número é par ou ímpar.
numero = int(input("Digite um número para verificar se é par ou ímpar: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

# 4* Verifique o tipo de triângulo com base nos lados fornecidos.
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))
if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")

# 5* Verifique se um número é múltiplo de 5 e 7.
numero = int(input("Digite um número para verificar se é múltiplo de 5 e 7: "))
if numero % 5 == 0 and numero % 7 == 0:
    print(f"O número {numero} é múltiplo de 5 e 7.")
else:
    print(f"O número {numero} não é múltiplo de 5 e 7.")

# 6* Verifique se um número é positivo e maior que 10.
numero = int(input("Digite um número para verificar se é positivo e maior que 10: "))
if numero > 10:
    print(f"O número {numero} é positivo e maior que 10.")
else:
    print(f"O número {numero} não é positivo e maior que 10.")

# 7* Verifique se um número é divisível por 3 ou 5.
numero = int(input("Digite um número para verificar se é divisível por 3 ou 5: "))
if numero % 3 == 0 or numero % 5 == 0:
    print(f"O número {numero} é divisível por 3 ou 5.")
else:
    print(f"O número {numero} não é divisível por 3 ou 5.")
