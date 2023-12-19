# Importa os módulos necessários
import socket
import threading

# Dicionário para mapear os comandos do usuário para os comandos AOT
PROTOCOLO_AOT = {
    'assentos_disponiveis': 'ASSD',
    'reservar_assentos': 'RESV',
    'cancelar_reserva': 'CANC'
}

# Dicionário para mapear os códigos de erro para as mensagens de erro
ERROS_AOT = {
    'ERRO 444': 'Comando não reconhecido',
}

# Lista de assentos disponíveis
assentos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

# Cria um bloqueio para a lista de assentos. Isso é usado para prevenir condições de corrida.
bloqueio_assentos = threading.Lock()


# Função para mostrar os assentos disponíveis de uma maneira amigável ao usuário
def mostrar_assentos_disponiveis():
    response = "\nAssentos Disponíveis:\n  -------------------------"

    for linha in range(1, 4):
        assentos_disponiveis = []
        for coluna in range(1, 4):
            assento = f"{chr(ord('a') + linha - 1)}{coluna}"
            status = f"[ {assento} ]" if assento in assentos else "[ --- ]"
            assentos_disponiveis.append(status)
        response += "\n  " + ' '.join(assentos_disponiveis)

    response += "\n  -------------------------\n"
    return response


# Função para tratar a mensagem do cliente
def trata_msg(request):
    # Usa o bloqueio para garantir que apenas uma thread acesse a lista de assentos de cada vez
    bloqueio_assentos.acquire()

    # Traduz o comando do usuário para o comando AOT correspondente
    comando_aot = PROTOCOLO_AOT.get(request.split(' ')[0], 'ERRO 444')

    # Se o comando AOT não for reconhecido, retorna uma mensagem de erro
    if comando_aot == 'ERRO 444':
        resposta = 'ERRO 444'
    else:
        # Processa o comando do usuário de acordo com o comando AOT correspondente
        if comando_aot == 'ASSD':
            # Processa o comando 'assentos_disponiveis'
            resposta = mostrar_assentos_disponiveis()
        elif comando_aot == 'RESV':
            # Processa o comando 'reservar_assentos'
            partes = request.split(' ')
            if len(partes) < 2:
                resposta = "Por favor, forneça o número do assento que deseja reservar."
            else:
                assento = partes[1]
                if assento in assentos:
                    assentos.remove(assento)
                    resposta = "Assento " + assento + " reservado com sucesso!"
                else:
                    resposta = "Desculpe, o assento " + assento + " não está disponível."
        elif comando_aot == 'CANC':
            # Processa o comando 'cancelar_reserva'
            partes = request.split(' ')
            if len(partes) < 2:
                resposta = "Por favor, forneça o número do assento cuja reserva deseja cancelar."
            else:
                assento = partes[1]
                assentos.append(assento)
                resposta = "Reserva para o assento " + assento + " cancelada com sucesso!"

    # Libera o bloqueio para que outras threads possam acessar a lista de assentos.
    bloqueio_assentos.release()

    return resposta


# Função para tratar o cliente
def tratar_cliente(socket_cliente, endereco):
    print('Cliente conectado:', endereco)
    while True:
        # Recebe a solicitação do cliente
        request = socket_cliente.recv(2048).decode()
        print(f"Recebido de {endereco}: {request}")

        # Se o cliente enviar 'bye', termina a conexão com o cliente.
        if request == 'bye':
            print(f'Cliente {endereco} desconectado.')
            break

        # Trata a mensagem do cliente
        resposta = trata_msg(request)

        print(f"Enviando para {endereco}: {resposta}")
        # Envia a resposta ao cliente
        socket_cliente.send(bytes(resposta, 'UTF-8'))

        if request == 'bye':
            print(f'Cliente {endereco} desconectado.')
            break

    # Fecha o socket do cliente quando o cliente envia 'bye'
    socket_cliente.close()


# Função para iniciar o servidor
def iniciar_servidor():
    # Solicita o endereço IP e a porta do servidor ao usuário
    LOCALHOST = input("Digite o endereço IP do servidor: ")
    PORTA = int(input("Digite a porta do servidor: "))

    # Cria um socket para o servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula o socket a um endereço e porta
    servidor.bind((LOCALHOST, PORTA))
    # Começa a ouvir conexões
    servidor.listen(1)
    print("Servidor iniciado")

    try:
        while True:
            # Aceita uma nova conexão
            socket_cliente, endereco = servidor.accept()

            # Cria uma nova thread para tratar a conexão
            thread_cliente = threading.Thread(target=tratar_cliente, args=(socket_cliente, endereco))
            thread_cliente.start()
    finally:
        # Fecha o socket do servidor quando o servidor é encerrado.
        servidor.close()


# Inicia o servidor
iniciar_servidor()
