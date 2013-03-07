import socket
#import select

HOST = ''
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
s.settimeout(0.0001)
print 'Listening on port: ', PORT

connections = []
chatlog=[]
while True:
	try:
		conn, addr = s.accept()
		conn.settimeout(0.0001)
		print 'Connection accepted from:', addr
		connections.append((conn, addr))
	except socket.timeout:
		pass
	except 
		pass
	pass 
	#except for disconnect or connection reset?
	
	for conn, addr in connections:
		try:
			data = conn.recv(10)
			if data:
				for session in connections:
					if session[0] == conn:
						continue
					session[0].send(data)
			print "Received ", data, " from address:", addr
		except socket.timeout:
			pass