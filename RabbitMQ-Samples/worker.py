# esse codigo recebera as mensagem da fila e exibira na tela

import pika
import time


# Conectando ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criando uma fila, apesar de ter sido criado a fila no  programa new_task.py
channel.queue_declare(queue='Fila_Mensagens')

# Recebendo Mensagens da fila
# A biblioteca Pika faz a chamada da funcao callback sempre que recebe 
# uma mensagem.

def callback(ch, method, properties, body):
	print "[x] Recebido %r" %(body,)
	
	#como nao temos uma terefa real, a funcao time.sleep vai simular
	#o tempo de uma tarefa em alguns segundos
	time.sleep(body.count('.'))
	print "[x] Done"
	#Se um worker morre a tarefa vai ser entregue a outro worker
	ch.basic_ack(delivery_tag = method.delivery_tag)


# Informando ao Servidor RabbitMQ que a funcao callback deve receber
# as mensagens da 'task_queue'
# informa ao RabbitMQ nao entregar mais de uma menssagem por vez a um worker

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')

print '[*] Esperando Mensagens. Para sair pressione CTRL + C'

channel.start_consuming()
 
