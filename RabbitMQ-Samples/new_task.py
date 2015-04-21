# Neste exemplo criaremos uma fila de trabalho que sera usado para distribuir 
# tarefas demoradas entre varios trabalhadores.
# esse programa ira agendar tarefas na nossa fila de trabalho

import pika
import sys

# Estabelecendo uma conexao com o servidor RabbitMQ na maquina local - localhost

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# Criando uma fila para qual a mensagem sera entregue,
channel.queue_declare(queue = 'Fila_Mensagens')

# Criando uma fila duravel e persistente com o parametro durable
# o RabbitMQ nao permite redefinir uma fila existente com diferentes parametros
# uma forma rapida de se resolver e criar uma nova fila
# esse processo garante que mesmo se o RabbitMQ reiniciar a fila task_queue
# nao sera perdida

channel.queue_declare(queue = 'task_queue', durable = True)


message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='task_queue', body=message,
			properties = pika.BasicProperties(
				delivery_mode =2, #faz a mensagem persistente
			))

print "[x] Enviado %r " %(message,)

connection.close()
