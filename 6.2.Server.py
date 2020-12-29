import socket
import sys
import time
import errno
from multiprocessing import Process

ok_message = 'http/1.0 200 ok\n\n'
nok_message = 'http/1.0 404 notfound\n\n'

def process_start(s_sock):
	s_sock.send(str.encode('welcome to the server\n'))

	while True:

		data = s_sock.recv(2048)
		print (data)

		if not data:
			break

		s_sock.sendall(str.encode(ok_message))

	s_sock.close()

if __name__=='__main__':

	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	s.bind(( '' , 8888 ))
	print ('listening .......')
	s.listen(3)

	try:

		while True:
			try:
				s_sock, s_addr = s.accept()
				p = Process(target = process_start, args=(s_sock,))
				p.start()

			except socket.error:
				print ('there is a socket error')

	except Exception as e:

		print ('an exception occurred!')
		print (e)
