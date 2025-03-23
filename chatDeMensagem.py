import os #importando bb

mensagens = [] #Lista q vai armazenar mensagens

nome = input("Nome: ") # Recebe o nome do cara

while True:

    #Limpando terminal
    os.system('cls')

    if len(mensagens) > 0: # Verifica se tem mensagem na lista
        for m in mensagens: # Caso tenha exibe
            print(m['nome'], "-", m['texto'])

    print("_" * 15) # Faz uma divião para separação do texto

    # obtendo o texto
    texto = input("Mensagem: ") # Obtem o texto de usuario 
    if texto == "Fim" or texto == "fim": # Caso o usuario digite Fim ou fim cai no break
        break #Acaba a conversa

    # adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })