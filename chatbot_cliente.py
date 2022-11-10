""" cliente chatbot - pesquisa copa do mundo """
import socket

#1. Criar socket do cliente
scli  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. conecta com o servidor
host = socket.gethostname(); porta = 49153;
scli.connect((host, porta))

#3. realiza o diálogo
#receber a pergunta 1 e enviar a resposta 1
pergunta = scli.recv(1024).decode('utf-8')
print(pergunta)
nome = input()
scli.send(nome.encode('utf-8'))

pergunta2 = scli.recv(1024).decode('utf-8')
print(pergunta2)
copa = input()
scli.send(copa.encode('utf-8'))
if pergunta2.upper() == 'N':
    msg = scli.recv(1024).decode('utf-8')
    print(msg)
else:
    pergunta2 = scli.recv(1024).decode('utf-8')
    print(pergunta2)
    copa = input()
    scli.send(copa.encode('utf-8'))
#4. encerrar a conexão
scli.close()