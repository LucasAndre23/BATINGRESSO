# Importa o módulo de socket
import socket



# Função para iniciar o cliente
def iniciar_cliente():
    # Solicita o endereço IP e a porta do servidor ao usuário
    LOCALHOST = input("Digite o endereço IP do servidor: ")
    PORTA = int(input("\nDigite a porta do servidor: "))

    # Cria um socket para o cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta o socket a um endereço e porta
    cliente.connect((LOCALHOST, PORTA))

    # Imprime uma mensagem de boas-vindas e a lista de comandos disponíveis
    print('''  ____   _____  __  __  __     __ ___  _   _  ____    ___       _      ___    ____      _     _____  ___  _   _   ____  ____   _____  ____   ____    ___  
| __ ) | ___||  \/  | \ \   / /| || \ | ||  _ \  / _ \     / \    / _ \  | __ )    / \   |   || _|| \ | | / ___||  _ \ | ____|/ ___| / ___|  / _ \ 
|  _ \ |  |  | |\/| |  \ \ / /  | | |  \| || | | || | | |   / _ \  | | | | |  _ \   / _ \    | |   | | |  \| || |  _ | |_) ||  _|  \__ \ \___ \ | | | |
| |) || |__ | |  | |   \ V /   | | | |\  || || || |_| |  / ___ \ | |_| | | |_) | / ___ \   | |   | | | |\  || |_| ||  _ < | |__  ___) | ___) || |_| |
|____/ |_____||_|  |_|    \_/   |___||_| \_||____/  \___/  /_/   \_\ \___/  |____/ /_/   \_\  |_|  |___||_| \_| \____||_| \_\|_____||____/ |____/  \___/ 
''')
    print("=================Comandos disponíveis:==========================\n")
    print("•assentos_disponiveis: Mostra os assentos disponíveis.\n")
    print("•reservar_assentos [assento]: Reserva um assento.\n")
    print("•cancelar_reserva [assento]: Cancela a reserva de um assento.\n")
    print("•Digite 'bye' para sair.\n")

    while True:
        # Solicita um comando ao usuário
        comando = input("\nDigite o comando que você deseja usar: ")

        # Envia o comando ao servidor
        cliente.send(bytes(comando, 'UTF-8'))

        # Se o usuário digitar 'bye', imprime uma mensagem de despedida e encerra a conexão
        if comando == 'bye':
            print('\nObrigado pela preferência, até a próxima. ⊂(◉‿◉)つ')
            break

        # Recebe a resposta do servidor
        resposta = cliente.recv(2048).decode()

        # Imprime a resposta
        print(resposta)

    # Fecha o socket do cliente quando o usuário digita 'bye'
    cliente.close()


# Inicia o cliente
iniciar_cliente()
