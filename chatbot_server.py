""" servidor chatbot - pesquisa copa do mundo"""
import socket

#1. Criar socket do servidor
sserv  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. faz o bind do servidor com a porta do serviço
host = socket.gethostname(); porta = 49153; sserv.bind((host, porta))

#3. habilitar a escuta no servidor
sserv.listen()

while True:
    print('-' * 36 + '\nSERVIDOR CHATBOT - ESPERANDO CONEXÃO\n1' + '-' * 36)
    
   #4. espera por uma conexão (accept é função bloqueante). aceita quando chegar
    (conexao, end) = sserv.accept()
    print('conectado a ', end)
    
    #5. realiza o diálogo
    #enviar a pergunta 1 e receber a resposta 1
    conexao.send('qual é o seu nome?'.encode('utf-8'))
    nome = conexao.recv(1024).decode('utf-8')
    print('pergunta 1 processada...')
    conexao.send(' vai assistir a copa? (S/N)'.encode('utf-8'))
    copa = conexao.recv(1024).decode('utf-8')
    print('pergunta 2 processada...')
    
    #dependendo da resposta faz ou não outra pergunta
    if pergunta2.upper() == 'N':
        msg = nome + ', obrigado por participar'
        conexao.send(msg.encode('utf-8'))
    else:
        conexao.send('quem vai ser o campeao?'.encode('utf-8'))
        pergunta2 = conexao.recv(1024).decode('utf-8')
        pritn('pergunta 3 processada')
    
    

#6. encerrar o serviço
sserv.close()