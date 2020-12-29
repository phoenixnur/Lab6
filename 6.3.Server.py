import socket
import math
import errno
import sys
from multiprocessing import Process

def ProcessStart(server):

     while True:
            ch = server.recv(1024).decode()

            if ch == '1': #log
                numb = server.recv(1024).decode()
                calc = math.log(float(numb))

            elif ch  == '2': #square root
                numb = server.recv(1024).decode()
                calc = math.sqrt(float(numb))

            elif ch  == '3': #exponential
                numb = server.recv(1024).decode()
                calc = math.exp(float(numb))

            elif ch == '4': #exit
                server.close()
                break

            server.sendall(str(calc).encode())


if __name__ == '__main__':
    
    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 4848

    try:
        S.bind((host,port))
    except socket.error as e:
        print (str(e))
        sys.exit()

    S.listen(5)
    while True:
        try:
            server, addr = S.accept()
            print ('\n connected!')
        
            p = Process(target = ProcessStart, args=(server,))
            p.start()

        except socket.error:
            print ('an exception occurred!')

    S.close()
