import socket


host = "localhost"
port = 2405

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destino = (host,port)

tcp.connect(destino)

while(True):
	msg  = input("Digite a mensagem: ")
	tcp.send(msg.encode("utf-8"))
	tcp.recv(1024).decode("utf-8")
	if(msg == "sair"):break
tcp.close() 
