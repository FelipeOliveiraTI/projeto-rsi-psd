# Codigo que mostra um exemplo de como enviar uma unica mensagem para a fila

import pika


# Estabelecendo uma conexao como o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# Criando uma fila para qual a mensagem sera entregue,
# sera nomeada 'Fila_Mensagens'
channel.queue_declare(queue = 'Fila_Mensagens')

channel.basic_publish(exchange='',routing_key='Fila_Mensagens',body='Para o projeto!')

print "[x] Mensagem Enviada!"

connection.close()
