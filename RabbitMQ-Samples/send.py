# Codigo que mostra um exemplo de como enviar uma unica mensagem para a fila

import pika


# Estabelecendo uma conexao com o servidor RabbitMQ na maquina local - localhost
# para se conectar em uma maquina diferente temos que especificar o endereco IP
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# Criando uma fila para qual a mensagem sera entregue,
# sera nomeada 'Fila_Mensagens'
channel.queue_declare(queue = 'Fila_Mensagens')

channel.basic_publish(exchange='',routing_key='Fila_Mensagens',body='Hello World!')

print "[x] Mensagem Enviada!"

connection.close()
