# Neste exemplo implementaremos o modelo Publish/Subscribe
# Nos exemplos anteriores worker.py e new_task.py cada tarefa era entregue
# a  exatamente um consumidor. Nesse exemplo nos vamos entregar uma menssagem
# a varios consumidores.

# As mensagens serao transmitidas para todos os recepitores

import pika
import sys

# Estabelecendo uma conexao com o servidor RabbitMQ na maquina local - localhost

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

#declara um cambio para qual as mensagens serao publicadas
channel.exchange_declare(exchange = 'logs', type = 'fanout')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)

print "[x] Enviado %r " %(message,)

connection.close()
