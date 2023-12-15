import socket
import threading

# Cria um bloqueio para a lista de assentos. Isso é usado para prevenir condições de corrida.
bloqueio_assentos = threading.Lock()

# Esta função é executada em uma nova thread para cada cliente que se conecta ao servidor.
def tratar_cliente(socket_cliente):
    while True:
        # Recebe a solicitação do cliente
        request = socket_cliente.recv(2048).decode()
        print(f"Recebido: {request}")
        
        # Se o cliente enviar 'bye', termina a conexão com o cliente.
        if request == 'bye':
            print ('Cliente desconectado.')
            break
        
        # Usa o bloqueio para garantir que apenas uma thread acesse a lista de assentos de cada vez
        bloqueio_assentos.acquire()
        
        # Se o cliente solicitar os assentos disponíveis, envia a lista de assentos disponíveis.
        if request == 'assentos_disponiveis':
            if assentos:
                resposta = ','.join(assentos)
            else :
                resposta ='Desculpe, todos os assentos foram vendidos/reservados.'
        # Se o cliente solicitar para reservar um assento, verifica se o assento está disponível e, em caso afirmativo, reserva o assento.
        elif request.startswith('reservar_assentos'):
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
        # Se o cliente solicitar para comprar um ingresso, verifica se o assento está disponível e, em caso afirmativo, vende o ingresso.
        elif request.startswith('comprar_ingressos'):
            partes = request.split(' ')
            if len(partes) < 2:
                resposta = "Por favor, forneça o número do assento que deseja comprar."
            else:
                assento = partes[1]
                if assento not in assentos:
                    resposta = "Ingresso para o assento " + assento + " comprado com sucesso!"
                else:
                    resposta = "Desculpe, o assento " + assento + " ainda está disponível, você precisa reservá-lo primeiro."
        # Se o cliente solicitar para cancelar uma reserva, cancela a reserva.
        elif request.startswith('cancelar_reserva'):
            partes = request.split(' ')
            if len(partes) < 2:
                resposta = "Por favor, forneça o número do assento cuja reserva deseja cancelar."
            else:
                assento = partes[1]
                assentos.append(assento)
                resposta = "Reserva para o assento " + assento + " cancelada com sucesso!"
        else:
            resposta = 'Comando não reconhecido.'
        
        # Libera o bloqueio para que outras threads possam acessar a lista de assentos.
        bloqueio_assentos.release()
        
        print(resposta)
        # Envia a resposta ao cliente
        socket_cliente.send(bytes(resposta,'UTF-8'))
        
        if request == 'bye':
            print ('Cliente desconectado.')
            break
    
    # Fecha o socket do cliente quando o cliente envia 'bye'
    socket_cliente.close()


# Esta função inicia o servidor.
def iniciar_servidor():
    # Cria um socket para o servidor
    servidor= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Vincula o socket a um endereço e porta
    servidor.bind((LOCALHOST, PORTA))
    # Começa a ouvir conexões
    servidor.listen(1)
    print("Servidor iniciado")
    try :
        while True:
            # Aceita uma nova conexão
            socket_cliente, endereco = servidor.accept()
            
            print ('Cliente :',endereco)
            # Cria uma nova thread para tratar a conexão
            thread_cliente = threading.Thread(target=tratar_cliente, args=(socket_cliente,))
            thread_cliente.start()
    finally:
        # Fecha o socket do servidor quando o servidor é encerrado.
        servidor.close()

LOCALHOST = "192.168.56.1"
PORTA = 4000
# Lista de assentos disponíveis
assentos = [ 'a1','a2','a3'] #,'b1','b2','b3','c1','c2','c3']

# Inicia o servidor
iniciar_servidor()
