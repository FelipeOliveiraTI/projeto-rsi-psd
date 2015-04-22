# Cliente generico UDP que nao saabe o IP do destinatario
# Ele envia o pacote como faz para qualquer outro endereco IP e porta
# pra fazer o teste, rode o servidor em N maquinas da mesma rede logica
# e cada mensagem do cliente ira aparecer em todos os servidores

import sys, socket

if __name__=='__main__':
	try:
		addr = sys.argv[1]
		port = int(sys.argv[2])
		buff = sys.argv[3]
	except IndexError:
		print 'use: %s addr port buff' %sys.argv[0]
		sys.exit(1)

	fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	fd.sendto(buff, (addr,port))

	modifiedMessage, serverAddress = fd.recvfrom(2048)
	print ("Retorno do Servidor:" + modifiedMessage)

	fd.close()

