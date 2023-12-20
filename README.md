# BATINGRESSO
Sistema de Reserva de Assentos

Autores: Mateus Polari, Thiago Alexandre, Lucas André
Email: mateus.castro@academico.ifpb.edu.br

Disciplinas: Protocolos e Interconexão de Redes de Computadores e Sistemas Operacionais
Docentes: Leonidas Francisco de Lima Junior ,Gustavo Wagner Diniz Mendes

Descrição Problema:  Este sistema permite que os usuários visualizem, reservem e cancelem reservas de assentos. Ele é composto por um servidor que gerencia as reservas de assentos e um cliente que permite aos usuários interagir com o sistema.

Arquivos do Projeto: 
- Arquivo servidor: Responsável pela criação do servidor e pelo tratamento das requisições do cliente.
- Arquivo cliente: Responsável pela criação do cliente, por solicitar conexão com o servidor e enviar requisições ao servidor.

Instruções para execução: Execute o arquivo servidor.py, ao executá-lo, será solicitado o IP do servidor e sua porta. Logo em seguida, execute o arquivo cliente.py uma ou mais vezes e realize a conexão com o servidor, informando o IP do servidor que foi iniciado e a porta informada no servidor. Feito isto, já é possível utilizar os protocolos com seus respectivos parâmetros nos clientes. Ao terminar as requisições por parte do cliente, feitas através do protocolo de aplicação, basta digitar a palavra "bye" no terminal de cada um dos clientes inicializados e a conexão do cliente com o servidor será encerrada.

Recursos Utilizados Socket: O sistema usa sockets para permitir a comunicação entre o servidor e o cliente. O servidor cria um socket e começa a ouvir conexões. Quando um cliente se conecta, o servidor aceita a conexão e cria um novo socket para o cliente.

Threads: O sistema usa threads para permitir que o servidor trate múltiplos clientes simultaneamente. Quando um cliente se conecta, o servidor cria uma nova thread para tratar a conexão.

Semáforos: O sistema usa um bloqueio para prevenir condições de corrida ao acessar a lista de assentos. Quando uma thread está modificando a lista de assentos, outras threads são impedidas de acessá-la.

Comandos O sistema suporta os seguintes comandos:

assentos_disponiveis: Este comando mostra todos os assentos disponíveis para reserva. Não requer nenhum argumento adicional.

reservar_assentos [assento]: Este comando é usado para reservar um assento. Você deve fornecer o número do assento que deseja reservar como argumento. Por exemplo, reservar_assentos a1.

cancelar_reserva [assento]: Este comando é usado para cancelar a reserva de um assento. Você deve fornecer o número do assento cuja reserva deseja cancelar como argumento. Por exemplo, cancelar_reserva a1.

Códigos de Erro O sistema usa os seguintes códigos de erro para indicar diferentes situações de erro:

ERRO-444: Este erro significa que o comando que você digitou não é reconhecido. Isso pode ocorrer se você digitar um comando que não seja assentos_disponiveis, reservar_assentos ou cancelar_reserva.

ERRO-855: Este erro significa que o assento que você está tentando reservar não está disponível. Isso pode ocorrer se você tentar reservar um assento que já foi reservado ou que não existe.

ERRO-777: Este erro significa que você não forneceu o número do assento que deseja reservar. Isso pode ocorrer se você digitar o comando reservar_assentos sem fornecer um número de assento.

ERRO-202: Este erro significa que você não forneceu o número do assento cuja reserva deseja cancelar. Isso pode ocorrer se você digitar o comando cancelar_reserva sem fornecer um número de assento.

ERRO-303: Este erro significa que você não pode cancelar uma reserva que não fez. Isso ocorre quando um cliente tenta cancelar a reserva de outro cliente.
