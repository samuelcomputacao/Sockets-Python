import socket;
import threading;

def conecao(conecao,client):
	print("Conectado: "  + str( client))
	msg = conecao.recv(1024).decode("utf-8")
	while(msg != "sair"):
		print(str(client) + " : " + str(msg))
		msg = conecao.recv(1024).decode("utf-8")
		#conecao.send("Recebi uma mensagem".encode("utf-8"))
	conecao.close()
	

host = 'localhost'
port = 2406

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origi = (host,port)

tcp.bind(origi)
tcp.listen(1)
print (origi)

while (True):
	con, client = tcp.accept()
	con.send(1111)
	threading._start_new_thread(conecao, (con,client))

tcp.close() 

