c = 0
while c >= 0   :
   if c <= 1000 :
    print(c)
    c =+ (c + 1 )
   else :
    break

def calcular_media(notas):
    return sum(notas) / len(notas)


def sistema_de_notas():
    usuario_correto = "admin"
    senha_correta = "1234"
    
    tentativas = 0
    
    while tentativas < 3:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        
        if usuario == usuario_correto and senha == senha_correta:
            print("Acesso concedido.")
            break
        else:
            tentativas += 1
            print(f"Credenciais incorretas. Você tem {3 - tentativas} tentativa(s) restantes.")
        
        if tentativas == 3:
            print("Conta bloqueada. Você excedeu o número de tentativas.")
            return 
    
 
    notas = []
    for i in range(3): 
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1}: "))
                if 0 <= nota <= 10:  
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Por favor, insira um número válido.")
    
   
    media = calcular_media(notas)
    print(f"A média das notas é: {media:.2f}")
    
   
    if media >= 7:
        print("Parabéns, você foi aprovado!")
    else:
        print("Infelizmente, você foi reprovado.")


sistema_de_notas()
