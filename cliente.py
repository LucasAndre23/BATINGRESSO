import socket




def iniciar_cliente():
    # Cria um socket para o cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta o socket a um endereço e porta
    cliente.connect((LOCALHOST, PORTA))
    print ('''  ____   _____  __  __  __     __ ___  _   _  ____    ___       _      ___    ____      _     _____  ___  _   _   ____  ____   _____  ____   ____    ___  
| __ ) | ____||  \/  | \ \   / /|_ _|| \ | ||  _ \  / _ \     / \    / _ \  | __ )    / \   |_   _||_ _|| \ | | / ___||  _ \ | ____|/ ___| / ___|  / _ \ 
|  _ \ |  _|  | |\/| |  \ \ / /  | | |  \| || | | || | | |   / _ \  | | | | |  _ \   / _ \    | |   | | |  \| || |  _ | |_) ||  _|  \___ \ \___ \ | | | |
| |_) || |___ | |  | |   \ V /   | | | |\  || |_| || |_| |  / ___ \ | |_| | | |_) | / ___ \   | |   | | | |\  || |_| ||  _ < | |___  ___) | ___) || |_| |
|____/ |_____||_|  |_|    \_/   |___||_| \_||____/  \___/  /_/   \_\ \___/  |____/ /_/   \_\  |_|  |___||_| \_| \____||_| \_\|_____||____/ |____/  \___/ 
''')
    print("=================Comandos disponíveis:==========================\n")
    print("•assentos_disponiveis: Mostra os assentos disponíveis.\n")
    print("•reservar_assentos [assento]: Reserva um assento.\n")
    print("•comprar_ingressos [assento]: Compra um ingresso.\n")
    print("•cancelar_reserva [assento]: Cancela a reserva de um assento.\n")
    print("•Digite 'bye' para sair.\n")
    
    while True:
        # Solicita um comando ao usuário
        comando = input("Digite o comando que você deseja usar: ")
        # Envia o comando ao servidor
        cliente.send(bytes(comando,'UTF-8'))
        if comando == 'bye':
            break
        # Recebe a resposta do servidor
        resposta = cliente.recv(2048).decode()
        print(resposta)
    # Fecha o socket do cliente quando o usuário digita 'bye'
    cliente.close()

LOCALHOST = "192.168.56.1"
PORTA = 4000

# Inicia o cliente
iniciar_cliente()

