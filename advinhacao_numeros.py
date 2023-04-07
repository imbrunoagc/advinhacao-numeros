import random

print("Seja muito bem vindo ao Guess Number do Bruno!")
choice_number = input("Digite o número teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: valor informado não é númerico. Favor execute novamente e informe um número!")
    quit()
    
random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    # Usuário inserir o valor de chute!
    answer_user = input("Advinhe o número: ")
    
    # Verificar se o chute é numérico
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
    # Se não for númerico, apresentar o erro
        print("Erro: valor informado não é númerico. Favor execute novamente e informe um número!")
        continue
    
    # Número de tentativas
    n_choices = n_choices + 1
    
    # Se acertar o chute for igual ao número aleatório - encerrar o programa
    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto, o número randômico é menor que isso..")
    else:
        print("Chutou baixo, o número randômico é maior que isso..")

print("Nº de tentativas: " + str(n_choices))