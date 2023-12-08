import socket
import threading

# Cria um bloqueio para a lista de assentos
bloqueio_assentos = threading.Lock()

def tratar_cliente(socket_cliente):
    while True:
        # Envia a lista de assentos disponíveis ao cliente
        bloqueio_assentos.acquire()
        if len(assentos) == 0:
            resposta = "Todos os ingressos foram vendidos. Por favor, digite 'bye' para sair."
            socket_cliente.send(bytes(resposta, 'UTF-8'))
            bloqueio_assentos.release()
            break
        socket_cliente.send(bytes(','.join(assentos), 'UTF-8'))
        bloqueio_assentos.release()
        # Recebe a solicitação do cliente para um assento
        assento = socket_cliente.recv(2048).decode()
        if assento == 'bye':
            break
        # Usa o bloqueio para garantir que apenas uma thread acesse a lista de assentos de cada vez
        bloqueio_assentos.acquire()
        # Verifica se o assento está disponível
        if assento in assentos:
            # Se estiver, remove o assento da lista e envia uma resposta ao cliente
            assentos.remove(assento)
            resposta = "Ingresso para o assento " + assento + " vendido!"
        else:
            # Se não estiver, envia uma resposta ao cliente
            resposta = "Desculpe, o assento " + assento + " não está disponível."
        bloqueio_assentos.release()
        print(resposta)
        # Envia a resposta ao cliente
        socket_cliente.send(bytes(resposta,'UTF-8'))
    # Fecha o socket do cliente quando o cliente envia 'bye'
    socket_cliente.close()

def iniciar_servidor():
    # Cria um socket para o servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Vincula o socket a um endereço e porta
    servidor.bind((LOCALHOST, PORTA))
    # Começa a ouvir conexões
    servidor.listen(1)
    print("Servidor iniciado")
    while True:
        # Aceita uma nova conexão
        socket_cliente, _ = servidor.accept()
        # Cria uma nova thread para tratar a conexão
        thread_cliente = threading.Thread(target=tratar_cliente, args=(socket_cliente,))
        thread_cliente.start()

LOCALHOST = "127.0.0.1"
PORTA = 50000
# Cria uma lista de assentos disponíveis
assentos = [ 'a1','a2','a3','b1','b2','b3','c1','c2','c3']

# Inicia o servidor
iniciar_servidor()
