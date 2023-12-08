import socket

def iniciar_cliente():
    # Cria um socket para o cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta o socket a um endereço e porta
    cliente.connect((LOCALHOST, PORTA))
    while True:
        # Recebe a lista de assentos disponíveis do servidor
        assentos = cliente.recv(2048).decode()
        print("\nAssentos disponíveis: ", assentos,'\n')
        # Solicita um assento ao usuário
        assento = input("Digite o assento que você deseja comprar ou 'bye' para sair: ")
        # Envia a solicitação do assento ao servidor
        cliente.send(bytes(assento,'UTF-8'))
        if assento == 'bye':
            break
        # Recebe a resposta do servidor
        resposta = cliente.recv(2048).decode()
        print(resposta)
    # Fecha o socket do cliente quando o usuário digita 'bye'
    cliente.close()

LOCALHOST = "127.0.0.1"
PORTA = 50000

# Inicia o cliente
iniciar_cliente()
