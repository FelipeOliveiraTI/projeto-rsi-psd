# esse codigo recebera as mensagem da fila e exibira na tela

import pika

# Conectando ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Criando uma fila, apesar de ter sido criado a fila no  programa send.py
#Temos que ter a certeza que a fila existe se nao a mensagem e perdida
channel.queue_declare(queue='Fila_Mensagens')

#Recebendo Mensagens da fila
def callback(ch, method, properties, body):
	print "[x] Received %r" %(body,)

# Informando ao Servidor RabbitMQ que a funcao callback deve reeceber
# as mensagens da fila 'Fila_Mensagens'

channel.basic_consume(callback, queue='Fila_Mensagens', no_ack=True)

print '[*] Esperando Mensagens. Para sair pressione CTRL + C'

channel.start_consuming()
 
