
# Desafio 1

# Você é um intrépido explorador em uma jornada por uma terra 
# desconhecida repleta de desafios emocionantes. Ao se deparar
# com uma floresta misteriosa, você percebe que a única maneira
# de atravessá-la é desvendando seus caminhos por meio de um código em Python.
# Prepare-se para a "Aventura do Explorador"!

# Entrada
# Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo,
# representando a quantidade de passos que o explorador deve dar na floresta.

# Saída
# O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta.
# Utilize um laço de repetição para simular os passos do explorador. A cada passo,
# imprima uma mensagem informando a distância percorrida até o momento.

##   Código

# Desafio: A Aventura do Explorador

#// Adicione uma condição para verificar se a quantidade de passos é positiva.
#// Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
#// Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

# Desafio: A Aventura do Explorador

# Adicione uma condição para verificar se a quantidade de passos é positiva.
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

# Entrada
quantidade_passos = int(input())

if quantidade_passos > 0:
    for passo in range(1, quantidade_passos + 1):
        if passo == 1:
            print(f"Explorador: {passo} passo")
        else:
            print(f"Explorador: {passo} passos")
else:
    print("Nenhum passo dado na floresta.")
