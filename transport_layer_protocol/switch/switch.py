import socket

class Switch:
	"""Simple client for transporting layer"""
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket()
		self.sock.connect((self.host, self.port))

	def send_msg(self,msg):
		self.sock.send(msg)

	def close_sock(self):
		self.sock.close()		

def main():
	Sw = Switch('localhost', 5555)
	Sw.send_msg("Message for test".encode())
	Sw.close_sock()

if __name__ == '__main__':
	main()